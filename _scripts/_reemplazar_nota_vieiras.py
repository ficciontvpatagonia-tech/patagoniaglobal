#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reemplaza la nota de vieiras (29/10/2026) por la versión completa: nombres, lugares y datos de la fuente."""
import json, re, sys, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE); sys.path.insert(0, BASE)
NID = "20261029-una-tecnica-del-conicet-logra-cuadruplicar-la-tapa"
TITULO = "Vieiras en el golfo San José: el método del CONICET que cuadruplicó la captación de semillas"
BAJADA = ("Un equipo del CESIMAR instala redes en el mar para que las larvas de vieira se fijen y crezcan, y después las siembra en el fondo "
          "para ayudar a recuperar bancos que la pesca deja casi agotados. Con un nuevo diseño de colectores, ya captan cuatro veces más semillas.")
CUERPO = "\n\n".join([
"En las aguas del golfo San José, en la costa de Chubut, hay redes con vieiras del tamaño de una lenteja creciendo bajo el agua. Son parte de un proyecto científico que busca algo difícil: ayudar a que se recuperen los bancos de vieira Tehuelche, el recurso emblemático de los marisqueros artesanales de la zona. Con un nuevo diseño de colectores, el equipo logró cuadruplicar la cantidad de juveniles captados.",
"El proyecto lo lideran Leandro Getino Mamet, becario posdoctoral del CONICET, y Gaspar Soria, investigador del Consejo, ambos del Centro para el Estudio de Sistemas Marinos (CESIMAR). Cuentan con el apoyo de Matías Soutric, de la Secretaría de Pesca de Chubut, y de Camila Martínez, alumna de la Universidad Nacional de la Patagonia San Juan Bosco (UNPSJB). También participan los buzos profesionales del Área de Náutica y Buceo del CENPAT.",
"El problema de fondo es conocido. La vieira se extrae a mano, buceando, en bancos de hasta unos 25 metros de profundidad. Esos bancos pueden llegar a 150 ejemplares por metro cuadrado, pero después de la pesca quedan casi agotados. A eso se suman los ciclos naturales de abundancia y escasez, de modo que recuperarse puede llevar varias temporadas.",
"Las vieiras son hermafroditas y, cuando maduran, desovan directamente en el agua inducidas por cambios bruscos de temperatura. El desove ocurre entre fines de diciembre y enero, y las larvas nadan alrededor de un mes buscando dónde fijarse. En la naturaleza se adhieren a algas o conchillas. El equipo aprovecha ese comportamiento con colectores de una red llamada Netlon, donde las larvas se asientan y empiezan a crecer, al principio con apenas dos o tres milímetros. Cuando alcanzan un tamaño adecuado, los científicos las recuperan y las siembran en el fondo marino. Así no dependen solo de que las nuevas generaciones sobrevivan por su cuenta.",
"La experiencia empezó en el verano de 2025. Los colectores se instalaron en Fracasso y, en abril, las semillas se sembraron en Los Morros, a escala experimental: unas 30.000 vieiras, con densidades similares a las naturales. El trabajo contó con financiamiento del Lerner-Gray Fund for Marine Research, del Museo de Historia Natural de Nueva York, y la idea era seguir a los ejemplares durante unos 18 meses. Hoy, a un año y medio, algunos ya alcanzaron los 60 milímetros, una talla cercana a la establecida legalmente para su captura, y crecieron a un ritmo similar al de las poblaciones naturales.",
"El obstáculo llegó por otro lado. Las ascidias, que en la zona llaman \"papas de mar\", colonizan las redes y complican la recuperación de las vieiras pequeñas. Durante 2026 el equipo probó limpiezas por buceo y modificó el diseño de los colectores. Según Getino Mamet, los resultados fueron \"prometedores\": ayudaron a reducir el efecto de las papas de mar y el tiempo de trabajo para recuperar las semillas, y aumentaron la captación y el crecimiento. El nuevo modelo captó cuatro veces más semillas que en las experiencias anteriores.",
"El contexto institucional también cuenta. El Plan de Manejo del Área Natural Protegida Península Valdés incluye repoblar bancos de bivalvos como respuesta al impacto de la pesca, y este proyecto es el primer paso concreto para aplicar esa medida en el golfo San José. \"El objetivo a largo plazo es generar conocimiento y herramientas que permitan replicar esta experiencia a mayor escala\", dijo Getino Mamet cuando comenzó la experiencia.",
"Por ahora sigue siendo una prueba piloto: no hay datos publicados sobre cuántos kilos se obtendrán ni cuánto costaría llevar el método a escala comercial. Del otro lado de la cordillera, la vieira se cultiva con concesiones desde hace años en Los Lagos y Aysén. Si el sistema se sostiene fuera del piloto, la Patagonia argentina tendría una herramienta propia para cuidar el recurso y el trabajo de los marisqueros artesanales.",
])
FUENTE = "Diario Río Negro"

for f in ("noticias.json", "historial.json"):
    d = json.load(open(f, encoding="utf-8"))
    n = d["tapa"] if f == "noticias.json" else next(x for x in d if x.get("id") == NID)
    n["titulo"], n["bajada"], n["cuerpo"] = TITULO, BAJADA, CUERPO
    n["imagen_keywords"] = "vieiras mariscos golfo san josé"
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("OK", f)

# index.html: tapa estática + archivo
h = open("index.html", encoding="utf-8").read()
VIEJO = "Una técnica del CONICET logra cuadruplicar la captación de vieiras en Chubut"
assert h.count(VIEJO) == 2, h.count(VIEJO)
h = h.replace(VIEJO, TITULO)
m = re.search(r'(<h3>' + re.escape(TITULO) + r'</h3>\s*<p><span[^>]*>🇦🇷</span> )(.*?)(</p>)', h, flags=re.S)
h = h[:m.start(2)] + BAJADA + h[m.end(2):]
open("index.html", "w", encoding="utf-8").write(h)
print("OK index.html")
