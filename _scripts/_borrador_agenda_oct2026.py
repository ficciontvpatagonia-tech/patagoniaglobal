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
 N("claudio-gabis-bariloche-2026","Claudio Gabis en Bariloche","2026-10-16",None,"16 de octubre, 21 h","Bariloche","Río Negro, Argentina","AR","musica","🎸","El guitarrista histórico del blues y el rock argentino se presenta en la ciudad."),
 N("javier-malosetti-trio-bariloche-2026","Javier Malosetti Trío","2026-10-17",None,"17 de octubre","Bariloche","Río Negro, Argentina","AR","musica","🎷","El bajista y compositor presenta su formato trío en Bariloche."),
 N("noche-garcia-bariloche-2026","Noche García: 75 años de Charly","2026-10-23",None,"23 de octubre","Bariloche","Río Negro, Argentina","AR","musica","🎹","Noche en homenaje a Charly García por su cumpleaños número 75."),
 N("rossini-pequena-misa-solemne-camba-2026","Rossini: Pequeña Misa Solemne","2026-10-31",None,"31 de octubre","CAMBA, Bariloche","Río Negro, Argentina","AR","musica","🎼","Concierto con la Pequeña Misa Solemne de Rossini en el Centro Cultural CAMBA."),
 N("inti-illimani-puerto-varas-2026","Inti-Illimani en Puerto Varas","2026-11-07",None,"7 de noviembre","Puerto Varas","Región de Los Lagos, Chile","CL","musica","🪕","El grupo emblema de la nueva canción chilena se presenta en Dreams Puerto Varas."),
 N("ciro-y-los-persas-bariloche-2026","Ciro y los Persas en Bariloche","2026-11-11",None,"11 de noviembre","Bariloche","Río Negro, Argentina","AR","musica","🎸","Show de la banda liderada por Ciro Pertusi en Bariloche."),
 N("casi-presente-puerto-madryn-2026","Casi Presente","2026-11-14",None,"14 de noviembre, 21 h","Teatro del Muelle, Puerto Madryn","Chubut, Argentina","AR","cultura","🎭","Función teatral en el Teatro del Muelle de Puerto Madryn."),
 N("festival-muy-tango-bariloche-2026","Festival Muy Tango","2026-11-13","2026-11-15","13 al 15 de noviembre","Bariloche","Río Negro, Argentina","AR","cultura","💃","Tres jornadas de tango con shows y bailes en la ciudad."),
 N("fernando-ubiergo-puerto-varas-2026","Fernando Ubiergo en Puerto Varas","2026-12-06",None,"6 de diciembre","Puerto Varas","Región de Los Lagos, Chile","CL","musica","🎤","El cantautor chileno se presenta en Dreams Puerto Varas; el 10 de diciembre toca en Valdivia."),
 N("purga-ushuaia-2026","Purga","2026-12-17",None,"17 de diciembre, 21 h","Sala Niní Marshall, Ushuaia","Tierra del Fuego, Argentina","AR","cultura","🎭","Espectáculo en la Sala Niní Marshall de Ushuaia."),
 N("ciro-y-los-persas-comodoro-2026","Ciro y los Persas en Comodoro Rivadavia","2026-12-16",None,"16 de diciembre, 21 h","Predio Ferial, Comodoro Rivadavia","Chubut, Argentina","AR","musica","🎸","Show de la banda en el Predio Ferial de la ciudad petrolera."),
 N("francisca-valenzuela-punta-arenas-2026","Francisca Valenzuela en Punta Arenas","2026-12-18",None,"18 de diciembre","Punta Arenas","Región de Magallanes, Chile","CL","musica","🎹","La cantautora chilena se presenta en Dreams Punta Arenas."),
 N("mac-mcclure-teatro-del-lago-2027","Mac McClure en Teatro del Lago","2027-01-29",None,"29 de enero de 2027","Frutillar","Región de Los Lagos, Chile","CL","musica","🎻","Concierto del músico chileno en el Teatro del Lago, a orillas del lago Llanquihue."),
 N("fiesta-nacional-de-la-confluencia-2027","14° Fiesta Nacional de la Confluencia","2027-02-11","2027-02-14","11 al 14 de febrero de 2027","Isla 132, Neuquén","Neuquén, Argentina","AR","cultura","🎶","Cuatro jornadas del mayor festival de la Patagonia, fijadas por decreto municipal. La grilla de artistas aún no fue anunciada."),
]
AR = "Argentina"
F = lambda i,t,f,ff,disp,lug,reg,em,desc,cat="cultura": N(i,t,f,ff,disp,lug,f"{reg}, {AR}","AR",cat,em,desc)
NUEVOS += [
 # --- Fiestas con fecha exacta (viajoconvos.com.ar y guiadefiestas.com.ar) ---
 F("eisteddfod-del-chubut-2026","Eisteddfod del Chubut","2026-10-23","2026-10-24","23 y 24 de octubre","Trelew","Chubut","🎭","Tradicional certamen cultural galés de música, poesía y recitación en Trelew."),
 F("fiesta-provincial-cerveza-artesanal-alumine-octubre-2026","Fiesta Provincial de la Cerveza Artesanal","2026-10-23","2026-10-24","23 y 24 de octubre","Aluminé","Neuquén","🍺","Fiesta provincial de la cerveza artesanal en Aluminé.","gastronomia"),
 F("fiesta-provincial-del-pial-2026","Fiesta Provincial del Pial","2026-11-07","2026-11-08","7 y 8 de noviembre","Aguada San Roque","Neuquén","🐎","Fiesta provincial de tradición criolla en Aguada San Roque."),
 F("fiesta-nacional-del-chivito-chos-malal-2026","Fiesta Nacional del Chivito, la Danza y la Canción","2026-11-20","2026-11-22","20 al 22 de noviembre","Chos Malal","Neuquén","🎶","Fiesta nacional con música, danza y gastronomía del norte neuquino.","gastronomia"),
 F("fiesta-provincial-cerveza-artesanal-alumine-diciembre-2026","Fiesta Provincial de la Cerveza Artesanal (diciembre)","2026-12-04","2026-12-07","4 al 7 de diciembre","Aluminé","Neuquén","🍺","Segunda edición del año de la fiesta de la cerveza artesanal en Aluminé.","gastronomia"),
 F("fiesta-provincial-petroleo-energia-catriel-2026","Fiesta Provincial del Petróleo y la Energía","2026-12-05","2026-12-06","5 y 6 de diciembre","Catriel","Río Negro","🛢️","Fiesta provincial en Catriel dedicada a la actividad petrolera y energética."),
 F("fiesta-provincial-del-criancero-el-huecu-2026","Fiesta Provincial del Criancero","2026-12-06","2026-12-07","6 y 7 de diciembre","El Huecú","Neuquén","🐐","Fiesta provincial en homenaje al criancero del norte neuquino."),
 F("fiesta-nacional-del-petroleo-comodoro-2026","Fiesta Nacional del Petróleo","2026-12-12","2026-12-13","12 y 13 de diciembre","Comodoro Rivadavia","Chubut","🛢️","Fiesta nacional en la capital del petróleo, con espectáculos y actividades en la ciudad."),
 F("fiesta-nacional-de-la-actividad-fisica-cipolletti-2027","Fiesta Nacional de la Actividad Física","2027-03-05","2027-03-08","5 al 8 de marzo de 2027","Cipolletti","Río Negro","🏃","Fiesta nacional con actividades deportivas y recreativas en Cipolletti.","deportes"),
 F("fiesta-provincial-de-la-vendimia-villa-regina-2027","Fiesta Provincial de la Vendimia","2027-03-06","2027-03-08","6 al 8 de marzo de 2027","Villa Regina","Río Negro","🍇","Fiesta provincial de la vendimia en el Alto Valle.","gastronomia"),
 F("fiesta-nacional-del-tomate-lamarque-2027","Fiesta Nacional del Tomate y la Producción","2027-03-12","2027-03-15","12 al 15 de marzo de 2027","Lamarque","Río Negro","🍅","Fiesta nacional que celebra la producción rionegrina en Lamarque.","gastronomia"),
 F("fiesta-provincial-regreso-del-veranador-barrancas-2027","Fiesta Provincial Regreso del Veranador","2027-03-13","2027-03-15","13 al 15 de marzo de 2027","Barrancas","Neuquén","🐄","Fiesta provincial que celebra el regreso de los crianceros de las veranadas."),
 F("fiesta-nacional-del-curanto-bariloche-2027","Fiesta Nacional del Curanto","2027-03-22",None,"22 de marzo de 2027","Bariloche","Río Negro","🍲","Fiesta nacional del curanto, comida tradicional patagónica, en Bariloche.","gastronomia"),
 # --- Fiestas de verano 2027 con FECHA A CONFIRMAR (solo mes; fecha_fin = fin del rango posible para que no se purguen antes) ---
 F("fiesta-nacional-pescadores-del-sur-2027","Fiesta Nacional de los Pescadores del Sur","2027-01-10","2027-01-31","Mediados de enero de 2027 (fecha a confirmar)","Puerto Rawson","Chubut","🎣","Fiesta nacional de la actividad pesquera en Puerto Rawson, de tres jornadas.","gastronomia"),
 F("fiesta-nacional-de-la-esquila-rio-mayo-2027","Fiesta Nacional de la Esquila","2027-01-16","2027-01-31","Segunda quincena de enero de 2027 (fecha a confirmar)","Río Mayo","Chubut","🐑","Fiesta nacional con destreza de esquiladores, jineteadas y espectáculos en Río Mayo."),
 F("fiesta-nacional-de-la-fruta-fina-el-hoyo-2027","Fiesta Nacional de la Fruta Fina","2027-01-16","2027-01-31","Segunda quincena de enero de 2027 (fecha a confirmar)","El Hoyo","Chubut","🍓","Fiesta nacional de la fruta fina de la Comarca Andina, de tres jornadas.","gastronomia"),
 F("fiesta-nacional-del-salmon-camarones-2027","Fiesta Nacional del Salmón","2027-02-06","2027-02-07","Primer fin de semana de febrero de 2027 (fecha a confirmar)","Camarones","Chubut","🐟","Fiesta nacional del salmón en la costa chubutense.","gastronomia"),
 F("fiesta-nacional-tren-a-vapor-el-maiten-2027","Fiesta Nacional del Tren a Vapor","2027-02-12","2027-02-21","Mediados de febrero de 2027 (fecha a confirmar)","El Maitén","Chubut","🚂","Fiesta de tres días en torno a La Trochita, el tren a vapor patagónico."),
 F("fiesta-nacional-atlantico-sur-rawson-2027","Fiesta Nacional Atlántico Sur","2027-02-01","2027-02-28","Un fin de semana de febrero de 2027 (fecha a confirmar)","Rawson","Chubut","🎤","Festival popular en la costa del Chubut con música y espectáculos."),
 # --- Recitales en Neuquén (agregadores Bandsintown/Songkick; confirmar con boletería) ---
 F("tan-bionica-neuquen-2026","Tan Biónica en Neuquén","2026-11-07",None,"7 de noviembre","Neuquén Rugby Club, Neuquén","Neuquén","🎤","El grupo de pop rock se presenta en el Neuquén Rugby Club.","musica"),
 F("rata-blanca-neuquen-2026","Rata Blanca en Neuquén","2026-11-27",None,"27 de noviembre","Casino Magic, Neuquén","Neuquén","🤘","La banda de heavy metal argentina toca en Neuquén.","musica"),
 F("diego-torres-neuquen-2026","Diego Torres en Neuquén","2026-11-28",None,"28 de noviembre","Estadio Ruca Che, Neuquén","Neuquén","🎤","El cantante se presenta en el Estadio Ruca Che.","musica"),
 F("kamada-neuquen-2026","Kamada en Neuquén","2026-12-06",None,"6 de diciembre","Mood Live, Neuquén","Neuquén","🎤","La banda de rock presenta su show en Mood Live.","musica"),
]
existentes = json.load(open("agenda.json", encoding="utf-8"))
ids = {e["id"] for e in existentes}
total = sorted(existentes + [n for n in NUEVOS if n["id"] not in ids], key=lambda e: e["fecha"])
# Los eventos de música se publican con categoría propia "musica" (pedido de Marto 14/10/2026)
MUSICA = {n["id"] for n in NUEVOS if n["categoria"] == "musica"} | {
 "claudio-gabis-bariloche-2026","javier-malosetti-trio-bariloche-2026","noche-garcia-bariloche-2026",
 "rossini-pequena-misa-solemne-camba-2026","inti-illimani-puerto-varas-2026","ciro-y-los-persas-bariloche-2026",
"fernando-ubiergo-puerto-varas-2026","ciro-y-los-persas-comodoro-2026",
 "francisca-valenzuela-punta-arenas-2026","mac-mcclure-teatro-del-lago-2027"}
for e in total:
    if e["id"] in MUSICA:
        e["categoria"] = "musica"
json.dump(total, open("_scripts/_borrador_agenda_oct2026.json","w",encoding="utf-8"), ensure_ascii=False, indent=2)
rows = "".join(f"<tr><td>{html.escape(e['fecha_display'])}</td><td>{e['emoji']} <b>{html.escape(e['titulo'])}</b><br><small>{html.escape(e['descripcion'])}</small></td><td>{html.escape(e['lugar'])}<br><small>{html.escape(e['region'])}</small></td><td>{e['categoria']}</td></tr>" for e in total)
open("/Users/jm/Desktop/PREVIEW_agenda.html","w",encoding="utf-8").write(f"""<!doctype html><meta charset=utf-8><title>PREVIEW agenda</title>
<style>body{{font:15px/1.5 system-ui;background:#f0ede8;color:#252830;max-width:900px;margin:2rem auto;padding:0 1rem}}table{{border-collapse:collapse;width:100%}}td{{border-bottom:1px solid #ccc;padding:.6rem;vertical-align:top}}.b{{background:#8c6b4a;color:#fff;padding:.5rem;text-align:center}}</style>
<div class=b>PREVIEW — NO PUBLICADO · {len(total)} eventos ({len(existentes)} actuales + {len(total)-len(existentes)} nuevos)</div><table>{rows}</table>""")
print(len(existentes), "->", len(total))
