#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera notas/{id}-en/-pt/-zh.html del informe datacenter usando las traducciones
ya escritas en propios.json (sin API, sin truncado). Reusa el template del sitio
(generar_paginas_og) + el helper de switcher/hreflang/SEO de traducir_multiidioma."""
import os, sys, json
os.environ.setdefault("ANTHROPIC_API_KEY", "dummy-no-se-usa")  # solo para poder importar el módulo

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
sys.path.insert(0, os.path.join(BASE, "_scripts"))

import actualizar_noticias as A
import traducir_multiidioma as T

BID = "20260629-propio-datacenter-ia-patagonia"
LANGS = ["en", "pt", "zh"]

propios = json.load(open(os.path.join(BASE, "propios.json"), encoding="utf-8"))
entry = next(p for p in propios if p["id"] == BID)

# Pool real para "También te puede interesar"
pool = []
for src in ("historial.json","propios.json","propios_historial.json","historias.json",
            "noticias.json","turismo.json","deportes_feed.json","negocios.json","cultura.json","guias.json"):
    p = os.path.join(BASE, src)
    if os.path.exists(p):
        pool += A._notas_de_fuente(p)
pool = [n for n in pool if isinstance(n, dict) and n.get("id")]

# Dicts sintéticos por idioma: id sufijado, contenido traducido, SIN titulo_en/pt/zh
# (para que generar_paginas_og no arme hreflang equivocados; los pone el helper después)
synth = []
for lang in LANGS:
    e = {
        "id": f"{BID}-{lang}",
        "titulo": entry[f"titulo_{lang}"],
        "bajada": entry[f"bajada_{lang}"],
        "cuerpo": entry[f"cuerpo_{lang}"],
        "tag": entry.get("tag",""),
        "categoria": entry.get("categoria",""),
        "fuente": entry.get("fuente","GLOBALpatagonia"),
        "autor": entry.get("autor",""),
        "propio": True,
        "pais": entry.get("pais",""),
        "imagen": entry.get("imagen",""),
        "fecha": entry.get("fecha",""),
        "meta": entry.get("meta",""),
    }
    synth.append(e)

A.generar_paginas_og(pool + synth)

# Arreglar lang/switcher/hreflang/og:locale/fuentes-chinas con el helper (sin API)
NOTAS = os.path.join(BASE, "notas")
for lang in LANGS:
    path = os.path.join(NOTAS, f"{BID}-{lang}.html")
    html = open(path, encoding="utf-8").read()
    html = T.update_switcher_and_hreflang(html, BID, lang)
    open(path, "w", encoding="utf-8").write(html)
    print(f"  ✓ {BID}-{lang}.html — switcher/hreflang/SEO aplicado")

# Y al ES también (para que tenga el switcher visible que apunta a las variantes)
es_path = os.path.join(NOTAS, f"{BID}.html")
html = open(es_path, encoding="utf-8").read()
html = T.update_switcher_and_hreflang(html, BID, "es")
open(es_path, "w", encoding="utf-8").write(html)
print(f"  ✓ {BID}.html (ES) — switcher aplicado")
print("LISTO")
