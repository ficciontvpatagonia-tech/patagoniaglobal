# PatagoniaGLOBAL — Contexto para Claude

Portal de noticias panpatagónico (Argentina + Chile). Fundado por Marto.
- **URL:** https://globalpatagonia.org
- **Repo:** `ficciontvpatagonia-tech/patagoniaglobal` (GitHub Pages)
- **Push siempre sin preguntar:**
  ```
  git add <archivos> && git commit -m "mensaje" && TOKEN=$(gh auth token --user martinsubira) && git push https://martinsubira:${TOKEN}@github.com/ficciontvpatagonia-tech/patagoniaglobal.git main
  ```

## Archivos clave
| Archivo | Qué es |
|---|---|
| `index.html` | Página principal (~1600 líneas) |
| `nota.html` | Vista individual de nota (`?id=ID`) |
| `noticias.json` | Feed diario (script automático) |
| `historial.json` | Archivo acumulativo de todas las notas |
| `historias.json` | Notas permanentes (nunca se borran) |
| `propios.json` | Artículos de J. Martineau → sección INFORMES |
| `propios_historial.json` | Informes archivados (rotación) |
| `negocios.json` | Economía & Empresas |
| `deportes_feed.json` | Deportes & Aventura |
| `turismo.json` | Turismo en Patagonia |
| `guias.json` | Guías de destinos |
| `agenda.json` | Eventos patagónicos |
| `videos.json` | Cinemateca Patagónica |
| `fotos/` | Fotos propias |
| `actualizar_noticias.py` | Script RSS → Claude → JSONs (corre en GitHub Actions) |

## Reglas críticas

**INFORMES (`propios.json`):**
- Máximo 3 activos. Al agregar uno nuevo → el más antiguo pasa a `propios_historial.json`, el nuevo va al inicio.
- Nunca van a tapa ni al feed de noticias. Solo sección INFORMES.
- El script diario NO toca `propios.json`.

**Notas completas:**
- Todo artículo agregado manualmente a cualquier sección (turismo, deportes, guias, negocios) DEBE tener su `cuerpo` completo en `historial.json`.
- Los JSONs de sección solo guardan el resumen para el card.
- Notas manuales en esos JSONs llevan `"excluir_feed": true`.

**`nota.html` busca en este orden:** noticias.json → historias.json → propios.json → historial.json → turismo.json

**`historias.json`** (Rubén Patagonia, huelgas 1921, etc.) nunca se archivan en propios.json — tienen su propia sección "Cultura Patagónica & Pueblos Originarios".

**Layout:** `DIAGRAMACION.pdf` en ~/Desktop es la referencia fija. No agregar secciones que no estén en él.

## Paleta visual
`#1c2d3d` azul cordillera · `#7aadcc` azul glacial · `#252830` gris granito · `#8c6b4a` arcilla · `#f0ede8` fondo
Tipografías: **Playfair Display** (títulos) + **Inter** (cuerpo)

## Cinemateca (`videos.json`)
- Series: una sola tarjeta agrupada (campo `serie`). El panel despliega episodios al click.
- `serie_descripcion` = sinopsis general de la serie.
- Thumbnail: el de mayor impacto visual (no necesariamente ep01).

## Secrets en GitHub
`ANTHROPIC_API_KEY`, `UNSPLASH_ACCESS_KEY`

## GA4 / AdSense
GA4: `G-5FP2F41BZG` | AdSense: `ca-pub-1924505291132800`
