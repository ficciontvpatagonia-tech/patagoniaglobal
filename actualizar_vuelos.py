#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Actualiza el tablero de vuelos de aeropuertos patagónicos leyendo la API
oficial de Aeropuertos Argentina (server-side, sin el bloqueo CORS que impide
el fetch desde el navegador). Escribe un JSON estático por aeropuerto que la
página conectividad.html consume con un simple fetch (mismo origen).

Prueba inicial: Bariloche (BRC). Para sumar aeropuertos, agregar a AEROPUERTOS.
"""
import json
import sys
import datetime
import urllib.request
import urllib.error
from zoneinfo import ZoneInfo

API = "https://webaa-api-h4d5amdfcze7hthn.a02.azurefd.net/web-prod/v1/api-aa/all-flights"
TZ = ZoneInfo("America/Argentina/Buenos_Aires")

# Aeropuertos patagónicos argentinos (API de Aeropuertos Argentina). iata -> nombre.
# Todo se guarda en un único archivo combinado (vuelos_patagonia.json).
SALIDA = "vuelos_patagonia.json"
# Solo los aeropuertos patagónicos operados por Aeropuertos Argentina 2000 (los
# demás —Ushuaia, El Calafate, Trelew, Madryn— son de otra concesionaria y su API
# no devuelve vuelos). Para esos, la UI usa enlaces a Flightradar24.
AEROPUERTOS = {
    "NQN": "Neuquén",
    "BRC": "Bariloche",
    "CRD": "Comodoro Rivadavia",
    "RGL": "Río Gallegos",
    "RGA": "Río Grande",
}

# Nombres limpios por código de aerolínea (la API trunca el nombre)
AEROLINEAS = {
    "AR": "Aerolíneas Argentinas", "WJ": "JetSMART", "FO": "Flybondi",
    "O4": "Andes", "LA": "LATAM", "H2": "SKY", "G3": "GOL", "JA": "JetSMART",
}


def _req(url):
    r = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://www.aeropuertosargentina.com/",
        "Accept": "application/json, text/plain, */*",
    })
    with urllib.request.urlopen(r, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _hora(s):
    # "30/06 10:00" -> "10:00"
    return s.split(" ")[-1] if s else ""


def _aerolinea(reg):
    code = (reg.get("idaerolinea") or "").strip()
    if code in AEROLINEAS:
        return AEROLINEAS[code]
    nombre = (reg.get("aerolinea") or "").strip()
    return nombre.title() if nombre else "—"


def _mapear(reg):
    prog = _hora(reg.get("stda", ""))
    real = _hora(reg.get("atda", "")) or _hora(reg.get("etda", ""))
    return {
        "hora": prog,
        "real": real if real and real != prog else "",
        "nro": (reg.get("nro") or "").strip(),
        "aerolinea": _aerolinea(reg),
        "ciudad": (reg.get("destorig") or "").strip(),
        "estado": (reg.get("estes") or "").strip(),
        "color": (reg.get("color") or "#555").strip(),
    }


def _fetch(iata, movtp, fecha):
    url = f"{API}?c=200&idarpt={iata}&movtp={movtp}&f={fecha}"
    data = _req(url)
    vuelos = [_mapear(r) for r in data] if isinstance(data, list) else []
    # ordenar por hora programada
    vuelos.sort(key=lambda v: v["hora"])
    return vuelos


def main():
    ahora = datetime.datetime.now(TZ)
    fecha = ahora.strftime("%d-%m-%Y")
    aeropuertos = {}
    errores = 0
    for iata, nombre in AEROPUERTOS.items():
        try:
            arribos = _fetch(iata, "A", fecha)
            partidas = _fetch(iata, "D", fecha)
        except (urllib.error.URLError, ValueError, TimeoutError) as e:
            print(f"[vuelos] ERROR {iata}: {e}", file=sys.stderr)
            errores += 1
            continue
        aeropuertos[iata] = {
            "nombre": nombre,
            "arribos": arribos,
            "partidas": partidas,
        }
        print(f"[vuelos] {iata} {nombre}: {len(arribos)} arribos, {len(partidas)} partidas")
    if not aeropuertos:
        print("[vuelos] sin datos de ningún aeropuerto, no se escribe el archivo", file=sys.stderr)
        return 1
    out = {
        "fuente": "Aeropuertos Argentina",
        "actualizado": ahora.isoformat(timespec="minutes"),
        "aeropuertos": aeropuertos,
    }
    with open(SALIDA, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"[vuelos] {len(aeropuertos)} aeropuertos -> {SALIDA}")
    # Falla solo si TODO falló; algunos aeropuertos chicos pueden no tener vuelos hoy
    return 0


if __name__ == "__main__":
    sys.exit(main())
