#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publica el tablero 'Parte de nieve' en Turismo (turismo.json) con cuerpo
completo en historial.json. Uso:
    python3 _scripts/publicar_parte_nieve.py --preview   → PREVIEW en Desktop
    python3 _scripts/publicar_parte_nieve.py             → publica ES en JSONs
Las variantes -en/-pt/-zh se generan con _scripts/_gen_variantes_nieve.py."""
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NID = "parte-de-nieve-patagonia"
IMG = "fotos/DEPORTES/CENTROS_SKY/"

CSS = "<style>.nv-kick{display:block;font-family:'Playfair Display',serif;font-weight:900;font-size:clamp(38px,7vw,66px);line-height:1.05;letter-spacing:-1px;color:#1c2d3d}.nv-sub{display:block;font-family:'Playfair Display',serif;font-weight:600;font-size:clamp(20px,3.4vw,32px);line-height:1.25;color:#4a5561;margin-top:10px}.ski-table{width:100%;border-collapse:collapse;margin:24px 0 8px;font-size:14px;border-radius:6px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.08)}.ski-table thead tr{background:#1c2d3d;color:#fff;text-align:left}.ski-table thead th{padding:12px 16px;font-weight:700;font-size:11px;letter-spacing:1px;text-transform:uppercase}.ski-table tbody tr:nth-child(even){background:#fff}.ski-table tbody tr:nth-child(odd){background:#f7f5f0}.ski-table tbody td{padding:11px 16px;color:#2a2a2a;border-bottom:1px solid #e8e5e0}.ski-table td strong{color:#1c2d3d}.ski-table a{color:#1c2d3d;font-weight:600}.c4-card{display:flex;gap:18px;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 2px 10px rgba(28,45,61,.1);margin:22px 0}.c4-card img{width:38%;object-fit:cover;min-height:220px}.c4-card .c4-body{padding:18px 18px 18px 0;flex:1}.c4-card h4{font-family:'Playfair Display',serif;color:#1c2d3d;font-size:18px;margin:0 0 8px}.c4-chips{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}.c4-chip{background:#f0ede8;border:1px solid #7aadcc;color:#1c2d3d;font-size:12px;font-weight:600;padding:3px 10px;border-radius:20px}.c4-nota{background:#fff8ec;border-left:4px solid #8c6b4a;padding:14px 18px;border-radius:0 8px 8px 0;font-size:15px;margin:22px 0}.nv-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:20px 0}.nv-card{background:#fff;border-radius:10px;padding:14px 16px;box-shadow:0 2px 10px rgba(28,45,61,.1);border-top:3px solid #7aadcc}.nv-card h5{font-family:'Playfair Display',serif;color:#1c2d3d;font-size:16px;margin:0 0 2px;display:flex;justify-content:space-between;align-items:center;gap:8px}.nv-reg{font-family:Inter,sans-serif;font-size:11px;color:#888;font-weight:400;margin-bottom:10px}.nv-temp{font-size:14px;font-weight:700;color:#1c2d3d;white-space:nowrap}.nv-row{display:flex;justify-content:space-between;font-size:13px;padding:4px 0;border-bottom:1px dashed #e8e5e0;color:#444}.nv-row:last-child{border-bottom:none}.nv-row b{color:#1c2d3d}.nv-next{font-size:12px;color:#8c6b4a;font-weight:600;margin-top:8px}.nv-upd{font-size:12px;color:#888;margin:4px 0 0}.nv-fall{background:#f7f5f0;border-radius:8px;padding:16px;font-size:14px;color:#555}@media(max-width:820px){.nv-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:640px){.nv-grid{grid-template-columns:1fr}.c4-card{flex-direction:column}.c4-card img{width:100%}.c4-card .c4-body{padding:16px}}</style>"

# ---------------- Tablero en vivo (JS, un solo bloque sin líneas vacías) ----
WIDGET = """<div id="nv-live"><div class="nv-fall">❄ Cargando el parte de nieve en vivo… Si no aparece, usá los partes oficiales de cada centro, más abajo en esta página.</div></div>
<script>/* gp-nieve-live */(function(){
var C=[["Cerro Catedral","🇦🇷 Bariloche · Río Negro",-41.17,-71.44,1400],
["Chapelco","🇦🇷 San Martín de los Andes · Neuquén",-40.24,-71.30,1500],
["Cerro Bayo","🇦🇷 Villa La Angostura · Neuquén",-40.75,-71.59,1400],
["Caviahue","🇦🇷 Caviahue · Neuquén",-37.88,-71.03,1900],
["La Hoya","🇦🇷 Esquel · Chubut",-42.93,-71.26,1600],
["Cerro Castor","🇦🇷 Ushuaia · Tierra del Fuego",-54.73,-68.02,600],
["Perito Moreno","🇦🇷 El Bolsón · Río Negro",-41.96,-71.54,1200],
["Corralco","🇨🇱 Volcán Lonquimay · La Araucanía",-38.43,-71.55,1600],
["Antillanca","🇨🇱 Volcán Casablanca · Los Lagos",-40.77,-72.21,1200],
["Volcán Osorno","🇨🇱 Puerto Varas · Los Lagos",-41.13,-72.49,1300],
["Cerro Mirador","🇨🇱 Punta Arenas · Magallanes",-53.16,-71.07,500]];
var WC={0:"☀️",1:"🌤",2:"⛅",3:"☁️",45:"🌫",48:"🌫",51:"🌦",53:"🌦",55:"🌦",61:"🌧",63:"🌧",65:"🌧",66:"🌧",67:"🌧",71:"🌨",73:"🌨",75:"❄️",77:"🌨",80:"🌧",81:"🌧",82:"🌧",85:"🌨",86:"❄️",95:"⛈"};
var DIAS=["dom","lun","mar","mié","jue","vie","sáb"];
var u="https://api.open-meteo.com/v1/forecast?latitude="+C.map(function(c){return c[2]}).join(",")+"&longitude="+C.map(function(c){return c[3]}).join(",")+"&elevation="+C.map(function(c){return c[4]}).join(",")+"&current=temperature_2m,wind_speed_10m,weather_code&hourly=snow_depth&daily=snowfall_sum&past_days=3&forecast_days=7&timezone=auto";
fetch(u).then(function(r){return r.json()}).then(function(data){
if(!Array.isArray(data))data=[data];
var h="";
data.forEach(function(d,i){
var sd=(d.hourly&&d.hourly.snow_depth||[]).filter(function(x){return x!=null});
var piso=sd.length?Math.round(sd[sd.length-1]*100):null;
var day=d.daily.snowfall_sum;
var cayo=Math.round((day[0]||0)+(day[1]||0)+(day[2]||0));
var viene=0;for(var k=3;k<day.length;k++)viene+=day[k]||0;viene=Math.round(viene);
var prox="sin nevadas a la vista";
for(var k=3;k<day.length;k++){if((day[k]||0)>=1){var dt=new Date(d.daily.time[k]+"T12:00:00");prox=(k===3?"hoy":DIAS[dt.getDay()]+" "+dt.getDate())+" ("+Math.round(day[k])+" cm)";break}}
var cur=d.current||{};
var emo=WC[cur.weather_code]||"";
h+='<div class="nv-card"><h5>'+C[i][0]+'<span class="nv-temp">'+emo+" "+Math.round(cur.temperature_2m)+'°C</span></h5><div class="nv-reg">'+C[i][1]+'</div>';
h+='<div class="nv-row"><span>Nieve en el suelo</span><b>'+(piso!=null?piso+" cm":"s/d")+'</b></div>';
h+='<div class="nv-row"><span>Nevó (últ. 72 h)</span><b>'+cayo+" cm</b></div>";
h+='<div class="nv-row"><span>Viene (próx. 7 días)</span><b>'+viene+" cm</b></div>";
h+='<div class="nv-row"><span>Viento ahora</span><b>'+Math.round(cur.wind_speed_10m)+' km/h</b></div>';
h+='<div class="nv-next">❄ Próxima nevada: '+prox+"</div></div>";
});
var f=new Date();
h='<div class="nv-grid">'+h+'</div><div class="nv-upd">Actualizado el '+f.toLocaleDateString("es-AR")+" a las "+f.toLocaleTimeString("es-AR",{hour:"2-digit",minute:"2-digit",hour12:false})+" h · Datos: modelo Open-Meteo a cota media de cada centro. El parte oficial de cada cerro manda.</div>";
document.getElementById("nv-live").innerHTML=h;
}).catch(function(){});
})();</script>"""


def card(img, alt, titulo, chips, texto, links, pos=None):
    ch = "".join(f'<span class="c4-chip">{c}</span>' for c in chips)
    ln = " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in links)
    st = f' style="object-position:{pos}"' if pos else ""
    return (f'<div class="c4-card"><img src="{IMG}{img}" alt="{alt}" loading="lazy"{st}>'
            f'<div class="c4-body"><h4>{titulo}</h4><div class="c4-chips">{ch}</div>'
            f'<p style="font-size:15px;margin:0 0 10px">{texto}</p>'
            f'<p style="font-size:14px;margin:0">🔗 {ln}</p></div></div>')


def tabla(headers, filas):
    th = "".join(f"<th>{h}</th>" for h in headers)
    tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>" for f in filas)
    return f'<table class="ski-table"><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>'


# ============================== ESPAÑOL ==============================
cuerpo_es = "\n\n".join([
    CSS,
    "<p>¿Hay nieve hoy en el Catedral? ¿Cómo están las pistas de Chapelco? ¿Cuándo llega la próxima nevada? Esta página responde esas preguntas <b>todos los días de la temporada</b>: el tablero de abajo muestra cuánta nieve hay en el suelo, cuánto nevó en las últimas 72 horas y cuánto viene en camino en <b>11 centros de ski de la Patagonia argentina y chilena</b> — con datos meteorológicos que se actualizan solos cada vez que abrís la página, más las webcams y los partes oficiales de cada cerro.</p>",
    "<h3>❄ El tablero de nieve, centro por centro</h3>",
    WIDGET,
    '<div class="c4-nota">💡 <b>Cómo leerlo:</b> "Nieve en el suelo" es la estimación del modelo meteorológico a media montaña — sirve para comparar cerros y seguir la tendencia, pero la palabra final la tiene el <b>parte diario oficial</b> de cada centro (los links están en las fichas de abajo). Antes de salir a la ruta, mirá también el <a href="../conectividad.html#rutas">estado de las rutas</a> y los <a href="../conectividad.html#pasos">pasos a Chile</a>.</div>',
    "<h3>Los centros argentinos, uno por uno</h3>",
    card("CATEDRAL.webp", "Pistas y medios de elevación del Cerro Catedral, Bariloche",
         "Cerro Catedral — Bariloche", ["Base 1.030 m · Cumbre ~2.100 m", "~120 km de pistas", "El mayor del hemisferio sur"],
         "El gigante de Sudamérica, a 19 km de Bariloche. La cota baja sufre en inviernos flojos, pero de media montaña hacia arriba la temporada es larga y los medios sobran. Si vas por primera vez, empezá por nuestra <a href=\"cerro-catedral-ski-2026.html\">guía completa del Catedral</a>.",
         [("Parte de nieve oficial", "https://catedralaltapatagonia.com/parte-de-nieve/"), ("Webcams", "https://catedralaltapatagonia.com/webcams/")]),
    card("CHAPELCO.webp", "Esquiadores en el cerro Chapelco, San Martín de los Andes",
         "Chapelco — San Martín de los Andes", ["Base 1.243 m · Cumbre 1.980 m", "140 ha esquiables", "Bosque de lengas"],
         "Pistas entre bosques y vista al volcán Lanín, a 19 km de San Martín de los Andes. Base alta: retiene bien la nieve. Si es tu primer día sobre esquíes, al lado está <a href=\"c4-parque-nieve-2026.html\">C4 Parque de Nieve</a>, pensado solo para principiantes.",
         [("Sitio oficial, parte y webcams", "https://www.chapelco.com.ar/")]),
    card("BAYO2.webp", "Vista del lago Nahuel Huapi desde las pistas del Cerro Bayo",
         "Cerro Bayo — Villa La Angostura", ["Base 1.050 m · Cumbre 1.782 m", "Centro boutique", "Vista al Nahuel Huapi"],
         "El centro chico y cuidado de Villa La Angostura, con la postal del lago Nahuel Huapi bajo los esquíes. Menos multitudes que sus vecinos grandes; ideal para ir en familia y esquiar con calma.",
         [("Sitio oficial y parte de nieve", "https://cerrobayoweb.com/")]),
    card("CAVIAHUE.webp", "Nieve y araucarias en Caviahue, al pie del volcán Copahue",
         "Caviahue — Norte neuquino", ["Base ~1.650 m · Volcán Copahue", "Araucarias milenarias", "Termas a minutos"],
         "El secreto del norte neuquino: base altísima, de las que más nieve juntan en la provincia, y un paisaje único de araucarias y volcán. A minutos, las termas de Copahue para cerrar el día.",
         [("Sitio oficial", "https://www.caviahue.com/")]),
    card("HOYA.webp", "Nieve seca en el cerro La Hoya, Esquel",
         "La Hoya — Esquel", ["Base ~1.350 m · Cumbre ~2.050 m", "Nieve seca famosa", "Orientación sur"],
         "La joya de Chubut: su orientación sur conserva la nieve seca y en polvo que la hizo famosa, y la temporada suele estirarse cuando otros cierran. Precios más amables que en los centros grandes.",
         [("Parte de nieve oficial", "https://skilahoya.com/parte-de-nieve/"), ("Sitio oficial", "https://skilahoya.com/")]),
    card("CERROCASTOR.webp", "Pistas del Cerro Castor entre bosques fueguinos, Ushuaia",
         "Cerro Castor — Ushuaia", ["Base 195 m · Cumbre ~1.000 m", "El más austral del mundo", "Temporada más larga de AR"],
         "A 26 km de Ushuaia, el centro de ski más austral del planeta. La latitud reemplaza a la altura: frío parejo, nieve de calidad de junio a octubre y la temporada más larga de la Argentina.",
         [("Sitio oficial y parte de nieve", "https://www.cerrocastor.com/")]),
    "<h3>Del lado chileno</h3>",
    "<p>La Patagonia chilena también esquía, de La Araucanía a Magallanes — casi siempre sobre volcanes:</p>",
    tabla(["Centro", "Dónde", "Perfil", "Parte oficial"], [
        ["<strong>Corralco</strong>", "Volcán Lonquimay · La Araucanía", "El grande del sur chileno: nieve en polvo y araucarias en la Reserva Malalcahuello", '<a href="https://www.corralco.com/" target="_blank" rel="noopener">corralco.com</a>'],
        ["<strong>Antillanca</strong>", "Volcán Casablanca · Los Lagos", "En el Parque Nacional Puyehue, con termas cerca; ambiente familiar", '<a href="https://antillanca.cl/" target="_blank" rel="noopener">antillanca.cl</a>'],
        ["<strong>Volcán Osorno</strong>", "Puerto Varas · Los Lagos", "Centro chico con la mejor vista: el lago Llanquihue entero bajo las pistas", '<a href="https://volcanosorno.cl/" target="_blank" rel="noopener">volcanosorno.cl</a>'],
        ["<strong>Cerro Mirador</strong>", "Punta Arenas · Magallanes", "Del Club Andino de Punta Arenas: uno de los pocos del mundo donde se esquía mirando el mar (Estrecho de Magallanes)", '<a href="https://clubandino.cl/" target="_blank" rel="noopener">clubandino.cl</a>'],
    ]),
    "<h3>Comparativa rápida: alturas y perfil</h3>",
    "<p>La altura de la base es el mejor predictor de nieve segura — cuanto más alta (o más austral), menos riesgo de pistas peladas:</p>",
    tabla(["Centro", "Base → Cumbre", "Su punto fuerte"], [
        ["🇦🇷 <strong>Cerro Catedral</strong>", "1.030 → ~2.100 m", "Tamaño: el mayor del hemisferio sur"],
        ["🇦🇷 <strong>Chapelco</strong>", "1.243 → 1.980 m", "Base alta + bosque + Lanín de fondo"],
        ["🇦🇷 <strong>Cerro Bayo</strong>", "1.050 → 1.782 m", "Boutique, sin multitudes"],
        ["🇦🇷 <strong>Caviahue</strong>", "~1.650 → ~2.000 m", "La base más alta de la Patagonia argentina"],
        ["🇦🇷 <strong>La Hoya</strong>", "~1.350 → ~2.050 m", "Nieve seca, temporada larga"],
        ["🇦🇷 <strong>Cerro Castor</strong>", "195 → ~1.000 m", "Latitud: frío parejo y temporada récord"],
        ["🇦🇷 <strong>Perito Moreno</strong>", "~900 → ~1.450 m", "El cerro de El Bolsón, en crecimiento"],
        ["🇨🇱 <strong>Corralco</strong>", "~1.500 → ~2.300 m", "Nieve en polvo sobre el volcán Lonquimay"],
        ["🇨🇱 <strong>Antillanca</strong>", "~1.050 → ~1.500 m", "Parque nacional + termas"],
        ["🇨🇱 <strong>Volcán Osorno</strong>", "~1.200 → ~1.670 m", "La vista al lago Llanquihue"],
        ["🇨🇱 <strong>Cerro Mirador</strong>", "~300 → ~600 m", "Esquiar mirando el Estrecho de Magallanes"],
    ]),
    '<div class="c4-nota">🧳 <b>Para planear el viaje:</b> el pronóstico extendido ciudad por ciudad está en nuestras páginas de clima (<a href="../clima-bariloche.html">Bariloche</a>, <a href="../clima-ushuaia.html">Ushuaia</a>, <a href="../clima-esquel.html">Esquel</a>), los vuelos y el estado de rutas y pasos fronterizos en <a href="../conectividad.html">Conectividad Patagónica</a>, y si venís de Chile o Brasil, el cambio del día en <a href="../cotizaciones.html">Divisas</a>.</div>',
    "<p><i>Datos meteorológicos: Open-Meteo (modelo a cota media de cada centro, actualización continua). Alturas y datos de cada centro: sitios oficiales. Esta página no reemplaza al parte diario oficial de cada cerro.</i></p>",
])

# H1 visual en dos niveles (se inyecta en la página estática al generarla;
# el titulo plano queda para <title>, og:title y cards del index)
H1_HTML = '<span class="nv-kick">¡LLEGÓ LA NIEVE!</span><span class="nv-sub">así están los principales centros de la Patagonia</span>'

entrada_historial = {
    "id": NID,
    "titulo": "¡Llegó la nieve! Así están los principales centros de la Patagonia",
    "bajada": "¿Hay nieve en el Catedral? ¿Cómo están las pistas de Chapelco? ¿Cuándo nieva de nuevo? El tablero de nieve de GLOBALpatagonia sigue en vivo 11 centros de ski de la Patagonia argentina y chilena: nieve en el suelo, lo que cayó, lo que viene — más webcams y partes oficiales de cada cerro. Se actualiza solo, todos los días de la temporada.",
    "cuerpo": cuerpo_es,
    "tag": "⛷ Turismo",
    "categoria": "turismo",
    "fuente": "GLOBALpatagonia",
    "url_original": "https://globalpatagonia.org/notas/parte-de-nieve-patagonia.html",
    "pais": "argentina",
    "imagen": f"{IMG}catedral-nieve.webp",
    "fecha": "2026-07-11",
    "meta": "Parte diario · GLOBALpatagonia",
    "excluir_feed": True,
    "galeria": [],
}

entrada_turismo = {
    "id": NID,
    "badge": "TURISMO",
    "titulo": entrada_historial["titulo"],
    "bajada": entrada_historial["bajada"],
    "imagen": entrada_historial["imagen"],
    "meta": "Parte diario · GLOBALpatagonia",
    "excluir_feed": True,
}


# ============================== PREVIEW ==============================
if "--preview" in sys.argv:
    site = "https://globalpatagonia.org/"
    body = cuerpo_es.replace(f'src="{IMG}', f'src="{site}{IMG}')
    body = body.replace('href="../', f'href="{site}')
    body = body.replace('href="cerro-catedral-ski-2026.html', f'href="{site}notas/cerro-catedral-ski-2026.html')
    body = body.replace('href="c4-parque-nieve-2026.html', f'href="{site}notas/c4-parque-nieve-2026.html')
    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>PREVIEW — {entrada_historial['titulo']}</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>body{{font-family:Inter,sans-serif;background:#f0ede8;margin:0;padding:30px 16px;color:#2a2a2a;line-height:1.6}}
.wrap{{max-width:860px;margin:0 auto}}h1{{font-family:'Playfair Display',serif;color:#1c2d3d;font-size:52px;font-weight:800;line-height:1.12;letter-spacing:-0.5px}}
h3{{font-family:'Playfair Display',serif;color:#1c2d3d;font-size:24px;margin-top:34px}}
.bajada{{font-size:17px;color:#555}}.pv{{background:#8c6b4a;color:#fff;display:inline-block;padding:4px 14px;border-radius:20px;font-size:12px;font-weight:700;letter-spacing:1px}}
img.hero{{width:100%;border-radius:10px;margin:18px 0}}</style></head><body><div class="wrap">
<span class="pv">PREVIEW — así se vería la nota</span>
<h1 style="margin:18px 0 6px">{H1_HTML}</h1>
<p class="bajada">{entrada_historial['bajada']}</p>
<img class="hero" src="{site}{IMG}catedral-nieve.webp" alt="portada">
{body}
</div></body></html>"""
    out = os.path.expanduser("~/Desktop/PREVIEW_parte_nieve.html")
    open(out, "w", encoding="utf-8").write(html)
    print(f"Preview → {out}")
    sys.exit(0)


# ============================== PUBLICAR ==============================
path_t = os.path.join(BASE, "turismo.json")
turismo = json.load(open(path_t, encoding="utf-8"))
turismo = [n for n in turismo if n.get("id") != NID]
turismo.insert(0, entrada_turismo)
while len(turismo) > 7:
    quitada = turismo.pop()
    print(f"Rotada fuera de turismo.json: {quitada['id']} (su página estática sigue viva)")
json.dump(turismo, open(path_t, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"turismo.json → {NID} en slot principal ({len(turismo)} activos)")

path_h = os.path.join(BASE, "historial.json")
historial = json.load(open(path_h, encoding="utf-8"))
historial = [n for n in historial if n.get("id") != NID]
historial.insert(0, entrada_historial)
json.dump(historial, open(path_h, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"historial.json → cuerpo completo ({len(historial)} notas)")
