const CACHE_STATIC = 'gp-static-v2';
const CACHE_DATA   = 'gp-data-v2';

const STATIC_ASSETS = [
  '/', '/index.html', '/nota.html', '/agenda.html', '/videos.html',
  '/acerca.html', '/apoyanos.html', '/buscar.html',
  '/logo-globalpatagonia.webp', '/favicon.ico'
];

// Cache static assets on install
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_STATIC).then(c => c.addAll(STATIC_ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys
        .filter(k => k !== CACHE_STATIC && k !== CACHE_DATA)
        .map(k => caches.delete(k))
      )
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);

  // Only handle same-origin requests
  if (url.origin !== location.origin) return;

  const isJSON = url.pathname.endsWith('.json');
  const isImage = /\.(jpg|jpeg|png|gif|webp|svg|ico)$/i.test(url.pathname);
  const isFont  = url.pathname.includes('/fonts/');

  if (isJSON) {
    // Network first, fall back to cache — JSONs update daily
    e.respondWith(
      fetch(e.request).then(res => {
        const clone = res.clone();
        caches.open(CACHE_DATA).then(c => c.put(e.request, clone));
        return res;
      }).catch(() => caches.match(e.request))
    );
  } else if (isImage || isFont) {
    // Stale-while-revalidate: sirve del cache al toque si existe, pero
    // SIEMPRE relanza el fetch en paralelo para refrescar esa URL en el
    // cache. Antes era cache-first puro sin vencimiento: una vez cacheada
    // una URL (ej. la foto de una nota, el logo) quedaba servida desde ahí
    // para siempre aunque el archivo cambiara en el servidor — el visitante
    // recurrente nunca se enteraba de un cambio de imagen.
    e.respondWith(
      caches.match(e.request).then(cached => {
        const fetchPromise = fetch(e.request).then(res => {
          const clone = res.clone();
          caches.open(CACHE_STATIC).then(c => c.put(e.request, clone));
          return res;
        }).catch(() => cached);
        return cached || fetchPromise;
      })
    );
  }
  // HTML and other resources: normal network (no SW interference)
});
