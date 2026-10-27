#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera notas/{id}.html (ES) + variantes -en/-pt/-zh del informe
argos-georgia usando las traducciones ya escritas en propios.json
(sin API). Patrón: _gen_variantes_kelper.py."""
import os, sys, json
os.environ.setdefault("ANTHROPIC_API_KEY", "dummy-no-se-usa")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
sys.path.insert(0, os.path.join(BASE, "_scripts"))

import actualizar_noticias as A
import traducir_multiidioma as T
from pool_variantes import pool_idioma

BID = "20261027-propio-argos-georgia"
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

# 1) ES sola (sin variantes en el pool)
A.generar_paginas_og(pool_es)
es_path = os.path.join(NOTAS, f"{BID}.html")
html = open(es_path, encoding="utf-8").read()
html = T.update_switcher_and_hreflang(html, BID, "es")
open(es_path, "w", encoding="utf-8").write(html)
print(f"✓ {BID}.html (ES) generada")

# 2) Variantes: cada una con el pool de su idioma
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
    A.generar_paginas_og(pool_es + pool_idioma(lang, excluir_base=BID) + [synth])
    path = os.path.join(NOTAS, f"{BID}-{lang}.html")
    html = open(path, encoding="utf-8").read()
    html = T.update_switcher_and_hreflang(html, BID, lang)
    open(path, "w", encoding="utf-8").write(html)
    print(f"✓ {BID}-{lang}.html generada (pool {lang})")


# Firma M. Galindo (el generador solo conoce a Martineau): avatar, enlace y JSON-LD
import re
for suf in ["", "-en", "-pt", "-zh"]:
    path = os.path.join(NOTAS, f"{BID}{suf}.html")
    h = open(path, encoding="utf-8").read()
    h = h.replace("avatar-j-martineau.webp", "avatar-m-galindo.webp")
    h = re.sub(r'(<div class="nota-meta">\s*)<img src="(\.\./fotos/PERSONAJES/avatar-m-galindo\.webp)" alt="M\. Galindo" class="autor-avatar"/><span>M\. Galindo</span>',
               r'\1<a href="../autor-m-galindo.html" style="display:flex;align-items:center;gap:10px;color:inherit;text-decoration:none;"><img src="\2" alt="M. Galindo" class="autor-avatar"/><span>M. Galindo</span></a>', h)
    # JSON-LD: autora Person (como en reino-desunido) y "Por M. Galindo" en el pie
    h = h.replace('"author": {\n    "@type": "Organization",\n    "name": "GLOBALpatagonia"\n  },',
                  '"author": {\n    "@type": "Person",\n    "name": "M. Galindo",\n    "url": "https://globalpatagonia.org/autor-m-galindo.html"\n  },')
    h = re.sub(r'(<div class="nota-fuente"><strong>[^<]*</strong>) </div>',
               r'\1 ' + {'': 'Por ', '-en': 'By ', '-pt': 'Por ', '-zh': '作者：'}[suf] + r'<a href="../autor-m-galindo.html" style="color:#252830;font-weight:600;">M. Galindo</a>.</div>', h)
    open(path, "w", encoding="utf-8").write(h)
print("LISTO")
