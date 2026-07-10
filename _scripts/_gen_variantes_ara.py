#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera notas/{id}.html (ES) + variantes -en/-pt/-zh del informe ARA San Juan
usando las traducciones ya escritas en propios.json (sin API, sin truncado)."""
import os, sys, json
os.environ.setdefault("ANTHROPIC_API_KEY", "dummy-no-se-usa")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
sys.path.insert(0, os.path.join(BASE, "_scripts"))

import actualizar_noticias as A
import traducir_multiidioma as T

BID = "20260710-propio-ara-san-juan"
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

# Dicts sintéticos por idioma (sin claves titulo_en/pt/zh)
synth = []
for lang in LANGS:
    synth.append({
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
    })

A.generar_paginas_og(pool + synth)

NOTAS = os.path.join(BASE, "notas")
for lang in LANGS:
    path = os.path.join(NOTAS, f"{BID}-{lang}.html")
    html = open(path, encoding="utf-8").read()
    html = T.update_switcher_and_hreflang(html, BID, lang)
    open(path, "w", encoding="utf-8").write(html)
    print(f"  ✓ {BID}-{lang}.html — switcher/hreflang/SEO aplicado")

es_path = os.path.join(NOTAS, f"{BID}.html")
html = open(es_path, encoding="utf-8").read()
html = T.update_switcher_and_hreflang(html, BID, "es")
open(es_path, "w", encoding="utf-8").write(html)
print(f"  ✓ {BID}.html (ES) — switcher aplicado")
print("LISTO")
