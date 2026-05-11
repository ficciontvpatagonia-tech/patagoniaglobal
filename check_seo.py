#!/usr/bin/env python3
"""Auditoría SEO semanal — GLOBALpatagonia"""

import os
import re
import xml.etree.ElementTree as ET
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

REPO = os.path.dirname(os.path.abspath(__file__))
SITEMAP_PATH = os.path.join(REPO, 'sitemap.xml')
NOTAS_DIR = os.path.join(REPO, 'notas')
ROBOTS_PATH = os.path.join(REPO, 'robots.txt')
BASE_URL = 'https://globalpatagonia.org'
EMAIL_DEST = 'ficciontvpatagonia@gmail.com'

ROBOTS_REQUIRED = ['Disallow: /nota.html', 'Disallow: /buscar.html', 'Sitemap:']


def send_email(app_password, subject, html_body):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = EMAIL_DEST
    msg['To'] = EMAIL_DEST
    msg.attach(MIMEText(html_body, 'html', 'utf-8'))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
        s.login(EMAIL_DEST, app_password)
        s.sendmail(EMAIL_DEST, EMAIL_DEST, msg.as_string())


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
    app_password = os.environ.get('GMAIL_APP_PASSWORD')

    ok, issues = audit()
    date_str = datetime.now().strftime('%d/%m/%Y')

    status = '🟢 Sin errores' if not issues else f'⚠️ {len(issues)} problema(s)'
    subject = f'[GP] Auditoría SEO — {date_str} — {status}'

    lines = [
        '<h2 style="color:#1c2d3d">🔍 Auditoría SEO — GLOBALpatagonia</h2>',
        f'<p style="color:#666">{date_str}</p>',
    ]

    if not issues:
        lines.append('<p>🟢 <strong>Todo en orden.</strong> Sin errores detectados.</p>')

    if issues:
        lines.append('<h3 style="color:#c0392b">⚠️ Problemas encontrados:</h3><ul>')
        for i in issues:
            lines.append(f'<li>{i}</li>')
        lines.append('</ul>')

    if ok:
        lines.append('<h3 style="color:#27ae60">Sin problemas:</h3><ul>')
        for i in ok:
            lines.append(f'<li>{i}</li>')
        lines.append('</ul>')

    html_body = '\n'.join(lines)

    if app_password:
        send_email(app_password, subject, html_body)
        print('Reporte enviado por email.')
    else:
        print(html_body)


if __name__ == '__main__':
    main()
