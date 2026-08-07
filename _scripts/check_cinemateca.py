#!/usr/bin/env python3
"""Auditoría mensual de la Cinemateca Patagónica — GLOBALpatagonia

Revisa videos.json: verifica que los videos (YouTube/embed) y thumbnails
sigan online, y busca películas/series filmadas en Patagonia que todavía
no estén en el catálogo. No modifica videos.json — todo se reporta en un
GitHub Issue para revisión manual (mismo patrón que check_seo.py)."""

import os
import json
import time
import urllib.request
import urllib.error
import anthropic

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEOS_PATH = os.path.join(REPO, 'videos.json')
GH_REPO = 'ficciontvpatagonia-tech/patagoniaglobal'
API_KEY = os.environ.get('ANTHROPIC_API_KEY')


def create_github_issue(token, title, body):
    url = f'https://api.github.com/repos/{GH_REPO}/issues'
    payload = json.dumps({'title': title, 'body': body, 'labels': ['cinemateca']}).encode()
    req = urllib.request.Request(url, data=payload, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github+json',
    })
    urllib.request.urlopen(req, timeout=10)


def http_ok(url, timeout=10):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.status < 400
    except urllib.error.HTTPError as e:
        # 403/999 etc. suelen ser bloqueo de bots, no video caído
        return e.code not in (404, 410)
    except Exception:
        return False


def check_youtube(video_id, timeout=10):
    url = f'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status == 200
    except Exception:
        return False


def check_thumbnail(thumb):
    if not thumb:
        return True
    if thumb.startswith('http'):
        return http_ok(thumb)
    return os.path.isfile(os.path.join(REPO, thumb))


def revisar_links(videos):
    rotos = []
    for v in videos:
        titulo = v.get('titulo', v.get('id', '?'))
        video_ok = True
        if v.get('youtube_id'):
            video_ok = check_youtube(v['youtube_id'])
        elif v.get('embed_url'):
            video_ok = http_ok(v['embed_url'])
        thumb_ok = check_thumbnail(v.get('thumbnail'))
        if not video_ok or not thumb_ok:
            rotos.append({
                'id': v.get('id'),
                'titulo': titulo,
                'video_roto': not video_ok,
                'thumb_roto': not thumb_ok,
            })
        time.sleep(0.3)
    return rotos


def buscar_candidatos(videos):
    if not API_KEY:
        return []
    titulos_existentes = sorted({v.get('titulo', '') for v in videos if v.get('titulo')})
    client = anthropic.Anthropic(api_key=API_KEY)
    prompt = (
        "Buscá películas o series (ficción o documental) filmadas totalmente o "
        "parcialmente en la Patagonia (Argentina o Chile) que NO estén en esta "
        "lista de títulos ya catalogados:\n\n"
        + "\n".join(f"- {t}" for t in titulos_existentes)
        + "\n\nUsá la búsqueda web para encontrar candidatos reales y verificables "
        "(Wikipedia, IMDb, FilmAffinity, prensa). Priorizá films conocidos con "
        "ficha verificable, no inventes títulos ni datos. Devolvé ÚNICAMENTE un "
        "array JSON (sin texto antes ni después), máximo 8 candidatos, cada uno:\n"
        '{"titulo": "...", "anio": 2020, "director": "...", "sinopsis": "1-2 frases", '
        '"lugar_filmacion": "...", "fuente": "URL que confirma el rodaje en Patagonia"}'
    )

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4000,
        tools=[{"type": "web_search_20260209", "name": "web_search"}],
        messages=[{"role": "user", "content": prompt}],
    )
    texto = "".join(b.text for b in response.content if b.type == "text")
    inicio, fin = texto.find("["), texto.rfind("]") + 1
    if inicio < 0 or fin <= inicio:
        return []
    try:
        return json.loads(texto[inicio:fin])
    except json.JSONDecodeError:
        return []


def main():
    with open(VIDEOS_PATH, encoding='utf-8') as f:
        videos = json.load(f)

    print(f"Revisando {len(videos)} videos...")
    rotos = revisar_links(videos)
    print(f"  {len(rotos)} con problemas")

    print("Buscando candidatos nuevos...")
    candidatos = buscar_candidatos(videos)
    print(f"  {len(candidatos)} candidatos encontrados")

    if not rotos and not candidatos:
        print("Nada para reportar.")
        return

    body_parts = ["_Auditoría automática mensual de la Cinemateca Patagónica. "
                  "No se modificó videos.json — esto es solo un reporte._\n"]

    if rotos:
        body_parts.append("## 🔗 Links rotos o con problemas\n")
        for r in rotos:
            problemas = []
            if r['video_roto']:
                problemas.append("video")
            if r['thumb_roto']:
                problemas.append("thumbnail")
            body_parts.append(f"- **{r['titulo']}** (`{r['id']}`) — {', '.join(problemas)} roto")
        body_parts.append("")

    if candidatos:
        body_parts.append("## 🎬 Candidatos nuevos para la Cinemateca\n")
        for c in candidatos:
            body_parts.append(
                f"### {c.get('titulo', '?')} ({c.get('anio', '?')})\n"
                f"- **Director:** {c.get('director', '?')}\n"
                f"- **Lugar de filmación:** {c.get('lugar_filmacion', '?')}\n"
                f"- **Sinopsis:** {c.get('sinopsis', '')}\n"
                f"- **Fuente:** {c.get('fuente', '')}\n"
            )

    body = "\n".join(body_parts)
    gh_token = os.environ.get('GITHUB_TOKEN')
    if gh_token:
        create_github_issue(gh_token, f"Auditoría Cinemateca — {time.strftime('%Y-%m-%d')}", body)
        print("Issue creado.")
    else:
        print(body)


if __name__ == '__main__':
    main()
