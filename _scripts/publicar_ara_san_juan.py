#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publica el informe ARA San Juan (fallo del juicio) en propios.json,
con traducciones EN/PT/ZH escritas a mano (leídas de _borrador_ara_cuerpo_*.txt)."""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROPIOS = os.path.join(BASE, "propios.json")
HISTORIAL = os.path.join(BASE, "propios_historial.json")
SCRIPTS = os.path.join(BASE, "_scripts")
MAX_ACTIVOS = 7

def cuerpo(lang):
    with open(os.path.join(SCRIPTS, f"_borrador_ara_cuerpo_{lang}.txt"), encoding="utf-8") as f:
        return f.read().strip()

nueva_entrada = {
    "id": "20260710-propio-ara-san-juan",
    "titulo": "ARA SAN JUAN: UNA SOLA CONDENA POR LA MUERTE DE LOS 44",
    "bajada": "El Tribunal Oral Federal de Santa Cruz condenó a tres años en suspenso al ex jefe de la Fuerza de Submarinos, Claudio Villamide, y absolvió a los otros tres altos mandos juzgados. Los familiares apelarán. Qué se juzgó, qué decidió el tribunal y qué viene ahora, a casi nueve años del hundimiento.",
    "cuerpo": cuerpo("es"),
    "titulo_en": "ARA SAN JUAN: A SINGLE CONVICTION FOR THE DEATHS OF THE 44",
    "bajada_en": "The Federal Oral Court of Santa Cruz handed a three-year suspended sentence to the former head of the Submarine Force, Claudio Villamide, and acquitted the other three senior officers on trial. The families will appeal. What was judged, what the court decided and what comes next, almost nine years after the sinking.",
    "cuerpo_en": cuerpo("en"),
    "titulo_pt": "ARA SAN JUAN: UMA ÚNICA CONDENAÇÃO PELA MORTE DOS 44",
    "bajada_pt": "O Tribunal Oral Federal de Santa Cruz condenou a três anos de prisão em suspenso o ex-chefe da Força de Submarinos, Claudio Villamide, e absolveu os outros três altos oficiais julgados. As famílias vão recorrer. O que foi julgado, o que o tribunal decidiu e o que vem agora, quase nove anos após o naufrágio.",
    "cuerpo_pt": cuerpo("pt"),
    "titulo_zh": "阿根廷“圣胡安号”潜艇案宣判:44人遇难,仅一人被判刑",
    "bajada_zh": "圣克鲁斯联邦口头法庭判处前潜艇部队司令克劳迪奥·维亚米德三年缓刑,其余三名受审高级军官被判无罪。遇难者家属将提出上诉。距离潜艇沉没近九年,本文梳理这场审判的来龙去脉。",
    "cuerpo_zh": cuerpo("zh"),
    "tag": "⚓ Justicia",
    "categoria": "sociedad|historia|argentina",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "argentina",
    "imagen": "fotos/ara-san-juan-submarino.webp",
    "imagen_keywords": "ara san juan submarino armada argentina juicio fallo condena villamide",
    "hashtags_en": "#ARASanJuan #Argentina #Patagonia #Submarine #Navy",
    "meta": "10 de Julio de 2026 · J. Martineau",
    "excluir_feed": True,
    "galeria": []
}

with open(PROPIOS, encoding="utf-8") as f:
    propios = json.load(f)
with open(HISTORIAL, encoding="utf-8") as f:
    historial = json.load(f)

if any(p.get("id") == nueva_entrada["id"] for p in propios):
    raise SystemExit("Ya existe esa entrada en propios.json — abortado.")

if len(propios) >= MAX_ACTIVOS:
    mas_antiguo = propios.pop()
    historial.insert(0, mas_antiguo)
    print(f"Movido al historial: {mas_antiguo['id']}")

propios.insert(0, nueva_entrada)
print(f"Nuevo informe en propios[0]: {nueva_entrada['id']}")
print(f"Total activos: {len(propios)}")

with open(PROPIOS, "w", encoding="utf-8") as f:
    json.dump(propios, f, ensure_ascii=False, indent=2)
with open(HISTORIAL, "w", encoding="utf-8") as f:
    json.dump(historial, f, ensure_ascii=False, indent=2)

print("OK — propios.json y propios_historial.json actualizados.")
