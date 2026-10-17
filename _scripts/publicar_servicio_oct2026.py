#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Notas de SERVICIO del 17/10/2026 (FUAS 2027 + Zona Fría), escritas a mano.
Entran como las 2 SECUNDARIAS de portada; la tapa actual queda; las secundarias
actuales bajan a las tarjetas de la semana. El Action de las 6:00 las rota solo después.

Etapa 1:  python3 _scripts/publicar_servicio_oct2026.py imagenes   → borrador + preview (NO toca el sitio)
Etapa 2:  python3 _scripts/publicar_servicio_oct2026.py publicar   → SOLO con OK de Marto
"""
import os, re, sys, json, html
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import actualizar_noticias as A

BORRADOR = os.path.join(BASE, "_scripts", "_borrador_servicio_oct2026.json")
PREVIEW = "/Users/jm/Desktop/PREVIEW_notas_servicio.html"
HOY = datetime.now().strftime("%Y%m%d")

fuas = {
    "titulo": "FUAS 2027: hasta el 22 de octubre para pedir becas, créditos y gratuidad",
    "bajada": "El formulario único para acceder a ayudas de la educación superior en Chile cierra el jueves 22. Es gratis, se completa online y no exige haber rendido la PAES. Cómo hacerlo, qué se puede pedir y qué pasa con la Beca Magallanes.",
    "cuerpo": (
        "Quedan días para uno de los trámites que más define el futuro de miles de jóvenes patagónicos: el FUAS 2027, el "
        "Formulario Único de Acreditación Socioeconómica, que se completa hasta el jueves 22 de octubre en fuas.cl. "
        "Es gratuito, funciona desde el celular, una tablet o una computadora y no requiere haber rendido la PAES.\n\n"
        "El formulario sirve para quienes quieren entrar en 2027 a un centro de formación técnica, un instituto profesional "
        "o una universidad, y también para quienes ya estudian sin apoyo económico y buscan acceder a la gratuidad u otro "
        "beneficio. Con una sola postulación se pide todo: la gratuidad, becas como Bicentenario, Nuevo Milenio, Juan Gómez "
        "Millas o Excelencia Académica, y los créditos Fondo Solidario y CAE. El detalle de cada ayuda está en "
        "beneficiosestudiantiles.cl.\n\n"
        "La Subsecretaría de Educación Superior valida los datos declarados para determinar el nivel de ingresos y los "
        "requisitos de cada beneficio. Una de las fuentes de verificación es el Registro Social de Hogares (RSH): se puede "
        "postular sin él, pero tenerlo actualizado agiliza la revisión. Quien no lo tenga deberá acreditar su situación "
        "socioeconómica en la institución donde se matricule. El RSH se obtiene o actualiza en registrosocial.gob.cl, en el "
        "municipio o en ventanillaunicasocial.gob.cl con Clave Única.\n\n"
        "La subsecretaria Fernanda Valdés hizo un llamado especial a las familias del 60% de menores ingresos del país a "
        "completarlo. Las consultas se atienden en Ayuda Mineduc, al 600 600 2626.\n\n"
        "Para quienes estudian en Magallanes hay otra novedad que conviene tener en el radar: según el informe de evaluación "
        "ex ante del presupuesto 2027, la Beca Magallanes dejará de existir como programa propio y se fusionará con las becas "
        "Aysén y Patagonia Aysén en un nuevo programa llamado Becas Patagonia. Hoy la beca entrega $1.090.650 anuales de libre "
        "disposición a estudiantes con familia en la región que cursan educación superior en ella, y la reciben 1.173 "
        "alumnos de la Universidad de Magallanes. Las condiciones del nuevo programa todavía no se detallaron."
    ),
    "tag": "🎓 Becas",
    "categoria": "bienestar",
    "fuente": "Mineduc Magallanes · La Prensa Austral",
    "url_original": "https://magallanes.mineduc.cl/2026/10/01/fuas-2027-ya-esta-abierta-la-postulacion-a-becas-creditos-y-gratuidad-para-la-educacion-superior/",
    "pais": "chile",
    "imagen": None,
    "imagen_keywords": "estudiantes universidad chile",
}

zona = {
    "titulo": "Zona Fría: qué cambia en la factura de gas patagónica con la nueva ley",
    "bajada": "La ley 27.828 ya fue publicada en el Boletín Oficial. El descuento deja de cubrir toda la factura y el 50% ya no está garantizado por ley. Qué se sabe y qué todavía no.",
    "cuerpo": (
        "El régimen de Zona Fría, el descuento en el gas que alivia las boletas de los hogares patagónicos desde hace "
        "décadas, cambió. La ley 27.828, votada por mayoría en el Congreso, fue publicada en el Boletín Oficial y modifica "
        "dos puntos centrales de cómo se calcula el beneficio. Nadie lo había puesto todavía en números: ese es, por ahora, "
        "el dato que falta.\n\n"
        "Primero, el alcance. Según el nuevo artículo 75, inciso a), la bonificación se aplica solamente sobre el precio "
        "del gas, y ya no sobre la factura completa. Quedan afuera los componentes de transporte y distribución, de modo que "
        "el descuento pesa menos en lo que el usuario efectivamente paga.\n\n"
        "Segundo, el porcentaje. El beneficio pasa a ser de \"hasta el 50%\", y el monto final queda a criterio del Poder "
        "Ejecutivo y de la autoridad de aplicación. Antes, ese piso de 50% estaba garantizado por ley. Para acceder a un "
        "descuento mayor, cada usuario deberá demostrar ante las autoridades una situación de imposibilidad de pago.\n\n"
        "El diputado rionegrino Marcelo Mango, que alertó sobre la publicación, anticipó: \"Se viene un aumento del gas en "
        "toda la Patagonia\", y dijo que trabajará para modificar nuevamente la ley y recuperar el beneficio. También "
        "cuestionó a legisladores y gobernadores de la región. Hasta ahora, según los medios que recogieron sus "
        "declaraciones, los mandatarios mencionados no respondieron públicamente.\n\n"
        "Qué falta saber: cuánto subirán las boletas dependerá del porcentaje que fije el Ejecutivo, y no hay todavía una "
        "estimación oficial ni una fecha para la reglamentación. Lo cierto es que el tema toca de lleno a Neuquén, Río "
        "Negro, Chubut, Santa Cruz y Tierra del Fuego, en pleno cambio de estación y a meses del próximo invierno, y que "
        "reabre una discusión de fondo: la Patagonia produce buena parte del gas del país y es, a la vez, la región donde "
        "más pesa en el bolsillo."
    ),
    "tag": "🔥 Servicios",
    "categoria": "bienestar",
    "fuente": "Bariloche2000 · Realidad SM",
    "url_original": "https://www.bariloche2000.com/sociedad/impacto-en-la-patagonia-promulgan-la-ley-que-modifica-el-regimen-de-zona-fria-y-aumenta-la-tarifa-del-gas-20261013-0008.html",
    "pais": "argentina",
    "imagen": None,
    "imagen_keywords": "gas invierno patagonia hogar",
}

fuas["id"] = f"{HOY}-{A.slugify(fuas['titulo'])}-sec1"
zona["id"] = f"{HOY}-{A.slugify(zona['titulo'])}-sec2"
NOTAS = [fuas, zona]


def imagenes():
    fotos = A.fotos_propias_disponibles()
    usadas = set()
    for n in NOTAS:
        n["imagen"] = A.resolver_imagen(n, fotos, usadas)
        n["meta"] = f"Hoy · {n['fuente']}"
        if n.get("imagen"):
            usadas.add(n["imagen"])
    json.dump({"notas": NOTAS}, open(BORRADOR, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    h = ['<!doctype html><meta charset="utf-8"><body style="font:17px/1.7 Inter,system-ui;max-width:720px;margin:0 auto;padding:20px;background:#f0ede8">'
         '<div style="background:#8c6b4a;color:#fff;text-align:center;padding:.5rem">PREVIEW — NO PUBLICADO</div>']
    for n in NOTAS:
        img = os.path.join(BASE, n["imagen"]) if n.get("imagen") else ""
        h.append(f'<hr><p style="color:#7aadcc;font-weight:700">{html.escape(n["tag"])} · {html.escape(n["pais"])}</p>')
        h.append(f'<h1 style="font-family:Georgia;color:#1c2d3d">{html.escape(n["titulo"])}</h1><p><em>{html.escape(n["bajada"])}</em></p>')
        if img: h.append(f'<img src="file://{img}" style="width:100%;border-radius:6px">')
        for p in n["cuerpo"].split("\n\n"): h.append(f"<p>{html.escape(p)}</p>")
        h.append(f'<p style="color:#888;font-size:.85rem">Fuente: {html.escape(n["fuente"])}</p>')
    open(PREVIEW, "w", encoding="utf-8").write("\n".join(h))
    for n in NOTAS: print(n["id"], "→", n.get("imagen"))
    print("Preview:", PREVIEW)


def publicar():
    b = json.load(open(BORRADOR, encoding="utf-8"))["notas"]
    actual = json.load(open(os.path.join(BASE, "noticias.json"), encoding="utf-8"))
    tapa = actual["tapa"]
    prev_sec = actual.get("secundarias", [])
    prev_noticias = actual.get("noticias", [])
    ticker = actual.get("ticker", [])

    historial = A.cargar_historial()
    for n in b:
        n["excluir_feed"] = False
    historial = b + historial
    A.guardar_historial(historial)
    A._persistir_urls_nuevas(b)

    datos = A.construir_noticias_json(tapa, b, None, prev_sec, prev_noticias, ticker)
    A.guardar_json(datos)
    A.inyectar_tapa_en_index(datos)

    notas = list(b) + [tapa]
    for f in ("historial.json", "propios.json", "propios_historial.json", "historias.json", "noticias.json",
              "turismo.json", "deportes_feed.json", "negocios.json", "cultura.json", "guias.json"):
        notas += A._notas_de_fuente(os.path.join(BASE, f))
    notas = [n for n in notas if isinstance(n, dict) and n.get("id")]
    A.generar_paginas_og(notas)
    A.actualizar_search_index()
    A.actualizar_archivo_en_index(notas)
    A.generar_paginas_temas(notas)
    A.generar_feed_rss()
    A.actualizar_sitemap()
    print("✓ publicado")


if __name__ == "__main__":
    {"imagenes": imagenes, "publicar": publicar}.get(sys.argv[1] if len(sys.argv) > 1 else "imagenes", imagenes)()
