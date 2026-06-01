# GLOBAL PATAGONIA — Estructura del proyecto
*Actualizado: 27/05/2026*

---

## Raíz del proyecto

```
GLOBAL PATAGONIA/
│
├── index.html                      ← Portada principal
├── nota.html                       ← Template de notas diarias
├── buscar.html                     ← Buscador interno
├── agenda.html                     ← Agenda de eventos
├── clima.html                      ← Pronóstico del tiempo (activo desde 10/05/2026)
├── guia.html                       ← Índice de guías turísticas
├── videos.html                     ← Galería de videos
├── colaboradores.html              ← Página de colaboradores
├── acerca.html                     ← Acerca del medio
├── apoyanos.html                   ← Página de apoyo
├── publicidad.html                 ← Info publicitaria
├── privacidad.html                 ← Política de privacidad
├── 404.html                        ← Página de error
│
├── CNAME                           ← Dominio personalizado (GitHub Pages)
├── robots.txt                      ← Directivas para crawlers
├── sitemap.xml                     ← Sitemap general
├── sitemap-news.xml                ← Sitemap Google News
├── feed.xml                        ← RSS feed
├── ads.txt                         ← Autorización de publicidad
├── manifest.json                   ← PWA manifest
├── sw.js                           ← Service Worker (PWA)
├── .nojekyll                       ← Desactiva Jekyll en GitHub Pages
│
├── favicon.svg
├── logo.svg / logo-globalpatagonia.png / .webp
├── logo-icono.png / icon-192.png / icon-512.png
├── apple-touch-icon.png
```

---

## Carpetas principales

### `/temas/` — Páginas por categoría temática
```
temas/
├── ciencia.html
├── conectividad.html
├── cultura.html
├── deportes.html
├── economia.html
├── historia.html
├── medio-ambiente.html
├── produccion.html
└── turismo.html
```

### `/notas/` — Notas propias (contenido evergreen)
```
notas/
│
├── GUÍAS TURÍSTICAS (con versiones en/pt/zh)
│   ├── guia-bariloche.html
│   ├── guia-calafate-4-dias.html
│   ├── guia-chalten.html
│   ├── guia-esquel.html                 (+ -zh)
│   ├── guia-ushuaia.html                (+ -en, -pt, -zh)
│   ├── guia-invierno-patagonia-10-destinos.html   (+ -en, -pt, -zh)
│   └── guia-patagonia-argentina-chile.html        (+ -en, -pt, -zh)
│
├── SKI / DEPORTES
│   ├── ski-patagonia-2026.html          (+ -en, -pt, -zh)
│   └── gran-fondo-calle-calle-2026.html
│
├── HISTORIA
│   ├── historia-colonos-galeses-chubut.html
│   ├── historia-conquista-desierto.html
│   ├── historia-fundacion-punta-arenas.html
│   ├── historia-huelgas-1921.html
│   ├── historia-kawesqar.html
│   ├── historia-perito-moreno.html
│   └── historia-selknam.html
│
├── CULTURA
│   ├── cultura-cantautores-malvinas.html
│   ├── cultura-chatwin-patagonia.html
│   ├── cultura-mapuche-patagonia.html
│   ├── cultura-patrimonio-aysen.html
│   ├── cultura-rodrigo-binet-fotografia.html
│   ├── cultura-ruben-patagonia.html
│   └── cultura-uriel-sokolowicz-mar-es-uno.html
│
├── TURISMO / NATURALEZA
│   ├── turismo-pucheguin-cochamo-2026.html
│   ├── trail-monte-leon-2026.html
│   ├── isla-estados-arqueologia-2026.html
│   ├── perito-moreno-timeout-2026.html
│   └── rescate-chalten-marzo-2026.html
│
└── NOTAS DIARIAS (formato: YYYYMMDD-slug-seccion)
    ── ~300 notas desde 10/03/2026 hasta 26/05/2026
    ── Secciones: tapa / sec1 / sec2 / neg / dep / cul / tur
    ── Últimas: 20260526-*.html
```

### `/fotos/` — Imágenes de noticias
```
fotos/
├── Imágenes en .jpg y .webp
├── Nomenclatura: YYYYMMDD-slug-seccion_ig.webp
└── ~200+ imágenes (mayo 2026)
```

---

## Datos JSON

```
noticias.json               ← Feed principal (actualización diaria)
noticias_ayer.json          ← Backup del día anterior
propios.json                ← Notas propias publicadas
propios_historial.json      ← Historial completo de propias
archivo.json                ← Archivo histórico de noticias
historial.json              ← Historial general
cultura.json                ← Feed de cultura
turismo.json                ← Feed de turismo
negocios.json               ← Feed de negocios/economía
deportes_feed.json          ← Feed de deportes
deportes_historial.json     ← Historial deportes
guias.json                  ← Índice de guías
guias_historial.json        ← Historial guías
agenda.json                 ← Eventos de agenda
efemerides.json             ← Efemérides patagónicas
videos.json                 ← Índice de videos
historias.json              ← Historias destacadas
search-index.json           ← Índice de búsqueda interna
urls_publicadas.json        ← URLs publicadas (IndexNow)
urls_vetadas.json           ← URLs excluidas de publicación
telegram_state.json         ← Estado del bot de Telegram
```

---

## GitHub Actions (`.github/workflows/`)

```
actualizar-noticias.yml     ← Corre diariamente, scraping + push
publicar-facebook.yml       ← Publica en Facebook automáticamente
publicar-instagram.yml      ← Publica en Instagram automáticamente
check-seo.yml               ← Verifica SEO del sitio
optimizar-imagenes.yml      ← Comprime imágenes nuevas (WebP)
```

---

## Scripts Python

```
actualizar_noticias.py      ← Motor principal de scraping y actualización
optimizar_imagenes.py       ← Convierte y comprime imágenes a WebP
traducir_multiidioma.py     ← Genera versiones en/pt/zh de notas
generar_sitemap_news.py     ← Regenera sitemap de Google News
reconstruir_search_index.py ← Reconstruye el índice de búsqueda
submit_indexnow.py          ← Envía URLs nuevas a IndexNow (Bing/Yandex)
generar_estaticas_faltantes.py ← Genera páginas estáticas faltantes
agregar_compartir.py        ← Inserta botones de compartir en notas
agregar_relacionadas.py     ← Inserta notas relacionadas
check_seo.py                ← Auditoría SEO local
check_site.js               ← Verificación de páginas del sitio (Node.js)
```

---

## Archivos de configuración

```
.env                        ← Variables de entorno (tokens, claves API)
.gitignore                  ← Archivos excluidos del repo
CLAUDE.md                   ← Instrucciones para Claude Code
LINEA-EDITORIAL.md          ← Criterios editoriales del medio
MEMORIA-DEL-PROYECTO.md     ← Historial de decisiones del proyecto
```

---

## Carpetas internas / no versionadas

```
venv/                       ← Entorno virtual Python (no en git)
__pycache__/                ← Cache Python (no en git)
ARCHIVO PROPIO GP/          ← Assets, logos, archivos de diseño
```

---

## Sitio en producción

- **URL:** https://globalpatagonia.com
- **Hosting:** GitHub Pages (rama `main`)
- **Dominio:** CNAME → `globalpatagonia.com`
- **PWA:** Sí (manifest + service worker)
- **Idiomas:** ES (principal) + EN / PT / ZH (guías y notas evergreen)
