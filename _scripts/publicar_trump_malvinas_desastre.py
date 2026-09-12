#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Publica una noticia puntual (secundaria) basada en la nota de Página/12:
"Trump planteó que un conflicto entre Argentina y el Reino Unido por las
Malvinas sería un 'desastre potencial'" (12/09/2026).

Reemplaza la secundaria 2 del día (Bariloche/turismo de reuniones), que
rota automáticamente a "Noticias de la semana" vía construir_noticias_json
(mismo mecanismo que usa el Action diario).
"""
import os
import sys
import json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

import actualizar_noticias as A

titulo = "Trump: un conflicto por Malvinas sería un \"desastre potencial\""
bajada = ("El presidente de Estados Unidos dijo en Dublín que Argentina y el "
          "Reino Unido están \"enfadados\" por las islas, y se ofreció a "
          "intervenir si ambos gobiernos se lo piden.")

cuerpo = "\n\n".join([
    "Donald Trump volvió a poner a Malvinas en el centro de la escena internacional. "
    "El presidente de Estados Unidos advirtió que un conflicto entre Argentina y el "
    "Reino Unido por la soberanía del archipiélago sería \"un desastre potencial\", y "
    "se mostró dispuesto a mediar si ambos países se lo piden. Lo dijo el sábado en "
    "Dublín, tras reunirse con el primer ministro irlandés, Micheál Martin.",

    "\"Estoy seguro de que me llamarán por ese potencial desastre, pero si lo hacen, "
    "probablemente podré resolverlo\", dijo Trump ante la prensa, en referencia a un "
    "eventual pedido de intervención de Buenos Aires o Londres. El mandatario "
    "caracterizó a ambos países como \"dos naciones\" que hoy están \"enfadadas\" entre "
    "sí por el reclamo de soberanía, vigente desde la guerra de 1982.",

    "Consultado sobre una posible mediación en el terreno, Trump relativizó sus "
    "propias chances de viajar hasta el Atlántico Sur: dijo no saber si los gobiernos "
    "estarían dispuestos a trasladarse \"tan lejos\" para un eventual encuentro, y "
    "bromeó con que el trayecto insumiría \"semanas\" en barco. También se refirió al "
    "conflicto de 1982: dijo haberlo \"observado muy de cerca\" en su momento y "
    "consideró que el Reino Unido \"las recuperó con bastante firmeza\", aunque aclaró "
    "que aquello \"quedó muy lejos\" en el tiempo.",

    "No es la primera vez que Trump menciona a Malvinas en público: semanas atrás ya "
    "se había referido al tema en una entrevista con el diario británico The "
    "Telegraph, en medio de la presión de su gobierno sobre los socios europeos de la "
    "OTAN. Con este nuevo comentario en Dublín se reactiva una pregunta que ni "
    "Buenos Aires ni Londres dan por cerrada: qué margen de maniobra tiene Washington "
    "—y su presidente— sobre uno de los litigios territoriales más antiguos de "
    "América del Sur.",
])

nota = {
    "titulo": titulo,
    "bajada": bajada,
    "cuerpo": cuerpo,
    "tag": "🌎 Atlántico Sur",
    "categoria": "general",
    "fuente": "Página/12",
    "url_original": "https://www.pagina12.com.ar/2026/09/12/trump-planteo-que-un-conflicto-entre-argentina-y-el-reino-unido-por-las-malvinas-seria-un-desastre-potencial/",
    "pais": "argentina",
    "imagen": "fotos/malvinas-milei-trump.webp",
    "imagen_keywords": "trump malvinas argentina reino unido conflicto",
    "meta": "Hoy · Página/12",
}
nota["id"] = f"{A.slugify(titulo)}-sec2"
if not nota["id"].startswith("20260912"):
    nota["id"] = "20260912-" + nota["id"]

with open(os.path.join(BASE, "noticias.json"), encoding="utf-8") as f:
    actual = json.load(f)

tapa = actual["tapa"]
sec_actuales = actual["secundarias"]
sec1_actual = sec_actuales[0]
prev_noticias = actual.get("noticias", [])
ticker = actual.get("ticker", [])

nuevas_secundarias = [sec1_actual, nota]

# Ticker: reemplaza la mención genérica anterior por el titular concreto
ticker = [
    "Trump: Malvinas sería un \"desastre potencial\"" if "Trump" in t else t
    for t in ticker
]

datos = A.construir_noticias_json(
    tapa=tapa,
    secundarias=nuevas_secundarias,
    prev_tapa=tapa,
    prev_secundarias=sec_actuales,
    prev_noticias=prev_noticias,
    ticker=ticker,
)

# Historial (permanente)
historial = A.cargar_historial()
historial = [nota] + historial
A.guardar_historial(historial)
A._persistir_urls_nuevas([nota])

A.guardar_json(datos)
print(f"Nueva secundaria: {nota['id']}")
print(f"Bariloche (sec2 anterior) rotó a noticias de la semana.")

# Inyectar tapa/secundarias en index.html
A.inyectar_tapa_en_index(datos)

# Página estática SEO
todas_notas = [tapa] + nuevas_secundarias + datos["noticias"]
for _fuente in ("historial.json", "propios.json", "propios_historial.json",
                "historias.json", "noticias.json", "turismo.json",
                "deportes_feed.json", "negocios.json", "cultura.json", "guias.json"):
    todas_notas += A._notas_de_fuente(os.path.join(BASE, _fuente))
todas_notas = [n for n in todas_notas if isinstance(n, dict) and n.get("id")]
A.generar_paginas_og(todas_notas)

A.actualizar_search_index()
A.actualizar_archivo_en_index(todas_notas)
A.generar_paginas_temas(todas_notas)
A.generar_feed_rss()
A.actualizar_sitemap()

print("OK — publicado.")
