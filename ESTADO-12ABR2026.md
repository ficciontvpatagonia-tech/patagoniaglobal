# Estado del sistema — 12 abril 2026
*Revisar el 13 de abril después de las 6am Argentina (cuando corre el workflow)*

## Cambios aplicados hoy

### Facebook — era el problema principal
- **Bug corregido:** conversión WebP→JPEG tenía un `else` que borraba la imagen después de convertirla exitosamente → publicaba sin foto
- **Auto-refresh de token implementado:** el script ahora renueva el token automáticamente cada ejecución usando App ID + App Secret → no debería vencer nunca más
- **Secrets nuevos agregados en GitHub:** `FACEBOOK_APP_ID`, `FACEBOOK_APP_SECRET`
- **Workflow corregido:** los secrets `FACEBOOK_APP_ID` y `FACEBOOK_APP_SECRET` no estaban en el `env` del workflow → el auto-refresh no hubiera funcionado aunque el código estaba bien

### Cultura.json — bug secundario
- El workflow no incluía `cultura.json` en el `git add` → el script lo actualizaba pero nunca se commiteaba
- **Corregido:** agregado al workflow
- La nota de hoy domingo (Tauscheck / Nahuel Huapi) se perdió — se cargará el próximo domingo automáticamente

### Instagram — sin cambios, funcionaba bien
- Solo verificar que siga funcionando

### Cinemateca
- Carrusel con orden editorial fijo: El Aura · Un Lugar en el Mundo · Rescatistas · Iluminados por el Fuego · La Patagonia Rebelde · Nacido y Criado

### Index.html
- Botón Instagram agregado al banner de redes y footer (junto a Telegram y Facebook)

---

## Qué revisar mañana 13 abril

### Facebook ✓ o ✗
- [ ] ¿Aparece una publicación nueva en la página de Facebook de hoy?
- [ ] ¿Tiene foto o es solo texto?
- [ ] En el log del workflow (GitHub → Actions → "Actualizar Noticias") buscar: `Facebook: token renovado automáticamente ✓` y `Facebook OK ✓`

### Instagram ✓ o ✗
- [ ] ¿Aparece publicación nueva en @global.patagonia?

### Telegram ✓ o ✗
- [ ] ¿Llegó mensaje al canal?

### Cultura ✓ o ✗
- [ ] Hoy es domingo → debería aparecer nota nueva en la sección Cultura de globalpatagonia.org

### Cómo ver el log del workflow
GitHub → ficciontvpatagonia-tech/patagoniaglobal → Actions → "Actualizar Noticias" → el run de hoy → paso "Correr script de noticias"
