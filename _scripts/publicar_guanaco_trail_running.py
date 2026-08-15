#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deportes manual — 15/08/2026
Guanaco Trail Running: nota en profundidad (categorías, circuito, contexto
turístico) como seguimiento del anuncio que GLOBALpatagonia ya había cubierto
el 05/08/2026 (notas/20260805-timaukel-lanza-el-primer-guanaco-trail-running-en-dep.html).
Fuentes: OvejeroNoticias, La Prensa Austral, Municipalidad de Timaukel.
"""
import os, sys, json
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import actualizar_noticias as A

HOY_SLUG = datetime.now().strftime("%Y%m%d")

deportes = {
    "id": f"{HOY_SLUG}-guanaco-trail-running-fecha-categorias-y-circuito-dep",
    "titulo": "Guanaco Trail Running 2027: fecha, categorías y circuito",
    "bajada": "La Municipalidad de Timaukel confirmó las tres categorías —Chulengo, 14K y Bagual— de la primera edición, fijada para el 13 de febrero de 2027 entre Pampa Guanaco y Lago Blanco, en el sur de Tierra del Fuego chilena.",
    "cuerpo": (
        "La primera edición del <strong>Guanaco Trail Running</strong> ya tiene fecha, categorías y trazado confirmados. La Municipalidad de Timaukel, en el corazón de la Tierra del Fuego chilena, precisó que la carrera se correrá el <strong>sábado 13 de febrero de 2027</strong> entre Pampa Guanaco y Lago Blanco, y espera reunir a más de <strong>300 corredores</strong> de Chile y Argentina en uno de los rincones menos transitados de la Patagonia.\n\n"
        'El anuncio, que GLOBALpatagonia adelantó a <a href="20260805-timaukel-lanza-el-primer-guanaco-trail-running-en-dep.html">comienzos de agosto</a>, generó bastante ruido entre los trail runners de Magallanes y también del lado argentino: no hay antecedentes de una carrera de montaña organizada puertas adentro de Timaukel, una comuna de apenas 423 habitantes. Estas son las precisiones que fue confirmando el municipio desde entonces.\n\n'
        "<h3>Tres carreras, un mismo paisaje</h3>\n\n"
        '<table class="ski-table"><thead><tr><th>Categoría</th><th>Distancia</th><th>Perfil</th></tr></thead><tbody>'
        '<tr><td><strong>Chulengo</strong></td>'
        '<td class="total-col">3 km</td><td>Circuito corto, pensado para familias y debutantes en el trail</td></tr>'
        '<tr><td><strong>14K</strong></td><td class="total-col">14 km</td>'
        '<td>Distancia intermedia, con tramos de bosque y turbera</td></tr>'
        '<tr><td><strong>Bagual</strong></td>'
        '<td class="total-col">30 km</td><td>El circuito completo: bosques, turba, cruces de río y desnivel entre Pampa Guanaco y Lago Blanco</td></tr>'
        "</tbody></table>\n\n"
        '<img src="../fotos/guanaco-corriendo-tierra-del-fuego.webp" alt="Guanaco corriendo en la estepa fueguina" style="width:100%;border-radius:6px;margin:24px 0 4px;display:block;"/>\n\n'
        '<p class="ski-nota">El guanaco, el animal que da nombre a la carrera y domina el paisaje de Timaukel.</p>\n\n'
        '<div style="background:#1c2d3d;color:white;border-radius:6px;padding:20px 24px;margin:32px 0;display:flex;align-items:center;gap:20px;">'
        '<div style="font-family:\'Playfair Display\',serif;font-size:44px;font-weight:900;color:#8ab8d4;line-height:1;flex-shrink:0;">423</div>'
        '<div style="font-size:14px;line-height:1.6;color:rgba(255,255,255,0.85);"><strong style="color:white;">Habitantes tiene Timaukel,</strong> la comuna que organiza la carrera: 12.850 km² de superficie —más grande que varias provincias argentinas— con capital en Villa Cameron, a orillas de la Bahía Inútil.</div>'
        "</div>\n\n"
        "<h3>Dónde queda Timaukel</h3>\n\n"
        "Timaukel es una de las comunas más extensas y menos pobladas de Chile: ocupa el sur de la Isla Grande de Tierra del Fuego, sobre la Bahía Inútil. Su capital administrativa es Villa Cameron, aunque el municipio ya tiene aprobado el traslado a Pampa Guanaco —a 100 km, y el punto de largada de la carrera— para aprovechar mejor su ubicación turística. Timaukel no tiene la infraestructura de Punta Arenas o Puerto Natales —tiene, en cambio, bosque subantártico, turberas y una población de guanacos, cóndores y zorros que casi no se cruza con nadie.\n\n"
        '<img src="../fotos/foto-20260805-timaukel-lanza-el-primer-guanaco-trail-running-en-dep.webp" alt="Costa de Tierra del Fuego, en la comuna de Timaukel" style="width:100%;border-radius:6px;margin:8px 0 4px;display:block;"/>\n\n'
        '<p class="ski-nota">La comuna de Timaukel, sobre la Bahía Inútil.</p>\n\n'
        "Se puede llegar por varios lados. Desde Chile, la vía más directa es por Porvenir, unos 150 km todo por tierra; desde Punta Arenas hay que cruzar el Estrecho de Magallanes en balsa por Primera Angostura (~25 minutos) y sumar otros 337 km de ruta. Desde Argentina la opción es más corta: por Río Grande, unos 80 km hasta el paso fronterizo Bellavista —abierto de 8 a 22 h, solo en temporada— y 12 km más hasta Pampa Guanaco, sin cruces de por medio.\n\n"
        "<h3>Una fiesta detrás de la carrera</h3>\n\n"
        "El Guanaco Trail Running no nace suelto: es la pieza deportiva de una apuesta turística más grande. La comuna presentó en septiembre de 2025 su temporada <strong>\"Tierra del Fuego Indómita\"</strong> en Punta Arenas, con la Tercera Fiesta del Guanaco como atracción central y la presencia del gobernador de Magallanes, Jorge Flies. El alcalde de Timaukel, <strong>Luis Barría Andrade</strong>, viene impulsando ese posicionamiento: la carrera busca consolidar a la comuna como destino de turismo deportivo ligado a la naturaleza.\n\n"
        "<h3>Tierra del Fuego ya tenía vocación extrema</h3>\n\n"
        "La apuesta de Timaukel no llega al vacío. Unos meses antes, en diciembre de 2025, la isla fue escenario de la tercera edición del Karukinka Gravel Race, la carrera de gravel por etapas más austral del mundo: 440 km en cuatro jornadas por la ruta Vicuña–Yendegaia, con apenas 40 cupos disponibles. Entre el gravel de resistencia y el trail running masivo, Tierra del Fuego empieza a construirse un calendario propio de deporte-aventura, en las antípodas del esquí de Bariloche o el trekking de El Chaltén.\n\n"
        "Lo que todavía no está confirmado es el detalle fino: la Municipalidad de Timaukel no publicó aún el link de inscripción, el valor de la entrada ni la premiación de cada categoría, algo esperable a casi año y medio de la largada. Quienes quieran anotarse o hacer seguimiento pueden hacerlo por los canales oficiales de la comuna —<a href=\"https://munitimaukel.cl/\" target=\"_blank\" rel=\"noopener\">munitimaukel.cl</a> y la cuenta de Instagram <a href=\"https://www.instagram.com/municipalidad.de.timaukel/\" target=\"_blank\" rel=\"noopener\">@municipalidad.de.timaukel</a>—, donde el municipio suele anunciar sus novedades. Para una comuna de 423 habitantes, sumar 300 corredores en un solo fin de semana no es un detalle menor —es, directamente, el evento más grande de su calendario."
    ),
    "tag": "🏃 Deportes",
    "categoria": "deportes",
    "fuente": "OvejeroNoticias y Municipalidad de Timaukel",
    "pais": "chile",
    "imagen": "fotos/foto-20260815-guanaco-trail-running-fecha-categorias-y-circuito-dep.webp",
    "imagen_keywords": "trail running tierra del fuego guanaco patagonia",
    "url_original": "https://www.ovejeronoticias.cl/2026/08/timaukel-apuesta-por-el-turismo-deportivo-con-el-lanzamiento-del-primer-el-guanaco-trail-running/",
    "meta": "Hoy · GLOBALpatagonia",
    "excluir_feed": True,
}


def publicar():
    print("\n" + "=" * 55)
    print("  Publicación Deportes — Guanaco Trail Running")
    print("=" * 55)

    print(f"  Título ({len(deportes['titulo'])} chars): {deportes['titulo']}")

    # Historial
    historial = A.cargar_historial()
    historial = [deportes] + historial
    A.guardar_historial(historial)
    A._persistir_urls_nuevas([deportes])
    print(f"  Agregada a historial ({len(historial)} entradas)")

    # Rotar deportes_feed.json
    A.rotar_deportes(deportes)

    # Página estática SEO
    print("  Generando página estática...")
    todas = []
    for src in ("historial.json", "propios.json", "propios_historial.json",
                "historias.json", "noticias.json", "turismo.json",
                "deportes_feed.json", "negocios.json", "cultura.json", "guias.json"):
        todas += A._notas_de_fuente(os.path.join(BASE, src))
    todas_filtradas = [n for n in todas if isinstance(n, dict) and n.get("id")]
    A.generar_paginas_og(todas_filtradas)

    print("  Actualizando índice de búsqueda...")
    A.actualizar_search_index()

    print("  Actualizando sitemap...")
    A.actualizar_sitemap()

    print(f"\n  OK — {A.fecha_display()}")
    print("=" * 55 + "\n")


def actualizar():
    """Corrige la nota ya publicada (foto, tabla, mapa) SIN volver a rotar
    deportes_feed.json — solo parchea el objeto existente in-place."""
    print("\n" + "=" * 55)
    print("  Actualizando nota ya publicada")
    print("=" * 55)

    nid = deportes["id"]

    # historial.json — reemplazar la entrada existente por la corregida
    historial = A.cargar_historial()
    reemplazado = False
    for i, n in enumerate(historial):
        if n.get("id") == nid:
            historial[i] = deportes
            reemplazado = True
            break
    if not reemplazado:
        print("  ADVERTENCIA: no se encontró la nota en historial.json")
    else:
        with open(os.path.join(BASE, "historial.json"), "w", encoding="utf-8") as f:
            json.dump(historial, f, ensure_ascii=False, indent=2)
        print("  historial.json parcheado")

    # deportes_feed.json — parchear imagen (y resto de campos de card) donde esté
    ruta_feed = os.path.join(BASE, "deportes_feed.json")
    with open(ruta_feed, encoding="utf-8") as f:
        feed = json.load(f)

    def to_card(art):
        return {
            "id": art.get("id", ""), "tag": art.get("tag", "🏃 Deportes"),
            "titulo": art.get("titulo", ""), "bajada": art.get("bajada", ""),
            "imagen": art.get("imagen", ""), "meta": art.get("meta", ""),
        }

    parcheado_feed = False
    if feed.get("principal", {}).get("id") == nid:
        feed["principal"] = to_card(deportes)
        parcheado_feed = True
    feed["secundarias"] = [to_card(deportes) if c.get("id") == nid else c for c in feed.get("secundarias", [])]
    feed["row_cards"] = [to_card(deportes) if c.get("id") == nid else c for c in feed.get("row_cards", [])]
    with open(ruta_feed, "w", encoding="utf-8") as f:
        json.dump(feed, f, ensure_ascii=False, indent=2)
    print(f"  deportes_feed.json parcheado (principal={parcheado_feed})")

    # Borrar la página estática vieja para que generar_paginas_og la regenere
    ruta_pagina = os.path.join(BASE, "notas", f"{nid}.html")
    if os.path.exists(ruta_pagina):
        os.remove(ruta_pagina)
        print("  Página estática vieja eliminada, regenerando...")

    todas = []
    for src in ("historial.json", "propios.json", "propios_historial.json",
                "historias.json", "noticias.json", "turismo.json",
                "deportes_feed.json", "negocios.json", "cultura.json", "guias.json"):
        todas += A._notas_de_fuente(os.path.join(BASE, src))
    todas_filtradas = [n for n in todas if isinstance(n, dict) and n.get("id")]
    A.generar_paginas_og(todas_filtradas)

    print("  Actualizando índice de búsqueda...")
    A.actualizar_search_index()

    print(f"\n  OK — {A.fecha_display()}")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "publicar"
    if modo == "actualizar":
        actualizar()
    else:
        publicar()
