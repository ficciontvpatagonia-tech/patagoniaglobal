#!/usr/bin/env python3
"""Genera la edición del día en PDF y la manda al canal de Telegram de GP.

No commitea el PDF (el repo ya pesa mucho): vive solo en Telegram.
Si noticias.json no es de hoy (hora Argentina) no manda nada, para no repetir
la edición de ayer cuando el Action de noticias falló.

Entorno: TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID.
Uso: python3 _scripts/enviar_edicion_telegram.py [--forzar] [--no-enviar]
"""
import json
import os
import sys
import tempfile
import urllib.request
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generar_edicion_pdf import BASE, generar  # noqa: E402


def hoy_argentina():
    return (datetime.now(timezone.utc) - timedelta(hours=3)).strftime("%Y-%m-%d")


def enviar_documento(token, canal, pdf, caption):
    boundary = "----GPedicion"
    campos = {"chat_id": canal, "caption": caption, "parse_mode": "HTML"}
    body = b""
    for k, v in campos.items():
        body += f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
    nombre = os.path.basename(pdf)
    body += (f'--{boundary}\r\nContent-Disposition: form-data; name="document"; '
             f'filename="{nombre}"\r\nContent-Type: application/pdf\r\n\r\n').encode()
    body += open(pdf, "rb").read() + f"\r\n--{boundary}--\r\n".encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendDocument", data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode())


def main():
    forzar = "--forzar" in sys.argv
    d = json.load(open(os.path.join(BASE, "noticias.json"), encoding="utf-8"))
    if not forzar and d.get("generado", "")[:10] != hoy_argentina():
        print(f"noticias.json es de {d.get('generado','?')[:10]}, no de hoy: no se envía.")
        return
    fecha = d.get("fecha_display", "")
    pdf = os.path.join(tempfile.mkdtemp(), "GLOBALpatagonia-edicion-del-dia.pdf")
    generar(pdf)
    print(f"PDF generado ({os.path.getsize(pdf) // 1024} KB)")
    if "--no-enviar" in sys.argv:
        return
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    canal = os.environ.get("TELEGRAM_CHANNEL_ID", "")
    if not token or not canal:
        sys.exit("Faltan TELEGRAM_BOT_TOKEN / TELEGRAM_CHANNEL_ID")
    caption = (f"📰 <b>Edición del día</b> · {fecha}\n\n"
               "Las notas de hoy en un PDF: tocá cualquier titular para leerla completa.\n\n"
               "<i>GLOBALpatagonia · Sur Global, principio de todo.</i>")
    res = enviar_documento(token, canal, pdf, caption)
    print("Telegram OK ✓" if res.get("ok") else f"Telegram error: {res.get('description')}")
    if not res.get("ok"):
        sys.exit(1)


if __name__ == "__main__":
    main()
