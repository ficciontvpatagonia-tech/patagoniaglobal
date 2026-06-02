#!/usr/bin/env python3
"""Auditoría SEO semanal — GLOBALpatagonia"""

import os
import re
import json
import xml.etree.ElementTree as ET
import urllib.request
from datetime import datetime

# El script vive en _scripts/ desde la reorg del 31/05/2026 → la raíz del repo
# es el directorio PADRE. (Antes apuntaba a _scripts/ y el auditor crasheaba.)
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP_PATH = os.path.join(REPO, 'sitemap.xml')
NEWS_SITEMAP_PATH = os.path.join(REPO, 'sitemap-news.xml')
NOTAS_DIR = os.path.join(REPO, 'notas')
ROBOTS_PATH = os.path.join(REPO, 'robots.txt')
BASE_URL = 'https://globalpatagonia.org'
GH_REPO = 'ficciontvpatagonia-tech/patagoniaglobal'

# robots.txt NO debe bloquear nota.html/guia.html (llevan noindex y deben ser
# rastreables para que Google lea ese noindex). Sí debe declarar el Sitemap.
ROBOTS_REQUIRED = ['Sitemap:']
ROBOTS_FORBIDDEN = ['Disallow: /nota.html', 'Disallow: /guia.html']


def create_github_issue(token, title, body):
    url = f'https://api.github.com/repos/{GH_REPO}/issues'
    payload = json.dumps({'title': title, 'body': body, 'labels': ['seo']}).encode()
    req = urllib.request.Request(url, data=payload, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github+json',
    })
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


def read_head(path, n=5000):
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
            issues.append(f'  - `{f}`')
        if len(missing_from_sitemap) > 12:
            issues.append(f'  - … y {len(missing_from_sitemap) - 12} más')
    else:
        ok.append(f'✅ Sitemap completo ({len(sm_files)} notas en sitemap, '
                  f'{len(all_files)} archivos en disco)')

    if missing_from_disk:
        issues.append(f'❌ En sitemap pero NO en disco ({len(missing_from_disk)}):')
        for f in missing_from_disk[:8]:
            issues.append(f'  - `{f}`')
    else:
        ok.append('✅ Sin URLs rotas en sitemap')

    if redirect_without_noindex:
        for f in redirect_without_noindex:
            issues.append(f'⚠️ Redirect stub sin noindex: `{f}`')
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
            issues.append(f'  - `{f}`')
        if len(canonical_missing) > 5:
            issues.append(f'  - … y {len(canonical_missing) - 5} más')
    if canonical_bad:
        issues.append(f'🔗 Canonical incorrecto ({len(canonical_bad)}):')
        for f in canonical_bad[:5]:
            issues.append(f'  - `{f}`')
        if len(canonical_bad) > 5:
            issues.append(f'  - … y {len(canonical_bad) - 5} más')
    if not canonical_missing and not canonical_bad:
        ok.append(f'✅ Canonicals correctos ({checked} páginas verificadas)')

    # ── 3. stubs nota.html / guia.html tienen noindex ───────────────────
    for stub in ('nota.html', 'guia.html'):
        h = read_head(os.path.join(REPO, stub))
        if 'noindex' not in h:
            issues.append(f'⚠️ {stub}: falta meta noindex')
        else:
            ok.append(f'✅ {stub} tiene noindex')

    # ── 4. robots.txt ────────────────────────────────────────────────────
    try:
        with open(ROBOTS_PATH, encoding='utf-8') as f:
            robots = f.read()
        robots_missing = [r for r in ROBOTS_REQUIRED if r not in robots]
        # líneas activas (ignora comentarios) para detectar bloqueos prohibidos
        robots_active = [ln.strip() for ln in robots.splitlines()
                         if ln.strip() and not ln.lstrip().startswith('#')]
        robots_bad = [r for r in ROBOTS_FORBIDDEN if r in robots_active]
        if robots_missing:
            for r in robots_missing:
                issues.append(f'🤖 robots.txt: falta `{r}`')
        if robots_bad:
            for r in robots_bad:
                issues.append(f'🤖 robots.txt: NO debe bloquear `{r}` '
                              f'(es noindex, debe ser rastreable)')
        if not robots_missing and not robots_bad:
            ok.append('✅ robots.txt con reglas correctas')
    except FileNotFoundError:
        issues.append('❌ robots.txt no encontrado')

    # ── 5. news sitemap con el nombre correcto ───────────────────────────
    if os.path.isfile(NEWS_SITEMAP_PATH):
        ok.append('✅ sitemap-news.xml presente (nombre que conoce robots/Google)')
    else:
        issues.append('❌ falta sitemap-news.xml — ¿se generó como news-sitemap.xml? '
                      '(usar generar_sitemap_news.py)')

    # ── 6. ninguna URL noindex/redirect del sitemap debe estar listada ───
    try:
        sm_listed = sitemap_notas()  # set de basenames de notas en el sitemap
        leaked = []
        for f in sm_listed:
            h = read_head(os.path.join(NOTAS_DIR, f), 2500)
            if 'noindex' in h or 'window.location.replace' in h or 'http-equiv="refresh"' in h:
                leaked.append(f)
        if leaked:
            issues.append(f'🔗 Stubs/noindex que NO deberían estar en el sitemap ({len(leaked)}):')
            for f in leaked[:8]:
                issues.append(f'  - {f}')
        else:
            ok.append('✅ Sitemap sin stubs ni páginas noindex')
    except Exception:
        pass

    return ok, issues


def main():
    token = os.environ.get('GITHUB_TOKEN')

    ok, issues = audit()
    date_str = datetime.now().strftime('%d/%m/%Y')

    status = '🟢 Sin errores' if not issues else f'⚠️ {len(issues)} problema(s)'
    title = f'Auditoría SEO — {date_str} — {status}'

    lines = [f'## 🔍 Auditoría SEO — GLOBALpatagonia', f'_{date_str}_', '']

    if not issues:
        lines.append('🟢 **Todo en orden.** Sin errores detectados.')
        lines.append('')

    if issues:
        lines.append('### ⚠️ Problemas encontrados')
        lines.extend(issues)
        lines.append('')

    if ok:
        lines.append('### ✅ Sin problemas')
        lines.extend(ok)

    body = '\n'.join(lines)

    if token:
        create_github_issue(token, title, body)
        print('Issue creado en GitHub.')
    else:
        print(body)


if __name__ == '__main__':
    main()
