#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Publicación MANUAL — one-off del 02/06/2026.

El Action diario no corrió hoy (sin fondos en la API de Anthropic).
En vez de fetch RSS + reescritura con Claude, las notas vienen ya elegidas
y reescritas a mano (Jacques/Claude en conversación) y se inyectan en el
MISMO pipeline de actualizar_noticias.py: imágenes, historial, rotaciones,
noticias.json, páginas estáticas SEO, sitemap, feed y búsqueda.

NO publica en Telegram/Facebook/Instagram (esos tokens viven en Actions).
Uso:  python3 _scripts/publicar_manual.py
"""
import os
import re
import sys
import json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

import actualizar_noticias as A
from datetime import datetime

BORRADOR = os.path.join(BASE, "_scripts", "_borrador_manual.json")

HOY_SLUG = datetime.now().strftime("%Y%m%d")


def _id(titulo, sufijo):
    return f"{HOY_SLUG}-{A.slugify(titulo)}-{sufijo}"


# ══════════════════════════════════════════════════════════════════
#  TAPA — Glaciares / reforma de la ley en Santa Cruz
# ══════════════════════════════════════════════════════════════════
tapa = {
    "titulo": "Glaciares: la Cámara revoca la cautelar y habilita la reforma de la ley en Santa Cruz",
    "bajada": "La Cámara Federal de Comodoro Rivadavia dejó sin efecto la medida que frenaba la Ley provincial 3.123, cuestionada desde El Calafate. El tribunal sostuvo que la norma santacruceña conserva estándares de protección casi idénticos a la ley nacional. El pulso por quién manda sobre los hielos patagónicos vuelve a abrirse.",
    "cuerpo": (
        "La pregunta de fondo es vieja como la cordillera: ¿quién decide sobre el hielo que define a la Patagonia? "
        "La Cámara Federal de Comodoro Rivadavia volvió a ponerla en el centro al revocar la medida cautelar que, "
        "dictada por el Juzgado Federal de Río Gallegos, mantenía suspendida la reforma de la ley de glaciares en Santa Cruz. "
        "Con esa decisión, la Ley provincial 3.123 queda habilitada mientras la discusión de fondo sigue su curso.\n\n"
        "La cautelar había sido impulsada por autoridades municipales y legisladores nacionales vinculados a El Calafate, "
        "la localidad que vive a los pies del Campo de Hielo Sur y del glaciar Perito Moreno, y que hizo del hielo su "
        "identidad y su economía. El planteo advertía que una norma provincial podía abrir la puerta a actividades "
        "—mineras, inmobiliarias, energéticas— en zonas hoy resguardadas por la Ley nacional 26.639, sancionada en 2010 "
        "tras años de debate y el primer inventario nacional de glaciares.\n\n"
        "El tribunal de Comodoro, sin embargo, fue en otra dirección: sostuvo que la Ley 3.123 contiene "
        "\"estándares de protección prácticamente idénticos a la redacción original de la norma nacional\", y que no "
        "se acreditó el daño inminente que justifica una cautelar. En los hechos, el fallo no resuelve el conflicto: "
        "lo devuelve a foja cero y deja la pelea concentrada en el fondo de la cuestión, donde se definirá si la "
        "provincia puede legislar sobre sus propios hielos sin debilitar el piso que fijó la Nación.\n\n"
        "El tema excede a Santa Cruz. Los glaciares patagónicos son la reserva de agua dulce que alimenta ríos, lagos "
        "y economías a ambos lados de la frontera: el Campo de Hielo Sur es compartido con Chile, y lo que se decida "
        "sobre su periferia argentina resuena en toda la región. Las organizaciones ambientales ya anticiparon que "
        "seguirán de cerca cada paso, convencidas de que la protección del hielo no es un tema local sino el primer "
        "capítulo de cualquier futuro patagónico. La discusión, lejos de cerrarse, recién empieza."
    ),
    "tag": "🏔 Ambiente",
    "categoria": "medio ambiente",
    "fuente": "Página/12",
    "url_original": "https://www.pagina12.com.ar/2026/06/01/glaciares-revocaron-la-medida-cautelar-que-suspendia-la-reforma-de-la-ley-en-santa-cruz/",
    "pais": "argentina",
    "imagen": None,
    "imagen_keywords": "glaciar perito moreno santa cruz",
    "skip_og_image": True,
}

# ══════════════════════════════════════════════════════════════════
#  SECUNDARIA 1 — Tragedia en el glaciar Vinciguerra
# ══════════════════════════════════════════════════════════════════
sec1 = {
    "titulo": "Tragedia en el glaciar Vinciguerra: mueren una turista y un guía en Tierra del Fuego",
    "bajada": "Los cuerpos fueron hallados tras un operativo de búsqueda en una zona de difícil acceso y con condiciones climáticas cambiantes, en las alturas que dominan Ushuaia.",
    "cuerpo": (
        "La montaña fueguina volvió a recordar que su belleza convive con el riesgo. Una turista y un guía murieron "
        "durante una excursión al glaciar Vinciguerra, el cuerpo de hielo que se descuelga sobre Ushuaia y que en los "
        "últimos años se volvió uno de los trekkings más buscados de Tierra del Fuego. Los cuerpos fueron hallados tras "
        "un operativo de búsqueda en un sector de difícil acceso, complicado por condiciones climáticas que cambiaron "
        "con rapidez.\n\n"
        "El Vinciguerra se ubica en la cordillera que enmarca la ciudad más austral del continente, a pocas horas de "
        "caminata desde el valle de Andorra. El recorrido —que suele incluir la laguna de los Témpanos al pie del "
        "glaciar— atraviesa turbales, bosque y roca expuesta antes de ganar altura. Es una zona donde el clima puede "
        "virar en minutos: viento, niebla y nieve aparecen sin aviso incluso en plena temporada, y la cobertura de "
        "señal es escasa.\n\n"
        "El hecho reabre una conversación que la Patagonia repite cada temporada: la del turismo de montaña que crece "
        "más rápido que la infraestructura de seguridad que debería acompañarlo. La figura del guía habilitado, los "
        "partes meteorológicos, el registro de excursiones y los protocolos de rescate no son trámites: son la línea "
        "que separa una jornada inolvidable de una tragedia.\n\n"
        "Las autoridades fueguinas trabajaban para reconstruir lo ocurrido y asistir a las familias. Más allá de las "
        "causas puntuales, queda el duelo de una comunidad que conoce sus montañas y sabe, mejor que nadie, que el "
        "respeto por el terreno y por el clima austral nunca es opcional."
    ),
    "tag": "· Tierra del Fuego ·",
    "categoria": "general",
    "fuente": "Página/12",
    "url_original": "https://www.pagina12.com.ar/2026/06/02/tragedia-en-tierra-del-fuego-una-turista-y-un-guia-murieron-en-una-excursion-al-glaciar-vinciguerra/",
    "pais": "argentina",
    "imagen": None,
    "imagen_keywords": "glaciar vinciguerra ushuaia montaña",
}

# ══════════════════════════════════════════════════════════════════
#  SECUNDARIA 2 — Kast / conectividad Carretera Austral  (CHILE)
# ══════════════════════════════════════════════════════════════════
sec2 = {
    "titulo": "Kast anuncia un plan de conectividad \"sin precedentes\" para la Carretera Austral",
    "bajada": "El gobierno chileno presentará el jueves una intervención mayor sobre la Ruta 7 en Aysén, con puentes, conectividad lacustre, marítima y digital. Las obras podrían demorar cuatro o cinco años.",
    "cuerpo": (
        "La Carretera Austral —la Ruta 7 que cose 1.200 kilómetros de fiordos, bosques y glaciares en el sur de Chile— "
        "vuelve al centro de la agenda. El presidente José Antonio Kast anunció en Coyhaique un plan integral de "
        "conectividad para la Región de Aysén que incluye una intervención \"sin precedentes\" sobre la mítica ruta, "
        "y que el gobierno presentará formalmente este jueves.\n\n"
        "El anuncio se hizo durante un encuentro ciudadano en el marco de la iniciativa \"Presidente Presente\", junto "
        "al ministro de Obras Públicas, Martín Arrau, y los titulares de Transportes, Louis de Grange, y de Economía y "
        "Minería, Daniel Mas. Arrau adelantó que el plan traerá \"un anuncio muy potente de inversión, puentes\", y que "
        "abarcará además \"conectividad de otro tipo: lacustre, marítima, conectividad digital\".\n\n"
        "Entre los avances destacados, las autoridades mencionaron la construcción del Aeródromo Balmaceda de Coyhaique "
        "y la contratación de las reparaciones del Puente Presidente Ibáñez, en Aysén, que había sufrido daños tras el "
        "corte de un cable principal durante el verano. Kast aclaró que las obras de conectividad \"posiblemente se "
        "demoren cuatro o cinco años en terminar\", pero se completarán.\n\n"
        "Para Aysén, la región más aislada del Chile continental, la Carretera Austral no es una ruta más: es la "
        "columna vertebral que define quién queda dentro y quién queda afuera del mapa. Es, del lado chileno, lo que la "
        "Ruta 40 representa para la Patagonia argentina. Cada puente, cada balsa y cada antena que se suma a ese "
        "corredor empuja en la misma dirección que sueña toda la Patagonia binacional: un sur conectado, donde la "
        "distancia deje de ser destino."
    ),
    "tag": "· Conectividad ·",
    "categoria": "conectividad",
    "fuente": "La Tercera",
    "url_original": "https://www.latercera.com/nacional/noticia/presidente-kast-anuncia-plan-de-conectividad-sin-precedentes-para-la-carretera-austral/",
    "pais": "chile",
    "imagen": None,
    "imagen_keywords": "carretera austral aysen ruta",
    "skip_og_image": True,
}

# ══════════════════════════════════════════════════════════════════
#  TURISMO — Puerto Pirámides / Best Tourism Villages
# ══════════════════════════════════════════════════════════════════
turismo = {
    "titulo": "Puerto Pirámides, la única villa patagónica que compite por ser la mejor del mundo",
    "bajada": "El pueblo chubutense, dentro de Península Valdés —Patrimonio de la Humanidad—, es el único candidato de la Patagonia en el Best Tourism Villages de ONU Turismo. La votación es en diciembre, entre 56 postulantes.",
    "cuerpo": (
        "Mil habitantes, una bahía y las ballenas. Con eso le alcanza a Puerto Pirámides para mirar de igual a igual al "
        "resto del planeta: el único pueblo de la Patagonia que compite en el programa Best Tourism Villages de ONU "
        "Turismo, el sello que distingue a las mejores villas turísticas del mundo. La definición llegará en diciembre, "
        "cuando se vote entre 56 candidatas de todo el globo.\n\n"
        "Ubicado en plena Península Valdés —área natural protegida y Patrimonio de la Humanidad de la UNESCO—, Pirámides "
        "tiene una particularidad que ningún otro postulante argentino puede mostrar. \"Es la única villa turística "
        "ubicada dentro del área natural protegida de Península Valdés, que además es Patrimonio de la Humanidad\", "
        "resumió el intendente Jorge Perversi. Esa condición, sostenida en una biodiversidad marina y terrestre única, "
        "es su mejor carta de presentación.\n\n"
        "El gran imán sigue siendo el avistaje de la ballena franca austral, que cada año convierte al Golfo Nuevo en "
        "un anfiteatro natural. La temporada 2026 abre el 9 de junio con un acto oficial y las primeras navegaciones, "
        "justo cuando la postulación entra en su tramo decisivo.\n\n"
        "El camino no fue corto: la candidatura llevó más de dos años de trabajo. Ocho pueblos argentinos superaron la "
        "preselección y, de los seis que presentó Chubut, solo Pirámides avanzó. La provincia ya sabe lo que significa "
        "el reconocimiento: en 2024 lo obtuvieron Gaiman y Trevelin, dos joyas del valle y la cordillera chubutense. "
        "Ahora le toca al pueblo de las ballenas intentar sumar a la Patagonia, otra vez, al mapa de lo mejor del mundo."
    ),
    "tag": "🏔 Turismo",
    "categoria": "turismo",
    "fuente": "LMNeuquén",
    "url_original": "https://www.lmneuquen.com/patagonia/unico-el-pueblo-patagonico-que-es-patrimonio-la-humanidad-y-busca-ser-el-mejor-sitio-turistico-del-mundo-n1240734",
    "pais": "argentina",
    "imagen": None,
    "imagen_keywords": "puerto piramides ballena peninsula valdes",
}

# ══════════════════════════════════════════════════════════════════
#  CULTURA — Festival de la Escarcha / Cochrane  (CHILE)
# ══════════════════════════════════════════════════════════════════
cultura = {
    "titulo": "El Festival de la Escarcha corona el Mes del Patrimonio en Cochrane",
    "bajada": "La localidad de Aysén despidió mayo con una agenda cultural intensa que celebró su identidad invernal y patrimonial en el corazón de la Patagonia chilena.",
    "cuerpo": (
        "En el extremo sur de la Región de Aysén, donde la Carretera Austral se adentra entre montañas y la temperatura "
        "ya anuncia el invierno, Cochrane despidió el Mes del Patrimonio con su sello más propio: el Festival de la "
        "Escarcha. La capital de la provincia Capitán Prat hizo de la helada que cubre sus mañanas una marca de "
        "identidad y una excusa para encontrarse.\n\n"
        "El Mes del Patrimonio, que en Chile se celebra a lo largo de mayo, encontró en Cochrane una agenda cultural "
        "variada que combinó música, oficios, memoria local y vida comunitaria. En pueblos como este, donde el "
        "aislamiento geográfico marcó la historia de los colonos que llegaron a poblar la Patagonia chilena, el "
        "patrimonio no es solo un edificio antiguo: son las historias de los pioneros, los saberes del campo, las "
        "tradiciones que pasan de generación en generación.\n\n"
        "El Festival de la Escarcha condensa ese espíritu. Antes que resignarse al frío, Cochrane lo celebra: convierte "
        "el invierno austral en motivo de fiesta y reafirma el orgullo de habitar uno de los rincones más remotos del "
        "continente. Es la misma actitud que se respira a lo largo de toda la Patagonia, a un lado y otro de la "
        "frontera, donde las comunidades pequeñas defienden su cultura como quien defiende un territorio.\n\n"
        "El cierre del Mes del Patrimonio deja en Cochrane la postal de un pueblo que sabe que su mayor riqueza no está "
        "solo en el paisaje que lo rodea, sino en la identidad que cultiva puertas adentro."
    ),
    "tag": "🎭 Cultura",
    "categoria": "cultura",
    "fuente": "Diario Regional Aysén",
    "url_original": "https://www.diarioregionalaysen.cl/noticia/actualidad/2026/06/festival-de-la-escarcha-y-variada-agenda-cultural-dieron-vida-al-mes-del-patrimonio-en-cochrane",
    "pais": "chile",
    "imagen": None,
    "imagen_keywords": "cochrane aysen patagonia invierno",
    "skip_og_image": True,
}

# ══════════════════════════════════════════════════════════════════
#  NEGOCIOS 1 — Súper RIGI
# ══════════════════════════════════════════════════════════════════
neg_rigi = {
    "titulo": "Súper RIGI: el régimen que apunta a litio, hidrógeno y energía con piso de USD 1.000 millones",
    "bajada": "El proyecto que el Gobierno envió al Congreso complementa el RIGI con beneficios más agresivos para industrias nuevas. La Patagonia, con Vaca Muerta y la minería, vuelve a aparecer en el centro del tablero.",
    "cuerpo": (
        "El Gobierno nacional sumó una nueva pieza a su esquema de incentivos: el Súper RIGI, un Régimen de Incentivo "
        "para Grandes Inversiones en Nuevas Industrias que ya ingresó al Congreso. No reemplaza al RIGI original —que "
        "cubre minería, petróleo, gas y energía— sino que lo complementa, con un foco preciso: las industrias que "
        "todavía no existen en el país o están en fase experimental.\n\n"
        "La lista de sectores alcanzados dibuja el mapa de la transición energética: cadena del litio, manufactura de "
        "baterías, hidrógeno verde, GNL onshore, pequeños reactores nucleares, paneles solares, turbinas eólicas, "
        "vehículos eléctricos, petroquímica, uranio y fertilizantes especializados. Para entrar, cada proyecto deberá "
        "comprometer al menos USD 1.000 millones y ejecutar el 20% en los dos primeros años.\n\n"
        "Los beneficios son notorios: el impuesto a las Ganancias baja del 25% al 15%, hay amortización acelerada "
        "(60% el primer año), exención de retenciones a la exportación desde el inicio, arancel cero a la importación "
        "de bienes clave y 30 años de estabilidad normativa. Las provincias que adhieran deberán aceptar una alícuota "
        "de Ingresos Brutos de hasta 0,5% y resignar la posibilidad de imponer compras a proveedores locales si no son "
        "competitivas frente al mercado.\n\n"
        "Ese último punto es el que enciende las alarmas en la Patagonia. Río Negro, Neuquén y Santa Cruz están en el "
        "centro de varios de estos procesos —Vaca Muerta, el GNL costero, la minería metalífera—, pero el desafío de "
        "fondo es viejo y conocido: que la gran inversión no se lleve solo el recurso, sino que deje capacidades "
        "instaladas en el territorio: empleo, proveedores, tecnología, conocimiento. El proyecto todavía debe ser "
        "tratado por el Congreso. Su verdadero impacto se medirá no en los anuncios, sino en lo que quede en el sur "
        "cuando las plantas estén en marcha."
    ),
    "tag": "💼 Economía",
    "categoria": "economia",
    "fuente": "El Cordillerano",
    "url_original": "https://www.elcordillerano.com.ar/noticias/2026/05/28/241875-el-gobierno-impulsa-el-super-rigi-que-cambia-frente-al-regimen-actual-y-por-que-puede-impactar-en-energia-mineria-e-industria",
    "pais": "argentina",
    "imagen": None,
    "imagen_keywords": "vaca muerta energia mineria patagonia",
    "skip_og_image": True,
}

# ══════════════════════════════════════════════════════════════════
#  NEGOCIOS 2 — Zafra del langostino en Santa Cruz
# ══════════════════════════════════════════════════════════════════
neg_langostino = {
    "titulo": "Arrancó la zafra del langostino con los primeros desembarcos en los puertos de Santa Cruz",
    "bajada": "Caleta Paula y Puerto Deseado recibieron las primeras descargas con señales de muy buena abundancia. Mientras Chubut negocia un conflicto gremial, Santa Cruz se perfila para una gran temporada.",
    "cuerpo": (
        "El sur ya huele a langostino. Se lanzó oficialmente la temporada de zafra en aguas nacionales y los primeros "
        "desembarcos en los puertos santacruceños confirman lo que la región esperaba: un nivel de abundancia que "
        "promete una muy buena campaña. \"La verdad que es muy prometedor\", resumió el secretario de Pesca de Santa "
        "Cruz, Sergio Klimenko, en diálogo con Radio LU12.\n\n"
        "La apertura comprendió cuatro áreas —dos en la zona norte y las subáreas 15 y 16 en el sur—, donde operan "
        "tangoneros congeladores y fresqueros. En Caleta Paula, el buque Porto Velo II completó toda su carga en apenas "
        "un día y medio: \"Eso significa que hay muy buena abundancia de langostino\", destacó Klimenko. En Puerto "
        "Deseado, en tanto, ingresó el Tapeirón, tangonero congelador de la empresa Vieira, con capturas de la zona "
        "norte y la subárea 15. El mejor ritmo, por ahora, lo da la subárea 16.\n\n"
        "El arranque de la zafra es una reactivación clave para la mano de obra local: detrás de cada buque están la "
        "gente de la estiba, el güinchero, el apuntador, el camionero, además del comercio, los víveres y los servicios "
        "de toda la comunidad portuaria. Puerto Deseado se consolida como el tercer puerto del país en volumen de "
        "descargas, con un alza del 27% interanual, mientras Caleta Paula sostiene su lugar como segundo puerto "
        "argentino en merluza.\n\n"
        "El contraste con Chubut ordena el mapa pesquero del sur. Allí el sector reclama la emergencia pesquera y "
        "arrastra un conflicto con el gremio por los valores de descarga; Klimenko anticipó que varios buques chubutenses "
        "evalúan venir a descargar a Caleta Paula si no se destraba la situación. El gran nubarrón, advirtió, es el "
        "precio del combustible —\"el talón de Aquiles de toda la parte productiva\"—, en una actividad donde el valor "
        "del langostino lo fija el mercado internacional y no los puertos del sur."
    ),
    "tag": "💼 Economía",
    "categoria": "economia",
    "fuente": "La Opinión Austral",
    "url_original": "https://laopinionaustral.com.ar/politica-y-economia/se-realizaron-los-primeros-desembarcos-de-langostino-en-los-puertos-de-santa-cruz-667553.html",
    "pais": "argentina",
    "imagen": None,
    "imagen_keywords": "langostino pesca puerto barco",
}

# ══════════════════════════════════════════════════════════════════
#  DEPORTES — Susana Morales, atletismo máster
# ══════════════════════════════════════════════════════════════════
deportes = {
    "titulo": "Otra hazaña de Susana Morales: oro, récord y bandera neuquina en el Iberoamericano",
    "bajada": "La atleta máster de Neuquén capital, mayor de 65 años, se consagró campeona iberoamericana con récord en 300 metros con vallas en Perú, tras un viaje hecho a pulmón y peso por peso.",
    "cuerpo": (
        "Hay hazañas que no se miden solo en medallas. Susana Morales, atleta de Neuquén capital y figura del atletismo "
        "máster en la categoría mayores de 65 años, volvió a hacer historia: se consagró campeona iberoamericana con "
        "récord en los 300 metros con vallas en el Segundo Iberoamericano de Atletismo disputado en Perú. \"Salí "
        "campeona iberoamericana con récord y lo traemos para Argentina\", contó, con la emoción intacta.\n\n"
        "Lo suyo es vigencia pura. Recuperada de una lesión que la marginó nueve meses, encadenó una gira que arrancó "
        "en San Luis —tres oros en el Meeting Internacional \"Serranías Puntanas\", en 80 metros con vallas, 300 con "
        "vallas y la posta 4x100 mixta— y siguió en Lima, donde además del oro con récord sumó un bronce en 80 metros "
        "con vallas y una plata integrando el equipo argentino de postas. Un dato pinta su trayectoria: hace una década, "
        "en el primer Iberoamericano, ya tenía el récord, entonces en la categoría mayores de 55.\n\n"
        "Pero la verdadera carrera la corrió fuera de la pista. Morales juntó \"peso por peso\" para viajar y buscó el "
        "pasaje más barato posible, con escalas eternas —una de ellas, larga, en Santiago de Chile— que estiraron el "
        "viaje mucho más de lo recomendable. \"Me metí en muchas deudas para ir a Perú\", admitió, sin perder la "
        "sonrisa. Representa al Club La Ribera, y dice que escuchar el himno en el estadio \"es muy emocionante\".\n\n"
        "Ahora asoma la cita máxima de la categoría, el Mundial Máster, pero la cuenta no cierra sola. \"Si veo que "
        "junto el dinero, confirmaré mi participación. Si no, es imposible\", avisó. Su historia es la de tantos "
        "deportistas patagónicos que compiten contra el cronómetro y contra la distancia: poniendo el cuerpo, el "
        "bolsillo y el orgullo de representar al sur en cada largada."
    ),
    "tag": "🏃 Deportes",
    "categoria": "deportes",
    "fuente": "LMNeuquén",
    "url_original": "https://www.lmneuquen.com/deportes/otra-hazana-susana-morales-gran-esfuerzo-economico-un-viaje-eterno-y-medallas-neuquen-n1240748",
    "pais": "argentina",
    "imagen": None,
    "imagen_keywords": "atletismo pista corredora vallas",
}

# ── IDs ──────────────────────────────────────────────────────────
tapa["id"]           = _id(tapa["titulo"], "tapa")
sec1["id"]           = _id(sec1["titulo"], "sec1")
sec2["id"]           = _id(sec2["titulo"], "sec2")
turismo["id"]        = _id(turismo["titulo"], "tur")
cultura["id"]        = _id(cultura["titulo"], "cul")
neg_rigi["id"]       = _id(neg_rigi["titulo"], "neg1")
neg_langostino["id"] = _id(neg_langostino["titulo"], "neg2")
deportes["id"]       = _id(deportes["titulo"], "dep")

secundarias = [sec1, sec2]
ticker = [
    "Revocan la cautelar que frenaba la reforma de la ley de glaciares en Santa Cruz",
    "Tragedia en el glaciar Vinciguerra: mueren una turista y un guía en Tierra del Fuego",
    "Kast promete un plan de conectividad \"sin precedentes\" para la Carretera Austral",
    "Puerto Pirámides, única villa patagónica que compite por ser la mejor del mundo",
    "Arranca la zafra del langostino con buena abundancia en los puertos santacruceños",
]


def resolver():
    """ETAPA 1 — resuelve imágenes y galerías; guarda borrador. No toca el sitio."""
    print("\n" + "=" * 55)
    print("  ETAPA 1 — Resolución de imágenes")
    print("=" * 55)

    todas = [tapa] + secundarias + [turismo, cultura, neg_rigi, neg_langostino, deportes]

    # Normalizar tag "Medio Ambiente" → "Ambiente"
    for n in todas:
        if n.get("tag"):
            n["tag"] = re.sub(r"medio ambiente", "Ambiente", n["tag"], flags=re.IGNORECASE)

    fotos_propias = A.fotos_propias_disponibles()
    print(f"\n  Fotos propias en biblioteca: {len(fotos_propias)}")
    print("\n  Resolviendo imágenes...")
    fotos_usadas = set()
    for n in todas:
        n["imagen"] = A.resolver_imagen(n, fotos_propias, fotos_usadas)
        if "meta" not in n:
            n["meta"] = f"Hoy · {n.get('fuente', 'GLOBALpatagonia')}"

    # Galerías solo para tapa + secundarias (las notas de portada)
    print("\n  Descargando galerías...")
    for n in [tapa] + secundarias:
        url = n.get("url_original", "")
        if url.startswith("http"):
            galeria = A.extraer_galeria_articulo(url, n["id"])
            if galeria:
                n["galeria"] = galeria
                print(f"    [{n['id']}] galería: {len(galeria)} foto(s)")

    with open(BORRADOR, "w", encoding="utf-8") as f:
        json.dump({
            "tapa": tapa, "secundarias": secundarias, "turismo": turismo,
            "cultura": cultura, "neg_rigi": neg_rigi, "neg_langostino": neg_langostino,
            "deportes": deportes, "ticker": ticker,
        }, f, ensure_ascii=False, indent=2)

    print("\n  Imágenes resueltas:")
    for n in todas:
        print(f"    [{n['id'][:42]:42}] {n.get('imagen')}")
    print(f"\n  Borrador guardado en {BORRADOR}")
    print("  Revisá las imágenes y luego corré:  python3 _scripts/publicar_manual.py publicar")
    print("=" * 55 + "\n")


def publicar():
    """ETAPA 2 — usa el borrador para historial, rotaciones, noticias.json, SEO."""
    print("\n" + "=" * 55)
    print("  ETAPA 2 — Publicación en el sitio")
    print("=" * 55)

    with open(BORRADOR, encoding="utf-8") as f:
        b = json.load(f)
    tapa, secundarias = b["tapa"], b["secundarias"]
    turismo, cultura = b["turismo"], b["cultura"]
    neg_rigi, neg_langostino, deportes = b["neg_rigi"], b["neg_langostino"], b["deportes"]
    ticker = b["ticker"]

    historial     = A.cargar_historial()
    noticias_prev = A.cargar_noticias_previas()
    prev_tapa        = noticias_prev.get("tapa")
    prev_secundarias = noticias_prev.get("secundarias", [])
    prev_noticias    = noticias_prev.get("noticias", [])
    print(f"\n  Historial actual: {len(historial)} artículos")

    todas = [tapa] + secundarias + [turismo, cultura, neg_rigi, neg_langostino, deportes]

    # 5. Historial (tapa + secundarias + secciones con cuerpo)
    extras = [turismo, cultura, neg_rigi, neg_langostino, deportes]
    for e in extras:
        e["excluir_feed"] = True
    nuevas = [tapa] + secundarias + extras
    historial = nuevas + historial
    A.guardar_historial(historial)
    A._persistir_urls_nuevas(nuevas)
    print(f"\n  Artículos nuevos en historial: {len(nuevas)}")

    # 6. Rotaciones
    A.rotar_deportes(deportes)
    A.rotar_negocios(neg_rigi)          # entra primero
    A.rotar_negocios(neg_langostino)    # queda al frente
    A.rotar_cultura(cultura)
    A.rotar_turismo(turismo)

    # 7. noticias.json
    datos = A.construir_noticias_json(tapa, secundarias, prev_tapa, prev_secundarias, prev_noticias, ticker)
    fotos_usadas_final = set()
    for art in [datos["tapa"]] + datos["secundarias"] + datos["noticias"]:
        img = art.get("imagen", "")
        if not img or not os.path.exists(img):
            fb = A._foto_fallback(fotos_usadas_final)
            if fb:
                print(f"  ⚠ Sin foto: [{art.get('id')}] → fallback {fb}")
                art["imagen"] = fb
        else:
            fotos_usadas_final.add(img)
    A.guardar_json(datos)
    print(f"  Feed: tapa + {len(datos['secundarias'])} sec + {len(datos['noticias'])} noticias semana")

    # 7c. Inyectar tapa en index.html
    print("\n  Inyectando tapa en index.html...")
    A.inyectar_tapa_en_index(datos)

    # 8. Agenda (purga vencidos; sin crudas no agrega nada)
    print("\n  Actualizando agenda...")
    A.actualizar_agenda([])

    # Páginas estáticas SEO
    print("\n  Generando páginas estáticas...")
    _notas_og = list(todas)
    for _fuente in ("historial.json", "propios.json", "propios_historial.json",
                    "historias.json", "noticias.json", "turismo.json",
                    "deportes_feed.json", "negocios.json", "cultura.json", "guias.json"):
        _notas_og += A._notas_de_fuente(os.path.join(BASE, _fuente))
    _notas_og_filtradas = [n for n in _notas_og if isinstance(n, dict) and n.get("id")]
    A.generar_paginas_og(_notas_og_filtradas)

    print("\n  Actualizando índice de búsqueda...")
    A.actualizar_search_index()

    print("\n  Actualizando archivo estático en index.html...")
    A.actualizar_archivo_en_index(_notas_og_filtradas)

    print("\n  Generando páginas de temas...")
    A.generar_paginas_temas(_notas_og_filtradas)

    print("\n  Generando feed RSS...")
    A.generar_feed_rss()

    print("\n  Actualizando sitemap...")
    A.actualizar_sitemap()

    print(f"\n  ✓ Listo — {A.fecha_display()}")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "imagenes"
    if modo in ("imagenes", "resolver"):
        resolver()
    elif modo == "publicar":
        publicar()
    else:
        print("Uso: python3 _scripts/publicar_manual.py [imagenes|publicar]")
