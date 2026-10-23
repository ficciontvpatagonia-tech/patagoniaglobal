#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nota de sección ECONOMÍA — Neuquén récord de petróleo (septiembre 2026).
Fuente: Diario Río Negro (22/10/2026). Reescrita en voz GP.
Dos etapas, como publicar_manual.py:
  python3 _scripts/publicar_vaca_muerta_record.py imagenes   # resuelve foto, guarda borrador
  python3 _scripts/publicar_vaca_muerta_record.py publicar   # historial + negocios + SEO (una sola vez)
NO toca la tapa ni noticias.json. NO publica en redes.
"""
import os
import re
import sys
import json
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import actualizar_noticias as A

BORRADOR = os.path.join(BASE, "_scripts", "_borrador_vaca_muerta_record.json")
HOY_SLUG = datetime.now().strftime("%Y%m%d")

nota = {
    "titulo": "Neuquén rompió su propio récord: 714.000 barriles de petróleo por día",
    "bajada": "En septiembre la provincia sumó casi 29.000 barriles diarios respecto de agosto y marcó un nuevo máximo histórico, impulsada casi por completo por Vaca Muerta. El gas, en cambio, retrocedió por la menor demanda posterior al invierno.",
    "cuerpo": (
        "Neuquén volvió a superarse. Según los datos de la subsecretaría de Hidrocarburos provincial, en septiembre "
        "la provincia produjo en promedio 714.089 barriles de petróleo por día, el nivel más alto de su historia. "
        "Son 28.773 barriles más que en agosto (685.316), un avance del 4,2% en un solo mes, y un 25,95% más que en "
        "septiembre de 2025. En lo que va del año, de enero a septiembre, la producción acumula un 29,83% de "
        "crecimiento interanual.\n\n"
        "La explicación tiene nombre propio: Vaca Muerta. El petróleo no convencional aportó 697.595 barriles "
        "diarios, el 97,69% de todo lo que se extrae en la provincia. El salto mensual se apoyó en un puñado de "
        "áreas: Bandurria Sur (+8.654 barriles diarios), Rincón de Aranda (+5.990), La Angostura Sur I (+4.913), "
        "Bajada del Palo Oeste (+4.347), El Trapial Este (+3.692) y Loma Jarillosa Este (+2.309).\n\n"
        "El dato llega después de un agosto de récords simultáneos para Vaca Muerta, Neuquén y el país, que alcanzó "
        "por primera vez los 926.925 barriles diarios. La meta de llegar al millón de barriles por día antes de fin "
        "de año sigue sobre la mesa. Neuquén concentra cerca del 75% del petróleo y del gas que produce la "
        "Argentina.\n\n"
        "El gas, a contramano. La producción de septiembre fue de 104,76 millones de metros cúbicos diarios, un "
        "9,28% menos que los 115,47 millones de agosto. Las bajas se concentraron en Fortín de Piedra, Sierra Chata, "
        "La Calera, Aguada Pichana Este, El Mangrullo y Aguada Pichana Oeste. La provincia atribuye la caída sobre "
        "todo a factores estacionales: con el fin del invierno baja el consumo residencial. Frente a septiembre de "
        "2025 el gas igual crece 9,46%, y el acumulado del año suma 6,09%. El no convencional representa el 91,36% "
        "del total (95,71 millones de m³ diarios, de los cuales 85,97 son shale gas y 9,75 tight gas).\n\n"
        "Las cifras se difundieron en el marco de AOG Patagonia 2026, la gran feria de la industria energética de "
        "la región."
    ),
    "tag": "💼 Economía",
    "categoria": "economia",
    "fuente": "Diario Río Negro",
    "url_original": "https://www.rionegro.com.ar/energia/vaca-muerta-llevo-a-neuquen-a-un-nuevo-record-historico-supero-los-714-000-barriles-diarios-de-petroleo-4768076/",
    "pais": "argentina",
    "imagen": None,
    "imagen_keywords": "vaca muerta petroleo neuquen",
}
nota["id"] = f"{HOY_SLUG}-{A.slugify(nota['titulo'])}-neg"


def resolver():
    nota["tag"] = re.sub(r"medio ambiente", "Ambiente", nota["tag"], flags=re.IGNORECASE)
    fotos_propias = A.fotos_propias_disponibles()
    nota["imagen"] = A.resolver_imagen(nota, fotos_propias, set())
    nota["meta"] = f"Hoy · {nota['fuente']}"
    with open(BORRADOR, "w", encoding="utf-8") as f:
        json.dump(nota, f, ensure_ascii=False, indent=2)
    print(f"\n  Imagen: {nota['imagen']}\n  Borrador: {BORRADOR}")


def publicar():
    with open(BORRADOR, encoding="utf-8") as f:
        n = json.load(f)
    n["excluir_feed"] = True
    historial = A.cargar_historial()
    A.guardar_historial([n] + historial)
    A._persistir_urls_nuevas([n])
    A.rotar_negocios(n)

    notas_og = [n]
    for fuente in ("historial.json", "propios.json", "propios_historial.json", "historias.json",
                   "noticias.json", "turismo.json", "deportes_feed.json", "negocios.json",
                   "cultura.json", "guias.json"):
        notas_og += A._notas_de_fuente(os.path.join(BASE, fuente))
    notas_og = [x for x in notas_og if isinstance(x, dict) and x.get("id")]
    A.generar_paginas_og(notas_og)
    A.actualizar_search_index()
    A.actualizar_archivo_en_index(notas_og)
    A.generar_paginas_temas(notas_og)
    A.generar_feed_rss()
    A.actualizar_sitemap()
    print(f"\n  ✓ Publicada localmente: {n['id']}")


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "imagenes"
    resolver() if modo in ("imagenes", "resolver") else publicar() if modo == "publicar" else print("imagenes|publicar")
