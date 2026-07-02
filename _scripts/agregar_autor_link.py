#!/usr/bin/env python3
"""Retrofit de firma de autor en notas estáticas ya publicadas.

En cada notas/*.html firmado por J. Martineau:
  1. JSON-LD: al author Person se le agrega "url" → autor-j-martineau.html
  2. La firma visible (avatar + nombre) queda envuelta en <a> a esa página
  3. Avatares con inline style 54px pasan a 96px (estándar de firma grande)

Idempotente: cada paso se saltea si la página ya lo tiene.
Correr desde la raíz del proyecto: python3 _scripts/agregar_autor_link.py
"""
import glob
import re
from pathlib import Path

BASE = Path(__file__).parent.parent
AUTOR_URL = "https://globalpatagonia.org/autor-j-martineau.html"
LINK_REL = "../autor-j-martineau.html"
LINK_STYLE = "display:flex;align-items:center;gap:10px;color:inherit;text-decoration:none;"

# 1) Person sin url → Person con url (tolera espaciado variable)
RE_PERSON = re.compile(
    r'\{\s*"@type":\s*"Person"\s*,\s*"name":\s*"J\. Martineau"\s*\}')
PERSON_CON_URL = ('{"@type": "Person","name": "J. Martineau",'
                  f'"url": "{AUTOR_URL}"}}')

# 2a) Variante del generador: <img .../><span>J. Martineau</span>
RE_FIRMA_GEN = re.compile(
    r'(?<!none;">)(<img [^>]*avatar-j-martineau[^>]*>)<span>J\. Martineau</span>')

# 2b) Variante manual: <span style="display:flex..."><img ...> J. Martineau</span>
RE_FIRMA_SPAN = re.compile(
    r'(<span[^>]*display:flex[^>]*>)\s*(<img [^>]*avatar-j-martineau[^>]*>)\s*'
    r'(J\. Martineau)\s*(</span>)')

# 2c) Variante manual sin estilo: <span><img ...> J. Martineau</span>
RE_FIRMA_SPAN_SIMPLE = re.compile(
    r'(<span>)(<img [^>]*avatar-j-martineau[^>]*>)\s?(J\. Martineau)(</span>)')

# 2d) Pie de nota: <strong>Por/By J. Martineau</strong> · Nota de producción propia
RE_FIRMA_PIE = re.compile(r'<strong>(Por|By|Autor:) (J\. Martineau)</strong>')

# 2e) Pie zh: <strong>J. Martineau 撰写</strong> o <strong>J. Martineau</strong>
RE_FIRMA_PIE_ZH = re.compile(r'<strong>(J\. Martineau)( 撰写)?</strong>')

# 2f) Meta: <span>J. Martineau · GLOBALpatagonia</span> / <span>fecha · J. Martineau</span>
# El lookahead (?!</a>) evita re-enlazar el <span> que vive DENTRO del <a>
# que arma la regla 2a (quedaría un anchor anidado, HTML inválido).
RE_FIRMA_META = re.compile(
    r'<span>(?P<pre>[^<]*· )?(J\. Martineau)(?P<post> · [^<]*)?</span>(?!</a>)')

# 2g) Byline card: <span class="byline-nombre">J. Martineau</span>
RE_FIRMA_BYLINE = re.compile(r'(<span class="byline-nombre">)(J\. Martineau)(</span>)')

# 1b) author Organization GLOBALpatagonia en página firmada → Person con url
RE_AUTHOR_ORG = re.compile(
    r'"author":\s*\{\s*"@type":\s*"Organization",\s*"name":\s*"GLOBALpatagonia"\s*\}')

FIRMA_VISIBLE = re.compile(r'(Por|By) J\. Martineau|J\. Martineau 撰写|'
                           r'<span>J\. Martineau|> ?J\. Martineau</span>')

LINK_INLINE = f'<a href="{LINK_REL}" style="color:inherit;">J. Martineau</a>'


def procesar(path):
    html = Path(path).read_text(encoding="utf-8")
    orig = html
    cambios = []

    if AUTOR_URL not in html or RE_PERSON.search(html):
        nuevo = RE_PERSON.sub(PERSON_CON_URL, html)
        if nuevo != html:
            cambios.append("jsonld-url")
            html = nuevo

    # Solo en páginas firmadas visiblemente por Martineau (las de "Redacción"
    # usan el mismo avatar pero no llevan firma personal → no se tocan).
    firmada = bool(FIRMA_VISIBLE.search(html)) or bool(RE_FIRMA_GEN.search(html))

    if firmada and RE_AUTHOR_ORG.search(html):
        html = RE_AUTHOR_ORG.sub('"author": ' + PERSON_CON_URL, html)
        cambios.append("jsonld-org→person")

    if firmada:
        for regex, repl, tag_c in (
            (RE_FIRMA_GEN,
             rf'<a href="{LINK_REL}" style="{LINK_STYLE}">\1'
             r'<span>J. Martineau</span></a>', "link-firma"),
            (RE_FIRMA_SPAN,
             rf'\1<a href="{LINK_REL}" style="{LINK_STYLE}">\2 \3</a>\4',
             "link-firma-span"),
            (RE_FIRMA_SPAN_SIMPLE,
             rf'\1<a href="{LINK_REL}" style="{LINK_STYLE}">\2 \3</a>\4',
             "link-firma-span-simple"),
            (RE_FIRMA_PIE, rf'<strong>\1 {LINK_INLINE}</strong>', "link-pie"),
            (RE_FIRMA_PIE_ZH, rf'<strong>{LINK_INLINE}\2</strong>', "link-pie-zh"),
            (RE_FIRMA_META,
             rf'<span>\g<pre>{LINK_INLINE}\g<post></span>', "link-meta"),
            (RE_FIRMA_BYLINE, rf'\1{LINK_INLINE}\3', "link-byline"),
        ):
            nuevo = regex.sub(repl, html)
            if nuevo != html:
                cambios.append(tag_c)
                html = nuevo

    # 3) avatar chico → 96px (solo el inline style del avatar de Martineau)
    def _agrandar(m):
        return m.group(0).replace("width:54px;height:54px", "width:96px;height:96px")
    nuevo = re.sub(r'<img [^>]*avatar-j-martineau[^>]*54px[^>]*>', _agrandar, html)
    if nuevo != html:
        cambios.append("avatar-96px")
        html = nuevo

    if html != orig:
        Path(path).write_text(html, encoding="utf-8")
    return cambios


def main():
    tocados = 0
    for f in sorted(glob.glob(str(BASE / "notas" / "*.html"))):
        if "martineau" not in Path(f).read_text(encoding="utf-8").lower():
            continue
        cambios = procesar(f)
        if cambios:
            tocados += 1
            print(f"{Path(f).name}: {', '.join(cambios)}")
    print(f"\n{tocados} páginas modificadas.")


if __name__ == "__main__":
    main()
