#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Borrador de reposición de agenda.json (14/10/2026). Fuente de fechas: calendariodecarreras.ar/sur
# y Diario Río Negro (Lúpulo). NO modifica agenda.json: genera preview en el Escritorio.
import json, html
N = lambda i,t,f,ff,disp,lug,reg,pais,cat,em,desc: dict(id=i,titulo=t,fecha=f,fecha_fin=ff,fecha_display=disp,lugar=lug,region=reg,pais=pais,categoria=cat,emoji=em,descripcion=desc)
NUEVOS = [
 N("ultra-fitz-roy-el-chalten-2026","Ultra Fitz Roy","2026-10-16",None,"16 de octubre","El Chaltén","Santa Cruz, Argentina","AR","deportes","🏔️","Carrera de montaña al pie del Fitz Roy con distancias de 100, 70, 42, 21 y 10 km."),
 N("k42-villa-la-angostura-2026","K42 Villa La Angostura","2026-11-05",None,"5 de noviembre","Villa La Angostura","Neuquén, Argentina","AR","deportes","🏃","Maratón de montaña con distancias de 42 km, 2x21, 21 y 10 km en la región de los siete lagos."),
 N("patagonia-bariloche-utmb-2026","Patagonia Bariloche by UTMB","2026-11-18",None,"18 de noviembre","San Carlos de Bariloche","Río Negro, Argentina","AR","deportes","⛰️","Trail running bajo el sello UTMB con distancias de 132, 86, 57, 36, 22 y 12 km."),
 N("gran-fondo-7-lagos-2026","Gran Fondo 7 Lagos","2026-11-21",None,"21 de noviembre","San Martín de los Andes","Neuquén, Argentina","AR","deportes","🚴","Prueba de ciclismo de 110 km por el circuito de los Siete Lagos."),
 N("el-cruce-la-etapa-2026","El Cruce y La Etapa","2026-12-05",None,"5 de diciembre","San Carlos de Bariloche","Río Negro, Argentina","AR","deportes","🏃","Dos carreras de montaña en la cordillera: El Cruce de 100 km y La Etapa de 33 y 15 km."),
 N("ushuaia-trail-race-2026","Ushuaia Trail Race","2026-12-11",None,"11 de diciembre","Ushuaia","Tierra del Fuego, Argentina","AR","deportes","🏃","Trail running en el fin del mundo con distancias de 42, 21, 15 y 9 km."),
 N("desafio-wayra-el-bolson-2026","Desafío Wayra","2026-12-12",None,"12 de diciembre","El Bolsón","Río Negro, Argentina","AR","deportes","⛰️","Carrera de montaña en la Comarca Andina con distancias de 50, 35, 25, 15 y 8 km, categorías infantiles y kilómetro vertical."),
 N("lanin-extremo-2027","Lanín Extremo","2027-02-13",None,"13 de febrero de 2027","Junín de los Andes","Neuquén, Argentina","AR","deportes","🌋","Trail running al pie del volcán Lanín con distancias de 33, 21, 15 y 6 km."),
 N("la-mision-race-villa-la-angostura-2027","La Misión Race","2027-02-18",None,"18 de febrero de 2027","Villa La Angostura","Neuquén, Argentina","AR","deportes","🏃","Ultra trail con distancias de 200, 160, 120, 80, 60 y 40 km."),
 N("fiesta-nacional-del-lupulo-2027","49° Fiesta Nacional del Lúpulo","2027-02-18","2027-02-21","18 al 21 de febrero de 2027","El Bolsón","Río Negro, Argentina","AR","gastronomia","🍺","Cuatro jornadas de fiesta popular y gratuita en la Comarca Andina, con el tradicional circuito de cerveza artesanal, espacios gastronómicos y artistas regionales."),
 N("cuatro-refugios-bariloche-2027","4 Refugios","2027-02-26",None,"26 de febrero de 2027","San Carlos de Bariloche","Río Negro, Argentina","AR","deportes","🏔️","Clásica travesía de montaña entre refugios de Bariloche con distancias de 41, 39, 31, 14 y 5,6 km."),
 N("bariloche100-ultra-trail-2027","Bariloche100 Ultra Trail","2027-03-12",None,"12 de marzo de 2027","San Carlos de Bariloche","Río Negro, Argentina","AR","deportes","⛰️","Ultra trail con distancias de 100, 80, 57, 42, 27 y 12 km."),
]
NUEVOS += [
 N("claudio-gabis-bariloche-2026","Claudio Gabis en Bariloche","2026-10-16",None,"16 de octubre, 21 h","Bariloche","Río Negro, Argentina","AR","cultura","🎸","El guitarrista histórico del blues y el rock argentino se presenta en la ciudad."),
 N("javier-malosetti-trio-bariloche-2026","Javier Malosetti Trío","2026-10-17",None,"17 de octubre","Bariloche","Río Negro, Argentina","AR","cultura","🎷","El bajista y compositor presenta su formato trío en Bariloche."),
 N("noche-garcia-bariloche-2026","Noche García: 75 años de Charly","2026-10-23",None,"23 de octubre","Bariloche","Río Negro, Argentina","AR","cultura","🎹","Noche en homenaje a Charly García por su cumpleaños número 75."),
 N("rossini-pequena-misa-solemne-camba-2026","Rossini: Pequeña Misa Solemne","2026-10-31",None,"31 de octubre","CAMBA, Bariloche","Río Negro, Argentina","AR","cultura","🎼","Concierto con la Pequeña Misa Solemne de Rossini en el Centro Cultural CAMBA."),
 N("inti-illimani-puerto-varas-2026","Inti-Illimani en Puerto Varas","2026-11-07",None,"7 de noviembre","Puerto Varas","Región de Los Lagos, Chile","CL","cultura","🪕","El grupo emblema de la nueva canción chilena se presenta en Dreams Puerto Varas."),
 N("ciro-y-los-persas-bariloche-2026","Ciro y los Persas en Bariloche","2026-11-11",None,"11 de noviembre","Bariloche","Río Negro, Argentina","AR","cultura","🎸","Show de la banda liderada por Ciro Pertusi en Bariloche."),
 N("casi-presente-puerto-madryn-2026","Casi Presente","2026-11-14",None,"14 de noviembre, 21 h","Teatro del Muelle, Puerto Madryn","Chubut, Argentina","AR","cultura","🎭","Función teatral en el Teatro del Muelle de Puerto Madryn."),
 N("festival-muy-tango-bariloche-2026","Festival Muy Tango","2026-11-13","2026-11-15","13 al 15 de noviembre","Bariloche","Río Negro, Argentina","AR","cultura","💃","Tres jornadas de tango con shows y bailes en la ciudad."),
 N("fernando-ubiergo-puerto-varas-2026","Fernando Ubiergo en Puerto Varas","2026-12-06",None,"6 de diciembre","Puerto Varas","Región de Los Lagos, Chile","CL","cultura","🎤","El cantautor chileno se presenta en Dreams Puerto Varas; el 10 de diciembre toca en Valdivia."),
 N("purga-ushuaia-2026","Purga","2026-12-17",None,"17 de diciembre, 21 h","Sala Niní Marshall, Ushuaia","Tierra del Fuego, Argentina","AR","cultura","🎭","Espectáculo en la Sala Niní Marshall de Ushuaia."),
 N("ciro-y-los-persas-comodoro-2026","Ciro y los Persas en Comodoro Rivadavia","2026-12-16",None,"16 de diciembre, 21 h","Predio Ferial, Comodoro Rivadavia","Chubut, Argentina","AR","cultura","🎸","Show de la banda en el Predio Ferial de la ciudad petrolera."),
 N("francisca-valenzuela-punta-arenas-2026","Francisca Valenzuela en Punta Arenas","2026-12-18",None,"18 de diciembre","Punta Arenas","Región de Magallanes, Chile","CL","cultura","🎹","La cantautora chilena se presenta en Dreams Punta Arenas."),
 N("mac-mcclure-teatro-del-lago-2027","Mac McClure en Teatro del Lago","2027-01-29",None,"29 de enero de 2027","Frutillar","Región de Los Lagos, Chile","CL","cultura","🎻","Concierto del músico chileno en el Teatro del Lago, a orillas del lago Llanquihue."),
 N("fiesta-nacional-de-la-confluencia-2027","14° Fiesta Nacional de la Confluencia","2027-02-11","2027-02-14","11 al 14 de febrero de 2027","Isla 132, Neuquén","Neuquén, Argentina","AR","cultura","🎶","Cuatro jornadas del mayor festival de la Patagonia, fijadas por decreto municipal. La grilla de artistas aún no fue anunciada."),
]
existentes = json.load(open("agenda.json", encoding="utf-8"))
ids = {e["id"] for e in existentes}
total = sorted(existentes + [n for n in NUEVOS if n["id"] not in ids], key=lambda e: e["fecha"])
json.dump(total, open("_scripts/_borrador_agenda_oct2026.json","w",encoding="utf-8"), ensure_ascii=False, indent=2)
rows = "".join(f"<tr><td>{html.escape(e['fecha_display'])}</td><td>{e['emoji']} <b>{html.escape(e['titulo'])}</b><br><small>{html.escape(e['descripcion'])}</small></td><td>{html.escape(e['lugar'])}<br><small>{html.escape(e['region'])}</small></td><td>{e['categoria']}</td></tr>" for e in total)
open("/Users/jm/Desktop/PREVIEW_agenda.html","w",encoding="utf-8").write(f"""<!doctype html><meta charset=utf-8><title>PREVIEW agenda</title>
<style>body{{font:15px/1.5 system-ui;background:#f0ede8;color:#252830;max-width:900px;margin:2rem auto;padding:0 1rem}}table{{border-collapse:collapse;width:100%}}td{{border-bottom:1px solid #ccc;padding:.6rem;vertical-align:top}}.b{{background:#8c6b4a;color:#fff;padding:.5rem;text-align:center}}</style>
<div class=b>PREVIEW — NO PUBLICADO · {len(total)} eventos ({len(existentes)} actuales + {len(total)-len(existentes)} nuevos)</div><table>{rows}</table>""")
print(len(existentes), "->", len(total))
