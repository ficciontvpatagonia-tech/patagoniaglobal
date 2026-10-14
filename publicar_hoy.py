#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script puntual para publicar las noticias del 16/08/2026 en GLOBALpatagonia,
reusando las funciones de generación del sitio (actualizar_noticias.py) para
mantener consistencia con lo que produce el pipeline automático diario.
No llama APIs externas (Claude / Unsplash) — las notas ya vienen redactadas
y las imágenes se reutilizan del banco fotos/ existente.
"""
import json
import os
import sys

BASE = "/sessions/happy-friendly-dirac/mnt/CLAUDCODE/GLOBAL PATAGONIA"
sys.path.insert(0, BASE)
os.chdir(BASE)

import actualizar_noticias as an

# ─────────────────────────────────────────────────────────────
# 1. Cargar estado anterior (tapa/secundarias/noticias de ayer)
# ─────────────────────────────────────────────────────────────
with open("noticias.json", encoding="utf-8") as f:
    prev = json.load(f)

prev_tapa = prev.get("tapa")
prev_secundarias = prev.get("secundarias", [])
prev_noticias = prev.get("noticias", [])

# ─────────────────────────────────────────────────────────────
# 2. Notas nuevas de hoy (16/08/2026) — reescritas con voz propia
# ─────────────────────────────────────────────────────────────

tapa = {
    "id": "20260816-bariloche-fiesta-de-la-nieve-cierra-con-antorchas-tapa",
    "titulo": "Antorchas en la montaña: Bariloche despide su Fiesta de la Nieve con el mejor invierno en años",
    "bajada": "El cierre de la Fiesta Nacional de la Nieve llega hoy al Centro Cívico tras una semana de nevadas constantes que devolvieron al Cerro Catedral las condiciones que el invierno patagónico venía debiendo. Con la montaña prácticamente completa y una afluencia que no se veía desde antes de la pandemia, la temporada 2026 se perfila como una de las mejores de la última década.",
    "cuerpo": (
        "Después de dos inviernos flojos por escasez de nieve, agosto de 2026 vino a saldar la deuda en Bariloche. "
        "Desde comienzos de mes las nevadas se sucedieron casi sin pausa sobre el Cerro Catedral, dejando la base y "
        "los sectores altos en condiciones que hacía tiempo no se veían: capas de nieve seca, pistas habilitadas casi "
        "en su totalidad y un movimiento de turistas que la ciudad no registraba desde antes de la pandemia.\n\n"
        "El punto más alto de la celebración llegó el jueves con la tradicional Bajada de Antorchas, cuando unos 600 "
        "esquiadores y snowboardistas descendieron formando una serpiente de luz sobre la ladera nocturna del cerro, "
        "uno de los rituales más fotografiados del invierno rionegrino. Hoy, domingo, el Centro Cívico recibe el cierre "
        "formal de la Fiesta Nacional de la Nieve, con la plaza colmada y funcionarios locales destacando —una vez "
        "más— el \"sentido de pertenencia\" que el evento despierta entre los barilochenses, más allá de su rédito turístico.\n\n"
        "El fenómeno no es exclusivo de Río Negro. Del otro lado de la cordillera, los centros invernales del sur de "
        "Chile también reportan una temporada con nieve abundante, en un invierno que finalmente trató parejo a ambos "
        "lados de los Andes patagónicos. Para el corredor turístico binacional que conecta Bariloche con el sur "
        "chileno a través de los pasos cordilleranos, eso significa una oferta de nieve robusta en los dos países, "
        "justo cuando la demanda internacional empieza a mirar hacia el hemisferio sur.\n\n"
        "Con la Fiesta de la Nieve cerrando su edición 2026, la pregunta que queda flotando en Bariloche es si este "
        "envión de nieve tardío alcanza para sostener una temporada alta que, apenas tres semanas atrás, generaba más "
        "preocupación que entusiasmo entre los operadores turísticos locales."
    ),
    "tag": "❄️ Turismo",
    "categoria": "turismo",
    "fuente": "Diario El Cordillerano (Bariloche)",
    "url_original": "https://www.elcordillerano.com.ar/noticias/2026/08/16/256759-hoy-llega-el-gran-cierre-de-la-fiesta-de-la-nieve-en-bariloche",
    "pais": "argentina",
    "imagen": "fotos/foto-20260814-travesia-nocturna-en-bariloche-24-esquiadores-se-dep.webp",
    "imagen_keywords": "bariloche nieve esqui antorchas cerro catedral",
    "meta": "Hoy · Diario El Cordillerano",
}

sec1 = {
    "id": "20260816-villa-pehuenia-el-rincon-alpino-de-neuquen-sec1",
    "titulo": "El pueblo que parece de los Alpes está en Neuquén: Villa Pehuenia vive su semana más blanca",
    "bajada": "Entre los lagos Aluminé y Moquehue, la localidad neuquina combina bosques de araucarias, montañas nevadas y un parque de nieve administrado por la comunidad mapuche Puel. Con la temporada alta de Batea Mahuida terminando el lunes, esta es la última semana para vivirla en su mejor versión invernal.",
    "cuerpo": (
        "A la hora de pensar en nieve patagónica, la conversación suele arrancar y terminar en Bariloche. Pero a unos "
        "200 kilómetros al norte, en plena cordillera neuquina, Villa Pehuenia ofrece una postal que sorprende a "
        "quien la descubre por primera vez: casas de madera, bosques de pehuenes centenarios y montañas nevadas "
        "asomando sobre las aguas del lago Aluminé, cuyo nombre en mapudungún —\"olla reluciente\"— describe bien el "
        "brillo que toma con la luz de invierno.\n\n"
        "El corazón deportivo de la zona es el Parque de Nieve Batea Mahuida, montado sobre un volcán homónimo y "
        "administrado por la Agrupación Mapuche Puel, un dato que distingue a este centro de esquí de la mayoría de "
        "los complejos patagónicos: la gestión del territorio y de la actividad turística está en manos de la "
        "comunidad originaria local. Ahí se puede esquiar y hacer snowboard, pero también hay caminatas con "
        "raquetas, cabalgatas y paseos en motos de nieve para quienes no buscan pista.\n\n"
        "La ventana ideal se está por cerrar: la temporada alta del parque —con tarifas más elevadas— corre hasta el "
        "lunes 17 de agosto, y desde el martes empieza la temporada baja. Es, además, la última semana en que el "
        "paisaje combina nieve fresca en las montañas con los lagos todavía sin el movimiento náutico que trae el verano.\n\n"
        "Villa Pehuenia comparte con el sur de Chile —del otro lado del paso Icalma, a poco más de una hora— el "
        "mismo cordón de bosques de araucarias que las comunidades pehuenche y mapuche consideran sagrado desde "
        "mucho antes de que existiera la frontera. Esa continuidad natural y cultural, más que la comparación con "
        "los Alpes, es lo que le da a este rincón neuquino su identidad más genuina."
    ),
    "tag": "🏔️ Turismo",
    "categoria": "turismo",
    "fuente": "Canal26",
    "url_original": "https://www.canal26.com/turismo/2026/08/13/parece-un-pueblo-de-suiza-pero-esta-en-argentina-asi-es-villa-pehuenia-el-destino-ideal-para-disfrutar-de-la-nieve/",
    "pais": "argentina",
    "imagen": "fotos/foto-20260701-primera-gran-nevada-temporada-nieve-patagonia-tur.webp",
    "imagen_keywords": "villa pehuenia neuquen nieve lago araucarias",
    "meta": "Hoy · Canal26",
}

sec2 = {
    "id": "20260816-trail-del-agrio-caviahue-250-corredores-sec2",
    "titulo": "Kilómetro vertical entre volcanes: Caviahue hizo temblar la montaña con su Trail del Agrio",
    "bajada": "Doscientos cincuenta corredores desafiaron senderos técnicos y desniveles exigentes en la localidad volcánica de Neuquén, con modalidades de Kilómetro Vertical, 10K y 21K. El evento confirma a la Patagonia argentina y chilena como uno de los territorios más activos del trail running sudamericano.",
    "cuerpo": (
        "Mientras Bariloche celebraba la nieve con antorchas, a 400 kilómetros al norte otra montaña patagónica "
        "también tuvo su fin de semana a pura adrenalina. Caviahue, la localidad neuquina asentada sobre paisajes "
        "volcánicos y bosques de araucarias, fue escenario del Trail del Agrio \"El Origen\" 2026, una de las citas "
        "de montaña más exigentes del calendario patagónico de carreras.\n\n"
        "El formato repartió el desafío en dos jornadas: el sábado, el Kilómetro Vertical puso a prueba a quienes "
        "buscan el ascenso más explosivo posible en el menor tiempo; el domingo llegó el turno de las distancias de "
        "fondo, con 10 y 21 kilómetros de senderos técnicos, desniveles pronunciados y vistas que solo un entorno "
        "volcánico como el del Agrio puede ofrecer. Con cupo limitado a 250 participantes, la organización priorizó "
        "una experiencia cuidada por sobre la masividad.\n\n"
        "El trail running patagónico no conoce fronteras: ese mismo fin de semana, corredores de ambos lados de la "
        "cordillera compartían calendario con carreras en Chubut, Río Negro y Santa Cruz, mientras que en el sur "
        "profundo chileno el circuito de montaña se prepara para pruebas de gran fondo como el Patagonman, en los "
        "fiordos de Aysén. Entre kilómetros verticales, ultra trails y triatlones extremos, la región se consolida "
        "como uno de los polos de deporte de montaña más completos del continente, con una temporada que no da "
        "tregua entre el invierno y el verano australes.\n\n"
        "Para el trail running neuquino, carreras como la del Agrio cumplen una doble función: ponen a prueba a los "
        "corredores locales y, de paso, exportan al resto del país —y a Chile— una postal de la cordillera del "
        "norte patagónico que rara vez comparte protagonismo con Bariloche o El Chaltén."
    ),
    "tag": "🏃 Deportes & Aventura",
    "categoria": "deportes",
    "fuente": "Calendario de Carreras Patagónicas",
    "url_original": "https://calendariodecarreras.ar/sur/carrera/trail-del-agrio-caviahue-el-origen/2026/",
    "pais": "argentina",
    "imagen": "fotos/foto-20260419-bopp-trail-dep.webp",
    "imagen_keywords": "trail running caviahue neuquen montaña",
    "meta": "Hoy · Calendario de Carreras Patagónicas",
}

noticia1 = {
    "id": "20260816-neuquen-debate-convenio-169-comunidades-mapuche",
    "titulo": "A 25 años del Convenio 169, Neuquén discute si el Estado cumple con los pueblos originarios",
    "bajada": "Un debate en la Universidad del Comahue reunió a referentes mapuche, un obispo, un premio Nobel de la Paz y organismos de derechos humanos para analizar el estado del tratado que protege los territorios indígenas. El reclamo llega en medio de un proyecto legislativo que las comunidades consideran una amenaza directa a sus tierras.",
    "cuerpo": (
        "Hace 25 años que el Convenio 169 de la Organización Internacional del Trabajo tiene rango de ley en la "
        "Argentina, y esa vigencia formal fue la excusa para poner en la mesa una pregunta más incómoda: cuánto de "
        "ese marco legal se traduce, en los hechos, en derechos reales para las comunidades mapuche de la Patagonia "
        "norte. El lunes pasado, la Universidad Nacional del Comahue, en Neuquén capital, fue sede de una mesa "
        "debate que reunió a la Confederación Mapuche de Neuquén, al Parlamento Mapuche Tehuelche de Río Negro, al "
        "CELS, a la vicerrectora de la universidad, al obispo local y, por videollamada, al premio Nobel de la Paz "
        "Adolfo Pérez Esquivel.\n\n"
        "El disparador inmediato fue un proyecto legislativo nacional sobre \"inviolabilidad de la propiedad "
        "privada\" que, según explicaron los referentes indígenas, incluye artículos sobre desalojos exprés que "
        "impactarían directamente sobre comunidades asentadas en tierras codiciadas por productores y capitales "
        "extranjeros. El texto perdió parte de su fuerza inicial —los capítulos de tierras y manejo del fuego "
        "fueron retirados tras la presión social del 6 de agosto— pero los capítulos sobre desalojos y "
        "expropiaciones siguen en danza en Diputados.\n\n"
        "Los números que se manejaron en el debate dan una idea del volumen del reclamo: en Neuquén hay 70 "
        "comunidades mapuche, 30 de ellas cerca de la formación de Vaca Muerta, con 12 concentradas solo en Añelo, "
        "el epicentro del boom hidrocarburífero no convencional. La tensión entre actividad extractiva y derechos "
        "territoriales, señalaron los participantes, no es un dato menor: es, según sus propias palabras, la "
        "explicación de fondo detrás de la resistencia del Estado a otorgar personerías jurídicas y avanzar con los "
        "relevamientos territoriales pendientes.\n\n"
        "El planteo excede a la provincia. En Río Negro, el Parlamento Mapuche Tehuelche denuncia que solo 64 de "
        "las 124 comunidades fueron relevadas bajo la ley nacional 26.160, con el equipo técnico encargado de "
        "censarlas actualmente suspendido. Es un reclamo que, aunque se discute puertas adentro de Neuquén, dialoga "
        "con procesos similares en el sur de Chile, donde las comunidades mapuche y pehuenche del otro lado de la "
        "cordillera enfrentan tensiones territoriales de una lógica muy parecida: extracción de recursos versus "
        "derechos preexistentes sobre la tierra."
    ),
    "tag": "✊ Pueblos Originarios",
    "categoria": "sociedad",
    "fuente": "Revista Acción",
    "url_original": "https://accion.coop/2026/08/15/pais/sociedad/pueblos-originarios-ley-tierras-neuquen/",
    "pais": "argentina",
    "imagen": "fotos/foto-20260810-justicia-confirma-restitucion-de-dos-predios-mapuche-tapa.webp",
    "imagen_keywords": "mapuche neuquen convenio 169 comunidades",
    "meta": "Ayer · Revista Acción",
}

noticia2 = {
    "id": "20260816-magallanes-convocatoria-artesania-indigena-2026",
    "titulo": "Magallanes abre su convocatoria de artesanía indígena: el otro lado de la cordillera también reivindica lo propio",
    "bajada": "El Ministerio de las Culturas de Chile recibe hasta el miércoles las postulaciones al Sello Artesanía Indígena 2026 en la región más austral. Mientras en Neuquén se discute el cumplimiento de los derechos territoriales mapuche, en Magallanes el Estado chileno apuesta a certificar el oficio de los pueblos originarios australes.",
    "cuerpo": (
        "Hasta el miércoles 19 de agosto, los artesanos y artesanas de comunidades indígenas de la región de "
        "Magallanes tienen tiempo para postular al Sello Artesanía Indígena 2026, una certificación que impulsa el "
        "Ministerio de las Culturas, las Artes y el Patrimonio de Chile para reconocer y visibilizar el trabajo de "
        "quienes mantienen vivas las técnicas y los saberes de los pueblos originarios australes: selk'nam, "
        "kawésqar, yagán y mapuche, entre las comunidades presentes en el extremo sur.\n\n"
        "El sello no es solo un reconocimiento simbólico: certificar una pieza como artesanía indígena la distingue "
        "en un mercado —el turístico, sobre todo— donde la demanda de objetos \"auténticos\" convive con una oferta "
        "masiva de souvenirs sin ningún vínculo real con las comunidades que dicen representar. Para artesanos de "
        "Punta Arenas, Puerto Natales o Puerto Williams, la certificación puede significar mejores precios, acceso "
        "a ferias oficiales y una trazabilidad que hoy escasea en la región más austral del continente.\n\n"
        "La convocatoria llega en un momento en que Magallanes viene sosteniendo una agenda activa en torno a sus "
        "pueblos originarios: circulan gestiones sobre restos kawésqar en disputa entre fundaciones y comunidades, "
        "becas educativas específicas para jóvenes de ese pueblo y la vigilancia constante de la comunidad yagán "
        "sobre el río Ukika, en Puerto Williams. El Sello Artesanía Indígena se suma a ese entramado como una "
        "herramienta más de política cultural, aunque acotada a un rubro puntual.\n\n"
        "La coincidencia con el debate que esa misma semana se dio en Neuquén, del otro lado de la cordillera, "
        "sobre el estado del Convenio 169, no es casual: mientras Chile institucionaliza el reconocimiento de los "
        "oficios originarios, Argentina discute si cumple siquiera con el reconocimiento territorial básico. Son "
        "las dos caras binacionales de una misma pregunta pendiente sobre cómo los estados patagónicos —el "
        "argentino y el chileno— saldan su deuda con los pueblos que habitaban la región mucho antes de que "
        "existiera una frontera entre ambos países."
    ),
    "tag": "🎨 Cultura & Pueblos Originarios",
    "categoria": "cultura",
    "fuente": "Radio Polar",
    "url_original": "https://www.radiopolar.com/artesanos-magallanes-postular-sello-artesania-indigena-2026-19-agosto",
    "pais": "chile",
    "imagen": "fotos/foto-20260510-conadi-convoca-a-mapuche-selknam-y-kawesqar-para-cul.webp",
    "imagen_keywords": "artesania indigena magallanes kawesqar selknam",
    "meta": "Hoy · Radio Polar",
}

ticker = [
    "Bariloche cierra la Fiesta de la Nieve con la mejor temporada en años",
    "Villa Pehuenia vive su última semana de temporada alta en Batea Mahuida",
    "250 corredores desafiaron el Trail del Agrio en Caviahue, Neuquén",
    "Neuquén debate a 25 años del Convenio 169 con las comunidades mapuche",
    "Magallanes abre su convocatoria de artesanía indígena 2026",
]

# ─────────────────────────────────────────────────────────────
# 3. Construir noticias.json con la misma lógica de rotación del sitio
#    e inyectar directamente noticia1/noticia2 al frente del grid de hoy
# ─────────────────────────────────────────────────────────────
datos = an.construir_noticias_json(tapa, [sec1, sec2], prev_tapa, prev_secundarias, prev_noticias, ticker)

# Insertar las 2 noticias frescas adicionales al frente del grid "Noticias de la Semana"
ids_ya = {n.get("id") for n in datos["noticias"]}
frescas = [n for n in (noticia1, noticia2) if n.get("id") not in ids_ya]
datos["noticias"] = (frescas + datos["noticias"])[:8]

an.guardar_json(datos)
print("noticias.json actualizado. IDs en noticias:", [n.get("id") for n in datos["noticias"]])

# ─────────────────────────────────────────────────────────────
# 4. historial.json — acumulativo
# ─────────────────────────────────────────────────────────────
todas = [tapa, sec1, sec2, noticia1, noticia2]
an.guardar_historial(todas)
print("historial.json actualizado.")

# ─────────────────────────────────────────────────────────────
# 5. Inyectar tapa + noticias en index.html (bloques estáticos)
# ─────────────────────────────────────────────────────────────
an.inyectar_tapa_en_index(datos)
print("index.html: bloques TAPA / NOTICIAS inyectados.")

# ─────────────────────────────────────────────────────────────
# 6. Generar notas/[id].html para las 5 notas nuevas
# ─────────────────────────────────────────────────────────────
an.generar_paginas_og(todas)
print("notas/*.html generadas.")

print("\nLISTO.")
