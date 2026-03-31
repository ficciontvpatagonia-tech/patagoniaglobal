#!/usr/bin/env python3
"""
PatagoniaGLOBAL — Actualizador de Noticias
Obtiene noticias de fuentes RSS, filtra las patagónicas y las reescribe con Claude.
Acumula artículos en historial.json (1-3 nuevos por corrida).
Genera noticias.json que el sitio web carga automáticamente.

Uso:
    python3 actualizar_noticias.py
"""

import json
import sys
import os
import random
import urllib.request
import urllib.parse
from datetime import datetime

import feedparser
import anthropic

# ══════════════════════════════════════════════════════════
#  CONFIGURACIÓN
# ══════════════════════════════════════════════════════════

# Carga las claves desde el archivo .env si existe
_env_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(_env_path):
    with open(_env_path) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _v = _line.split("=", 1)
                os.environ.setdefault(_k.strip(), _v.strip())

API_KEY          = os.environ.get("ANTHROPIC_API_KEY", "")
UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY", "")

FUENTES_RSS = [
    # ── Argentina · Regionales ──
    {"nombre": "Diario Río Negro",        "url": "https://www.rionegro.com.ar/feed/",                    "region": "Río Negro"},
    {"nombre": "La Opinión Austral",      "url": "https://laopinionaustral.com.ar/feed/",                "region": "Santa Cruz"},
    {"nombre": "El Patagónico",           "url": "https://www.elpatagonico.com/rss/portada.xml",         "region": "Chubut"},
    {"nombre": "Jornada Patagonia",       "url": "https://www.diariojornada.com.ar/rss/",                "region": "Chubut"},
    {"nombre": "ADN Sur",                 "url": "https://www.adnsur.com.ar/feed/",                      "region": "Patagonia"},
    {"nombre": "El Cordillerano",         "url": "https://www.elcordillerano.com.ar/rss/home.xml",       "region": "Río Negro"},
    {"nombre": "Bariloche2000",           "url": "https://www.bariloche2000.com/feed/",                  "region": "Bariloche"},
    {"nombre": "InfoFueguina",            "url": "https://www.infofueguina.com/rss",                     "region": "Tierra del Fuego"},
    {"nombre": "Neuquén Informa",         "url": "https://www.neuqueninforma.gob.ar/feed/",              "region": "Neuquén"},
    {"nombre": "LMNeuquén",              "url": "https://www.lmneuquen.com/rss/",                       "region": "Neuquén"},
    # ── Argentina · Nacional ──
    {"nombre": "La Nación",               "url": "https://www.lanacion.com.ar/arc/outboundfeeds/rss/",   "region": "Nacional"},
    {"nombre": "Infobae",                 "url": "https://www.infobae.com/feeds/rss/",                   "region": "Nacional"},
    {"nombre": "Clarín",                  "url": "https://www.clarin.com/rss/lo-ultimo/",                "region": "Nacional"},
    # ── Chile · Regionales ──
    {"nombre": "La Prensa Austral",       "url": "https://laprensaaustral.cl/feed/",                     "region": "Magallanes"},
    {"nombre": "El Divisadero",           "url": "https://www.eldivisadero.cl/feed/",                    "region": "Aysén"},
    {"nombre": "El Llanquihue",           "url": "https://www.elllanquihue.cl/feed/",                    "region": "Los Lagos"},
    {"nombre": "El Pingüino",             "url": "https://www.elpinguino.com/feed/",                     "region": "Magallanes"},
    {"nombre": "Diario de Valdivia",      "url": "https://www.diariodevaldivia.cl/feed/",                "region": "Los Ríos"},
]

PALABRAS_CLAVE = [
    # Provincias y regiones
    "patagonia", "neuquén", "neuquen", "río negro", "rio negro", "chubut",
    "santa cruz", "tierra del fuego",
    # Ciudades Argentina
    "bariloche", "ushuaia", "calafate", "chaltén", "chalten", "comodoro",
    "madryn", "trelew", "esquel", "zapala", "viedma", "bolsón", "bolson",
    "san martín de los andes", "junín de los andes", "río gallegos",
    "cipolletti", "general roca", "villa la angostura", "puerto madryn",
    "río colorado", "neuquén capital", "las heras", "perito moreno",
    "puerto deseado", "caleta olivia", "pico truncado", "chos malal",
    "plottier", "piedra buena", "comandante piedra buena", "los antiguos",
    # Chile
    "magallanes", "punta arenas", "puerto natales", "torres del paine",
    "coyhaique", "aysén", "aysen", "puerto aysén", "puerto aysen",
    "puerto montt", "chiloé", "chiloe",
    "valdivia", "osorno", "pucón", "pucon", "villa o'higgins",
    "cochrane", "caleta tortel", "puerto williams", "cabo de hornos",
    # Medio ambiente — PRIORIDAD MÁXIMA
    "glaciar", "glaciares", "ley de glaciares", "periglacial",
    "minería", "minero", "sobrepesca", "pesca ilegal", "zona económica exclusiva",
    "incendio", "incendio forestal", "contaminación", "derrame",
    "parque nacional", "reserva natural", "área protegida",
    "huemul", "cóndor", "ballena", "lobo marino", "puma", "guanaco",
    "macá tobiano", "fauna patagónica", "especie invasora", "jabalí",
    "microplástico", "cambio climático", "recurso hídrico",
    # Pueblos Originarios
    "mapuche", "tehuelche", "aonikenk", "kawésqar", "kawesqar",
    "selknam", "ona", "yagán", "yagan", "pueblo originario",
    "comunidad indígena", "territorio ancestral",
    # Deportes patagónicos
    "fitz roy", "cerro torre", "nahuel huapi",
    "trail running", "ultra trail", "patagonia run", "ultra fiord",
    "final frontier", "canotaje", "kayak", "escalada", "andinismo",
    "esquí", "esqui", "snowboard", "ski", "cerro catedral",
    "expedición", "trekking", "mountain bike", "ciclismo de montaña",
    "canapino", "turismo carretera", "automovilismo", "rally",
    # Producción y economía regional
    "langostino", "merluza", "pesca artesanal", "golfo san jorge",
    "vaca muerta", "petróleo", "gas patagónico", "energía eólica",
    "frutilla", "cereza", "fruta fina", "vitivinicultura",
    "ganadería patagónica", "oveja", "lana", "carne de guanaco",
    "conicet", "paleontología", "dinosaurio", "hallazgo fósil",
    # Conectividad e infraestructura
    "ruta 3", "ruta 22", "ruta 40", "paso fronterizo",
    "aeropuerto", "vuelo", "aerolíneas", "lade", "jetsmart", "flybondi",
    "conectividad aérea", "puente patagónico",
    # Cultura e historia
    "historia patagónica", "pionero", "inmigrante patagónico",
    "fiesta regional", "festival", "artista patagónico",
    # Servicios cotidianos
    "clima", "alerta meteorológica", "viento", "nevada", "temporal",
]

MAX_HISTORIAL = 50   # artículos máximos a guardar
MAX_FEED      = 15   # artículos máximos a mostrar en el feed

# ══════════════════════════════════════════════════════════

DIAS_ES   = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
MESES_ES  = ["","Enero","Febrero","Marzo","Abril","Mayo","Junio",
             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]


def fecha_display():
    hoy = datetime.now()
    return f"{DIAS_ES[hoy.weekday()]}, {hoy.day} de {MESES_ES[hoy.month]} de {hoy.year}"


def es_patagonica(titulo, resumen):
    texto = (titulo + " " + resumen).lower()
    return any(kw in texto for kw in PALABRAS_CLAVE)


def obtener_imagen_rss(entry):
    if hasattr(entry, "media_content") and entry.media_content:
        for m in entry.media_content:
            if m.get("type", "").startswith("image"):
                return m.get("url")
    if hasattr(entry, "enclosures") and entry.enclosures:
        for enc in entry.enclosures:
            if enc.get("type", "").startswith("image"):
                return enc.get("href")
    if hasattr(entry, "media_thumbnail") and entry.media_thumbnail:
        return entry.media_thumbnail[0].get("url")
    return None


# ── Historial ──────────────────────────────────────────────

def cargar_historial():
    path = os.path.join(os.path.dirname(__file__), "historial.json")
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def guardar_historial(articulos):
    """Guarda los últimos MAX_HISTORIAL artículos. Los que salen van a archivo.json."""
    path = os.path.join(os.path.dirname(__file__), "historial.json")
    archivo_path = os.path.join(os.path.dirname(__file__), "archivo.json")

    # Notas que quedan fuera del historial → van al archivo
    descartadas = articulos[MAX_HISTORIAL:]
    if descartadas:
        try:
            with open(archivo_path, encoding="utf-8") as f:
                archivo = json.load(f)
        except Exception:
            archivo = {"_info": "Notas que rotaron del feed principal. Base del buscador.", "notas": []}
        ids_existentes = {n.get("id") for n in archivo.get("notas", [])}
        nuevas = [n for n in descartadas if n.get("id") not in ids_existentes]
        archivo["notas"] = archivo.get("notas", []) + nuevas
        with open(archivo_path, "w", encoding="utf-8") as f:
            json.dump(archivo, f, ensure_ascii=False, indent=2)
        print(f"  → {len(nuevas)} nota(s) movidas a archivo.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(articulos[:MAX_HISTORIAL], f, ensure_ascii=False, indent=2)


def urls_ya_publicadas(historial):
    return {a.get("url_original", "") for a in historial if a.get("url_original")}


# ── RSS ────────────────────────────────────────────────────

def fetch_noticias_crudas():
    noticias = []
    print(f"\n{'='*55}")
    print(f"  PatagoniaGLOBAL — Actualizando noticias")
    print(f"  {fecha_display()}")
    print(f"{'='*55}\n")

    for fuente in FUENTES_RSS:
        print(f"  Leyendo: {fuente['nombre']} ...", end=" ", flush=True)
        try:
            feed = feedparser.parse(fuente["url"])
            encontradas = 0
            for entry in feed.entries[:20]:
                titulo  = entry.get("title", "")
                resumen = entry.get("summary", "")
                if not titulo:
                    continue
                if es_patagonica(titulo, resumen):
                    noticias.append({
                        "fuente":           fuente["nombre"],
                        "region":           fuente["region"],
                        "titulo_original":  titulo,
                        "resumen_original": resumen[:500] if resumen else "",
                        "url":              entry.get("link", ""),
                        "imagen_rss":       obtener_imagen_rss(entry),
                    })
                    encontradas += 1
            print(f"{encontradas} patagónicas")
        except Exception as e:
            print(f"error ({e})")

    print(f"\n  Total encontradas: {len(noticias)} noticias patagónicas\n")
    return noticias[:30]


# ── Claude ─────────────────────────────────────────────────

def reescribir_con_claude(noticias_crudas, historial):
    if not noticias_crudas:
        print("  ⚠ No se encontraron noticias patagónicas.")
        return None

    client = anthropic.Anthropic(api_key=API_KEY)

    ya_publicadas  = urls_ya_publicadas(historial)
    noticias_nuevas = [n for n in noticias_crudas if n["url"] not in ya_publicadas]
    print(f"  Noticias nuevas (no publicadas aún): {len(noticias_nuevas)}")

    if not noticias_nuevas:
        print("  ⚠ No hay noticias nuevas para agregar hoy.")
        return None

    listado = ""
    for i, n in enumerate(noticias_nuevas):
        listado += f"""
--- Noticia {i+1} ---
Fuente: {n['fuente']} ({n['region']})
Título original: {n['titulo_original']}
Resumen: {n['resumen_original']}
URL: {n['url']}
"""

    hoy = datetime.now().strftime('%Y%m%d-%H%M')

    prompt = f"""Sos el editor jefe de PatagoniaGLOBAL, el primer medio digital panpatagónico. Slogan: "Sur Global, principio de todo." Cobertura: Argentina y Chile sin fronteras.

IDENTIDAD EDITORIAL:
- La Patagonia no es periferia — es el comienzo. Escribís desde adentro, no desde Buenos Aires ni Santiago.
- Voz: directa, contextual, apasionada por la región, rigurosa. Nunca alarmista, nunca partidaria.
- Cada nota tiene perspectiva propia: qué significa para la Patagonia binacional, antecedentes, qué viene después.
- Si el hecho cruza la frontera Argentina-Chile, marcarlo siempre.
- NUNCA copiés párrafos de la fuente. Reescribí con voz propia.

CRITERIO DE SELECCIÓN — solo entran notas con anclaje patagónico real:
✓ Medio Ambiente: glaciares, agua, fauna, ecosistemas, legislación ambiental, especies invasoras, contaminación
✓ Pueblos Originarios: Mapuche, Tehuelche, Kawésqar, Selknam — territorio, derechos, cultura viva
✓ Deportes Patagónicos: trail, escalada, kayak, ski, triatlón, expediciones, carreras aventura
✓ Desarrollo & Producción: economía regional, pesca, ganadería, energía, infraestructura, conectividad
✓ Cultura: arte, música, identidad, historia, gastronomía, fiestas regionales, pioneros
✓ Ciencia & Tecnología: hallazgos CONICET, paleontología, innovación aplicada al territorio
✓ Turismo & Guías: destinos, temporadas, premios internacionales a Patagonia
✓ Bienestar: salud, comunidad, calidad de vida con impacto regional concreto

PRIORIDADES EDITORIALES — orden estricto:
1. MEDIO AMBIENTE CRÍTICO: glaciares, pesca ilegal en ZEE, incendios, especies en peligro, contaminación → TAPA AUTOMÁTICA.
2. PUEBLOS ORIGINARIOS: cualquier nota sobre comunidades originarias patagónicas con hecho concreto.
3. DEPORTES ÚNICOS: premios internacionales, expediciones históricas, trail, escalada, ski.
4. PRODUCCIÓN CON IDENTIDAD: historia de productor patagónico, producto único de la región, primer hito económico local.
5. TURISMO & CULTURA: destinos, fiestas regionales, artistas, premiaciones.
6. DESARROLLO: infraestructura, conectividad, energía con impacto concreto.
7. POLÍTICA: SOLO decisión de gobierno con impacto territorial directo y concreto. Sin política partidaria.

DESCARTAR SIEMPRE: policiales, accidentes de tránsito, crónica roja, economía nacional sin anclaje patagónico, política porteña o santiaguina sin efecto en el territorio.

REGLA DE ORO: el lector viene a leer la Patagonia. Ante la duda, elegí la nota que habla de territorio, naturaleza, gente o cultura.

Tenés estas noticias nuevas disponibles hoy:
{listado}

Tu tarea:
1. Elegí LA MEJOR para la tapa del día (medio ambiente y pueblos originarios tienen prioridad automática)
2. Elegí entre 1 y 3 noticias adicionales para el feed del día
3. Escribí el artículo completo de cada una con voz propia de PatagoniaGLOBAL
4. Generá 5 titulares breves para el ticker (hechos concretos, sin clickbait)

Estructura del artículo (campo "cuerpo"):
- Párrafo de entrada: el hecho central con ángulo patagónico propio
- 2-3 párrafos: contexto regional, qué significa para la Patagonia, antecedentes, conexión binacional si aplica
- Párrafo de cierre: diagnóstico editorial, qué se espera o qué está en juego
- Separar párrafos con \\n\\n — entre 350 y 500 palabras

Respondé SOLO con este JSON válido (sin texto adicional):
{{
  "ticker": ["titular corto 1", "titular corto 2", "titular corto 3", "titular corto 4", "titular corto 5"],
  "tapa": {{
    "id": "{hoy}-tapa",
    "titulo": "Título reescrito atractivo (máx 15 palabras)",
    "bajada": "Bajada con contexto y ángulo propio (2-3 oraciones)",
    "cuerpo": "Artículo completo con párrafos separados por \\n\\n",
    "tag": "emoji + categoría",
    "categoria": "medio ambiente|pueblos originarios|deportes|turismo|cultura|ciencia|producción|conectividad|bienestar|pesca|historia|general",
    "fuente": "Nombre del medio original",
    "url_original": "url completa",
    "pais": "argentina|chile|ambos",
    "imagen": null,
    "imagen_keywords": "2-3 palabras en inglés para buscar foto (ej: glacier patagonia, indigenous patagonia, trail running mountains)"
  }},
  "nuevas": [
    {{
      "id": "{hoy}-1",
      "titulo": "Título (máx 12 palabras)",
      "bajada": "Una oración de contexto con dato concreto",
      "cuerpo": "Artículo completo con párrafos separados por \\n\\n",
      "tag": "· Categoría ·",
      "categoria": "...",
      "fuente": "...",
      "url_original": "url completa",
      "pais": "argentina|chile|ambos",
      "imagen": null,
      "imagen_keywords": "2-3 palabras en inglés"
    }}
  ]
}}"""

    print("  Enviando a Claude para reescritura editorial...", end=" ", flush=True)
    try:
        response = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )
        texto = response.content[0].text.strip()
        if "```" in texto:
            partes = texto.split("```")
            for parte in partes:
                if parte.startswith("json"):
                    texto = parte[4:].strip()
                    break
                elif parte.strip().startswith("{"):
                    texto = parte.strip()
                    break
        inicio = texto.find("{")
        fin    = texto.rfind("}") + 1
        if inicio >= 0 and fin > inicio:
            texto = texto[inicio:fin]
        datos = json.loads(texto)
        print("OK")
        return datos
    except json.JSONDecodeError as e:
        print(f"error parseando JSON: {e}")
        debug_path = os.path.join(os.path.dirname(__file__), "debug_claude_response.txt")
        try:
            with open(debug_path, "w") as f:
                f.write(texto)
            print(f"  Respuesta guardada en {debug_path}")
        except Exception:
            pass
        return None
    except Exception as e:
        print(f"error: {e}")
        return None


# ── Imágenes ───────────────────────────────────────────────

def fotos_propias_disponibles():
    indice_path = os.path.join(os.path.dirname(__file__), "fotos", "index.json")
    if not os.path.exists(indice_path):
        return []
    try:
        with open(indice_path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def extraer_og_image(url_articulo, nota_id):
    """Descarga la og:image del artículo fuente y la guarda en fotos/."""
    if not url_articulo:
        return None
    try:
        import re
        req = urllib.request.Request(url_articulo, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="ignore")

        # Buscar og:image en ambos órdenes de atributos
        match = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']', html)
        if not match:
            match = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', html)
        if not match:
            return None

        img_url = match.group(1).strip()
        if not img_url.startswith("http"):
            return None

        # Determinar extensión
        ext = img_url.split("?")[0].rsplit(".", 1)[-1].lower()
        if ext not in ("jpg", "jpeg", "png", "webp"):
            ext = "jpg"

        filename = f"foto-{nota_id}.{ext}"
        ruta_local = os.path.join(os.path.dirname(__file__), "fotos", filename)

        # No descargar si ya existe
        if os.path.exists(ruta_local):
            return f"fotos/{filename}"

        img_req = urllib.request.Request(img_url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(img_req, timeout=10) as resp:
            contenido = resp.read()

        with open(ruta_local, "wb") as f:
            f.write(contenido)

        return f"fotos/{filename}"

    except Exception as e:
        print(f"(og:image error: {e})")
        return None


def buscar_foto_propia(nota, fotos):
    # Solo matchea contra imagen_keywords (campo específico que Claude genera para la foto)
    # No usa el título para evitar falsos positivos por palabras comunes como "neuquén" o "historia"
    keywords_nota = nota.get("imagen_keywords", "").lower()
    if not keywords_nota:
        return None
    for foto in fotos:
        if any(kw in keywords_nota for kw in foto.get("keywords", [])):
            return f"fotos/{foto['archivo']}"
    return None


def _unsplash_query(keywords):
    try:
        query = urllib.parse.quote(keywords)
        url   = f"https://api.unsplash.com/search/photos?query={query}&per_page=5&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
        req   = urllib.request.Request(url, headers={"Accept-Version": "v1"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            data    = json.loads(resp.read())
            results = data.get("results", [])
            if results:
                return results[0]["urls"]["regular"]
    except Exception:
        pass
    return None


def buscar_imagen_unsplash(keywords):
    if not UNSPLASH_ACCESS_KEY or UNSPLASH_ACCESS_KEY == "PEGAR_ACA_TU_UNSPLASH_KEY":
        return None
    resultado = _unsplash_query(keywords)
    if resultado:
        return resultado
    primera = keywords.split()[0] if keywords else "patagonia"
    resultado = _unsplash_query(f"{primera} patagonia")
    if resultado:
        return resultado
    return _unsplash_query("patagonia landscape argentina")


def resolver_imagen(nota, fotos_propias, fotos_usadas):
    """RSS > og:image fuente > foto propia > Unsplash."""
    # 1. Imagen del RSS
    if nota.get("imagen") and str(nota["imagen"]).startswith("http"):
        print(f"    [{nota['id']}] imagen RSS ✓")
        return nota["imagen"]

    # 2. og:image de la URL original del artículo
    url_original = nota.get("url_original", "")
    if url_original:
        print(f"    [{nota['id']}] og:image fuente...", end=" ", flush=True)
        og_img = extraer_og_image(url_original, nota["id"])
        if og_img:
            print(f"OK → {og_img}")
            return og_img
        print("no encontrada")

    # 3. Foto propia por keywords (sin repetir)
    foto_propia = buscar_foto_propia(nota, fotos_propias)
    if foto_propia and foto_propia not in fotos_usadas:
        fotos_usadas.add(foto_propia)
        print(f"    [{nota['id']}] foto propia: {foto_propia} ✓")
        return foto_propia

    # 4. Unsplash
    keywords = nota.get("imagen_keywords", "patagonia landscape")
    print(f"    [{nota['id']}] Unsplash: '{keywords}' ...", end=" ", flush=True)
    url = buscar_imagen_unsplash(keywords)
    if url:
        print("OK")
        return url
    print("sin resultado")
    return None


# ── JSON de salida ─────────────────────────────────────────

def cargar_historias_permanentes():
    """Carga las notas permanentes desde historias.json (nunca se sobreescribe)."""
    ruta = os.path.join(os.path.dirname(__file__), "historias.json")
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, encoding="utf-8") as f:
            data = json.load(f)
        return data.get("notas", [])
    except Exception:
        return []


def construir_noticias_json(tapa, historial, ticker):
    """Arma noticias.json con tapa + feed del historial. Preserva historias permanentes."""
    # El feed son los últimos MAX_FEED artículos (excluyendo la tapa)
    feed = [a for a in historial if a.get("id") != tapa.get("id")][:MAX_FEED]

    # Secundarias: los 2 primeros del feed
    secundarias = feed[:2]
    # Cards del feed: del 3ro en adelante
    noticias_cards = feed[2:]

    # Las historias permanentes (Historia, Cultura) nunca se borran
    historias = cargar_historias_permanentes()

    return {
        "generado":      datetime.now().isoformat(),
        "fecha_display": fecha_display(),
        "ticker":        ticker,
        "tapa":          tapa,
        "secundarias":   secundarias,
        "noticias":      noticias_cards,
        "historias":     historias,
    }


def guardar_json(datos):
    ruta = os.path.join(os.path.dirname(__file__), "noticias.json")
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    print(f"\n  ✓ noticias.json guardado")
    return ruta


# ── Main ───────────────────────────────────────────────────

def main():
    # 1. Cargar historial
    historial = cargar_historial()
    print(f"\n  Historial actual: {len(historial)} artículos publicados")

    # 2. Obtener noticias crudas de RSS
    noticias_crudas = fetch_noticias_crudas()

    # 3. Reescribir con Claude (solo noticias nuevas)
    resultado = reescribir_con_claude(noticias_crudas, historial)
    if not resultado:
        print("\n  ✗ No se generaron artículos nuevos.\n")
        sys.exit(1)

    tapa   = resultado.get("tapa", {})
    nuevas = resultado.get("nuevas", [])
    ticker = resultado.get("ticker", [])

    todos_nuevos = [tapa] + nuevas

    # 4. Resolver imágenes
    fotos_propias = fotos_propias_disponibles()
    if fotos_propias:
        print(f"\n  Fotos propias en biblioteca: {len(fotos_propias)}")
    print("\n  Resolviendo imágenes...")
    fotos_usadas = set()
    for nota in todos_nuevos:
        nota["imagen"] = resolver_imagen(nota, fotos_propias, fotos_usadas)
        # Agregar meta si no tiene
        if "meta" not in nota:
            nota["meta"] = f"Hoy · {nota.get('fuente','PatagoniaGLOBAL')}"

    # 5. Agregar al historial (nuevos van al frente)
    historial = todos_nuevos + historial
    guardar_historial(historial)
    print(f"\n  Artículos nuevos agregados: {len(todos_nuevos)}")
    print(f"  Total en historial: {min(len(historial), MAX_HISTORIAL)}")

    # 6. Construir y guardar noticias.json
    datos = construir_noticias_json(tapa, historial, ticker)
    guardar_json(datos)

    print(f"\n  Feed visible: tapa + {len(datos['secundarias'])} secundarias + {len(datos['noticias'])} cards")
    print(f"\n  Listo. Publicá en Netlify.")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
