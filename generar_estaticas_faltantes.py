#!/usr/bin/env python3
"""
Genera notas/[id].html para todas las notas que existen en el historial de git
pero no tienen página estática. Solo crea archivos nuevos, nunca sobreescribe.
"""
import json, subprocess, os, sys

BASE = os.path.dirname(__file__)
sys.path.insert(0, BASE)
from actualizar_noticias import generar_paginas_og

def git_log_hashes(archivo):
    r = subprocess.run(
        ["git", "log", "--format=%H", "--", archivo],
        capture_output=True, text=True, cwd=BASE
    )
    return [h for h in r.stdout.strip().split("\n") if h]

def git_show(sha, archivo):
    r = subprocess.run(
        ["git", "show", f"{sha}:{archivo}"],
        capture_output=True, text=True, cwd=BASE
    )
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except Exception:
        return None

def main():
    notas_dir = os.path.join(BASE, "notas")
    estaticas = set()
    for f in os.listdir(notas_dir):
        if f.endswith(".html"):
            estaticas.add(f.replace(".html", ""))

    # Recolectar todas las notas con cuerpo del historial de git
    todas = {}
    hashes = git_log_hashes("historial.json")
    print(f"Procesando {len(hashes)} versiones de historial.json...")
    for sha in hashes:
        data = git_show(sha, "historial.json")
        if not isinstance(data, list):
            continue
        for nota in data:
            nid = nota.get("id")
            if not nid or nid in todas:
                continue
            if nota.get("cuerpo"):  # solo notas con contenido completo
                todas[nid] = nota

    # Filtrar las que no tienen página estática
    faltantes = [n for nid, n in todas.items() if nid not in estaticas]
    print(f"Notas con cuerpo en git: {len(todas)} — sin página estática: {len(faltantes)}")

    if not faltantes:
        print("Nada que generar.")
        return

    generar_paginas_og(faltantes)
    print(f"\n✓ Listo.")

if __name__ == "__main__":
    main()
