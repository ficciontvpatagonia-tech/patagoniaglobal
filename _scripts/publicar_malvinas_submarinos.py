#!/usr/bin/env python3
"""Publica el INFORME 'Reino Unido sin submarinos de ataque' en propios.json,
genera su página estática indexable y actualiza el sitemap.
Sigue el patrón de publicar_puente_chacao.py."""
import json, os, shutil, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
from actualizar_noticias import generar_paginas_og, actualizar_sitemap, _notas_de_fuente

PROPIOS = f"{BASE}/propios.json"
HISTORIAL = f"{BASE}/propios_historial.json"
MAX_ACTIVOS = 7

NID = "20260609-propio-malvinas-submarinos"

# ---- 1. Copiar fotos al repo ----
COPIAS = [
    ("/Users/jm/Desktop/_94253524_mediaitem94253523.jpg", f"{BASE}/fotos/submarino-astute-royal-navy.jpg"),
    ("/Users/jm/Desktop/ARA-GENERAL-BELGRANO_11zon.webp", f"{BASE}/fotos/ara-general-belgrano-1982.webp"),
]
for src, dst in COPIAS:
    if not os.path.exists(dst):
        shutil.copy2(src, dst)
        print(f"Foto copiada: {os.path.basename(dst)}")
    else:
        print(f"Ya existía: {os.path.basename(dst)}")

# ---- 2. Cuerpo (HTML crudo, sin figura inline; la figura del Belgrano se
#         inserta a mano en la estática y va en galeria para el visor) ----
cuerpo = (
    "<p>No es una especulación ni un rumor de redes sociales. La información fue revelada por <strong>The Mail on Sunday</strong> y replicada por The Telegraph, LBC y Daily Mail: por primera vez, la flota de submarinos de ataque de la Royal Navy —los cazadores nucleares clase Astute— se encuentra completamente inmovilizada en puerto.</p>\n\n"
    "<h3>Toda la flota de ataque, atracada</h3>\n\n"
    "<p>Los <strong>cinco submarinos operativos</strong> de la clase —HMS Astute, Ambush, Artful, Audacious y Anson— están amarrados, sometidos a mantenimiento y reparaciones. Un sexto, el HMS Agamemnon, fue incorporado a fines de 2025 pero sigue en pruebas de mar, y el séptimo, el HMS Achilles, todavía se construye en Barrow-in-Furness. El resultado es inédito: el Reino Unido no tiene hoy ningún submarino de ataque disponible para desplegar.</p>\n\n"
    "<p>La causa, según ex altos mandos británicos, es estructural: años de recortes presupuestarios, falta de diques secos y una crisis de personal especializado. El ship-lift de la base de Faslane lleva más de un año inoperante y las obras en Devonport reducen cuántas unidades pueden repararse a la vez. <strong>Lord West</strong>, ex jefe de la Royal Navy, calificó la situación de \"inaceptable\" y \"muy preocupante\". El ex comandante de submarino Ryan Ramsey fue más crudo ante The Telegraph: el Reino Unido, dijo, \"luce desdentado\".</p>\n\n"
    "<p>Cada uno de estos cazadores desplaza 7.400 toneladas, mide 97 metros, navega impulsado por un reactor nuclear Rolls-Royce y carga torpedos pesados Spearfish y misiles de crucero Tomahawk. En teoría, es una de las armas más sofisticadas del arsenal británico. Hoy, ninguna está en condiciones de hacerse a la mar.</p>\n\n"
    "<h3>Un vacío estratégico en el Atlántico Sur</h3>\n\n"
    "<p>En 1982, el HMS Conqueror —un submarino nuclear británico— hundió al crucero <strong>ARA General Belgrano</strong> y forzó a toda la flota argentina a replegarse a puerto por el resto de la guerra. Aquel episodio convirtió a la amenaza submarina en la carta más temida del Reino Unido para sostener el control militar del archipiélago.</p>\n\n"
    "<p>Cuatro décadas después, el tablero se invirtió. No hay un solo submarino de ataque británico en condiciones de patrullar el Atlántico Sur. Los lanzamisiles Trident de la clase Vanguard siguen operativos, pero quedaron sin la escolta que esos cazadores les proporcionaban. La misma desprotección alcanza a la base aérea de Monte Agradable (Mount Pleasant) y a las aguas que rodean las Islas Malvinas.</p>\n\n"
    "<p>La pregunta surge sola: si Londres no puede siquiera desplegar sus principales activos navales de combate, ¿con qué sostiene su discurso de \"defensa inquebrantable\" del territorio que ocupa?</p>\n\n"
    "<h3>Una crisis anunciada</h3>\n\n"
    "<p>El problema no es un hecho aislado. Décadas de recortes, una industria naval en decadencia y la falta de tripulantes calificados arrastraron a la Royal Navy a su peor momento operativo en mucho tiempo. Ya en enero de 2026 había trascendido que solo <strong>tres de sus seis destructores</strong> Type 45 estaban en servicio.</p>\n\n"
    "<p>El Ministerio de Defensa se limitó a señalar que \"se está trabajando en un plan de recuperación del mantenimiento\". El First Sea Lord, almirante Sir Gwyn Jenkins, lo lanzó el <strong>15 de enero de 2026</strong> con una meta modesta: devolver al menos tres Astute a alta disponibilidad antes de fin de año. No ofreció plazos ni garantías sobre cuándo volverá a flote la flota completa.</p>\n\n"
    "<h3>Qué significa para el reclamo argentino</h3>\n\n"
    "<p>Conviene ser claro: desde la perspectiva argentina, esto no abre ninguna oportunidad militar. Ningún análisis serio sostiene que el país tenga hoy la capacidad logística, naval o aérea para una reconquista armada, y esa tampoco es la política de Estado que impulsa la diplomacia nacional.</p>\n\n"
    "<p>El verdadero impacto es político y simbólico. Durante décadas, el Reino Unido justificó su negativa a negociar con el argumento de que las islas estaban protegidas por una fuerza \"moderna y creíble\". Ese relato se resquebraja cuando todos sus submarinos de combate están fuera de servicio al mismo tiempo. En los foros internacionales donde se discute la Cuestión Malvinas queda expuesta una contradicción incómoda: Londres exige respeto por la autodeterminación de los kelpers, pero no puede garantizar la defensa efectiva del territorio que administra.</p>\n\n"
    "<h3>Conclusión</h3>\n\n"
    "<p>El dato es verificable y sus consecuencias, concretas: la Royal Navy atraviesa una etapa en la que su brazo submarino —su herramienta de proyección más temida— simplemente no está disponible.</p>\n\n"
    "<p>Para el reclamo argentino de soberanía, no es una invitación a la aventura militar, sino una confirmación de que el poder británico tiene límites y grietas. La diplomacia nacional cuenta ahora con un hecho objetivo para cuestionar la supuesta \"garantía de defensa\" que Londres esgrime cada vez que se niega a sentarse a negociar.</p>\n\n"
    "<p>Desde la Patagonia, atentos a una crisis que desnuda las debilidades de una potencia que alguna vez dominó todos los mares.</p>\n\n"
    "<p style=\"font-size:13px;color:#888;font-style:italic;margin-top:32px\">Informe elaborado con información de The Mail on Sunday, The Telegraph, LBC y declaraciones de ex autoridades de la Royal Navy. Junio de 2026.</p>"
)

nueva_entrada = {
    "id": NID,
    "titulo": "Reino Unido sin submarinos de ataque: sin defensa ni disuasión en Malvinas",
    "bajada": "Por primera vez en décadas, toda la flota de cazadores nucleares clase Astute de la Royal Navy está atracada por fallas de mantenimiento. Sin su principal arma de combate en el Atlántico Sur, Londres ya no puede sostener con credibilidad su discurso de \"defensa inquebrantable\" del archipiélago ocupado. Desde la Patagonia, una grieta que la diplomacia argentina tiene derecho a señalar.",
    "cuerpo": cuerpo,
    "tag": "🗺️ Soberanía",
    "categoria": "soberania|malvinas|geopolitica",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "argentina",
    "fecha": "2026-06-09",
    "imagen": "fotos/submarino-astute-royal-navy.jpg",
    "imagen_keywords": "royal navy submarino nuclear astute malvinas atlántico sur defensa",
    "meta": "9 de Junio de 2026 · J. Martineau",
    "excluir_feed": True,
    "galeria": ["fotos/ara-general-belgrano-1982.webp"],
}

# ---- 3. Rotación propios.json ----
with open(PROPIOS, encoding="utf-8") as f:
    propios = json.load(f)
with open(HISTORIAL, encoding="utf-8") as f:
    historial = json.load(f)

if any(p.get("id") == NID for p in propios):
    print("Ya estaba en propios.json — no se duplica.")
else:
    if len(propios) >= MAX_ACTIVOS:
        mas_antiguo = propios.pop()
        historial.insert(0, mas_antiguo)
        print(f"Movido al historial: {mas_antiguo['id']}")
    propios.insert(0, nueva_entrada)
    with open(PROPIOS, "w", encoding="utf-8") as f:
        json.dump(propios, f, ensure_ascii=False, indent=2)
    with open(HISTORIAL, "w", encoding="utf-8") as f:
        json.dump(historial, f, ensure_ascii=False, indent=2)
    print(f"Nuevo informe en propios[0]: {NID} — total activos: {len(propios)}")

# ---- 4. Página estática (pool completo para 'También te puede interesar') ----
pool = list(nueva_entrada and [nueva_entrada])
for fuente in ("historial.json", "propios.json", "propios_historial.json",
               "historias.json", "noticias.json", "turismo.json",
               "deportes_feed.json", "negocios.json", "cultura.json", "guias.json"):
    pool += _notas_de_fuente(os.path.join(BASE, fuente))
pool = [n for n in pool if isinstance(n, dict) and n.get("id")]
generar_paginas_og(pool)

# ---- 5. Sitemap ----
actualizar_sitemap()
print("OK — propios.json, página estática y sitemap actualizados.")
