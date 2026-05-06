#!/usr/bin/env python3
"""Auditoría SEO semanal — GLOBALpatagonia"""

import os
import re
import xml.etree.ElementTree as ET
import json
import urllib.request
from datetime import datetime

REPO = os.path.dirname(os.path.abspath(__file__))
SITEMAP_PATH = os.path.join(REPO, 'sitemap.xml')
NOTAS_DIR = os.path.join(REPO, 'notas')
ROBOTS_PATH = os.path.join(REPO, 'robots.txt')
BASE_URL = 'https://globalpatagonia.org'

ROBOTS_REQUIRED = ['Disallow: /nota.html', 'Disallow: /buscar.html', 'Sitemap:']


def send_telegram(token, chat_id, msg):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = json.dumps({
        'chat_id': chat_id,
        'text': msg,
        'parse_mode': 'HTML',
        'disable_web_page_preview': True
    }).encode()
    req = urllib.request.Request(url, data=payload,
                                 headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(req, timeout=10)


def sitemap_notas():
    tree = ET.parse(SITEMAP_PATH)
    root = tree.getroot()
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    result = set()
    for url in root.findall('sm:url', ns):
        loc = url.find('sm:loc', ns).text
        if '/notas/' in loc:
            result.add(loc.split('/notas/')[-1])
    return result


def read_head(path, n=2500):
    try:
        with open(path, encoding='utf-8') as f:
            return f.read(n)
    except Exception:
        return ''


def is_redirect_stub(path):
    h = read_head(path)
    return 'http-equiv="refresh"' in h or (
        'window.location.replace' in h and 'nota.html' in h
    )


def get_canonical(path):
    h = read_head(path)
    m = re.search(r'<link\s[^>]*rel=["\']canonical["\']\s[^>]*href=["\'](.*?)["\']', h)
    if not m:
        m = re.search(r'<link\s[^>]*href=["\'](.*?)["\']\s[^>]*rel=["\']canonical["\']', h)
    return m.group(1).rstrip('/') if m else None


def audit():
    ok = []
    issues = []

    # ── 1. Sitemap vs disco ──────────────────────────────────────────────
    all_files = {f for f in os.listdir(NOTAS_DIR) if f.endswith('.html')}
    sm_files = sitemap_notas()

    missing_from_sitemap = []
    redirect_without_noindex = []

    for f in sorted(all_files):
        if f in sm_files:
            continue
        path = os.path.join(NOTAS_DIR, f)
        if is_redirect_stub(path):
            if 'noindex' not in read_head(path):
                redirect_without_noindex.append(f)
        else:
            missing_from_sitemap.append(f)

    missing_from_disk = sorted(f for f in sm_files if f not in all_files)

    if missing_from_sitemap:
        issues.append(f'📋 En disco pero NO en sitemap ({len(missing_from_sitemap)}):')
        for f in missing_from_sitemap[:12]:
            issues.append(f'  · {f}')
        if len(missing_from_sitemap) > 12:
            issues.append(f'  · … y {len(missing_from_sitemap) - 12} más')
    else:
        ok.append(f'✅ Sitemap completo ({len(sm_files)} notas en sitemap, '
                  f'{len(all_files)} archivos en disco)')

    if missing_from_disk:
        issues.append(f'❌ En sitemap pero NO en disco ({len(missing_from_disk)}):')
        for f in missing_from_disk[:8]:
            issues.append(f'  · {f}')
    else:
        ok.append('✅ Sin URLs rotas en sitemap')

    if redirect_without_noindex:
        for f in redirect_without_noindex:
            issues.append(f'⚠️ Redirect stub sin noindex: {f}')
    else:
        ok.append('✅ Todos los redirect stubs tienen noindex')

    # ── 2. Canonical de cada nota estática ──────────────────────────────
    canonical_bad = []
    canonical_missing = []
    checked = 0

    for f in sorted(all_files):
        path = os.path.join(NOTAS_DIR, f)
        if is_redirect_stub(path):
            continue
        canonical = get_canonical(path)
        expected = f'{BASE_URL}/notas/{f}'
        if canonical is None:
            canonical_missing.append(f)
        elif canonical != expected:
            canonical_bad.append(f'{f} → {canonical}')
        checked += 1

    if canonical_missing:
        issues.append(f'🔗 Sin canonical ({len(canonical_missing)}):')
        for f in canonical_missing[:5]:
            issues.append(f'  · {f}')
        if len(canonical_missing) > 5:
            issues.append(f'  · … y {len(canonical_missing) - 5} más')
    if canonical_bad:
        issues.append(f'🔗 Canonical incorrecto ({len(canonical_bad)}):')
        for f in canonical_bad[:5]:
            issues.append(f'  · {f}')
        if len(canonical_bad) > 5:
            issues.append(f'  · … y {len(canonical_bad) - 5} más')
    if not canonical_missing and not canonical_bad:
        ok.append(f'✅ Canonicals correctos ({checked} páginas verificadas)')

    # ── 3. nota.html template tiene noindex ─────────────────────────────
    nota_path = os.path.join(REPO, 'nota.html')
    nota_head = read_head(nota_path)
    if 'noindex' not in nota_head:
        issues.append('⚠️ nota.html: falta meta noindex')
    else:
        ok.append('✅ nota.html tiene noindex')

    # ── 4. robots.txt ────────────────────────────────────────────────────
    try:
        with open(ROBOTS_PATH, encoding='utf-8') as f:
            robots = f.read()
        robots_missing = [r for r in ROBOTS_REQUIRED if r not in robots]
        if robots_missing:
            for r in robots_missing:
                issues.append(f'🤖 robots.txt: falta "{r}"')
        else:
            ok.append('✅ robots.txt con reglas correctas')
    except FileNotFoundError:
        issues.append('❌ robots.txt no encontrado')

    return ok, issues


def main():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_ADMIN_CHAT_ID') or os.environ.get('TELEGRAM_CHANNEL_ID')

    ok, issues = audit()
    date_str = datetime.now().strftime('%d/%m/%Y')

    lines = ['<b>🔍 Auditoría SEO — GLOBALpatagonia</b>', f'<i>{date_str}</i>', '']

    if not issues:
        lines.append('🟢 <b>Todo en orden.</b> Sin errores detectados.')
        lines.append('')

    if issues:
        lines.append('<b>⚠️ Problemas encontrados:</b>')
        lines.extend(issues)
        lines.append('')

    if ok:
        lines.append('<b>Sin problemas:</b>')
        lines.extend(ok)

    msg = '\n'.join(lines)

    if token and chat_id:
        send_telegram(token, chat_id, msg)
        print('Reporte enviado a Telegram.')
    else:
        print(msg)


if __name__ == '__main__':
    main()
