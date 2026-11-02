#!/usr/bin/env python3
"""Afiches A4 con QR para imprimir (hostels, oficinas de turismo, cartelería).

Una página por destino. Cada QR lleva utm_source=qr&utm_medium=impreso, así
Analytics mide cuánta gente entra desde cada afiche.

Uso: python3 _scripts/generar_qr_guias.py [salida.pdf]
"""
import os
import sys

from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generar_edicion_pdf import (A4, AZUL, BASE, FONDO, GLACIAL, GRANITO, H, SITE, W,  # noqa: E402
                                 qr_codigo, recorte)

AFICHES = [
    {"campania": "guia-torres-es", "path": "notas/guia-torres-del-paine.html",
     "foto": "fotos/CIUDADES/torres-del-paine-hero.webp",
     "tag": "GUÍA DE VIAJE", "titulo": ["Torres del Paine"],
     "bajada": "Circuitos W y O, cuándo ir, cómo llegar y dónde dormir. Con mapa.",
     "cta": "Escaneá y leé la guía"},
    {"campania": "guia-torres-en", "path": "notas/guia-torres-del-paine-en.html",
     "foto": "fotos/CIUDADES/torres-del-paine-hero.webp",
     "tag": "TRAVEL GUIDE", "titulo": ["Torres del Paine"],
     "bajada": "W and O circuits, when to go, how to get there and where to stay. With map.",
     "cta": "Scan to read the guide"},
    {"campania": "guia-circuito-es", "path": "notas/guia-circuito-austral.html",
     "foto": "fotos/CIUDADES/calafate-glaciar-tempanos-aereo.webp",
     "tag": "GUÍA DE VIAJE", "titulo": ["Circuito Austral", "12 días, 2 países"],
     "bajada": "De El Calafate a Ushuaia pasando por Chile, día por día.",
     "cta": "Escaneá y armá tu viaje"},
    {"campania": "guia-circuito-en", "path": "notas/guia-circuito-austral-en.html",
     "foto": "fotos/CIUDADES/calafate-glaciar-tempanos-aereo.webp",
     "tag": "TRAVEL GUIDE", "titulo": ["Southern Circuit", "12 days, 2 countries"],
     "bajada": "From El Calafate to Ushuaia via Chile, day by day.",
     "cta": "Scan and plan your trip"},
    {"campania": "whatsapp", "url": "https://whatsapp.com/channel/0029VbDPKE6DJ6Gyg2eQTH2j", "path": "",
     "foto": "fotos/CIUDADES/torres-del-paine-hero.webp",
     "tag": "CANAL DE WHATSAPP", "titulo": ["La edición del día,", "en tu WhatsApp"],
     "bajada": "Sumate al canal de GLOBALpatagonia y recibí cada mañana las noticias de la Patagonia.",
     "cta": "Escaneá y sumate"},
    {"campania": "sitio", "path": "",
     "foto": "fotos/CIUDADES/torres-del-paine-hero.webp",
     "tag": "NOTICIAS", "titulo": ["La Patagonia,", "todos los días"],
     "bajada": "Noticias de Argentina y Chile, clima, mareas, vuelos y guías de viaje.",
     "cta": "Escaneá y entrá"},
]


def afiche(c, a):
    c.setFillColor(FONDO)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    recorte(c, a["foto"], 0, H - 380, W, 380)
    c.setFillColor(AZUL)
    c.rect(0, H - 62, W, 62, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(GLACIAL)
    c.drawString(40, H - 42, "GLOBAL")
    c.setFillColor(white)
    c.setFont("Helvetica", 28)
    c.drawString(40 + c.stringWidth("GLOBAL", "Helvetica-Bold", 28), H - 42, "patagonia")
    # bloque de título
    c.setFillColor(AZUL)
    c.rect(0, H - 380 - 150, W, 150, fill=1, stroke=0)
    c.setFillColor(GLACIAL)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, H - 380 - 30, a["tag"])
    c.setFillColor(white)
    y = H - 380 - 62
    for ln in a["titulo"]:
        c.setFont("Times-Bold", 36)
        c.drawString(40, y, ln)
        y -= 38
    # QR
    url = a.get("url") or f"{SITE}/{a['path']}?utm_source=qr&utm_medium=impreso&utm_campaign={a['campania']}"
    lado = 190
    qr_codigo(c, url, 40, 95, lado)
    c.setFillColor(AZUL)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(260, 245, a["cta"])
    c.setFillColor(GRANITO)
    c.setFont("Helvetica", 12)
    from reportlab.lib.utils import simpleSplit
    yy = 220
    for ln in simpleSplit(a["bajada"], "Helvetica", 12, W - 260 - 40):
        c.drawString(260, yy, ln)
        yy -= 16
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(AZUL)
    c.drawString(260, 130, "globalpatagonia.org")
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(GRANITO)
    c.drawString(40, 50, "GLOBALpatagonia · Sur Global, principio de todo.")


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "qr-afiches.pdf")
    c = canvas.Canvas(out, pagesize=A4)
    c.setTitle("GLOBALpatagonia — afiches QR")
    for a in AFICHES:
        afiche(c, a)
        c.showPage()
    c.save()
    print("PDF →", out)


if __name__ == "__main__":
    main()
