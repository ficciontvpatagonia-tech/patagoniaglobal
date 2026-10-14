#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Turismo manual — 01/07/2026
Primera gran nevada del invierno + inicio temporada 2026.
"""
import os, sys, json
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import actualizar_noticias as A

BORRADOR = os.path.join(BASE, "_scripts", "_borrador_manual.json")
HOY_SLUG = datetime.now().strftime("%Y%m%d")

turismo = {
    "id": f"{HOY_SLUG}-primera-gran-nevada-temporada-nieve-patagonia-tur",
    "titulo": "Arrancó la temporada de nieve: estado de los centros de esquí patagónicos",
    "bajada": "Con la primera gran nevada del invierno y varios centros ya operativos, el mapa de la nieve patagónica empieza a tomar forma. Acá el estado real de cada cerro al 1° de julio de 2026.",
    "cuerpo": (
        "La Patagonia entró en ritmo de invierno. La nevada que cayó en las últimas horas sobre las cumbres de la cordillera suma centímetros a los centros de esquí que ya arrancaron la temporada, y pone en marcha a los que están por abrir. Repasamos el estado real de cada cerro.\n\n"
        '<div style="background:#1c2d3d;color:white;border-radius:6px;padding:20px 24px;margin:32px 0;display:flex;align-items:center;gap:20px;">'
        '<div style="font-family:\'Playfair Display\',serif;font-size:52px;font-weight:900;color:#8ab8d4;line-height:1;flex-shrink:0;">−7°</div>'
        '<div style="font-size:14px;line-height:1.6;color:rgba(255,255,255,0.85);"><strong style="color:white;">Temperatura en cumbre hoy.</strong> La nevada llega con frío seco y viento moderado desde el oeste. Las condiciones son las mejores para fabricar nieve artificial y consolidar la natural. El pronóstico anticipa nuevas precipitaciones entre el miércoles y el jueves.</div>'
        "</div>\n\n"
        "<h3>Cerro Catedral — Bariloche</h3>\n\n"
        '<div class="ski-centro-card">'
        '<img class="ski-centro-img" src="../fotos/DEPORTES/CENTROS_SKY/catedral-moderno-1.webp" alt="Cerro Catedral" onerror="this.src=\'../fotos/DEPORTES/CENTROS_SKY/CATEDRAL.webp\'"/>'
        '<div class="ski-centro-body">'
        '<div><span style="display:inline-block;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:3px 10px;border-radius:20px;background:#fff3cd;color:#856404;">⚠ Abierto — solo peatones</span></div>'
        '<div class="ski-centro-nombre">Cerro Catedral</div>'
        '<div class="ski-stats-row">'
        '<div class="ski-stat"><span class="ski-stat-label">Nieve cima</span><span class="ski-stat-val">~36 cm</span></div>'
        '<div class="ski-stat"><span class="ski-stat-label">Temp. cima</span><span class="ski-stat-val">−7°C</span></div>'
        '<div class="ski-stat"><span class="ski-stat-label">Pistas ski</span><span class="ski-stat-val">Sin abrir</span></div>'
        '<div class="ski-stat"><span class="ski-stat-label">Remontes</span><span class="ski-stat-val">Sin abrir</span></div>'
        "</div>"
        '<p class="ski-centro-desc">El más grande de Sudamérica (120 km de pistas) abrió el 29 de junio para peatones. Las pistas aún no están en condiciones óptimas de seguridad para el esquí. La nevada de hoy suma los centímetros clave. Por contrato debe garantizar 90 días de temporada desde el 1° de julio.</p>'
        '<a href="https://catedralaltapatagonia.com/parte-de-nieve/" target="_blank" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:#3a5a7a;text-decoration:none;margin-top:2px;">📋 Ver parte diario oficial →</a>'
        "</div></div>\n\n"
        '<p style="font-size:11px;color:#999;margin-top:6px;font-style:italic;">Novedad 2026: nuevo sector Playpark para principiantes. Pase diario desde $160.000 (3 cuotas sin interés hasta fin de mes).</p>\n\n'
        "<h3>Chapelco — San Martín de los Andes</h3>\n\n"
        '<div class="ski-centro-card">'
        '<img class="ski-centro-img" src="../fotos/DEPORTES/CENTROS_SKY/CHAPELCO.webp" alt="Chapelco" onerror="this.style.background=\'#1c2d3d\'"/>'
        '<div class="ski-centro-body">'
        '<div><span style="display:inline-block;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:3px 10px;border-radius:20px;background:#dce8f7;color:#1a4a7a;">🔵 Próxima apertura</span></div>'
        '<div class="ski-centro-nombre">Chapelco</div>'
        '<div class="ski-stats-row">'
        '<div class="ski-stat"><span class="ski-stat-label">Nieve cima</span><span class="ski-stat-val">30 cm</span></div>'
        '<div class="ski-stat"><span class="ski-stat-label">Nieve base</span><span class="ski-stat-val">10 cm</span></div>'
        '<div class="ski-stat"><span class="ski-stat-label">Temp. cima</span><span class="ski-stat-val">−12°C</span></div>'
        '<div class="ski-stat"><span class="ski-stat-label">Pistas</span><span class="ski-stat-val">24 km</span></div>'
        "</div>"
        '<p class="ski-centro-desc">La mejor base de nieve de los grandes centros patagónicos: 30 cm en cumbre y 10 en base. Prepara la apertura con una novedad importante: un telecabine nuevo que triplicará la capacidad de acceso a la montaña.</p>'
        '<a href="https://www.chapelco.com/" target="_blank" style="display:inline-flex;align-items:center;gap:5px;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:#3a5a7a;text-decoration:none;margin-top:2px;">📋 Ver parte diario oficial →</a>'
        "</div></div>\n\n"
        '<p style="font-size:11px;color:#999;margin-top:6px;margin-bottom:16px;font-style:italic;">Pronóstico Chapelco — próximos días: 3 cm miércoles noche, 2 cm jueves. Fuente: snow-forecast.com</p>\n\n'
        "<h3>Caviahue, Cerro Bayo y Batea Mahuida</h3>\n\n"
        '<table class="ski-table"><thead><tr><th>Centro</th><th>Estado</th><th>Apertura</th><th>Nieve cima</th><th>Próx. nevada</th></tr></thead><tbody>'
        '<tr><td><strong>Caviahue</strong><br><span style="font-size:11px;color:#999">Neuquén</span></td>'
        '<td><span style="display:inline-block;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:3px 10px;border-radius:20px;background:#d4f0dc;color:#1a6b35;">✓ Abierto</span></td>'
        "<td>27 jun</td><td>—</td><td><strong>6 cm</strong> mié noche</td></tr>"
        '<tr><td><strong>Cerro Bayo</strong><br><span style="font-size:11px;color:#999">Villa La Angostura</span></td>'
        '<td><span style="display:inline-block;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:3px 10px;border-radius:20px;background:#d4f0dc;color:#1a6b35;">✓ Abierto</span></td>'
        "<td>Jun 2026</td><td>—</td><td>—</td></tr>"
        '<tr><td><strong>Batea Mahuida</strong><br><span style="font-size:11px;color:#999">Villa Pehuenia</span></td>'
        '<td><span style="display:inline-block;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:3px 10px;border-radius:20px;background:#d4f0dc;color:#1a6b35;">✓ Abre hoy</span></td>'
        "<td>1° jul</td><td>—</td><td>—</td></tr>"
        '<tr><td><strong>Cerro Castor</strong><br><span style="font-size:11px;color:#999">Ushuaia</span></td>'
        '<td><span style="display:inline-block;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:3px 10px;border-radius:20px;background:#dce8f7;color:#1a4a7a;">🔵 Próximo</span></td>'
        "<td>Jul 2026</td><td>—</td><td>—</td></tr>"
        "</tbody></table>\n\n"
        '<p style="font-size:11px;color:#999;margin-top:6px;font-style:italic;">Batea Mahuida es el único parque de nieve de gestión mapuche de Argentina.</p>\n\n'
        "<h3>¿Qué esperar en julio?</h3>\n\n"
        "Julio es el mes bisagra de la temporada patagónica: las vacaciones de invierno traen el pico de turistas y suelen coincidir con las mejores condiciones de nieve. La nevada de esta semana es una señal positiva, aunque el pronóstico de corto plazo es mayormente seco. El dato alentador es Caviahue, con 6 cm previstos para el miércoles a la noche, y Chapelco, que con 30 cm en cumbre tiene la mejor base de la región.\n\n"
        "Para Catedral —el termómetro del turismo invernal patagónico— el calendario del contrato presiona: la temporada de 90 días empieza a correr desde hoy y la habilitación del esquí depende de que las pistas alcancen condiciones de seguridad. La nevada de las últimas horas es exactamente lo que el cerro necesitaba."
    ),
    "tag": "🏔 Turismo",
    "categoria": "turismo",
    "fuente": "Diario Río Negro",
    "pais": "argentina",
    "imagen": "fotos/DEPORTES/CENTROS_SKY/catedral-nieve.webp",
    "imagen_keywords": "cerro catedral nieve temporada esqui patagonia",
    "url_original": "https://www.rionegro.com.ar/sociedad/el-cerro-catedral-recibio-hasta-36-centimetros-de-nieve-y-crece-la-expectativa-por-la-temporada-4619021/",
    "meta": f"Hoy · GLOBALpatagonia",
    "excluir_feed": True,
}


def resolver():
    print("\n" + "=" * 55)
    print("  ETAPA 1 — Resolución de imagen")
    print("=" * 55)
    fotos_propias = A.fotos_propias_disponibles()
    fotos_usadas = set()
    turismo["imagen"] = A.resolver_imagen(turismo, fotos_propias, fotos_usadas)
    print(f"  Imagen resuelta: {turismo['imagen']}")
    with open(BORRADOR, "w", encoding="utf-8") as f:
        json.dump({"turismo": turismo}, f, ensure_ascii=False, indent=2)
    print(f"  Borrador guardado en {BORRADOR}")
    print("  Revisá la imagen y luego corré:  python3 _scripts/publicar_turismo_nevada.py publicar")
    print("=" * 55 + "\n")


def publicar():
    print("\n" + "=" * 55)
    print("  ETAPA 2 — Publicación turismo")
    print("=" * 55)

    with open(BORRADOR, encoding="utf-8") as f:
        b = json.load(f)
    nota = b["turismo"]
    nota["excluir_feed"] = True

    # Historial
    historial = A.cargar_historial()
    historial = [nota] + historial
    A.guardar_historial(historial)
    A._persistir_urls_nuevas([nota])
    print(f"  Agregada a historial ({len(historial)} entradas)")

    # Rotar turismo.json
    A.rotar_turismo(nota)

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

    print(f"\n  ✓ Listo — {A.fecha_display()}")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "imagenes"
    if modo in ("imagenes", "resolver"):
        resolver()
    elif modo == "publicar":
        publicar()
    else:
        print("Uso: python3 _scripts/publicar_turismo_nevada.py [imagenes|publicar]")
