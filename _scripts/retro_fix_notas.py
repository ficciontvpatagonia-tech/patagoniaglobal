#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Retro-aplica a las páginas YA generadas los arreglos de la auditoría de nov/2026.

Las notas nunca se regeneran (regla del proyecto), así que cada mejora de plantilla
hay que llevarla a mano a las existentes. Este script es idempotente: se puede
correr todas las veces que haga falta (p.ej. después de un merge) y solo toca
lo que todavía no está corregido. No modifica texto editorial ni URLs.

Uso:
    python3 _scripts/retro_fix_notas.py            # aplica
    python3 _scripts/retro_fix_notas.py --dry-run  # solo cuenta

Pasos:
  1. compartir   — comillas sin escapar en el botón "Copiar enlace" (JS roto).
  2. fuentes     — @import / <link> bloqueante de Google Fonts → carga no bloqueante.
  3. zh          — pila de fuentes CJK y bajada sin cursiva en páginas en chino.
  4. imágenes    — width/height reales + loading="lazy" fuera del primer pantallazo.
  5. iframes     — loading="lazy" + title.
  6. onesignal   — SDK y aviso de suscripción recién después de scroll (solo notas/).
"""
import glob, os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRY = "--dry-run" in sys.argv

try:
    from PIL import Image
except Exception:                      # sin Pillow: se saltea el paso de dimensiones
    Image = None

ONESIGNAL_APP_ID = "d351217a-5fe8-4af2-bb35-fffdafb5e30f"
ONESIGNAL_NOTAS = (
    '<script>/* gp-onesignal: el SDK se carga y el aviso aparece recien despues de scroll */\n'
    '(function(){var hecho=false;function ir(){if(hecho)return;'
    'if((window.scrollY||document.documentElement.scrollTop||0)<600)return;hecho=true;'
    "window.removeEventListener('scroll',ir);"
    'window.OneSignalDeferred=window.OneSignalDeferred||[];'
    'OneSignalDeferred.push(async function(OneSignal){'
    'await OneSignal.init({appId:"' + ONESIGNAL_APP_ID + '"});'
    'try{if(OneSignal.Notifications.isPushSupported()&&!OneSignal.Notifications.permission)'
    'OneSignal.Slidedown.promptPush();}catch(e){}});'
    "var s=document.createElement('script');"
    "s.src='https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js';s.defer=true;"
    "document.head.appendChild(s);}"
    "window.addEventListener('scroll',ir,{passive:true});})();</script>"
)

ZH_CSS = ('<style>/* gp-zh */html[lang^="zh"] body{font-family:\'Inter\',"PingFang SC","Noto Sans SC",'
          '"Microsoft YaHei",sans-serif;}html[lang^="zh"] .nota-bajada{font-style:normal;}</style>')

DIM_CSS = '<style>/* gp-dim */:where(img.gp-d){height:auto;}</style>'


def fuentes_link(url):
    """Hoja de fuentes sin bloquear el render (media=print → all al cargar)."""
    pre = ('<link rel="preconnect" href="https://fonts.googleapis.com"/>\n'
           '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>\n  ') if "googleapis" in url else ""
    return (pre + f'<link rel="stylesheet" href="{url}" media="print" onload="this.media=\'all\'"/>\n'
            f'  <noscript><link rel="stylesheet" href="{url}"/></noscript>')


# ── 1. compartir ───────────────────────────────────────────────────────────
_RE_COPIAR = re.compile(r"this\.textContent='((?:\\u00a1)?[^'\"\\]*)'\"")

def paso_compartir(s):
    return _RE_COPIAR.subn(
        lambda m: "this.textContent=\\x27" + m.group(1).replace("\\u00a1", "¡") + "\\x27\"", s)


# ── 2. fuentes ─────────────────────────────────────────────────────────────
_RE_IMPORT = re.compile(r"[ \t]*@import\s+url\(\s*['\"]?(https://fonts\.(?:googleapis\.com|loli\.net)/[^'\")]+)['\"]?\s*\)\s*;[ \t]*\n?")
_RE_LINK_FUENTE = re.compile(r"<link\b[^>]*href=[\"'](https://fonts\.(?:googleapis\.com|loli\.net)/css[^\"']+)[\"'][^>]*>")
_RE_PRELOAD_FUENTE = re.compile(r"[ \t]*<link\b[^>]*rel=[\"']preload[\"'][^>]*href=[\"']https://fonts\.(?:googleapis\.com|loli\.net)/css[^\"']+[\"'][^>]*>\s*\n?")

def paso_fuentes(s):
    n = 0
    # a) @import dentro de <style> → <link> no bloqueante antes de ese <style>
    while True:
        m = _RE_IMPORT.search(s)
        if not m:
            break
        url = m.group(1)
        ini_style = s.rfind("<style", 0, m.start())
        if ini_style < 0:
            break
        s = s[:m.start()] + s[m.end():]
        ya = url in s[:ini_style]            # la misma hoja ya enlazada antes: no duplicar
        if not ya:
            s = s[:ini_style] + fuentes_link(url) + "\n  " + s[ini_style:]
        n += 1
    # b) <link rel="stylesheet"> bloqueante → no bloqueante (y se quita el preload duplicado)
    def _link(m):
        nonlocal n
        tag = m.group(0)
        if "stylesheet" not in tag or "onload" in tag or "media=" in tag:
            return tag
        ini = s_ref[0].rfind("<noscript", 0, m.start())
        if ini >= 0 and s_ref[0].find("</noscript>", ini) > m.start():
            return tag                        # el de respaldo dentro de <noscript> queda como está
        n += 1
        url = m.group(1)
        return (f'<link rel="stylesheet" href="{url}" media="print" onload="this.media=\'all\'"/>'
                f'<noscript><link rel="stylesheet" href="{url}"/></noscript>')
    s_ref = [s]
    s2 = _RE_LINK_FUENTE.sub(_link, s)
    if s2 != s:
        s2 = _RE_PRELOAD_FUENTE.sub("", s2)
    return s2, n


# ── 3. zh ──────────────────────────────────────────────────────────────────
def paso_zh(s):
    if "gp-zh" in s or not re.search(r'<html[^>]*lang=["\']zh', s[:400]):
        return s, 0
    i = s.find("</head>")
    if i < 0:
        return s, 0
    return s[:i] + ZH_CSS + "\n" + s[i:], 1


# ── 4. imágenes ────────────────────────────────────────────────────────────
_dim_cache = {}

def _dim_local(src, pagina):
    """(w, h) del archivo local al que apunta src, o None."""
    if Image is None:
        return None
    u = src.split("?")[0].split("#")[0]
    m = re.match(r"https?://(?:www\.)?globalpatagonia\.org/(.*)", u)
    if m:
        rel = m.group(1)
    elif re.match(r"https?://|//|data:", u):
        return None
    elif u.startswith("/"):
        rel = u.lstrip("/")
    else:
        rel = os.path.normpath(os.path.join(os.path.dirname(pagina), u))
    from urllib.parse import unquote
    ruta = os.path.join(BASE, unquote(rel))
    if ruta not in _dim_cache:
        try:
            with Image.open(ruta) as im:
                _dim_cache[ruta] = im.size
        except Exception:
            _dim_cache[ruta] = None
    return _dim_cache[ruta]

_RE_IMG = re.compile(r"<img\b[^<>]*>")   # [^<>]: un <img sin cerrar no debe tragarse la etiqueta siguiente
_RE_SCRIPT = re.compile(r"<script\b.*?</script>", re.S | re.I)

def _attr(tag, nombre):
    m = re.search(r'\b' + nombre + r'\s*=\s*"([^"]*)"', tag) or re.search(r"\b" + nombre + r"\s*=\s*'([^']*)'", tag)
    return m.group(1) if m else None

def _add(tag, extra):
    return (tag[:-2].rstrip() + " " + extra + "/>") if tag.endswith("/>") else (tag[:-1].rstrip() + " " + extra + ">")

def paso_imagenes(s, pagina):
    # no tocar <img> que estén dentro de <script> (plantillas JS)
    vedado = [(m.start(), m.end()) for m in _RE_SCRIPT.finditer(s)]
    def en_script(pos):
        return any(a <= pos < b for a, b in vedado)
    n_dim = n_lazy = 0
    usa_clase = False
    out, ult, idx = [], 0, 0
    for m in _RE_IMG.finditer(s):
        if en_script(m.start()):
            continue
        tag = nuevo = m.group(0)
        src = _attr(tag, "src") or ""
        clases = (_attr(tag, "class") or "").split()
        if "${" in src or "'+" in src or not src:
            continue
        idx += 1
        w, h = _attr(tag, "width"), _attr(tag, "height")
        real = _dim_local(src, pagina)
        if real:
            if not w and not h:
                nuevo = _add(nuevo, f'width="{real[0]}" height="{real[1]}"')
                if "gp-d" not in clases:
                    if _attr(nuevo, "class") is not None:
                        nuevo = re.sub(r'\bclass\s*=\s*"([^"]*)"', lambda k: f'class="{(k.group(1) + " gp-d").strip()}"', nuevo, count=1)
                    else:
                        nuevo = _add(nuevo, 'class="gp-d"')
                usa_clase = True
                n_dim += 1
            elif "nota-imagen" in clases and w == "1200" and h == "630" and real != (1200, 630):
                # la plantilla escribía 1200x630 fijo: se pone la proporción real (el CSS ya da height:auto)
                nuevo = nuevo.replace('width="1200" height="630"', f'width="{real[0]}" height="{real[1]}"')
                n_dim += 1
        elif "gp-d" in clases:
            usa_clase = True
        primera_pantalla = (idx <= 3 and "rel-img" not in clases) or "logo-img" in clases \
            or "nota-imagen" in clases or "autor-avatar" in clases or _attr(tag, "fetchpriority") == "high"
        if not primera_pantalla and _attr(tag, "loading") is None:
            nuevo = _add(nuevo, 'loading="lazy" decoding="async"')
            n_lazy += 1
        if nuevo != tag:
            out.append(s[ult:m.start()]); out.append(nuevo); ult = m.end()
    if out:
        out.append(s[ult:]); s = "".join(out)
    if (usa_clase or "gp-d" in s) and "gp-dim" not in s:
        i = s.find("</head>")
        if i >= 0:
            s = s[:i] + DIM_CSS + "\n" + s[i:]
    return s, n_dim, n_lazy


# ── 5. iframes ─────────────────────────────────────────────────────────────
_RE_IFRAME = re.compile(r"<iframe\b[^<>]*>")

def paso_iframes(s):
    vedado = [(m.start(), m.end()) for m in _RE_SCRIPT.finditer(s)]
    n = 0
    def _f(m):
        nonlocal n
        if any(a <= m.start() < b for a, b in vedado):
            return m.group(0)
        tag = nuevo = m.group(0)
        src = _attr(tag, "src") or ""
        if _attr(tag, "loading") is None:
            nuevo = _add(nuevo, 'loading="lazy"')
        if _attr(tag, "title") is None:
            t = ("Video de YouTube" if "youtu" in src else "Mapa de viento (Windy)" if "windy" in src
                 else "Mapa" if "openstreetmap" in src or "google.com/maps" in src else "Contenido embebido")
            nuevo = _add(nuevo, f'title="{t}"')
        if nuevo != tag:
            n += 1
        return nuevo
    return _RE_IFRAME.sub(_f, s), n


# ── 6. onesignal (solo notas/) ─────────────────────────────────────────────
def paso_onesignal(s):
    if "OneSignal" in s or 'http-equiv="refresh"' in s[:3000]:
        return s, 0
    i = s.rfind("</body>")
    if i < 0:
        return s, 0
    return s[:i] + ONESIGNAL_NOTAS + "\n" + s[i:], 1


# ── Tanda 4: metadatos (datos estructurados y vista previa al compartir) ──
import html as _html, json as _json, unicodedata as _ud

FB_PAGE_ID = os.environ.get("FACEBOOK_PAGE_ID", "").strip()   # mismo origen que el generador
_RE_LD = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)
_RE_FB = re.compile(r'<meta\s+property="fb:pages"\s+content="[^"]*"\s*/?>')
_RE_OGIMG = re.compile(r'([ \t]*)<meta\s+property="og:image"\s+content="([^"]*)"\s*/?>')

def limpiar_etiqueta(txt):
    """Igual que _limpiar_etiqueta del generador: sin emojis, banderas ni adornos."""
    t = _ud.normalize("NFC", str(txt or ""))
    t = "".join(c for c in t if c != "·" and _ud.category(c) not in ("So", "Sk", "Cf", "Mn", "Me", "Cs", "Co"))
    return re.sub(r"\s+", " ", t).strip(" ,-")

def _kw(m):
    try:
        val = _json.loads('"' + m.group(2) + '"')
    except Exception:
        return m.group(0)
    out = []
    for parte in val.split(","):
        parte = limpiar_etiqueta(parte)
        if parte and parte.lower() not in [x.lower() for x in out]:
            out.append(parte)
    return m.group(1) + _json.dumps(", ".join(out), ensure_ascii=False)

def _ld(m):
    b = m.group(2)
    b = re.sub(r'("date(?:Published|Modified)":\s*")(\d{4}-\d{2}-\d{2})"', r'\1\2T06:00:00-03:00"', b)
    b = b.replace("https://globalpatagonia.org/favicon.svg", "https://globalpatagonia.org/icon-512.png")
    b = re.sub(r'("keywords":\s*)"((?:[^"\\]|\\.)*)"', _kw, b)
    return m.group(1) + b + m.group(3)

def paso_meta(s, pagina):
    orig = s
    s = _RE_LD.sub(_ld, s)
    s = re.sub(r'(<meta\s+property="article:(?:published|modified)_time"\s+content=")(\d{4}-\d{2}-\d{2})"',
               r'\1\2T06:00:00-03:00"', s)
    s = re.sub(r'(<meta\s+property="article:section"\s+content=")([^"]*)"',
               lambda m: m.group(1) + _html.escape(limpiar_etiqueta(_html.unescape(m.group(2))), quote=True) + '"', s)
    m = _RE_OGIMG.search(s)
    if m and "og:image:width" not in s:
        d = _dim_local(m.group(2), pagina)
        if d:
            s = (s[:m.end()] + f'\n{m.group(1)}<meta property="og:image:width" content="{d[0]}"/>'
                 f'\n{m.group(1)}<meta property="og:image:height" content="{d[1]}"/>' + s[m.end():])
    if FB_PAGE_ID:
        meta = f'<meta property="fb:pages" content="{FB_PAGE_ID}"/>'
        if _RE_FB.search(s):
            s = _RE_FB.sub(meta, s, count=1)
        else:
            m = _RE_OGIMG.search(s)
            if m:
                s = s[:m.start()] + f'{m.group(1)}{meta}\n' + s[m.start():]
    return s, int(s != orig)


# ── Tanda 6: selector de idioma solo texto y áreas táctiles ──
_RE_SWITCH = re.compile(r'(<(div|nav)\b[^>]*class="[^"]*lang-switcher[^"]*"[^>]*>)(.*?)(</\2>)', re.S)
_RE_BANDERA = re.compile(r'[\U0001F1E6-\U0001F1FF]{2}\s*')

def paso_idioma(s):
    n = [0]
    def _f(m):
        cuerpo = _RE_BANDERA.sub("", m.group(3))
        if cuerpo != m.group(3):
            n[0] += 1
        return m.group(1) + cuerpo + m.group(4)
    return _RE_SWITCH.sub(_f, s), n[0]

TAP_CSS = ('<style>/* gp-tap: area tactil de 44px sin cambiar el aspecto */'
           '.volver,a.nota-tag,.lang-switcher a,.btn-c,.nota-fuente a{position:relative}'
           '.volver::after,a.nota-tag::after,.nota-fuente a::after{content:"";position:absolute;inset:-12px -4px}'
           '.lang-switcher a::after,.btn-c::after{content:"";position:absolute;inset:-9px -4px}</style>')

def paso_tap(s):
    if "gp-tap" in s or "</head>" not in s:
        return s, 0
    return s.replace("</head>", TAP_CSS + "\n</head>", 1), 1


def main():
    tot = dict(paginas=0, compartir=0, fuentes=0, zh=0, dim=0, lazy=0, iframes=0, onesignal=0, meta=0, idioma=0, tap=0)
    archivos = (sorted(glob.glob(os.path.join(BASE, "notas", "*.html")))
                + sorted(glob.glob(os.path.join(BASE, "temas", "*.html")))
                + sorted(glob.glob(os.path.join(BASE, "autor-*.html"))))
    for ruta in archivos:
        rel = os.path.relpath(ruta, BASE)
        es_nota = rel.startswith("notas" + os.sep)
        with open(ruta, encoding="utf-8") as f:
            orig = s = f.read()
        s, a = paso_compartir(s);            tot["compartir"] += a
        s, a = paso_fuentes(s);              tot["fuentes"] += a
        s, a = paso_zh(s);                   tot["zh"] += a
        s, a, b = paso_imagenes(s, rel);     tot["dim"] += a; tot["lazy"] += b
        s, a = paso_iframes(s);              tot["iframes"] += a
        s, a = paso_idioma(s);               tot["idioma"] += a
        if es_nota:
            s, a = paso_tap(s);              tot["tap"] += a
        if es_nota and rel != os.path.join("notas", "index.html"):
            s, a = paso_onesignal(s);        tot["onesignal"] += a
            s, a = paso_meta(s, rel);        tot["meta"] += a
        if s != orig:
            tot["paginas"] += 1
            if not DRY:
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(s)
    print(("[dry-run] " if DRY else "") + " · ".join(f"{k}: {v}" for k, v in tot.items()))


if __name__ == "__main__":
    main()
