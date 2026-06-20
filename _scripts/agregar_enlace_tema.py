#!/usr/bin/env python3
"""Retrofit: convierte el <div class="nota-tag"> de cada notas/*.html en un
enlace al hub de su tema (../temas/{slug}.html).

Motivo: las páginas temas/ estaban huérfanas (solo en el sitemap). Enlazar cada
nota a su hub de categoría de-orfaniza esos hubs y le da a Google una ruta de
rastreo nota → hub → otras notas del tema, ayudando a indexar las páginas
"descubiertas/rastreadas sin indexar".

Idempotente: salta las notas que ya tienen <a class="nota-tag">. Solo toca notas
cuya categoría (leída de los JSON) mapea a un tema válido. Omite variantes de
idioma (-en/-pt/-zh). NO sobreescribe estructura: solo sustituye el bloque del tag.

El template de notas nuevas (generar_paginas_og en actualizar_noticias.py) ya
genera el enlace directamente; este script es solo para las notas ya existentes.
"""
import json, os, glob, re, unicodedata, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_TEMA_LABELS = {
    "medio-ambiente", "economia", "produccion", "cultura", "ciencia",
    "deportes", "turismo", "conectividad", "historia", "pueblos-originarios",
    "bienestar", "sociedad",
}

def _slug(cat):
    cat = cat.strip().lower()
    cat = unicodedata.normalize("NFD", cat)
    cat = "".join(c for c in cat if unicodedata.category(c) != "Mn")
    return cat.replace(" ", "-")

def construir_mapa_categorias():
    """id -> categoria, leyendo todos los JSON de la raíz + archivo/."""
    cat = {}
    fuentes = glob.glob(os.path.join(BASE, "*.json")) + \
              glob.glob(os.path.join(BASE, "archivo", "*.json"))
    for f in fuentes:
        try:
            with open(f, encoding="utf-8") as fh:
                data = json.load(fh)
        except Exception:
            continue
        lista = data.get("notas") if isinstance(data, dict) else data
        if not isinstance(lista, list):
            continue
        for n in lista:
            if isinstance(n, dict) and n.get("id") and n.get("categoria"):
                cat.setdefault(n["id"], n["categoria"])
    return cat

_RE_DIV = re.compile(r'<div class="nota-tag">(.*?)</div>', re.DOTALL)
# Enlaces ya creados que apuntan a un hub inexistente — para auto-reparar.
_RE_A = re.compile(r'<a class="nota-tag"[^>]*href="\.\./temas/([a-z-]+)\.html"[^>]*>(.*?)</a>', re.DOTALL)

def _tema_existe(slug):
    return bool(slug) and os.path.isfile(os.path.join(BASE, "temas", f"{slug}.html"))

def main():
    cat = construir_mapa_categorias()
    notas = [f for f in glob.glob(os.path.join(BASE, "notas", "*.html"))
             if not re.search(r"-(en|pt|zh)\.html$", f)]

    cambiadas = saltadas_ok = sin_tema = reparadas = 0
    for ruta in notas:
        with open(ruta, encoding="utf-8") as fh:
            html = fh.read()
        nid = os.path.basename(ruta)[:-5]

        # Auto-reparación: enlace a un hub que NO existe → volver a <div>.
        if '<a class="nota-tag"' in html:
            def _fix(m):
                nonlocal reparadas
                if _tema_existe(m.group(1)):
                    return m.group(0)
                reparadas += 1
                return f'<div class="nota-tag">{m.group(2)}</div>'
            nuevo = _RE_A.sub(_fix, html)
            if nuevo != html:
                with open(ruta, "w", encoding="utf-8") as fh:
                    fh.write(nuevo)
                html = nuevo
            if '<a class="nota-tag"' in html:   # sigue teniendo enlace válido
                saltadas_ok += 1
                continue

        if '<div class="nota-tag">' not in html:  # estructura distinta
            continue
        c0 = str(cat.get(nid, "")).split("|")[0].strip()
        slug = _slug(c0) if c0 else ""
        if not _tema_existe(slug):                # solo enlazar a hubs reales
            sin_tema += 1
            continue
        href = f"../temas/{slug}.html"
        nuevo = _RE_DIV.sub(
            lambda m: f'<a class="nota-tag" style="text-decoration:none" href="{href}">{m.group(1)}</a>',
            html, count=1)
        if nuevo != html:
            with open(ruta, "w", encoding="utf-8") as fh:
                fh.write(nuevo)
            cambiadas += 1

    print(f"Enlace a tema agregado: {cambiadas} | ya tenían: {saltadas_ok} | "
          f"reparadas (hub inexistente→div): {reparadas} | sin tema mapeable: {sin_tema}")

if __name__ == "__main__":
    main()
