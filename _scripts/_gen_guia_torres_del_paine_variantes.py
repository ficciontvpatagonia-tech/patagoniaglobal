#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera EN/PT/ZH de guia-torres-del-paine desde la ES + traducciones propias. Preview local: NO publica."""
import re, os, html as H
import _gen_guia_torres_del_paine_es as G
import _tr_torres_del_paine as T
BASE = G.BASE
META = {
 "en": ("Torres del Paine: travel guide — W and O circuits, glaciers and wildlife — GLOBALpatagonia",
        "Torres del Paine travel guide, Chilean Patagonia: when to go, how to get there from Puerto Natales and El Calafate, the W and O circuits, Base of the Towers, Grey Glacier, where to sleep and practical tips. With our own map."),
 "pt": ("Torres del Paine: guia de viagem — Circuitos W e O, geleiras e fauna — GLOBALpatagonia",
        "Guia de Torres del Paine, Patagônia chilena: quando ir, como chegar desde Puerto Natales e El Calafate, circuitos W e O, Base das Torres, geleira Grey, onde dormir e dicas práticas. Com mapa próprio."),
 "zh": ("百内国家公园旅行指南 — W环线与O环线、冰川与野生动物 — GLOBALpatagonia",
        "智利巴塔哥尼亚百内国家公园（Torres del Paine）旅行指南：何时前往、从纳塔莱斯港和埃尔卡拉法特如何到达、W环线与O环线、塔底、格雷冰川、住宿与实用提示。附自制地图。"),
}
FLAG = {"en": "🇬🇧 EN", "pt": "🇧🇷 PT", "zh": "🇨🇳 中文"}
def seg_translate(body, tr):
    i = [0]
    def f(m):
        txt = m.group(1) if m.group(1) is not None else m.group(2)
        if not txt.strip():
            return m.group(0)
        k = i[0]; i[0] += 1
        new = tr[k]
        if new is None:
            return m.group(0)
        if m.group(1) is not None:
            lead = txt[:len(txt) - len(txt.lstrip())]; trail = txt[len(txt.rstrip()):]
            return ">" + lead + new + trail + "<"
        return 'alt="' + H.escape(new, quote=True) + '"'
    out = re.sub(r'>([^<>]+)<|alt="([^"]+)"', f, body)
    assert i[0] == len(tr), (i[0], len(tr))
    return out

for lang in ("en", "pt", "zh"):
    tr = getattr(T, lang.upper())
    title, desc = META[lang]
    esq = open(f"{BASE}/notas/guia-esquel-{lang}.html", encoding="utf-8").read()
    head = esq[:esq.index('<div class="hero">')]
    old_title = re.search(r"<title>(.*?)</title>", head).group(1)
    old_desc = re.search(r'<meta name="description" content="(.*?)"/>', head).group(1)
    head = head.replace(old_title, H.escape(title, quote=False)).replace(old_desc, H.escape(desc))
    head = re.sub(r'("headline":\s*)"[^"]*"', lambda m: m.group(1) + '"' + title + '"', head)
    head = head.replace("guia-esquel", G.SLUG)
    head = re.sub(r"https://globalpatagonia\.org/fotos/CIUDADES/esquel-trochita-nieve\.(webp|jpg)", G.HERO_ABS, head)
    head = re.sub(r'"name":\s*"Esquel"', '"name": "Parque Nacional Torres del Paine"', head)
    head = head.replace("  </style>", G.extra_css + "  </style>", 1)
    assert "Esquel" not in head, re.findall(r".{40}Esquel.{40}", head)
    body = seg_translate(G.hero, tr)
    # selector de idioma: activo = este
    body = body.replace(' class="active">🇨🇱 ES', '>🇨🇱 ES').replace(f'-{lang}.html">{FLAG[lang]}', f'-{lang}.html" class="active">{FLAG[lang]}')
    # links de guías relacionadas al mismo idioma si existen
    for g in ("guia-calafate", "guia-patagonia-argentina-chile", "guia-ushuaia"):
        if os.path.exists(f"{BASE}/notas/{g}-{lang}.html"):
            body = body.replace(f"/notas/{g}.html", f"/notas/{g}-{lang}.html")
    tail = esq[esq.index('<div class="divider-footer">'):]
    out = head + body + tail
    p = f"{BASE}/notas/{G.SLUG}-{lang}.html"
    open(p, "w", encoding="utf-8").write(out)
    print("OK", p, len(out), "esp. restante:", len(re.findall(r"\b(el|los|las|para|con|desde)\b", re.sub(r"<[^>]+>", " ", body))) if lang != "pt" else "")
