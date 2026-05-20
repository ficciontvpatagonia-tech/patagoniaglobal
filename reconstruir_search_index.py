#!/usr/bin/env python3
"""
Reconstruye search-index.json acumulando todas las notas que alguna vez
estuvieron en historial.json a lo largo del historial de git.
"""
import json, subprocess, os, re

BASE = os.path.dirname(__file__)
INDEX_PATH = os.path.join(BASE, "search-index.json")

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

def normalizar(nota):
    nid = nota.get("id", "")
    if not nid or not nota.get("titulo"):
        return None
    return {
        "id":        nid,
        "titulo":    nota.get("titulo", ""),
        "bajada":    nota.get("bajada", ""),
        "fecha":     nota.get("fecha", ""),
        "categoria": nota.get("categoria", nota.get("tag", "")),
        "imagen":    nota.get("imagen", ""),
    }

def cargar_indice_existente():
    try:
        with open(INDEX_PATH, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def main():
    print("Reconstruyendo search-index.json desde historial de git...")

    indice_existente = cargar_indice_existente()
    ids_vistos = {n["id"] for n in indice_existente if n.get("id")}
    total_previo = len(ids_vistos)

    todas = {}

    # Fuentes estáticas actuales (JSONs en disco)
    fuentes_json = [
        "historial.json", "noticias.json", "historias.json",
        "turismo.json", "deportes_feed.json", "propios.json",
        "propios_historial.json", "negocios.json", "guias.json",
        "guias_historial.json", "deportes_historial.json", "cultura.json",
    ]
    for nombre in fuentes_json:
        ruta = os.path.join(BASE, nombre)
        if not os.path.exists(ruta):
            continue
        try:
            with open(ruta, encoding="utf-8") as f:
                data = json.load(f)
            notas = []
            if isinstance(data, list):
                notas = data
            elif isinstance(data, dict):
                if data.get("tapa"):
                    notas.append(data["tapa"])
                for clave in ("secundarias", "noticias", "historias", "notas", "row_cards"):
                    notas.extend(data.get(clave, []))
                if data.get("principal"):
                    notas.append(data["principal"])
            for n in notas:
                e = normalizar(n)
                if e and e["id"] not in todas:
                    todas[e["id"]] = e
        except Exception as e:
            print(f"  ⚠ Error leyendo {nombre}: {e}")

    # Historial completo de git para historial.json
    hashes = git_log_hashes("historial.json")
    print(f"  Procesando {len(hashes)} versiones de historial.json en git...")
    for sha in hashes:
        data = git_show(sha, "historial.json")
        if not isinstance(data, list):
            continue
        for n in data:
            e = normalizar(n)
            if e and e["id"] not in todas:
                todas[e["id"]] = e

    # Combinar con índice existente (mantener datos enriquecidos previos)
    for n in indice_existente:
        nid = n.get("id")
        if nid and nid not in todas:
            todas[nid] = n

    resultado = sorted(todas.values(), key=lambda n: n.get("fecha", ""), reverse=True)

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    nuevas = len(resultado) - total_previo
    print(f"  ✓ search-index.json: {len(resultado)} notas totales (+{nuevas} nuevas)")

if __name__ == "__main__":
    main()
