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


def imagen(ruta):
    p = os.path.join(BASE, ruta or "")
    if not ruta or not os.path.isfile(p):
        return None
    buf = io.BytesIO()
    Image.open(p).convert("RGB").save(buf, "JPEG", quality=85)
    buf.seek(0)
    return ImageReader(buf)


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


def qr_codigo(c, url, x, y, lado):
    codigo = qr.QrCodeWidget(url)
    b = codigo.getBounds()
    d = Drawing(lado, lado, transform=[lado / (b[2] - b[0]), 0, 0, lado / (b[3] - b[1]), 0, 0])
    d.add(codigo)
    renderPDF.draw(d, c, x, y)


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


def bloque_qr(c, ancho):
    c.setFillColor(AZUL)
    c.rect(M, 34, ancho, 80, fill=1, stroke=0)
    # QR sobre baldosa blanca: negro sobre fondo oscuro no se escanea
    c.setFillColor(white)
    c.roundRect(M + 8, 40, 68, 68, 4, fill=1, stroke=0)
    qr_codigo(c, f"{SITE}/?utm_source=qr&utm_medium=edicion-pdf&utm_campaign=edicion-diaria",
              M + 12, 44, 60)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(M + 92, 88, "Escaneá y leé el resto en globalpatagonia.org")
    c.setFont("Helvetica", 9)
    c.setFillColor(GLACIAL)
    c.drawString(M + 92, 72, "Toda la Patagonia argentina y chilena, todos los días.")
    c.drawString(M + 92, 59, "Cada titular de esta edición es un enlace a la nota completa.")


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
        tarjeta(c, n, M + i * (col + 16), y - 22, col, 160, 14, 4, 6)
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
        if k == len(paginas) - 1:
            bloque_qr(c, ancho)
        pie(c, k + 2)
        c.showPage()
    c.save()
    return salida


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "edicion-del-dia.pdf")
    print("PDF →", generar(out))
