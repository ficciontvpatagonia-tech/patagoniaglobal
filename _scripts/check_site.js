// check_site.js — auditoría automatizada de globalpatagonia.org
const { chromium } = require('/Users/jm/Desktop/CLAUDCODE/VISUAL_STUDIO_CODE/Proyectos/flight-search/node_modules/playwright');

const BASE = 'https://globalpatagonia.org';

const PAGES = [
  { name: 'Inicio',        url: '/' },
  { name: 'Agenda',        url: '/agenda.html' },
  { name: 'Videos',        url: '/videos.html' },
  { name: 'Acerca',        url: '/acerca.html' },
  { name: 'Buscar',        url: '/buscar.html' },
  { name: 'Colaboradores', url: '/colaboradores.html' },
  { name: 'Apoyanos',      url: '/apoyanos.html' },
  { name: 'Privacidad',    url: '/privacidad.html' },
];

const errors = [];
const warnings = [];

function log(msg) { process.stdout.write(msg + '\n'); }
function err(ctx, msg) { errors.push(`[${ctx}] ${msg}`); log(`  ❌ ${msg}`); }
function warn(ctx, msg) { warnings.push(`[${ctx}] ${msg}`); log(`  ⚠️  ${msg}`); }
function ok(msg) { log(`  ✓  ${msg}`); }

async function checkPage(browser, { name, url }) {
  log(`\n── ${name} (${url})`);
  const page = await browser.newPage();
  const consoleErrors = [];
  const failedRequests = [];

  page.on('console', msg => {
    if (msg.type() === 'error') consoleErrors.push(msg.text());
  });
  page.on('requestfailed', req => {
    failedRequests.push(`${req.failure().errorText} → ${req.url()}`);
  });
  page.on('response', resp => {
    const s = resp.status();
    const u = resp.url();
    if (s >= 400 && !u.includes('onesignal') && !u.includes('googletagmanager')) {
      err(name, `HTTP ${s} → ${u}`);
    }
  });

  let status;
  try {
    const resp = await page.goto(BASE + url, { waitUntil: 'networkidle', timeout: 30000 });
    status = resp.status();
    if (status >= 400) {
      err(name, `Página devolvió HTTP ${status}`);
      await page.close();
      return;
    }
    ok(`HTTP ${status}`);
  } catch (e) {
    err(name, `No cargó: ${e.message}`);
    await page.close();
    return;
  }

  // Esperar un poco para que los fetch de JSONs terminen
  await page.waitForTimeout(3000);

  // Errores de consola
  for (const ce of consoleErrors) {
    if (ce.includes('favicon') || ce.includes('onesignal')) continue;
    err(name, `Console error: ${ce.substring(0, 120)}`);
  }
  if (consoleErrors.filter(c => !c.includes('favicon') && !c.includes('onesignal')).length === 0) {
    ok('Sin errores de consola');
  }

  // Requests fallidos
  for (const fr of failedRequests) {
    if (fr.includes('onesignal') || fr.includes('googletagmanager')) continue;
    err(name, `Request fallido: ${fr.substring(0, 120)}`);
  }
  if (failedRequests.filter(f => !f.includes('onesignal') && !f.includes('googletagmanager')).length === 0) {
    ok('Sin requests fallidos');
  }

  // Links internos rotos (solo en Inicio para no tardar demasiado)
  if (url === '/') {
    const links = await page.$$eval('a[href]', els =>
      els.map(a => a.getAttribute('href')).filter(h =>
        h && !h.startsWith('http') && !h.startsWith('mailto') &&
        !h.startsWith('#') && !h.startsWith('javascript')
      )
    );
    const unique = [...new Set(links)];
    log(`  → Verificando ${unique.length} links internos...`);
    for (const link of unique.slice(0, 40)) {
      try {
        const r = await page.request.get(BASE + (link.startsWith('/') ? link : '/' + link));
        if (r.status() >= 400) warn(name, `Link roto (${r.status()}): ${link}`);
      } catch (e) {
        warn(name, `Link inaccesible: ${link}`);
      }
    }
    ok('Links internos verificados');
  }

  // Verificar que elementos clave estén presentes
  if (url === '/') {
    const hasNoticias = await page.$('#noticias-section, .noticias-semana, [data-section="noticias"]') !== null;
    const hasNav = await page.$('nav, header') !== null;
    const hasTicker = await page.$('#ticker, .ticker') !== null;
    if (!hasNav) warn(name, 'No se encontró nav/header');
    if (!hasNoticias) warn(name, 'Sección noticias no encontrada');
    if (!hasTicker) warn(name, 'Ticker no encontrado');
    if (hasNav && hasNoticias) ok('Elementos estructurales presentes');
  }

  // Screenshot
  const shotPath = `/tmp/gp_check_${name.toLowerCase().replace(/[^a-z]/g, '_')}.png`;
  await page.screenshot({ path: shotPath, fullPage: false });
  ok(`Screenshot → ${shotPath}`);

  await page.close();
}

async function checkJson(request, path) {
  try {
    const r = await request.get(BASE + path);
    const status = r.status();
    if (status !== 200) {
      err('JSON', `HTTP ${status} → ${path}`);
      return;
    }
    const text = await r.text();
    try {
      const data = JSON.parse(text);
      const count = Array.isArray(data) ? data.length : Object.keys(data).length;
      ok(`${path} — válido (${count} items)`);
    } catch (e) {
      err('JSON', `JSON inválido en ${path}: ${e.message}`);
    }
  } catch (e) {
    err('JSON', `No accesible ${path}: ${e.message}`);
  }
}

(async () => {
  log('═══════════════════════════════════════════════');
  log('  AUDITORÍA GLOBALPATAGONIA.ORG');
  log(`  ${new Date().toLocaleString('es-AR')}`);
  log('═══════════════════════════════════════════════');

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    viewport: { width: 1440, height: 900 },
  });

  // Verificar JSONs críticos
  log('\n── JSONs críticos');
  const req = context.request;
  const jsons = [
    '/noticias.json', '/historial.json', '/propios.json',
    '/agenda.json', '/turismo.json', '/deportes_feed.json',
    '/guias.json', '/videos.json', '/historias.json',
  ];
  for (const j of jsons) await checkJson(req, j);

  // Verificar páginas
  for (const p of PAGES) {
    await checkPage(context, p);
  }

  // Verificar una nota individual
  log('\n── Nota individual (nota.html)');
  try {
    const noticias = await (await req.get(BASE + '/noticias.json')).json();
    const primera = Array.isArray(noticias) ? noticias[0] : null;
    if (primera?.id) {
      await checkPage(context, { name: 'Nota', url: `/nota.html?id=${primera.id}` });
    }
  } catch (e) {
    warn('Nota', `No se pudo obtener ID de nota: ${e.message}`);
  }

  await browser.close();

  // Resumen
  log('\n═══════════════════════════════════════════════');
  log('  RESUMEN');
  log('═══════════════════════════════════════════════');
  if (errors.length === 0 && warnings.length === 0) {
    log('  ✅ Sin errores ni advertencias.');
  } else {
    if (errors.length > 0) {
      log(`\n  ❌ ERRORES (${errors.length}):`);
      errors.forEach(e => log(`     ${e}`));
    }
    if (warnings.length > 0) {
      log(`\n  ⚠️  ADVERTENCIAS (${warnings.length}):`);
      warnings.forEach(w => log(`     ${w}`));
    }
  }
  log('');
})();
