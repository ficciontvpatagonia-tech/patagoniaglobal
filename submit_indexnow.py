#!/usr/bin/env python3
"""
Envía las URLs del día a IndexNow (Bing, Yandex, etc.)
Ejecutar después de cada deploy.
"""

import json
import os
import urllib.request
import urllib.error

REPO = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://globalpatagonia.org"
INDEXNOW_ENDPOINT = "https://www.bing.com/indexnow"
INDEXNOW_KEY = os.environ.get("INDEXNOW_KEY", "")


def recolectar_urls():
    urls = []
    vistas = set()

    path = os.path.join(REPO, 'noticias.json')
    if not os.path.exists(path):
        return urls

    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    items = []
    if data.get('tapa'):
        items.append(data['tapa'])
    items += data.get('secundarias', [])
    items += data.get('noticias', [])

    for nota in items:
        nid = nota.get('id', '')
        if not nid or nid in vistas:
            continue
        vistas.add(nid)
        nota_html = os.path.join(REPO, 'notas', f'{nid}.html')
        if os.path.exists(nota_html):
            urls.append(f"{BASE_URL}/notas/{nid}.html")
        else:
            urls.append(f"{BASE_URL}/nota.html?id={nid}")

    # Siempre incluir la home
    urls.append(f"{BASE_URL}/")
    return urls


def submit(urls):
    if not INDEXNOW_KEY:
        print("INDEXNOW_KEY no configurado — omitiendo envío a IndexNow.")
        return

    payload = json.dumps({
        "host": "globalpatagonia.org",
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }).encode('utf-8')

    req = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"IndexNow OK ({resp.status}) — {len(urls)} URLs enviadas a Bing/Yandex")
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        print(f"IndexNow HTTP {e.code}: {body}")
    except Exception as e:
        print(f"IndexNow error: {e}")


if __name__ == '__main__':
    urls = recolectar_urls()
    print(f"URLs a enviar ({len(urls)}):")
    for u in urls:
        print(f"  {u}")
    submit(urls)
