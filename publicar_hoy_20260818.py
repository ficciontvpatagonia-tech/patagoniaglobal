#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script puntual para publicar las noticias del 18/08/2026 en GLOBALpatagonia,
reusando las funciones de generación del sitio (actualizar_noticias.py) para
mantener consistencia con lo que produce el pipeline automático diario.
No llama APIs externas (Claude / Unsplash) — las notas ya vienen redactadas
(voz editorial PatagoniaGLOBAL, a partir de búsquedas web) y las imágenes se
reutilizan del banco fotos/ existente.
"""
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
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
# 2. Notas nuevas de hoy (18/08/2026) — reescritas con voz propia
# ─────────────────────────────────────────────────────────────

tapa = {
    "id": "20260818-la-ruta-que-uniria-aysen-y-magallanes-sin-cruzar-a-argentina-tapa",
    "titulo": "El camino que Chile nunca terminó: buscan unir Aysén y Magallanes sin pisar el Campo de Hielo Sur",
    "bajada": "Ingenieros, navegantes y el Ejército coinciden en que la mítica ruta 'Chile por Chile' es viable si esquiva los glaciares por la isla Wellington, combinando caminos y ferris en un trazado de 700 kilómetros. El proyecto ya figura en la planificación de Obras Públicas hasta 2055, aunque su horizonte de construcción ronda el siglo.",
    "cuerpo": (
        "Para llegar de Aysén a Magallanes por tierra hoy hay que resignarse a una paradoja: cruzar a la Argentina. "
        "La Carretera Austral termina en Villa O'Higgins, a 533 kilómetros en línea recta de Puerto Natales, y cubrir "
        "esa distancia sin salir de Chile obliga a un viaje de más de 20 horas con varios pasos fronterizos y "
        "barcazas, o a un ferry de un par de días entre Puerto Natales y caleta Yungay. Es una situación que la "
        "propia región conoce de memoria: buena parte del corredor turístico binacional que hoy conecta el sur "
        "profundo con el resto de la Patagonia depende, en los hechos, de territorio argentino.\n\n"
        "La idea de una ruta enteramente chilena —bautizada 'Chile por Chile'— circula desde hace más de cuatro "
        "décadas, frenada siempre por la misma geografía: fiordos, glaciares, canales de cientos de metros de "
        "profundidad y un archipiélago fragmentado que impide pensar en una carretera continua. La novedad que "
        "empieza a instalarse entre especialistas es otra: en vez de forzar el paso por el Campo de Hielo Sur —zona "
        "de canales anchos por el retroceso de los glaciares—, el trazado podría rodearlo por el oeste, a través de "
        "la isla Wellington, donde los pasos marítimos son más angostos y los transbordos, más simples.\n\n"
        "El mapa que manejan ingenieros y fundaciones de la Patagonia occidental sale de Puerto Yungay hacia las "
        "islas Merino Jarpa y Wellington, cruza los fiordos Europa, Asia y Peel y llega, mediante un paso natural "
        "entre el ventisquero Grey y la cordillera Sarmiento, hasta Puerto Natales. El comandante de la División de "
        "Ingenieros del Ejército chileno calculó en unos 700 kilómetros el tramo por construir, con entre seis y "
        "siete sectores que necesitarán transbordadores por la fragmentación del territorio. La propuesta ya integra "
        "la planificación de Infraestructura 2025-2055 del Ministerio de Obras Públicas, aunque el propio organismo "
        "reconoce que el horizonte de construcción podría extenderse durante todo un siglo.\n\n"
        "Más allá de la ingeniería, el proyecto plantea una pregunta de fondo para toda la Patagonia binacional: qué "
        "significaría, para el turismo y la logística del sur profundo, que Chile dejara de depender de la "
        "Argentina para moverse dentro de su propio territorio. Especialistas en soberanía y conservación insisten "
        "en que la ruta solo será sostenible si viene acompañada de una red científica permanente —estaciones "
        "modulares, autosuficiencia energética, marinas de recalada— que ejerza presencia real sobre uno de los "
        "territorios menos habitados del planeta."
    ),
    "tag": "🛣️ Infraestructura",
    "categoria": "general",
    "fuente": "La Prensa Austral",
    "url_original": "https://laprensaaustral.cl/2026/08/17/estudian-ruta-alternativa-que-evitaria-campos-de-hielo-sur-para-conectar-aysen-y-magallanes/",
    "pais": "chile",
    "imagen": "fotos/foto-20260703-nueva-ruta-maritima-abre-el-extremo-sur-de-tierra-del-sec1.webp",
    "imagen_keywords": "fiordos patagonia chilena canales glaciares ruta austral",
    "meta": "Hoy · La Prensa Austral",
}

sec1 = {
    "id": "20260818-esquel-vuelve-a-sus-juegos-de-montana-sec1",
    "titulo": "Diez disciplinas y dos meses de adrenalina: Esquel vuelve a ser la capital argentina del deporte de montaña",
    "bajada": "La segunda edición de los Juegos de Montaña arrancó con el Cross Nocturno a la Cruz y sumará escalada, mountain bike, kayak, trail y hasta parapente de precisión internacional hasta principios de octubre, consolidando a la ciudad chubutense como uno de los polos de deporte outdoor más completos de la cordillera patagónica.",
    "cuerpo": (
        "En el noroeste de Chubut, la ciudad que se autoproclama Capital Provincial del Turismo Deportivo empezó a "
        "demostrarlo en los hechos. Esquel abrió el 15 de agosto la segunda edición de sus Juegos de Montaña con el "
        "Cross Nocturno Trepada a la Cruz, el primero de más de diez certámenes que, hasta octubre, van a recorrer "
        "los escenarios más emblemáticos de la ciudad: el cerro La Cruz, la Reserva Natural Urbana Laguna La Zeta y "
        "el centro de actividades La Hoya.\n\n"
        "El cronograma no da respiro. Al cross nocturno y el torneo de escalada indoor del Club Andino les sigue, el "
        "23 de agosto, una jornada de mountain bike en los senderos técnicos de la Laguna La Zeta. Ya en septiembre, "
        "mes en que el invierno patagónico empieza a ceder paso a la primavera, llegan el Downhill en el cerro La "
        "Cruz y un campeonato de esquí para categorías infantiles, antes de una fecha que reúne en un mismo día el "
        "Campeonato Argentino de Trail, de Kayak, de Arquería y una fecha nacional de Marcha Nórdica. El cierre, "
        "recién el 3 y 4 de octubre, queda para el campeonato argentino e internacional de Parapente de Precisión.\n\n"
        "Entre tanta disciplina nueva, hay una que sostiene la tradición: el 27 de septiembre se corre el 34° "
        "Tetratlón Esquel, una de las carreras con más historia de la Patagonia, que este año se suma oficialmente "
        "al calendario de los Juegos. La organización también ofrece talleres de nutrición deportiva, mecánica de "
        "bicicletas y primeros auxilios, pensados para acompañar a un público que crece edición tras edición.\n\n"
        "Del otro lado de la cordillera, a un salto por el paso internacional que conecta con Chiloé y Futaleufú, el "
        "sur de Chile sostiene su propio calendario de montaña en la misma temporada. Para el trail running y el "
        "deporte outdoor patagónico —que no entiende de fronteras ni de un solo idioma— cada nueva edición de los "
        "Juegos de Esquel suma una pieza más a un mapa deportivo que, de a poco, empieza a mirarse como una sola "
        "región de picos, lagos y senderos compartidos."
    ),
    "tag": "🏔️ Deportes & Aventura",
    "categoria": "deportes",
    "fuente": "Diario Binacional",
    "url_original": "https://www.diariobinacional.cl/noticia/eventos/2026/08/vuelven-los-juegos-de-montana-a-esquel-una-fiesta-para-vivir-naturaleza-y-deporte",
    "pais": "argentina",
    "imagen": "fotos/foto-20260419-bopp-trail-dep.webp",
    "imagen_keywords": "esquel chubut trail running montaña deporte",
    "meta": "Hoy · Diario Binacional",
}

sec2 = {
    "id": "20260818-fiscales-de-chile-y-argentina-alertan-sobre-el-crimen-sin-fronteras-sec2",
    "titulo": "Sin ríos ni montañas que las separen: los fiscales de Chile y Argentina advierten que el crimen ya no distingue la frontera patagónica",
    "bajada": "En una sesión inédita del Senado chileno en Punta Arenas, los fiscales de Magallanes y de Río Gallegos describieron una misma red binacional de narcotráfico, contrabando de cigarrillos y lavado de dinero, y reclamaron una cooperación institucional tan veloz como el delito que enfrentan.",
    "cuerpo": (
        "El extremo sur de la Patagonia tiene una particularidad geográfica que, según sus propios fiscales, se "
        "volvió también una vulnerabilidad: no hay un río ni una cordillera que marquen con claridad dónde termina "
        "Chile y empieza la Argentina. Esa fue la base del diagnóstico que compartieron el fiscal regional de "
        "Magallanes, Cristián Crisosto, y el fiscal federal de Río Gallegos, Julio César Zárate, ante la Comisión de "
        "Seguridad Pública del Senado chileno, que sesionó de forma descentralizada en Punta Arenas. La región tiene "
        "seis pasos fronterizos oficiales, remarcaron, pero el resto del territorio es, en la práctica, permeable.\n\n"
        "El diagnóstico compartido describe una logística sofisticada: organizaciones que compran estancias del "
        "lado argentino para asegurarse rutas de cruce, camiones de carga escoltados, comunicaciones por sistemas "
        "satelitales difíciles de rastrear y lavado de activos a través de billeteras virtuales y casas de cambio. "
        "El contrabando de cigarrillos, que suele mirarse como un delito menor, funciona en los hechos como fuente "
        "de financiamiento del narcotráfico: solo el año pasado se incautaron más de 600.000 cajetillas y hay más de "
        "120 vehículos —varios de alta gama— retenidos en causas vigentes. Ambos fiscales destacaron, como "
        "contracara, investigaciones coordinadas con detenciones simultáneas en los dos países el mismo día y a la "
        "misma hora.\n\n"
        "El reclamo central de la jornada fue la lentitud institucional frente a la velocidad del delito. Zárate "
        "comparó la situación con la de 'un equipo de fútbol improvisado' que debe enfrentar a un rival que entrena "
        "en conjunto, y pidió convenios que agilicen el intercambio de información entre ambos países. Crisosto sumó "
        "una dimensión marítima al problema: el tránsito de naves por el estrecho de Magallanes creció 47% entre "
        "2024 y 2025, hasta cerca de 1.500 embarcaciones, empujado por la sequía del canal de Panamá y las tensiones "
        "en el Caribe que reordenaron las rutas navieras globales. La ley chilena, advirtió, obliga a garantizar el "
        "paso de esas naves salvo que exista una denuncia previa, lo que deja a la autoridad sin base legal para "
        "abordar una embarcación sospechosa sin más indicios.\n\n"
        "El cuadro se completa puertas adentro: Magallanes mantiene 625 personas privadas de libertad desde 2023, "
        "con un 12,7% de extranjeros —en su mayoría colombianos— y un incremento de más del 200% en delitos "
        "vinculados a la Ley de Armas entre 2023 y 2026. Para una región que durante décadas se pensó como el margen "
        "aislado del continente, el mensaje de sus propios fiscales fue el mismo de un lado y del otro de la "
        "cordillera: el crimen organizado ya opera como una sola red patagónica, e incluso intercontinental, y las "
        "instituciones todavía responden como dos."
    ),
    "tag": "🚨 Seguridad Binacional",
    "categoria": "policial",
    "fuente": "La Prensa Austral",
    "url_original": "https://laprensaaustral.cl/2026/08/14/fiscalias-de-chile-y-argentina-advierten-que-el-crimen-organizado-opera-como-una-sola-red-en-la-patagonia/",
    "pais": "ambos",
    "imagen": "fotos/foto-20260610-paso-cordillerano-cerrado-y-frontera-en-alerta-el-tapa.webp",
    "imagen_keywords": "frontera patagonia seguridad control fronterizo",
    "meta": "Hoy · La Prensa Austral",
}

noticia1 = {
    "id": "20260818-neuquen-extiende-la-emergencia-hidrica-mientras-sus-cuencas-se-recuperan",
    "titulo": "Neuquén extiende seis meses más su emergencia hídrica, aunque sus cuencas empiezan a respirar",
    "bajada": "El Gobierno provincial prorrogó hasta octubre la Emergencia Hídrica, Social y Productiva. Los embalses siguen por debajo de sus niveles normales, pero las nevadas del invierno devolvieron algo de aire a un sistema que viene de varios años de déficit.",
    "cuerpo": (
        "La Provincia de Neuquén decidió extender por 180 días más su Emergencia Hídrica, Social y Productiva, una "
        "medida que regirá hasta mediados de octubre y que, según el secretario de Ambiente y Recursos Naturales, "
        "Hipólito Salvatori, busca sostener las herramientas de prevención y monitoreo mientras las cuencas siguen "
        "en proceso de recuperación. 'Las cuencas no llegan a recuperarse todavía', resumió el funcionario, aunque "
        "el diagnóstico de este invierno es menos sombrío que el de años anteriores.\n\n"
        "Los números explican la cautela: el embalse Piedra del Águila está unos nueve metros por debajo de su "
        "nivel máximo normal, y El Chocón, 3,4 metros. Las bajas temperaturas del invierno, sin embargo, permitieron "
        "retener buena parte de las precipitaciones en forma de nieve, lo que a futuro va a favorecer el deshielo y "
        "la recuperación de los embalses. La mejor noticia llegó del sistema Mari Menuco-Los Barreales, del que "
        "depende cerca del 70% del agua potable de la ciudad de Neuquén y que hoy está prácticamente en niveles "
        "normales.\n\n"
        "No todo el panorama es alentador: los estudios sobre napas subterráneas muestran una cuenca que 'se sigue "
        "deprimiendo', con perforaciones que en pocos meses pasaron de encontrar agua a 70 metros de profundidad a "
        "no hacerlo. Los pronósticos climáticos anticipan lluvias hasta septiembre, lo que permite proyectar un "
        "escenario mejor que el del año pasado, aunque Salvatori fue claro en que se trata de previsiones sujetas a "
        "variación.\n\n"
        "El patrón que describe Neuquén —años de sequía intercalados con temporadas de mayor disponibilidad "
        "hídrica— es el mismo que atraviesa buena parte de la Patagonia árida, de uno y otro lado de la cordillera, "
        "donde la gestión del agua se volvió una política de estado permanente antes que una respuesta de emergencia "
        "puntual."
    ),
    "tag": "💧 Medio Ambiente",
    "categoria": "medio ambiente",
    "fuente": "Neuquén al Instante",
    "url_original": "https://www.neuquenalinstante.com.ar/noticias/2026/08/17/138664-las-cuencas-hidricas-neuquinas-continuan-en-recuperacion",
    "pais": "argentina",
    "imagen": "fotos/foto-20260510-canon-hidrico-progresivo-santa-cruz-quiere-que-la-tapa.webp",
    "imagen_keywords": "embalse cuenca hidrica neuquen sequia patagonia",
    "meta": "Ayer · Neuquén al Instante",
}

noticia2 = {
    "id": "20260818-chile-y-argentina-preparan-su-cumbre-de-integracion-en-valdivia",
    "titulo": "Valdivia se prepara para la cumbre que más veces reunió a la Patagonia binacional",
    "bajada": "Delegaciones de cinco regiones chilenas y tres provincias argentinas se encuentran el 26 y 27 de agosto en la 40ª Reunión del Comité de Integración Los Lagos, una de las instancias de cooperación bilateral más antiguas entre ambos países, con foco en pasos fronterizos, comercio y turismo compartido.",
    "cuerpo": (
        "Neuquén, Río Negro, el norte de Chubut y Bahía Blanca del lado argentino; Biobío, La Araucanía, Los Lagos y "
        "Los Ríos del lado chileno. Ese es el mapa de regiones y provincias que, desde hace cuatro décadas, se "
        "turnan para ser sede de una de las citas de cooperación bilateral más longevas entre los dos países: el "
        "Comité de Integración Los Lagos, que llega este año a su 40ª edición y se realizará el 26 y 27 de agosto en "
        "Valdivia.\n\n"
        "Durante dos jornadas, las delegaciones van a trabajar en comisiones sobre facilitación fronteriza, "
        "infraestructura y transportes, comercio, turismo, gestión de riesgos, salud, cultura y desarrollo "
        "sostenible. La agenda retoma los acuerdos de la edición anterior, realizada en Neuquén, donde se avanzó en "
        "modelos de gestión compartida para circuitos turísticos binacionales y se discutieron mejoras edilicias y "
        "de coordinación en los pasos fronterizos, además de un consenso técnico sobre flujo comercial, economía "
        "circular y la logística del eje Chile-Zapala para potenciar exportaciones a través de puertos chilenos.\n\n"
        "El gobernador regional de Los Ríos, Luis Cuvertino, ya adelantó que espera que el encuentro impulse el "
        "mejoramiento de la conectividad a través del paso Hua Hum, la ruta que conecta Valdivia con San Martín de "
        "los Andes y que forma parte del corredor turístico que cada temporada mueve a miles de visitantes entre los "
        "lagos andinos de ambos países.\n\n"
        "Para una región que vive dividida por una cordillera pero unida por lagos, volcanes y comunidades que "
        "cruzan la frontera todos los días, encuentros como el de Los Ríos son la contracara institucional de una "
        "integración que, en los hechos, ya funciona hace rato en el comercio local y el turismo binacional. La "
        "pregunta, edición tras edición, es si los compromisos que se firman en la sesión plenaria de clausura se "
        "traducen después en obras concretas en los pasos y las rutas que unen a ambos países."
    ),
    "tag": "🤝 Integración Binacional",
    "categoria": "turismo",
    "fuente": "Diario Binacional",
    "url_original": "https://www.diariobinacional.cl/noticia/actualidad/2026/08/comercio-turismo-y-pasos-fronterizos-marcaran-reunion-binacional-en-los-rios",
    "pais": "ambos",
    "imagen": "",
    "imagen_keywords": "integracion binacional chile argentina reunion fronteriza",
    "meta": "Hace 1 semana · Diario Binacional",
}

ticker = [
    "Chile estudia una ruta 'Chile por Chile' que uniría Aysén y Magallanes sin cruzar a Argentina",
    "Esquel abrió sus Juegos de Montaña: diez disciplinas hasta octubre",
    "Fiscales de Chile y Argentina: el crimen organizado ya opera como una sola red patagónica",
    "Neuquén extiende su emergencia hídrica hasta octubre",
    "Valdivia será sede de la 40ª Reunión del Comité de Integración Los Lagos",
]

# ─────────────────────────────────────────────────────────────
# 3. Construir noticias.json con la misma lógica de rotación del sitio
#    e inyectar directamente noticia1/noticia2 al frente del grid de hoy
# ─────────────────────────────────────────────────────────────
datos = an.construir_noticias_json(tapa, [sec1, sec2], prev_tapa, prev_secundarias, prev_noticias, ticker)

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

# ─────────────────────────────────────────────────────────────
# 7. Registrar URLs como publicadas (evita duplicados en próximas corridas)
# ─────────────────────────────────────────────────────────────
try:
    with open("urls_publicadas.json", encoding="utf-8") as f:
        publicadas = json.load(f)
except Exception:
    publicadas = []
nuevas_urls = [n["url_original"] for n in todas if n.get("url_original")]
for u in nuevas_urls:
    if u not in publicadas:
        publicadas.append(u)
with open("urls_publicadas.json", "w", encoding="utf-8") as f:
    json.dump(publicadas, f, ensure_ascii=False, indent=2)
print("urls_publicadas.json actualizado.")

print("\nLISTO.")
