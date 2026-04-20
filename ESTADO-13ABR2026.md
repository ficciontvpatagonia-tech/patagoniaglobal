# Estado del sistema — 13 abril 2026
*Revisar el 14 de abril después de las 6am Argentina (cuando corre el workflow)*

## Cambios aplicados hoy

### Facebook — fix definitivo
- El auto-refresh de token (`fb_exchange_token`) devolvía un User Token, no un Page Token → error 100/33
- **Fix:** después del exchange, se llama a `/me/accounts` para obtener el Page Token real (que nunca expira)

### Instagram — nuevo diseño 4:5 portrait
- Antes: cuadrado 1080×1080 (se recortaba en PC)
- Ahora: portrait 1080×1350 (formato óptimo para feed Instagram)
- Layout: header "GLOBALpatagonia" | foto grande | badge de categoría | título Arial Black | "ver nota completa"
- Fix: emojis en el badge se stripean (aparecía □ en vez del emoji)
- Fix fuentes: paths macOS + Noto Sans Black en Ubuntu (workflow instala `fonts-noto`)
- Fallback imágenes: si `_ig.jpg` falla, reintenta con imagen original

### Redes — cobertura completa
- Antes: solo tapa + informes se posteaban
- Ahora: tapa + deportes (diario) + negocios (diario) + turismo (domingo) + cultura (domingo) + informes
- Notas manuales: cualquier nota con `"postear_redes": true` en cualquier JSON de sección se postea automáticamente
- Estado se guarda en `telegram_state.json` (evita duplicados en reintento)

---

## Qué revisar mañana 14 abril

### Facebook ✓ o ✗
- [ ] ¿Publicó? Buscar `Facebook OK ✓` en el log
- [ ] ¿Publicaron también deportes y negocios?

### Instagram ✓ o ✗
- [ ] ¿Nuevo diseño portrait 4:5?
- [ ] ¿Badge sin caracteres extraños?
- [ ] ¿Publicaron también secciones?

### Telegram ✓ o ✗
- [ ] ¿Llegaron más mensajes que ayer (debería incluir deportes y negocios además de tapa)?

### Cómo ver el log
GitHub → ficciontvpatagonia-tech/patagoniaglobal → Actions → "Actualizar Noticias" → run de hoy → "Correr script de noticias"
