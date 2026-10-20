#!/usr/bin/env python3
"""Mareas Patagonia -> mareas.json

Fuente: mareógrafos en tiempo real del SHOA (Armada de Chile) y del SHN (Argentina),
publicados por la Comisión Oceanográfica Intergubernamental de la UNESCO (IOC).

Por cada estación:
  - baja ~30 días de nivel del mar,
  - ajusta por mínimos cuadrados las componentes armónicas principales,
  - predice pleamares/bajamares y curva de hoy y mañana (estimación referencial),
  - guarda el nivel real medido más reciente y las últimas 24 h.

Uso: python3 actualizar_mareas.py [--backtest]
"""
import datetime as dt
import json
import sys
import urllib.request
from zoneinfo import ZoneInfo

import numpy as np

API = "https://www.ioc-sealevelmonitoring.org/service.php?query=data&code={c}&timestart={a}&timestop={b}&format=json"
DIAS = 30
SALIDA = "mareas.json"

# Velocidades angulares (grados/hora). Con ~30 días no se separan K2/S2 ni P1/K1: se usan solo las separables.
ARM = {
    "M2": 28.9841042, "S2": 30.0, "N2": 28.4397295, "K1": 15.0410686, "O1": 13.9430356,
    "Q1": 13.3986609, "M4": 57.9682084, "MS4": 58.9841042, "MN4": 57.4238337,
}

# (código IOC, nombre, país, zona horaria, región)
ESTACIONES = [
    ("pmon", "Puerto Montt", "Chile", "America/Santiago", "Los Lagos"),
    ("ancu", "Ancud (Chiloé)", "Chile", "America/Santiago", "Los Lagos"),
    ("cstr", "Castro (Chiloé)", "Chile", "America/Santiago", "Los Lagos"),
    ("pcha", "Puerto Chacabuco", "Chile", "America/Santiago", "Aysén"),
    ("pnat", "Puerto Natales", "Chile", "America/Punta_Arenas", "Magallanes"),
    ("ptar", "Punta Arenas", "Chile", "America/Punta_Arenas", "Magallanes"),
    ("pwil", "Puerto Williams", "Chile", "America/Punta_Arenas", "Magallanes"),
    ("madry", "Puerto Madryn", "Argentina", "America/Argentina/Buenos_Aires", "Chubut"),
    ("dese", "Puerto Deseado", "Argentina", "America/Argentina/Buenos_Aires", "Santa Cruz"),
    ("ushu", "Ushuaia", "Argentina", "America/Argentina/Ushuaia", "Tierra del Fuego"),
]

# Puertos sin mareógrafo en la red IOC: marea estimada con el modelo oceánico de Open-Meteo
# (validado contra Madryn y Deseado: correlación 0,88–0,95). Sin altura real medida.
# (código, nombre, país, zona, región, lat, lon)
ESTACIONES_MODELO = [
    ("rgal", "Río Gallegos", "Argentina", "America/Argentina/Buenos_Aires", "Santa Cruz", -51.625, -68.79),
    ("sjul", "San Julián", "Argentina", "America/Argentina/Buenos_Aires", "Santa Cruz", -49.29, -67.54),
    ("comod", "Comodoro Rivadavia", "Argentina", "America/Argentina/Buenos_Aires", "Chubut", -45.875, -67.375),
    ("saoe", "San Antonio Oeste", "Argentina", "America/Argentina/Buenos_Aires", "Río Negro", -40.79, -64.875),
]
MARINE = ("https://marine-api.open-meteo.com/v1/marine?latitude={la}&longitude={lo}"
          "&hourly=sea_level_height_msl&timezone=UTC&past_days=14&forecast_days=3")

EPOCA = dt.datetime(2026, 1, 1)


def horas(t):
    """datetime UTC naive -> horas desde EPOCA."""
    return (t - EPOCA).total_seconds() / 3600.0


def descargar(codigo, fin):
    ini = fin - dt.timedelta(days=DIAS)
    url = API.format(c=codigo, a=ini.strftime("%Y-%m-%d"), b=(fin + dt.timedelta(days=1)).strftime("%Y-%m-%d"))
    with urllib.request.urlopen(url, timeout=180) as r:
        return json.load(r)


def serie(datos):
    """Elige el sensor con más datos y promedia a bloques de 10 min. Devuelve (t_horas, nivel_m, sensor)."""
    cuenta = {}
    for x in datos:
        if x["sensor"] in ("rad", "ra2", "ra3", "prs") and x["slevel"] is not None:
            cuenta[x["sensor"]] = cuenta.get(x["sensor"], 0) + 1
    if not cuenta:
        raise ValueError("sin datos de nivel")
    sensor = max(cuenta, key=cuenta.get)
    filas = sorted((dt.datetime.strptime(x["stime"], "%Y-%m-%d %H:%M:%S"), x["slevel"])
                   for x in datos if x["sensor"] == sensor and x["slevel"] is not None)
    t = np.array([horas(f[0]) for f in filas])
    y = np.array([f[1] for f in filas])
    b = np.floor(t * 6).astype(int)
    _, idx = np.unique(b, return_inverse=True)
    n = np.bincount(idx)
    return np.bincount(idx, t) / n, np.bincount(idx, y) / n, sensor


def diseno(t):
    cols = [np.ones_like(t)]
    for v in ARM.values():
        a = np.radians(v) * t
        cols += [np.cos(a), np.sin(a)]
    return np.vstack(cols).T


def ajustar(t, y):
    """Mínimos cuadrados robustos (descarta outliers a 3 sigma)."""
    m = np.ones(len(t), bool)
    coef = None
    for _ in range(4):
        coef, *_ = np.linalg.lstsq(diseno(t[m]), y[m], rcond=None)
        r = y - diseno(t) @ coef
        s = 1.4826 * np.median(np.abs(r[m] - np.median(r[m]))) or 0.05
        m = np.abs(r) < 3 * s
    return coef


def predecir(coef, t, t_ref=None, y_ref=None, serie_t=None, serie_y=None):
    """Predicción armónica + corrección por residuo meteorológico reciente (decae en ~12 h)."""
    p = diseno(t) @ coef
    if serie_t is not None and len(serie_t):
        ult = serie_t > serie_t[-1] - 3
        res = float(np.mean(serie_y[ult] - diseno(serie_t[ult]) @ coef))
        t0 = serie_t[-1]
        peso = np.where(t >= t0, np.exp(-(t - t0) / 12.0), 0.0)
        p = p + res * peso
    return p


def extremos(t, p, zona):
    """Pleamares/bajamares: máximos y mínimos locales con ventana de ±90 min."""
    n = 18  # pasos de 5 min -> 90 min
    out = []
    for i in range(n, len(p) - n):
        v = p[i]
        w = p[i - n:i + n + 1]
        if v == w.max() and v > w.min() + 0.05:
            out.append((i, "pleamar"))
        elif v == w.min() and v < w.max() - 0.05:
            out.append((i, "bajamar"))
    res = []
    for i, tipo in out:
        loc = (EPOCA + dt.timedelta(hours=float(t[i]))).replace(tzinfo=dt.timezone.utc).astimezone(zona)
        res.append({"tipo": tipo, "fecha": loc.strftime("%Y-%m-%d"), "hora": loc.strftime("%H:%M"), "altura": float(p[i])})
    return res


def procesar(codigo, nombre, pais, tz, region, ahora, corte=None):
    datos = descargar(codigo, ahora)
    t, y, sensor = serie(datos)
    if corte is not None:
        k = t < corte
        t, y = t[k], y[k]
    if t[-1] - t[0] < 24 * 10:
        raise ValueError("serie demasiado corta")
    coef = ajustar(t, y)
    zona = ZoneInfo(tz)
    ahora_loc = ahora.replace(tzinfo=dt.timezone.utc).astimezone(zona)
    ini_loc = ahora_loc.replace(hour=0, minute=0, second=0, microsecond=0)
    ini_utc = ini_loc.astimezone(dt.timezone.utc).replace(tzinfo=None)
    t_ini = horas(ini_utc)
    tp = np.arange(t_ini, t_ini + 48, 5 / 60)  # hoy + mañana, paso 5 min
    pp = predecir(coef, tp, serie_t=t, serie_y=y)

    # Cero de referencia: bajamar astronómica mínima esperable en los datos (≈ nivel de reducción)
    base_t = np.arange(t[-1] - 24 * 28, t[-1], 0.25)
    cero = float(np.min(diseno(base_t) @ coef))
    pp_rel = pp - cero

    ex = extremos(tp, pp_rel, zona)
    hoy = ini_loc.strftime("%Y-%m-%d")
    man = (ini_loc + dt.timedelta(days=1)).strftime("%Y-%m-%d")

    # Curva de hoy cada 30 min (hora local)
    paso = 6  # 6 * 5 min
    curva = []
    for i in range(0, 24 * 12, paso):
        curva.append(round(float(pp_rel[i]), 2))

    # Observado: últimas 24 h cada 30 min + valor actual
    k = t > t[-1] - 24
    obs = []
    for ti, yi in zip(t[k][::3], y[k][::3]):
        loc = (EPOCA + dt.timedelta(hours=float(ti))).replace(tzinfo=dt.timezone.utc).astimezone(zona)
        obs.append({"t": loc.strftime("%Y-%m-%dT%H:%M"), "h": round(float(yi - cero), 2)})
    actual = float(y[-1] - cero)
    edad_min = (horas(ahora) - t[-1]) * 60
    ref = t[-1] - 1.0
    tendencia = float(y[-1] - np.interp(ref, t, y))
    return {
        "codigo": codigo, "nombre": nombre, "pais": pais, "region": region, "zona": tz,
        "sensor": sensor,
        "actual": {
            "altura": round(actual, 2),
            "hora": (EPOCA + dt.timedelta(hours=float(t[-1]))).replace(tzinfo=dt.timezone.utc).astimezone(zona).strftime("%H:%M"),
            "edad_min": round(edad_min),
            "tendencia": "subiendo" if tendencia > 0.03 else "bajando" if tendencia < -0.03 else "estable",
        },
        "rango_mes": [round(float(np.percentile(y, 1) - cero), 2), round(float(np.percentile(y, 99) - cero), 2)],
        "hoy": [e for e in ex if e["fecha"] == hoy],
        "manana": [e for e in ex if e["fecha"] == man],
        "curva_hoy": curva,
        "observado": obs,
    }


def catmull_rom(t, v, tx):
    """Interpolación cúbica (Catmull-Rom) de una serie horaria regular."""
    i = np.clip(np.searchsorted(t, tx) - 1, 1, len(t) - 3)
    u = (tx - t[i]) / (t[i + 1] - t[i])
    p0, p1, p2, p3 = v[i - 1], v[i], v[i + 1], v[i + 2]
    return 0.5 * ((2 * p1) + (-p0 + p2) * u + (2 * p0 - 5 * p1 + 4 * p2 - p3) * u ** 2 + (-p0 + 3 * p1 - 3 * p2 + p3) * u ** 3)


def procesar_modelo(codigo, nombre, pais, tz, region, lat, lon, ahora):
    with urllib.request.urlopen(MARINE.format(la=lat, lo=lon), timeout=60) as r:
        h = json.load(r)["hourly"]
    t = np.array([horas(dt.datetime.fromisoformat(x)) for x in h["time"]])
    v = np.array([np.nan if x is None else x for x in h["sea_level_height_msl"]])
    ok = ~np.isnan(v)
    if ok.sum() < 24 * 10:
        raise ValueError("modelo sin datos en este punto")
    t, v = t[ok], v[ok]
    cero = float(np.min(v))
    zona = ZoneInfo(tz)
    ahora_loc = ahora.replace(tzinfo=dt.timezone.utc).astimezone(zona)
    ini_loc = ahora_loc.replace(hour=0, minute=0, second=0, microsecond=0)
    t_ini = horas(ini_loc.astimezone(dt.timezone.utc).replace(tzinfo=None))
    tp = np.arange(t_ini, t_ini + 48, 5 / 60)
    pp = catmull_rom(t, v, tp) - cero  # suave: los extremos no quedan clavados en horas exactas
    ex = extremos(tp, pp, zona)
    hoy = ini_loc.strftime("%Y-%m-%d")
    man = (ini_loc + dt.timedelta(days=1)).strftime("%Y-%m-%d")
    return {
        "codigo": codigo, "nombre": nombre, "pais": pais, "region": region, "zona": tz,
        "sensor": "modelo", "tipo_dato": "modelo",
        "actual": None,
        "rango_mes": [round(float(np.percentile(v, 1) - cero), 2), round(float(np.percentile(v, 99) - cero), 2)],
        "hoy": [e for e in ex if e["fecha"] == hoy],
        "manana": [e for e in ex if e["fecha"] == man],
        "curva_hoy": [round(float(pp[i]), 2) for i in range(0, 24 * 12, 6)],
        "observado": [],
    }


def main():
    ahora = dt.datetime.now(dt.timezone.utc).replace(tzinfo=None, second=0, microsecond=0)
    if "--backtest" in sys.argv:
        # Predice como si fuese hace 3 días y compara con lo medido
        for cod, nom, pais, tz, reg in ESTACIONES:
            datos = descargar(cod, ahora)
            t, y, _ = serie(datos)
            corte = t[-1] - 72
            k = t < corte
            coef = ajustar(t[k], y[k])
            p = predecir(coef, t[~k], serie_t=t[k], serie_y=y[k])
            e = y[~k] - p
            print(f"{nom:20s} RMSE {np.sqrt(np.mean(e**2)):.2f} m  (rango {np.ptp(y[~k]):.1f} m)")
        return
    estaciones, fallas = [], []
    for cod, nom, pais, tz, reg in ESTACIONES:
        try:
            estaciones.append(procesar(cod, nom, pais, tz, reg, ahora))
            print("OK ", nom)
        except Exception as ex:
            fallas.append(nom)
            print("ERR", nom, ex)
    for cod, nom, pais, tz, reg, la, lo in ESTACIONES_MODELO:
        try:
            estaciones.append(procesar_modelo(cod, nom, pais, tz, reg, la, lo, ahora))
            print("OK (modelo)", nom)
        except Exception as ex:
            fallas.append(nom)
            print("ERR", nom, ex)
    if not estaciones:
        sys.exit("Sin datos de ninguna estación; no se sobreescribe mareas.json")
    salida = {
        "generado": ahora.strftime("%Y-%m-%dT%H:%MZ"),
        "fuente": "SHOA (Armada de Chile) y SHN (Argentina) vía IOC/UNESCO Sea Level Monitoring; modelo oceánico Open-Meteo en puertos sin mareógrafo",
        "estaciones": estaciones,
        "sin_datos": fallas,
    }
    with open(SALIDA, "w", encoding="utf-8") as f:
        json.dump(salida, f, ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    main()
