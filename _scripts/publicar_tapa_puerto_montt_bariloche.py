#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tapa manual 27/10/2026: vuelos directos Puerto Montt–Bariloche (El Cordillerano).
La tapa vigente baja a sec1, sec1 a sec2 y sec2 a noticias[] (cascada de construir_noticias_json)."""
import os, sys, re
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import actualizar_noticias as A
from datetime import datetime

tapa = {
    "titulo": "De Puerto Montt a Bariloche en 45 minutos: la ruta aérea directa busca volver este verano",
    "bajada": "Una delegación del municipio chileno recorrió el aeropuerto de Bariloche y la reapertura de la ruta entra en su fase final. Falta un escáner de Aduanas para el aeropuerto El Tepual.",
    "cuerpo": (
        "Cruzar la cordillera entre Puerto Montt y Bariloche lleva entre cuatro y seis horas por tierra. En avión, unos 45 minutos. "
        "Esa diferencia explica por qué las dos ciudades trabajan para que los vuelos directos vuelvan a operar este verano.\n\n"
        "Las gestiones están en su etapa final. Una delegación municipal chilena, encabezada por el alcalde de Puerto Montt, Rodrigo Wainraihgt, "
        "visitó el Aeropuerto Internacional Teniente Luis Candelaria, en Bariloche, una terminal que movilizó más de 2,5 millones de pasajeros en 2025.\n\n"
        "La reapertura se había demorado por requerimientos técnicos. El obstáculo principal fue el control de Aduanas en El Tepual, el aeropuerto de Puerto Montt, "
        "que necesita un escáner bidireccional para habilitar vuelos internacionales. El avance llegó cuando el Consejo Regional de Los Lagos aprobó 146 millones de pesos para comprarlo.\n\n"
        "La licitación del equipo ya recibió ofertas. Si se concreta a tiempo, la ruta podría estar disponible en plena temporada de verano.\n\n"
        "La conexión directa importa para toda la región. Une dos de los destinos turísticos más fuertes de la Patagonia norte, acorta un cruce que hoy depende del estado de los pasos "
        "y de las horas de ruta, y suma a los viajeros de ambos lados de la frontera."
    ),
    "tag": "✈ Transporte",
    "categoria": "transporte",
    "fuente": "El Cordillerano",
    "url_original": "https://www.elcordillerano.com.ar/noticias/2026/10/26/269598-de-puerto-montt-a-bariloche-en-45-minutos-buscan-que-los-vuelos-directos-vuelvan-este-verano",
    "pais": "ambos",
    "imagen": "https://elcordillerano-s3.cdn.net.ar/s3i233/2025/05/elcordillerano/images/01/87/18/1871854_c74e19a5759a0c689ef596dd7262d42638b1b79b13fd40681ad145d8fd06a793/md.webp",
    "imagen_keywords": "aeropuerto bariloche",
}
tapa["id"] = f"{datetime.now():%Y%m%d}-{A.slugify(tapa['titulo'])}-tapa"
tapa["meta"] = "Hoy · El Cordillerano"

tapa["imagen"] = A.resolver_imagen(tapa, A.fotos_propias_disponibles(), set())
print("IMAGEN:", tapa["imagen"])

historial = A.cargar_historial()
prev = A.cargar_noticias_previas()
prev_tapa, prev_sec, prev_not = prev.get("tapa"), prev.get("secundarias", []), prev.get("noticias", [])

tapa["excluir_feed"] = True
A.guardar_historial([tapa] + historial)
A._persistir_urls_nuevas([tapa])

# cascada: tapa vieja -> sec1, sec1 -> sec2, sec2 -> noticias[]
nuevas_sec = [prev_tapa, prev_sec[0]]
ticker = ["De Puerto Montt a Bariloche en 45 minutos: buscan que vuelvan los vuelos directos"] + (prev.get("ticker") or [])[:4]
datos = A.construir_noticias_json(tapa, nuevas_sec, prev_tapa, prev_sec, prev_not, ticker)
# el sec2 desplazado (prev_sec[1]) entra a noticias[] al frente, sin duplicar
if prev_sec[1:] and prev_sec[1].get("id") not in {n.get("id") for n in datos["noticias"]}:
    datos["noticias"] = ([prev_sec[1]] + datos["noticias"])[:8]
A.guardar_json(datos)
A.inyectar_tapa_en_index(datos)

import json
notas = [tapa]
for f in ("historial.json","propios.json","propios_historial.json","historias.json","noticias.json","turismo.json",
          "deportes_feed.json","negocios.json","cultura.json","guias.json"):
    notas += A._notas_de_fuente(os.path.join(BASE, f))
notas = [n for n in notas if isinstance(n, dict) and n.get("id")]
A.generar_paginas_og(notas)
A.actualizar_search_index()
A.actualizar_archivo_en_index(notas)
A.generar_paginas_temas(notas)
A.generar_feed_rss()
A.actualizar_sitemap()
print("OK", tapa["id"])
