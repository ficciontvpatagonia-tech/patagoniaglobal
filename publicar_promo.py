#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
publicar_promo.py — Publica posteos PROMOCIONALES (no-noticia) en redes.

A diferencia del flujo diario (que postea la tapa/informes y enlaza a notas/),
esto publica placas de difusión que enlazan a páginas del sitio
(videos.html, clima.html, etc.).

Reutiliza el mismo patrón de API que actualizar_noticias.py (Telegram sendPhoto,
Facebook /photos, Instagram container→publish). Las credenciales se leen del
entorno (GitHub Secrets en el Action, o .env local):
  TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID,
  FACEBOOK_PAGE_ID, FACEBOOK_PAGE_TOKEN, FACEBOOK_APP_ID, FACEBOOK_APP_SECRET,
  INSTAGRAM_BUSINESS_ACCOUNT_ID

Uso:
  python3 publicar_promo.py --imagenes        # solo genera/actualiza las placas
  python3 publicar_promo.py cinemateca        # publica solo Cinemateca
  python3 publicar_promo.py clima             # publica solo Clima
  python3 publicar_promo.py ambas             # publica las dos (default)
  (flags opcionales: --no-telegram --no-facebook --no-instagram)

Instagram requiere que la imagen sea una URL pública de globalpatagonia.org,
así que las placas deben estar commiteadas y servidas por Pages ANTES de correr
la publicación a IG.
"""
import os, sys, json, time, re, tempfile
import urllib.request, urllib.parse, urllib.error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Cargar .env local si existe (no pisa variables ya presentes en el entorno)
_env_path = os.path.join(BASE_DIR, ".env")
if os.path.exists(_env_path):
    with open(_env_path) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _v = _line.split("=", 1)
                os.environ.setdefault(_k.strip(), _v.strip())

SITE = "https://globalpatagonia.org"
FIRMA = "GLOBALpatagonia · Sur Global, principio de todo."

# ══════════════════════════════════════════════════════════
#  DEFINICIÓN DE LAS PROMOS
# ══════════════════════════════════════════════════════════
PROMOS = {
    "cinemateca": {
        "emoji": "🎬",
        "titulo": "CINEMATECA PATAGÓNICA",
        "link": f"{SITE}/videos.html",
        "imagen": "fotos/promo-cinemateca.jpg",        # ruta en el repo
        "cuerpo": (
            "Más de 100 títulos del cine del sur, gratis y en un solo lugar:\n\n"
            "🎥 Películas: La Patagonia Rebelde, Wakolda, Un Lugar en el Mundo, "
            "Iluminados por el Fuego y más.\n"
            "📺 Series completas: Érase una vez en la Patagonia, Rescatistas, "
            "Atlántico Sur, Around Patagonia.\n"
            "🐋 Documentales de naturaleza, mar y pueblos originarios.\n\n"
            "Ficción, historia y aventura del fin del mundo, organizado como tu "
            "plataforma favorita."
        ),
        "cta": "▶️ Entrá a la Cinemateca",
        "hashtags": "#Patagonia #CineArgentino #Cinemateca #PatagoniaRebelde "
                    "#Wakolda #CineChileno #SurGlobal #GLOBALpatagonia",
    },
    "clima": {
        "emoji": "🌦️",
        "titulo": "EL CLIMA DE LA PATAGONIA",
        "link": f"{SITE}/clima.html",
        "imagen": "fotos/promo-clima.jpg",
        "cuerpo": (
            "El pronóstico de todo el sur en un solo lugar:\n\n"
            "📍 Argentina: Bariloche, Ushuaia, El Calafate, El Chaltén, Neuquén, "
            "Puerto Madryn, Comodoro y más.\n"
            "🇨🇱 Chile: Puerto Montt, Punta Arenas y el sur chileno.\n"
            "🐧 Y hasta la Antártida argentina y chilena.\n\n"
            "Temperatura, viento, pronóstico a 7 días y el clima mes a mes para "
            "planear tu viaje. Con la temporada de esquí en marcha, tenelo a mano."
        ),
        "cta": "❄️ Mirá el clima",
        "hashtags": "#Patagonia #ClimaPatagonia #Bariloche #Ushuaia #ElCalafate "
                    "#Pronostico #ViajarPatagonia #SurGlobal #GLOBALpatagonia",
    },
}

# Fotos base para generar las placas (si la promo no trae una placa ya armada)
FUENTES_PLACA = {
    "clima": "fotos/foto-20260514-catedral-lanza-pases-2026-desde-160000-la-nieve-ya-dep.webp",
}


# ══════════════════════════════════════════════════════════
#  GENERACIÓN DE PLACAS (1080×1350, diseño GLOBALpatagonia)
# ══════════════════════════════════════════════════════════
def _fuente(paths, size):
    from PIL import ImageFont
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default(size=size)

_SANS_BOLD = [
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]
_SANS_REG = [
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/Arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
]
_BLACK = [
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Black.ttf",
    "/Library/Fonts/Arial Black.ttf",
]


def generar_placa(base_path, titulo, tag, cta, out_path):
    """Placa portrait 4:5 (1080×1350): header + foto + banda oscura con tag, título y CTA."""
    from PIL import Image, ImageDraw
    import numpy as np

    ANCHO, ALTO = 1080, 1350
    H_HEADER, H_FOTO, Y_DARK = 65, 780, 845
    C_DARK   = (28, 45, 61)
    C_TEAL   = (122, 173, 204)
    C_BLANCO = (255, 255, 255)
    C_CREMA  = (240, 237, 232)
    C_SHADOW = (10, 20, 30)

    canvas = Image.new("RGB", (ANCHO, ALTO), C_DARK)
    draw = ImageDraw.Draw(canvas)

    img = Image.open(base_path).convert("RGB")
    w, h = img.size
    target = ANCHO / H_FOTO
    if w / h > target:
        nw = int(h * target); left = (w - nw) // 2
        img = img.crop((left, 0, left + nw, h))
    else:
        nh = int(w / target); top = (h - nh) // 3
        img = img.crop((0, top, w, top + nh))
    img = img.resize((ANCHO, H_FOTO), Image.LANCZOS)
    canvas.paste(img, (0, H_HEADER))

    arr = np.array(canvas, dtype=np.float32)
    g0 = H_HEADER + H_FOTO - 120
    azul = np.array(C_DARK, dtype=np.float32)
    for y in range(g0, H_HEADER + H_FOTO):
        a = ((y - g0) / 120) * 0.75
        arr[y] = arr[y] * (1 - a) + azul * a
    canvas = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
    draw = ImageDraw.Draw(canvas)

    f_logo_b = _fuente(_SANS_BOLD, 38)
    f_logo_r = _fuente(_SANS_REG, 38)
    f_titulo = _fuente(_BLACK, 86)
    f_tag    = _fuente(_SANS_BOLD, 34)
    f_cta    = _fuente(_SANS_BOLD, 40)

    # Header
    bg = draw.textbbox((0, 0), "GLOBAL", font=f_logo_b)
    bp = draw.textbbox((0, 0), "patagonia", font=f_logo_r)
    tw = (bg[2] - bg[0]) + (bp[2] - bp[0])
    x0 = (ANCHO - tw) // 2
    y0 = (H_HEADER - (bg[3] - bg[1])) // 2
    draw.text((x0, y0), "GLOBAL", font=f_logo_b, fill=C_TEAL)
    draw.text((x0 + bg[2] - bg[0], y0), "patagonia", font=f_logo_r, fill=C_BLANCO)

    PAD = 60
    # Tag
    if tag:
        t = f"- {tag.strip()} -"
        bt = draw.textbbox((0, 0), t, font=f_tag)
        tgw = (bt[2] - bt[0]) + 44
        tgh = (bt[3] - bt[1]) + 18
        ty = Y_DARK - tgh - 18
        draw.rectangle([(PAD, ty), (PAD + tgw, ty + tgh)], fill=C_TEAL)
        draw.text((PAD + 22, ty + 9), t, font=f_tag, fill=C_DARK)

    # Título (hasta 3 líneas)
    MAXPX = ANCHO - PAD * 2
    words = titulo.replace("\n", " ").split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if draw.textbbox((0, 0), test, font=f_titulo)[2] <= MAXPX:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    lines = lines[:3]
    y = Y_DARK + 40
    for ln in lines:
        draw.text((PAD + 2, y + 2), ln, font=f_titulo, fill=C_SHADOW)
        draw.text((PAD, y), ln, font=f_titulo, fill=C_CREMA)
        y += 104

    # CTA (barra teal abajo)
    if cta:
        bc = draw.textbbox((0, 0), cta, font=f_cta)
        cw = (bc[2] - bc[0]) + 56
        ch = (bc[3] - bc[1]) + 34
        cx = PAD
        cy = ALTO - ch - 55
        draw.rounded_rectangle([(cx, cy), (cx + cw, cy + ch)], radius=14, fill=C_TEAL)
        draw.text((cx + 28, cy + 15), cta, font=f_cta, fill=C_DARK)

    canvas.save(out_path, "JPEG", quality=92)
    print(f"  placa → {os.path.relpath(out_path, BASE_DIR)}")
    return out_path


def asegurar_placas():
    """Genera las placas que faltan. Cinemateca usa el banner propio ya existente."""
    from PIL import Image
    # Cinemateca: convertir el banner propio ad-cinemateca.webp (1200×800) a jpg
    out_cine = os.path.join(BASE_DIR, "fotos", "promo-cinemateca.jpg")
    src_cine = os.path.join(BASE_DIR, "fotos", "ad-cinemateca.webp")
    if os.path.exists(src_cine):
        Image.open(src_cine).convert("RGB").save(out_cine, "JPEG", quality=92)
        print(f"  placa → fotos/promo-cinemateca.jpg (desde ad-cinemateca.webp)")
    # Clima: generar placa de marca
    out_clima = os.path.join(BASE_DIR, "fotos", "promo-clima.jpg")
    src_clima = os.path.join(BASE_DIR, FUENTES_PLACA["clima"])
    if os.path.exists(src_clima):
        generar_placa(src_clima, "El clima de toda la Patagonia",
                      "Pronóstico del Sur", "Mirá el clima  ·  globalpatagonia.org",
                      out_clima)


# ══════════════════════════════════════════════════════════
#  CAPTIONS
# ══════════════════════════════════════════════════════════
def cap_telegram(p):
    return (f"{p['emoji']} <b>{p['titulo']}</b>\n\n"
            f"{p['cuerpo']}\n\n"
            f'<a href="{p["link"]}">{p["cta"]} →</a>\n\n'
            f"<i>{FIRMA}</i>")


def cap_facebook(p):
    return (f"{p['emoji']} {p['titulo']}\n\n"
            f"{p['cuerpo']}\n\n"
            f"🔗 {p['link']}\n\n"
            f"{FIRMA}")


def cap_instagram(p):
    base = (f"{p['emoji']} {p['titulo']}\n\n{p['cuerpo']}\n\n"
            f"{p['cta']} — link en la bio\n\n")
    return (base + p["hashtags"])[:2200]


# ══════════════════════════════════════════════════════════
#  PUBLICACIÓN
# ══════════════════════════════════════════════════════════
def _telegram_request(token, method, fields, file_path=None):
    url = f"https://api.telegram.org/bot{token}/{method}"
    if file_path:
        boundary = "----GPpromo"
        body = b""
        for k, v in fields.items():
            body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n").encode()
        with open(file_path, "rb") as fh:
            body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"photo\"; "
                     f"filename=\"placa.jpg\"\r\nContent-Type: image/jpeg\r\n\r\n").encode()
            body += fh.read() + f"\r\n--{boundary}--\r\n".encode()
        req = urllib.request.Request(url, data=body,
                                     headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    else:
        req = urllib.request.Request(url, data=urllib.parse.urlencode(fields).encode())
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode())


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
                                    {"chat_id": channel, "caption": cap_telegram(p), "parse_mode": "HTML"},
                                    file_path=img)
        else:
            res = _telegram_request(token, "sendMessage",
                                    {"chat_id": channel, "text": cap_telegram(p), "parse_mode": "HTML"})
        print("  Telegram OK ✓" if res.get("ok") else f"  Telegram error: {res.get('description')}")
    except Exception as e:
        print(f"  Telegram falló: {e}")


def _renovar_token_facebook(token):
    app_id = os.environ.get("FACEBOOK_APP_ID", "")
    app_secret = os.environ.get("FACEBOOK_APP_SECRET", "")
    page_id = os.environ.get("FACEBOOK_PAGE_ID", "")
    if not app_id or not app_secret:
        return token, page_id
    try:
        u = ("https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token"
             f"&client_id={app_id}&client_secret={app_secret}&fb_exchange_token={token}")
        with urllib.request.urlopen(u, timeout=30) as r:
            long_token = json.loads(r.read().decode()).get("access_token", token)
        with urllib.request.urlopen(
                f"https://graph.facebook.com/v21.0/me/accounts?access_token={long_token}", timeout=30) as r:
            data = json.loads(r.read().decode()).get("data", [])
        for pg in data:
            if not page_id or pg.get("id") == page_id:
                print("  Facebook: token renovado ✓")
                return pg.get("access_token", long_token), pg.get("id", page_id)
    except Exception as e:
        print(f"  Facebook: no se pudo renovar token ({e}), uso el actual")
    return token, page_id


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
            boundary = "----GPpromo"
            with open(img, "rb") as fh:
                body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"caption\"\r\n\r\n{mensaje}\r\n"
                        f"--{boundary}\r\nContent-Disposition: form-data; name=\"access_token\"\r\n\r\n{page_token}\r\n"
                        f"--{boundary}\r\nContent-Disposition: form-data; name=\"source\"; filename=\"placa.jpg\"\r\n"
                        f"Content-Type: image/jpeg\r\n\r\n").encode() + fh.read() + f"\r\n--{boundary}--\r\n".encode()
            req = urllib.request.Request(f"{api}/photos", data=body,
                                         headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
                                         method="POST")
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


# ══════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════
def main():
    args = [a for a in sys.argv[1:]]
    solo_img = "--imagenes" in args
    do_tg = "--no-telegram" not in args
    do_fb = "--no-facebook" not in args
    do_ig = "--no-instagram" not in args

    cuales = [a for a in args if a in PROMOS]
    if "ambas" in args or not cuales:
        cuales = ["cinemateca", "clima"]

    asegurar_placas()
    if solo_img:
        print("Solo imágenes — listo.")
        return

    for clave in cuales:
        p = PROMOS[clave]
        print(f"\n=== PROMO: {clave} → {p['link']} ===")
        if do_tg:
            pub_telegram(p)
        if do_fb:
            pub_facebook(p)
        if do_ig:
            pub_instagram(p)


if __name__ == "__main__":
    main()
