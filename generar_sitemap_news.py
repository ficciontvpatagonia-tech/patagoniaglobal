#!/usr/bin/env python3
"""
Genera sitemap-news.xml para Google News.
Solo incluye artículos de los últimos 2 días (requisito de Google News).
"""

import json
import os
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://globalpatagonia.org"
ARGENTINA_TZ = timezone(timedelta(hours=-3))


def fecha_desde_id(nota_id):
    """Extrae datetime desde ID formato YYYYMMDD-... Retorna None si no aplica."""
    try:
        if nota_id and len(nota_id) >= 8 and nota_id[:8].isdigit():
            y = int(nota_id[:4])
            m = int(nota_id[4:6])
            d = int(nota_id[6:8])
            return datetime(y, m, d, 9, 0, 0, tzinfo=ARGENTINA_TZ)
    except (ValueError, TypeError):
        pass
    return None


def es_reciente(nota_id, dias=2):
    fecha = fecha_desde_id(nota_id)
    if not fecha:
        return False
    return (datetime.now(ARGENTINA_TZ) - fecha).days < dias


def recolectar_notas():
    notas = []
    vistas = set()

    # noticias.json (tapa + secundarias + feed)
    path = os.path.join(REPO, 'noticias.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        items = []
        if data.get('tapa'):
            items.append(data['tapa'])
        items += data.get('secundarias', [])
        items += data.get('noticias', [])
        for nota in items:
            nid = nota.get('id', '')
            if nid and nid not in vistas and es_reciente(nid):
                vistas.add(nid)
                notas.append(nota)

    # historial.json (captura deportes, turismo, etc. del mismo día)
    path = os.path.join(REPO, 'historial.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        for nota in data:
            nid = nota.get('id', '')
            if nid and nid not in vistas and es_reciente(nid):
                vistas.add(nid)
                notas.append(nota)

    return notas


def url_de_nota(nid):
    nota_html = os.path.join(REPO, 'notas', f'{nid}.html')
    if os.path.exists(nota_html):
        return f"{BASE_URL}/notas/{nid}.html"
    return f"{BASE_URL}/nota.html?id={nid}"


def escape_xml(text):
    return (text or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def generar():
    notas = recolectar_notas()

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">',
    ]

    for nota in notas:
        nid = nota.get('id', '')
        titulo = escape_xml(nota.get('titulo', ''))
        fecha = fecha_desde_id(nid)
        if not fecha or not titulo:
            continue

        url = url_de_nota(nid)
        fecha_iso = fecha.strftime('%Y-%m-%dT09:00:00-03:00')

        lines += [
            '  <url>',
            f'    <loc>{url}</loc>',
            '    <news:news>',
            '      <news:publication>',
            '        <news:name>GLOBALpatagonia</news:name>',
            '        <news:language>es</news:language>',
            '      </news:publication>',
            f'      <news:publication_date>{fecha_iso}</news:publication_date>',
            f'      <news:title>{titulo}</news:title>',
            '    </news:news>',
            '  </url>',
        ]

    lines.append('</urlset>')

    out = os.path.join(REPO, 'sitemap-news.xml')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    print(f"sitemap-news.xml generado: {len(notas)} artículos recientes.")


if __name__ == '__main__':
    generar()
