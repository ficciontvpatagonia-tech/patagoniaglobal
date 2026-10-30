#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera EN/PT/ZH de guia-circuito-austral desde la ES + traducciones propias. Preview local: NO publica."""
import re, os, html as H
import _gen_guia_circuito_austral_es as G
import _tr_circuito_austral as T
BASE = G.BASE
META = {
 "en": ("Austral Circuit: 12 days from El Calafate to Ushuaia across Argentina and Chile — GLOBALpatagonia",
        "A 12-day itinerary through southern Patagonia across two countries: El Calafate, Torres del Paine, Puerto Natales, Punta Arenas and Ushuaia. Day by day, how to get between stops, border crossings, rental car costs and practical tips."),
 "pt": ("Circuito Austral: 12 dias de El Calafate a Ushuaia pela Argentina e pelo Chile — GLOBALpatagonia",
        "Roteiro de 12 dias pela Patagônia austral em dois países: El Calafate, Torres del Paine, Puerto Natales, Punta Arenas e Ushuaia. Dia a dia, como se deslocar entre as paradas, travessias de fronteira, custo do carro alugado e dicas práticas."),
 "zh": ("南方环线：从埃尔卡拉法特到乌斯怀亚，横跨阿根廷与智利的12天 — GLOBALpatagonia",
        "巴塔哥尼亚南部两国12天行程：埃尔卡拉法特、百内国家公园、纳塔莱斯港、蓬塔阿雷纳斯和乌斯怀亚。逐日安排、站点间交通、过境信息、租车费用和实用提示。"),
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
    head = re.sub(r'"@type":\s*"TouristDestination"', '"@type": "TouristTrip"', head)
    head = re.sub(r'"name":\s*"Esquel"', '"name": "' + {"en": "Austral Circuit: El Calafate, Torres del Paine, Punta Arenas and Ushuaia", "pt": "Circuito Austral: El Calafate, Torres del Paine, Punta Arenas e Ushuaia", "zh": "南方环线：埃尔卡拉法特、百内、蓬塔阿雷纳斯和乌斯怀亚"}[lang] + '"', head)
    head = head.replace("  </style>", G.extra_css + "  </style>", 1)
    assert "Esquel" not in head, re.findall(r".{40}Esquel.{40}", head)
    body = seg_translate(G.hero, tr)
    body = body.replace(' class="active">🇦🇷 ES', '>🇦🇷 ES').replace(f'-{lang}.html">{FLAG[lang]}', f'-{lang}.html" class="active">{FLAG[lang]}')
    for g in ("guia-calafate", "guia-torres-del-paine", "guia-ushuaia"):
        body = body.replace(f"/notas/{g}.html", f"/notas/{g}-{lang}.html").replace(f"href='{g}.html'", f"href='{g}-{lang}.html'")
    tail = esq[esq.index('<div class="divider-footer">'):]
    out = head + body + tail
    p = f"{BASE}/notas/{G.SLUG}-{lang}.html"
    open(p, "w", encoding="utf-8").write(out)
    print("OK", p, len(out))
