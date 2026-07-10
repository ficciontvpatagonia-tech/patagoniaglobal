#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenera las 4 páginas del informe ARA San Juan con relacionadas correctas:
ES → otras notas ES; -en/-pt/-zh → notas traducidas del mismo idioma (con
fallback a ES gracias al picker parcheado). Reaplica switcher/hreflang."""
import os, sys, json
os.environ.setdefault("ANTHROPIC_API_KEY", "dummy-no-se-usa")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
sys.path.insert(0, os.path.join(BASE, "_scripts"))

import actualizar_noticias as A
import traducir_multiidioma as T
from pool_variantes import pool_idioma

BID = "20260710-propio-ara-san-juan"
LANGS = ["en", "pt", "zh"]
NOTAS = os.path.join(BASE, "notas")

propios = json.load(open(os.path.join(BASE, "propios.json"), encoding="utf-8"))
entry = next(p for p in propios if p["id"] == BID)

pool_es = []
for src in ("historial.json","propios.json","propios_historial.json","historias.json",
            "noticias.json","turismo.json","deportes_feed.json","negocios.json","cultura.json","guias.json"):
    p = os.path.join(BASE, src)
    if os.path.exists(p):
        pool_es += A._notas_de_fuente(p)
pool_es = [n for n in pool_es if isinstance(n, dict) and n.get("id")]

# 1) ES: regenerar sola (sin variantes en el pool)
os.remove(os.path.join(NOTAS, f"{BID}.html"))
A.generar_paginas_og(pool_es)
html = open(os.path.join(NOTAS, f"{BID}.html"), encoding="utf-8").read()
html = T.update_switcher_and_hreflang(html, BID, "es")
open(os.path.join(NOTAS, f"{BID}.html"), "w", encoding="utf-8").write(html)
print(f"✓ {BID}.html (ES) regenerada")

# 2) Variantes: cada una con el pool de su idioma (descubierto en disco)
for lang in LANGS:
    synth = {
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
    path = os.path.join(NOTAS, f"{BID}-{lang}.html")
    os.remove(path)
    A.generar_paginas_og(pool_es + pool_idioma(lang, excluir_base=BID) + [synth])
    html = open(path, encoding="utf-8").read()
    html = T.update_switcher_and_hreflang(html, BID, lang)
    open(path, "w", encoding="utf-8").write(html)
    print(f"✓ {BID}-{lang}.html regenerada (pool {lang})")

print("LISTO")
