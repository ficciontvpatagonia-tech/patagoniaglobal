#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
publicar_informe_idioma.py — Publica un INFORME (propios.json) en redes en un
idioma traducido (en/pt/zh), enlazando a la página estática traducida
(notas/{id}-{lang}.html).

A diferencia del flujo diario (que postea el informe SOLO en español enlazando a
notas/{id}.html), esto distribuye activamente la versión traducida hacia el
público de ese idioma: caption en el idioma, hashtags del idioma y link directo a
la página -en/-pt/-zh.

Reutiliza la cañería probada de publicar_promo.py (generación de placa, renovación
de token de Facebook, transporte multipart de Telegram). Credenciales por entorno
(GitHub Secrets en el Action):
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID,
  FACEBOOK_PAGE_ID, FACEBOOK_PAGE_TOKEN, FACEBOOK_APP_ID, FACEBOOK_APP_SECRET,
  INSTAGRAM_BUSINESS_ACCOUNT_ID

Uso:
  python3 publicar_informe_idioma.py --id 20260629-propio-datacenter-ia-patagonia --lang en
  python3 publicar_informe_idioma.py --id <id> --lang en --imagen   # solo genera la placa
  (flags: --no-telegram --no-facebook --no-instagram)

Instagram publica por URL pública → la placa fotos/{id}_{lang}_promo.jpg debe
estar commiteada y servida por Pages ANTES de disparar IG.
"""
import os, sys, json, re, time, argparse
import urllib.request, urllib.parse, urllib.error

from publicar_promo import (
    BASE_DIR, SITE, generar_placa,
    _telegram_request, _renovar_token_facebook,
)

# ── Configuración por idioma ──────────────────────────────────────────────
LANG = {
    "en": {
        "tag_placa": "Technology",
        "cta": "Read the full report",
        "cta_placa": "Read the report  ·  globalpatagonia.org",
        "firma": "GLOBALpatagonia · Global South, the beginning of everything.",
        "bio": "link in bio",
        "read_more": "Read the full report",
        "hashtags": "#Patagonia #Argentina #SouthAtlantic #News #GLOBALpatagonia",
    },
    "pt": {
        "tag_placa": "Tecnologia",
        "cta": "Leia a reportagem completa",
        "cta_placa": "Leia a reportagem  ·  globalpatagonia.org",
        "firma": "GLOBALpatagonia · Sul Global, princípio de tudo.",
        "bio": "link na bio",
        "read_more": "Leia a reportagem completa",
        "hashtags": "#Patagônia #Argentina #AtlânticoSul #Notícias #GLOBALpatagonia",
    },
    "zh": {
        "tag_placa": "Technology",  # las fuentes del runner no renderizan CJK
        "cta": "阅读完整报道",
        "cta_placa": "globalpatagonia.org",
        "firma": "GLOBALpatagonia · 南方全球，万物之始。",
        "bio": "链接在简介中",
        "read_more": "阅读完整报道",
        "hashtags": "#巴塔哥尼亚 #阿根廷 #南大西洋 #新闻 #GLOBALpatagonia",
    },
}


def _strip_html(s):
    s = re.sub(r"(?is)<(script|style).*?</\1>", " ", s)
    s = re.sub(r"(?i)</p>|<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&nbsp;", " ", s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def _resumen(cuerpo, limite):
    """Primeros párrafos del cuerpo, cortados en límite de caracteres por párrafo."""
    txt = _strip_html(cuerpo)
    out, total = [], 0
    for par in [p.strip() for p in txt.split("\n") if p.strip()]:
        if total + len(par) > limite and out:
            break
        out.append(par)
        total += len(par)
    return "\n\n".join(out)


def construir(informe, lang):
    cfg = LANG[lang]
    titulo = informe.get(f"titulo_{lang}") or informe["titulo"]
    bajada = informe.get(f"bajada_{lang}") or informe.get("bajada", "")
    cuerpo = informe.get(f"cuerpo_{lang}") or informe.get("cuerpo", "")
    link = f"{SITE}/notas/{informe['id']}-{lang}.html"
    cuerpo_txt = _resumen(cuerpo, 700)
    # La placa solo entra 3 líneas: si el título es largo y tiene ":", usar el
    # gancho antes de los dos puntos; el título completo va en el caption.
    titulo_placa = titulo
    if len(titulo) > 38 and ":" in titulo:
        titulo_placa = titulo.split(":", 1)[0].strip()
    return {
        "id": informe["id"], "lang": lang, "cfg": cfg,
        "titulo": titulo, "titulo_placa": titulo_placa,
        "bajada": bajada, "cuerpo": cuerpo_txt, "link": link,
        "imagen": f"fotos/{informe['id']}_{lang}_promo.jpg",
        "base_foto": informe.get("imagen", ""),
        "hashtags": informe.get(f"hashtags_{lang}") or cfg.get("hashtags", ""),
    }


# ── Placa ─────────────────────────────────────────────────────────────────
def asegurar_placa(p):
    out = os.path.join(BASE_DIR, p["imagen"])
    base = os.path.join(BASE_DIR, p["base_foto"])
    if not os.path.exists(base):
        print(f"  ⚠️ falta la foto base {p['base_foto']} — no se genera placa")
        return None
    generar_placa(base, p["titulo_placa"], p["cfg"]["tag_placa"], p["cfg"]["cta_placa"], out)
    return out


# ── Captions ──────────────────────────────────────────────────────────────
def cap_telegram(p):
    link, cta, firma = p["link"], p["cfg"]["cta"], p["cfg"]["firma"]
    titulo, bajada = p["titulo"], p["bajada"]
    return (f"📡 <b>{titulo}</b>\n\n{bajada}\n\n"
            f'<a href="{link}">{cta} →</a>\n\n<i>{firma}</i>')


def cap_facebook(p):
    cuerpo = f"{p['bajada']}\n\n{p['cuerpo']}" if p["cuerpo"] else p["bajada"]
    return f"📡 {p['titulo']}\n\n{cuerpo}\n\n🔗 {p['link']}\n\n{p['cfg']['firma']}"


def cap_instagram(p):
    base = f"📡 {p['titulo']}\n\n{p['bajada']}\n\n{p['cfg']['read_more']} — {p['cfg']['bio']}\n\n"
    return (base + p["hashtags"]).strip()[:2200]


# ── Publicación (transporte reutilizado de publicar_promo) ─────────────────
def pub_telegram(p):
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    channel = os.environ.get("TELEGRAM_CHANNEL_ID", "")
    if not token or not channel:
        print("  Telegram: sin credenciales, se omite."); return
    img = os.path.join(BASE_DIR, p["imagen"])
    img = img if os.path.exists(img) else None
    try:
        if img:
            res = _telegram_request(token, "sendPhoto",
                {"chat_id": channel, "caption": cap_telegram(p), "parse_mode": "HTML"}, file_path=img)
        else:
            res = _telegram_request(token, "sendMessage",
                {"chat_id": channel, "text": cap_telegram(p), "parse_mode": "HTML"})
        print("  Telegram OK ✓" if res.get("ok") else f"  Telegram error: {res.get('description')}")
    except Exception as e:
        print(f"  Telegram falló: {e}")


def pub_facebook(p):
    page_token = os.environ.get("FACEBOOK_PAGE_TOKEN", "")
    if not page_token:
        print("  Facebook: sin credenciales, se omite."); return
    page_token, page_id = _renovar_token_facebook(page_token)
    if not page_id:
        print("  Facebook: sin página, se omite."); return
    img = os.path.join(BASE_DIR, p["imagen"])
    img = img if os.path.exists(img) else None
    mensaje = cap_facebook(p)
    try:
        api = f"https://graph.facebook.com/v21.0/{page_id}"
        if img:
            boundary = "----GPinforme"
            with open(img, "rb") as fh:
                body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"caption\"\r\n\r\n{mensaje}\r\n"
                        f"--{boundary}\r\nContent-Disposition: form-data; name=\"access_token\"\r\n\r\n{page_token}\r\n"
                        f"--{boundary}\r\nContent-Disposition: form-data; name=\"source\"; filename=\"placa.jpg\"\r\n"
                        f"Content-Type: image/jpeg\r\n\r\n").encode() + fh.read() + f"\r\n--{boundary}--\r\n".encode()
            req = urllib.request.Request(f"{api}/photos", data=body,
                headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}, method="POST")
        else:
            data = urllib.parse.urlencode({"message": mensaje, "link": p["link"],
                                           "access_token": page_token}).encode()
            req = urllib.request.Request(f"{api}/feed", data=data, method="POST")
        with urllib.request.urlopen(req, timeout=40) as r:
            res = json.loads(r.read().decode())
        print("  Facebook OK ✓" if res.get("id") else f"  Facebook error: {res}")
    except urllib.error.HTTPError as e:
        print(f"  Facebook falló {e.code}: {e.read().decode('utf-8', 'replace')}")
    except Exception as e:
        print(f"  Facebook falló: {e}")


def pub_instagram(p):
    ig = os.environ.get("INSTAGRAM_BUSINESS_ACCOUNT_ID", "")
    token = os.environ.get("FACEBOOK_PAGE_TOKEN", "")
    if not ig or not token:
        print("  Instagram: sin credenciales, se omite."); return
    token, _ = _renovar_token_facebook(token)
    image_url = f"{SITE}/{p['imagen']}"
    caption = cap_instagram(p)
    try:
        api = f"https://graph.facebook.com/v21.0/{ig}"
        data = urllib.parse.urlencode({"image_url": image_url, "caption": caption,
                                       "access_token": token}).encode()
        req = urllib.request.Request(f"{api}/media", data=data, method="POST")
        with urllib.request.urlopen(req, timeout=40) as r:
            res = json.loads(r.read().decode())
        cid = res.get("id")
        if not cid:
            print(f"  Instagram container error: {res}"); return
        for _ in range(12):
            time.sleep(5)
            try:
                purl = f"https://graph.facebook.com/v21.0/{cid}?fields=status_code&access_token={token}"
                with urllib.request.urlopen(purl, timeout=20) as rp:
                    st = json.loads(rp.read().decode()).get("status_code", "")
                if st == "FINISHED":
                    break
                if st == "ERROR":
                    print("  Instagram: error de procesamiento"); return
            except Exception:
                pass
        else:
            print("  Instagram: timeout de container"); return
        data = urllib.parse.urlencode({"creation_id": cid, "access_token": token}).encode()
        req = urllib.request.Request(f"{api}/media_publish", data=data, method="POST")
        with urllib.request.urlopen(req, timeout=40) as r:
            res = json.loads(r.read().decode())
        print("  Instagram OK ✓" if res.get("id") else f"  Instagram publish error: {res}")
    except urllib.error.HTTPError as e:
        print(f"  Instagram falló {e.code}: {e.read().decode('utf-8', 'replace')}")
    except Exception as e:
        print(f"  Instagram falló: {e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True)
    ap.add_argument("--lang", required=True, choices=["en", "pt", "zh"])
    ap.add_argument("--imagen", action="store_true", help="solo generar la placa")
    ap.add_argument("--no-telegram", action="store_true")
    ap.add_argument("--no-facebook", action="store_true")
    ap.add_argument("--no-instagram", action="store_true")
    a = ap.parse_args()

    arr = json.load(open(os.path.join(BASE_DIR, "propios.json")))
    match = [x for x in arr if x.get("id") == a.id]
    if not match:
        print(f"✗ informe {a.id} no está en propios.json"); sys.exit(1)
    if not match[0].get(f"titulo_{a.lang}"):
        print(f"✗ el informe no tiene traducción {a.lang} (falta titulo_{a.lang})"); sys.exit(1)

    p = construir(match[0], a.lang)
    print(f"=== INFORME {a.id} [{a.lang}] → {p['link']} ===")
    asegurar_placa(p)
    if a.imagen:
        print("Solo imagen — listo."); return
    if not a.no_telegram:  pub_telegram(p)
    if not a.no_facebook:  pub_facebook(p)
    if not a.no_instagram: pub_instagram(p)


if __name__ == "__main__":
    main()
