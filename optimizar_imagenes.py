#!/usr/bin/env python3
"""
Optimizador automático de imágenes para GLOBALpatagonia.

Detecta imágenes en fotos/ sin versión WebP o demasiado anchas,
las convierte/redimensiona, actualiza referencias en JSONs y HTMLs.

Uso:
    python3 optimizar_imagenes.py            # modo normal
    python3 optimizar_imagenes.py --dry-run  # solo muestra qué haría
    python3 optimizar_imagenes.py --force    # recomprimir aunque ya exista .webp
"""

import os
import re
import sys
import json
import argparse
import subprocess
from pathlib import Path

try:
    from PIL import Image
    PIL_OK = True
except ImportError:
    PIL_OK = False

BASE      = Path(__file__).parent
FOTOS_DIR = BASE / "fotos"

MAX_WIDTH  = 1200   # px — ancho máximo web
QUALITY    = 82     # calidad WebP
MIN_BYTES  = 50_000 # ignorar imágenes muy pequeñas (thumbnails IG, etc.)

# Subdirectorios a excluir (contienen imágenes no servidas en web)
SKIP_DIRS = set()   # vacío = procesar todo

# JSONs donde actualizar referencias de imágenes
JSON_FILES = [
    "noticias.json", "historial.json", "historias.json",
    "propios.json", "propios_historial.json",
    "turismo.json", "guias.json", "guias_historial.json",
    "deportes_feed.json", "deportes_historial.json",
    "negocios.json", "cultura.json", "videos.json", "agenda.json",
]


# ── Conversión ──────────────────────────────────────────────────────────────

def convertir_a_webp(src: Path, dry_run=False, force=False) -> Path | None:
    """Convierte src a WebP (máx MAX_WIDTH px). Retorna la ruta WebP o None si hubo error."""
    if not PIL_OK:
        print(f"  [SKIP] Pillow no disponible: {src.name}")
        return None

    dst = src.with_suffix(".webp")
    if dst.exists() and not force:
        return dst  # ya existe

    if dry_run:
        print(f"  [DRY]  {src.name} → {dst.name}")
        return dst

    try:
        with Image.open(src) as img:
            modo = "RGBA" if img.mode in ("RGBA", "LA", "P") else "RGB"
            img_c = img.convert(modo)
            if img_c.width > MAX_WIDTH:
                ratio  = MAX_WIDTH / img_c.width
                new_h  = int(img_c.height * ratio)
                img_c  = img_c.resize((MAX_WIDTH, new_h), Image.LANCZOS)
            img_c.save(dst, "WEBP", quality=QUALITY, method=4)
        print(f"  ✓ {src.name} ({src.stat().st_size//1024}KB) → {dst.name} ({dst.stat().st_size//1024}KB)")
        return dst
    except Exception as e:
        print(f"  ✗ {src.name}: {e}")
        return None


def recomprimir_webp(src: Path, dry_run=False) -> bool:
    """Redimensiona un WebP existente que supera MAX_WIDTH. Retorna True si cambió."""
    if not PIL_OK:
        return False
    try:
        with Image.open(src) as img:
            if img.width <= MAX_WIDTH:
                return False
            if dry_run:
                print(f"  [DRY]  resize {src.name} ({img.width}px → {MAX_WIDTH}px)")
                return True
            ratio = MAX_WIDTH / img.width
            new_h = int(img.height * ratio)
            img2  = img.convert("RGB").resize((MAX_WIDTH, new_h), Image.LANCZOS)
            img2.save(src, "WEBP", quality=QUALITY, method=4)
            print(f"  ↓ resize {src.name} ({img.width}px → {MAX_WIDTH}px)")
            return True
    except Exception as e:
        print(f"  ✗ resize {src.name}: {e}")
        return False


# ── Escaneo ──────────────────────────────────────────────────────────────────

def escanear(force=False):
    """Devuelve (a_convertir, a_recomprimir): listas de Path."""
    a_convertir    = []
    a_recomprimir  = []

    for root, dirs, files in os.walk(FOTOS_DIR):
        root_path = Path(root)
        # Filtrar subdirectorios excluidos
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for fn in files:
            fpath = root_path / fn
            ext   = fpath.suffix.lower()

            if ext in (".jpg", ".jpeg", ".png"):
                if fpath.stat().st_size < MIN_BYTES:
                    continue
                dst = fpath.with_suffix(".webp")
                if not dst.exists() or force:
                    a_convertir.append(fpath)

            elif ext == ".webp":
                if not PIL_OK:
                    continue
                try:
                    with Image.open(fpath) as img:
                        if img.width > MAX_WIDTH:
                            a_recomprimir.append(fpath)
                except Exception:
                    pass

    return a_convertir, a_recomprimir


# ── Actualizar referencias en JSONs ─────────────────────────────────────────

def actualizar_jsons(dry_run=False) -> int:
    """Reemplaza paths .jpg/.png → .webp en campos 'imagen' de los JSONs cuando el .webp existe."""
    cambios = 0
    pat = re.compile(r'"imagen":\s*"([^"]+\.(?:jpg|jpeg|png))"', re.IGNORECASE)

    for jf in JSON_FILES:
        fpath = BASE / jf
        if not fpath.exists():
            continue
        texto = fpath.read_text(encoding="utf-8")

        def reemplazar(m):
            img_path = m.group(1)
            webp_path = re.sub(r'\.(jpg|jpeg|png)$', '.webp', img_path, flags=re.IGNORECASE)
            full_webp = BASE / webp_path
            if full_webp.exists():
                return m.group(0).replace(img_path, webp_path)
            return m.group(0)

        nuevo = pat.sub(reemplazar, texto)
        if nuevo != texto:
            if dry_run:
                print(f"  [DRY]  actualizar {jf}")
            else:
                fpath.write_text(nuevo, encoding="utf-8")
                print(f"  ✓ actualizado {jf}")
            cambios += 1

    return cambios


def actualizar_htmls(dry_run=False) -> int:
    """Reemplaza src/content .jpg/.png → .webp en notas/*.html cuando el .webp existe."""
    cambios = 0
    notas_dir = BASE / "notas"
    if not notas_dir.exists():
        return 0

    pat = re.compile(
        r'(?:src|content)="([^"]+\.(?:jpg|jpeg|png))"',
        re.IGNORECASE
    )

    for html_file in notas_dir.glob("*.html"):
        texto = html_file.read_text(encoding="utf-8")

        def reemplazar_html(m):
            url = m.group(1)
            for domain in ["https://globalpatagonia.org/", "http://globalpatagonia.org/"]:
                if url.startswith(domain):
                    rel = url[len(domain):]
                    webp_rel = re.sub(r'\.(jpg|jpeg|png)$', '.webp', rel, flags=re.IGNORECASE)
                    if (BASE / webp_rel).exists():
                        return m.group(0).replace(url, domain + webp_rel)
                    return m.group(0)
            # Rutas relativas
            if url.startswith(("../fotos/", "fotos/")):
                clean = url.replace("../", "")
                webp_url = re.sub(r'\.(jpg|jpeg|png)$', '.webp', url, flags=re.IGNORECASE)
                if (BASE / re.sub(r'\.(jpg|jpeg|png)$', '.webp', clean, flags=re.IGNORECASE)).exists():
                    return m.group(0).replace(url, webp_url)
            return m.group(0)

        nuevo = pat.sub(reemplazar_html, texto)
        if nuevo != texto:
            if dry_run:
                print(f"  [DRY]  actualizar notas/{html_file.name}")
            else:
                html_file.write_text(nuevo, encoding="utf-8")
                print(f"  ✓ notas/{html_file.name}")
            cambios += 1

    return cambios


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Optimizador de imágenes GLOBALpatagonia")
    parser.add_argument("--dry-run",  action="store_true", help="Solo mostrar qué haría")
    parser.add_argument("--force",    action="store_true", help="Recomprimir aunque ya exista .webp")
    parser.add_argument("--no-refs",  action="store_true", help="No actualizar referencias en JSONs/HTML")
    args = parser.parse_args()

    if not PIL_OK:
        print("ERROR: Pillow no instalado. Correr: pip install Pillow")
        sys.exit(1)

    print(f"=== Optimizador de imágenes GLOBALpatagonia ===")
    print(f"    Directorio: {FOTOS_DIR}")
    print(f"    Máx ancho:  {MAX_WIDTH}px | Calidad WebP: {QUALITY}")
    if args.dry_run:
        print("    MODO DRY-RUN — no se harán cambios\n")

    a_convertir, a_recomprimir = escanear(force=args.force)

    total_conv = 0
    total_resize = 0

    if a_convertir:
        print(f"\n── Convertir a WebP ({len(a_convertir)} imágenes) ──")
        for src in sorted(a_convertir):
            result = convertir_a_webp(src, dry_run=args.dry_run, force=args.force)
            if result:
                total_conv += 1

    if a_recomprimir:
        print(f"\n── Redimensionar WebP anchos ({len(a_recomprimir)} imágenes) ──")
        for src in sorted(a_recomprimir):
            if recomprimir_webp(src, dry_run=args.dry_run):
                total_resize += 1

    if not args.no_refs and (total_conv > 0 or total_resize > 0 or args.force):
        print(f"\n── Actualizar referencias ──")
        c_json = actualizar_jsons(dry_run=args.dry_run)
        c_html = actualizar_htmls(dry_run=args.dry_run)
        print(f"   JSONs: {c_json}  |  HTMLs: {c_html}")

    print(f"\n=== Listo: {total_conv} convertidas, {total_resize} redimensionadas ===")

    # Exit code 1 si no hubo nada que hacer (útil para Action)
    if total_conv == 0 and total_resize == 0:
        sys.exit(0)
    sys.exit(0)


if __name__ == "__main__":
    main()
