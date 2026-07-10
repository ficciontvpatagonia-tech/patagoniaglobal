#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Helper: descubre en notas/ las páginas traducidas -en/-pt/-zh existentes y
devuelve entradas {id, titulo, tag, imagen} aptas para el pool de relacionadas
de generar_paginas_og. Así las páginas traducidas recomiendan notas del MISMO
idioma (el picker _pick_related las prefiere) en vez de notas en español.

Uso desde un _gen_variantes_*.py:
    from pool_variantes import pool_idioma
    A.generar_paginas_og(pool_es + pool_idioma("en") + [synth_en])
"""
import os, re, glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTAS = os.path.join(BASE, "notas")


def _og(html, prop):
    m = re.search(r'property="og:%s" content="(.*?)"' % prop, html)
    return m.group(1).strip() if m else ""


def pool_idioma(lang, excluir_base=None):
    """Entradas de pool para todas las notas/{*}-{lang}.html en disco.
    excluir_base: id base cuya variante no debe entrar (la nota actual)."""
    out = []
    for path in sorted(glob.glob(os.path.join(NOTAS, f"*-{lang}.html"))):
        nid = os.path.basename(path)[: -len(".html")]
        if excluir_base and nid == f"{excluir_base}-{lang}":
            continue
        try:
            html = open(path, encoding="utf-8").read()
        except Exception:
            continue
        titulo = _og(html, "title") or nid
        titulo = re.sub(r"\s+—\s+GLOBALpatagonia$", "", titulo)
        imagen = _og(html, "image")
        out.append({"id": nid, "titulo": titulo, "tag": "", "imagen": imagen})
    return out
