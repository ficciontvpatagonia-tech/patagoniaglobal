#!/usr/bin/env python3
"""Edición del día de GLOBALpatagonia en PDF, con hipervínculos y QR.

Lee noticias.json (tapa + secundarias + noticias) y arma un PDF A4 de 2 páginas.
Cada titular enlaza a la nota en la web con marca de campaña (utm), así Analytics
distingue el tráfico que viene del PDF.

Uso: python3 _scripts/generar_edicion_pdf.py [salida.pdf]
"""
import io
import json
import os
import re
import sys
import tempfile

from PIL import Image
from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader, simpleSplit
from reportlab.pdfgen import canvas

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://globalpatagonia.org"
UTM = "utm_source=pdf&utm_medium=edicion-del-dia&utm_campaign=edicion-diaria"

AZUL = HexColor("#1c2d3d")
GLACIAL = HexColor("#7aadcc")
GRANITO = HexColor("#252830")
ARCILLA = HexColor("#8c6b4a")
FONDO = HexColor("#f0ede8")

W, H = A4
M = 36  # margen

_EMOJI = re.compile(r"[^\w\s\-áéíóúüñÁÉÍÓÚÜÑ&/·,.:;()ªº%]", re.UNICODE)


def limpio(texto):
    """Quita emoji y símbolos que las fuentes base del PDF no dibujan."""
    return re.sub(r"\s+", " ", _EMOJI.sub("", texto or "")).strip(" ·")


def url_nota(nid):
    return f"{SITE}/notas/{nid}.html?{UTM}"


_TMP = tempfile.mkdtemp()


def imagen(ruta):
    p = os.path.join(BASE, ruta or "")
    if not ruta or not os.path.isfile(p):
        return None
    im = Image.open(p).convert("RGB")
    im.thumbnail((800, 800))  # el PDF se sube al repo cada día: livianito
    # Archivo .jpg real: así reportlab incrusta el JPEG tal cual en vez de re-comprimirlo
    ruta_tmp = os.path.join(_TMP, os.path.basename(p) + ".jpg")
    im.save(ruta_tmp, "JPEG", quality=68, optimize=True)
    return ImageReader(ruta_tmp)


def recorte(c, ruta, x, y, w, h):
    """Dibuja la foto rellenando el rectángulo (recorte centrado)."""
    img = imagen(ruta)
    if not img:
        c.setFillColor(AZUL)
        c.rect(x, y, w, h, fill=1, stroke=0)
        return
    iw, ih = img.getSize()
    esc = max(w / iw, h / ih)
    c.saveState()
    p = c.beginPath()
    p.rect(x, y, w, h)
    c.clipPath(p, stroke=0, fill=0)
    c.drawImage(img, x - (iw * esc - w) / 2, y - (ih * esc - h) / 2, iw * esc, ih * esc)
    c.restoreState()


def parrafo(c, texto, x, y, ancho, fuente, size, lead, color, max_lineas):
    """Escribe texto ajustado hacia abajo desde y; devuelve la y final."""
    c.setFillColor(color)
    c.setFont(fuente, size)
    lineas = simpleSplit(texto, fuente, size, ancho)[:max_lineas]
    if len(lineas) == max_lineas and len(simpleSplit(texto, fuente, size, ancho)) > max_lineas:
        lineas[-1] = lineas[-1].rstrip(" ,.;:") + "…"
    for ln in lineas:
        y -= lead
        c.drawString(x, y, ln)
    return y


def link(c, nid, x, y, w, h):
    c.linkURL(url_nota(nid), (x, y, x + w, y + h), relative=0)


def cabecera(c, fecha, pagina):
    c.setFillColor(AZUL)
    c.rect(0, H - 62, W, 62, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(GLACIAL)
    c.drawString(M, H - 40, "GLOBAL")
    ancho = c.stringWidth("GLOBAL", "Helvetica-Bold", 24)
    c.setFillColor(white)
    c.setFont("Helvetica", 24)
    c.drawString(M + ancho, H - 40, "patagonia")
    c.setFont("Helvetica", 9)
    c.setFillColor(GLACIAL)
    c.drawRightString(W - M, H - 30, "EDICIÓN DEL DÍA")
    c.setFillColor(white)
    c.drawRightString(W - M, H - 44, fecha)
    c.linkURL(f"{SITE}/?{UTM}", (0, H - 62, 260, H), relative=0)


def pie(c, pagina):
    c.setFillColor(GRANITO)
    c.setFont("Helvetica-Oblique", 8)
    c.drawString(M, 22, "GLOBALpatagonia · Sur Global, principio de todo.")
    c.drawRightString(W - M, 22, f"globalpatagonia.org · página {pagina}")


_LOGO = None


def _logo():
    """Logo de GP (domo + Fitz Roy) recortado, listo para el centro del QR."""
    global _LOGO
    if _LOGO is not None:
        return _LOGO
    im = Image.open(os.path.join(BASE, "logo-icono.png")).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    fondo = Image.new("RGBA", im.size, (28, 45, 61, 255))  # azul cordillera detrás del domo
    fondo.alpha_composite(im)
    fondo = fondo.convert("RGB")
    fondo.thumbnail((300, 300))
    _LOGO = ImageReader(fondo)
    return _LOGO


def qr_codigo(c, url, x, y, lado, logo=True):
    """QR (corrección H) con el logo de GP al centro, sobre baldosa blanca."""
    codigo = qr.QrCodeWidget(url, barLevel="H")
    b = codigo.getBounds()
    d = Drawing(lado, lado, transform=[lado / (b[2] - b[0]), 0, 0, lado / (b[3] - b[1]), 0, 0])
    d.add(codigo)
    renderPDF.draw(d, c, x, y)
    if logo:
        marco = lado * 0.27   # ~7% de la superficie: bien dentro de lo que corrige el nivel H
        cx, cy = x + lado / 2, y + lado / 2
        c.setFillColor(white)
        c.roundRect(cx - marco / 2, cy - marco / 2, marco, marco, marco * 0.12, fill=1, stroke=0)
        img = _logo()
        iw, ih = img.getSize()
        w = marco * 0.84
        h = w * ih / iw
        c.drawImage(img, cx - w / 2, cy - h / 2, w, h)


def tarjeta(c, n, x, y_top, ancho, alto_img, tit_size, lineas_tit, lineas_baj):
    """Foto + sección + titular + bajada. Devuelve la y inferior."""
    recorte(c, n.get("imagen"), x, y_top - alto_img, ancho, alto_img)
    y = y_top - alto_img - 4
    c.setFillColor(ARCILLA)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x, y - 9, limpio(n.get("tag", "")).upper())
    y -= 11
    y = parrafo(c, n["titulo"], x, y, ancho, "Times-Bold", tit_size, tit_size + 3, AZUL, lineas_tit)
    if lineas_baj:
        y = parrafo(c, n.get("bajada", ""), x, y - 1, ancho, "Helvetica", 8.5, 11, GRANITO, lineas_baj)
    link(c, n["id"], x, y - 2, ancho, y_top - y + 2)
    return y


def primera(archivo, excluir):
    """Primer item de un JSON de sección que no esté ya en la edición."""
    try:
        datos = json.load(open(os.path.join(BASE, archivo), encoding="utf-8"))
    except (OSError, ValueError):
        return None
    return next((n for n in datos if n.get("id") not in excluir), None)


def notas_de_seccion(excluir):
    """La última nota de Informes, Guías, Cultura y Negocios, con la sección como etiqueta."""
    salida = []
    for archivo, etiqueta in (("propios.json", "Informe"), ("guias.json", "Guía de viaje"),
                              ("cultura.json", "Cultura"), ("negocios.json", "Negocios")):
        n = primera(archivo, excluir)
        if not n:
            continue
        n = dict(n)
        if archivo == "guias.json":
            n["titulo"] = n.get("destino", "")
            n["bajada"] = n.get("tagline", "") + ". " + n.get("descripcion", "")
        n["tag"] = etiqueta
        salida.append(n)
    return salida


QR_URL = f"{SITE}/?utm_source=qr&utm_medium=edicion-pdf&utm_campaign=edicion-diaria"
PDF_URL = f"{SITE}/edicion-del-dia.pdf"


def banda_qr(c, ancho):
    """Franja de portada: QR con logo + llamado a escanear."""
    c.setFillColor(AZUL)
    c.rect(M, 38, ancho, 96, fill=1, stroke=0)
    c.setFillColor(white)
    c.roundRect(M + 10, 44, 84, 84, 5, fill=1, stroke=0)
    qr_codigo(c, QR_URL, M + 14, 48, 76)
    c.linkURL(QR_URL, (M + 10, 44, M + 94, 128), relative=0)
    c.setFillColor(GLACIAL)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(M + 112, 108, "ESCANEÁ EL CÓDIGO")
    c.setFillColor(white)
    c.setFont("Times-Bold", 19)
    c.drawString(M + 112, 86, "Leé GLOBALpatagonia en tu celular")
    c.setFillColor(GLACIAL)
    c.setFont("Helvetica", 9.5)
    c.drawString(M + 112, 66, "Noticias de toda la Patagonia, argentina y chilena, todos los días.")
    c.drawString(M + 112, 53, "Cada titular de esta edición es un enlace a la nota completa.")


def contratapa(c, fecha, pagina):
    c.setFillColor(AZUL)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 34)
    c.setFillColor(GLACIAL)
    anch = c.stringWidth("GLOBAL", "Helvetica-Bold", 34) + c.stringWidth("patagonia", "Helvetica", 34)
    x0 = (W - anch) / 2
    c.drawString(x0, H - 110, "GLOBAL")
    c.setFillColor(white)
    c.setFont("Helvetica", 34)
    c.drawString(x0 + c.stringWidth("GLOBAL", "Helvetica-Bold", 34), H - 110, "patagonia")
    c.setFont("Times-Italic", 15)
    c.setFillColor(GLACIAL)
    c.drawCentredString(W / 2, H - 136, "Sur Global, principio de todo.")
    lado = 300
    x = (W - lado) / 2
    c.setFillColor(white)
    c.roundRect(x - 22, 262 - 22, lado + 44, lado + 44, 12, fill=1, stroke=0)
    qr_codigo(c, QR_URL, x, 262, lado)
    c.linkURL(QR_URL, (x - 22, 240, x + lado + 22, 262 + lado + 22), relative=0)
    c.setFillColor(white)
    c.setFont("Times-Bold", 28)
    c.drawCentredString(W / 2, 190, "Escaneá y leé el resto")
    c.setFont("Helvetica", 12)
    c.setFillColor(GLACIAL)
    c.drawCentredString(W / 2, 166, "Noticias, informes, guías de viaje, clima, mareas y vuelos")
    c.drawCentredString(W / 2, 150, "de toda la Patagonia argentina y chilena.")
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(white)
    c.drawCentredString(W / 2, 112, "globalpatagonia.org")
    c.setFont("Helvetica", 8)
    c.setFillColor(GLACIAL)
    c.drawCentredString(W / 2, 40, f"Edición del día · {fecha}")


def generar(salida):
    d = json.load(open(os.path.join(BASE, "noticias.json"), encoding="utf-8"))
    fecha = d.get("fecha_display", "")
    tapa = d["tapa"]
    resto = d.get("secundarias", []) + d.get("noticias", [])
    c = canvas.Canvas(salida, pagesize=A4)
    c.setTitle(f"GLOBALpatagonia — Edición del día — {fecha}")
    c.setAuthor("GLOBALpatagonia")

    # ── Página 1: tapa + 2 secundarias
    c.setFillColor(FONDO)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    cabecera(c, fecha, 1)
    ancho = W - 2 * M
    y = tarjeta(c, tapa, M, H - 78, ancho, 250, 22, 3, 4)
    col = (ancho - 16) / 2
    for i, n in enumerate(resto[:2]):
        tarjeta(c, n, M + i * (col + 16), y - 22, col, 150, 14, 4, 5)
    banda_qr(c, ancho)
    pie(c, 1)
    c.showPage()

    # ── Páginas siguientes: resto de las notas del día + una nota de cada sección
    items = resto[2:] + notas_de_seccion({n["id"] for n in [tapa] + resto})
    por_pagina = 6
    paginas = [items[i:i + por_pagina] for i in range(0, len(items), por_pagina)] or [[]]
    for k, grupo in enumerate(paginas):
        c.setFillColor(FONDO)
        c.rect(0, 0, W, H, fill=1, stroke=0)
        cabecera(c, fecha, k + 2)
        top = H - 80
        for i, n in enumerate(grupo):
            fila, colu = divmod(i, 2)
            tarjeta(c, n, M + colu * (col + 16), top - fila * 215, col, 92, 12, 3, 3)
        pie(c, k + 2)
        c.showPage()
    contratapa(c, fecha, len(paginas) + 2)
    c.save()
    return salida


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "edicion-del-dia.pdf")
    print("PDF →", generar(out))
