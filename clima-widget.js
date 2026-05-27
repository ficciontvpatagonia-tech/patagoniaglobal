// ── CLIMA-WIDGET.JS — GLOBALpatagonia ─────────────────────────────────────────
// Soporta window.__CLIMA_CIUDAD_DEFAULT y window.__CLIMA_PAIS_DEFAULT
// para que las páginas shell por ciudad inicien en la ciudad correcta.
// Soporta window.__CLIMA_SKIP_CANONICAL_UPDATE para que las shells no
// sobreescriban su propio canonical con el de clima.html.

// ── CIUDADES ──────────────────────────────────────────────────────────────────
const CITIES = {
  ar: [
    { id:'bariloche',  name:'Bariloche',              lat:-41.133, lon:-71.310, region:'Río Negro' },
    { id:'neuquen',    name:'Neuquén',                lat:-38.952, lon:-68.059, region:'Neuquén' },
    { id:'sanmartin',  name:'San Martín de los Andes',lat:-40.157, lon:-71.355, region:'Neuquén' },
    { id:'esquel',     name:'Esquel',                 lat:-42.908, lon:-71.318, region:'Chubut' },
    { id:'chalten',    name:'El Chaltén',             lat:-49.332, lon:-72.886, region:'Santa Cruz' },
    { id:'calafate',   name:'El Calafate',            lat:-50.338, lon:-72.265, region:'Santa Cruz' },
    { id:'madryn',     name:'Puerto Madryn',          lat:-42.769, lon:-65.038, region:'Chubut' },
    { id:'comodoro',   name:'Comodoro Rivadavia',     lat:-45.864, lon:-67.496, region:'Chubut' },
    { id:'gallegos',   name:'Río Gallegos',           lat:-51.623, lon:-69.217, region:'Santa Cruz' },
    { id:'ushuaia',    name:'Ushuaia',                lat:-54.802, lon:-68.303, region:'Tierra del Fuego' },
    { id:'malvinas',   name:'Islas Malvinas',         lat:-51.693, lon:-57.853, region:'Malvinas' },
  ],
  cl: [
    { id:'puertomontt', name:'Puerto Montt',  lat:-41.469, lon:-72.942, region:'Los Lagos' },
    { id:'castro',      name:'Castro',        lat:-42.480, lon:-73.762, region:'Chiloé' },
    { id:'coyhaique',   name:'Coyhaique',     lat:-45.571, lon:-72.068, region:'Aysén' },
    { id:'natales',     name:'Puerto Natales',lat:-51.726, lon:-72.500, region:'Magallanes' },
    { id:'puntaarenas',    name:'Punta Arenas',    lat:-53.164, lon:-70.917, region:'Magallanes' },
    { id:'puertowilliams', name:'Puerto Williams', lat:-54.935, lon:-67.616, region:'Magallanes — Isla Navarino' },
  ],
  ant: [
    { id:'esperanza',  name:'Base Esperanza',    lat:-63.400, lon:-56.990, region:'Antártida Argentina — Península' },
    { id:'marambio',   name:'Base Marambio',      lat:-64.237, lon:-56.630, region:'Antártida Argentina — Isla Seymour' },
    { id:'carlini',    name:'Base Carlini',       lat:-62.237, lon:-58.667, region:'Antártida Argentina — Isla 25 de Mayo' },
    { id:'belgrano2',  name:'Base Belgrano II',   lat:-77.873, lon:-34.628, region:'Antártida Argentina — Polo' },
    { id:'orcadas',    name:'Base Orcadas',       lat:-60.740, lon:-44.740, region:'Antártida Argentina — Islas Orcadas' },
    { id:'frei',       name:'Base Pres. Frei (CL)',      lat:-62.200, lon:-58.966, region:'Antártida Chilena — Isla Rey Jorge' },
    { id:'onais',      name:'Villa Las Estrellas (CL)',  lat:-62.193, lon:-58.963, region:'Antártida Chilena — asentamiento civil' },
    { id:'prat',       name:'Base Arturo Prat (CL)',     lat:-62.483, lon:-59.667, region:'Antártida Chilena — Isla Greenwich' },
    { id:'ohiggins',   name:'Base Bernardo O\'Higgins (CL)', lat:-63.317, lon:-57.900, region:'Antártida Chilena — Península' },
    { id:'gonzvidela', name:'Base G. González Videla (CL)', lat:-64.817, lon:-62.850, region:'Antártida Chilena — Bahía Paraíso' },
  ],
};

// ── WMO CODES ────────────────────────────────────────────────────────────────
const WMO = {
  0:  { desc:'Despejado',              emoji:'☀️' },
  1:  { desc:'Mayormente despejado',   emoji:'🌤️' },
  2:  { desc:'Parcialmente nublado',   emoji:'⛅' },
  3:  { desc:'Nublado',                emoji:'☁️' },
  45: { desc:'Niebla',                 emoji:'🌫️' },
  48: { desc:'Niebla con escarcha',    emoji:'🌫️' },
  51: { desc:'Llovizna ligera',        emoji:'🌦️' },
  53: { desc:'Llovizna',               emoji:'🌦️' },
  55: { desc:'Llovizna intensa',       emoji:'🌧️' },
  61: { desc:'Lluvia ligera',          emoji:'🌧️' },
  63: { desc:'Lluvia moderada',        emoji:'🌧️' },
  65: { desc:'Lluvia intensa',         emoji:'🌧️' },
  71: { desc:'Nieve ligera',           emoji:'🌨️' },
  73: { desc:'Nevada moderada',        emoji:'❄️' },
  75: { desc:'Nevada intensa',         emoji:'❄️' },
  77: { desc:'Granizo',                emoji:'🌨️' },
  80: { desc:'Chubascos ligeros',      emoji:'🌦️' },
  81: { desc:'Chubascos moderados',    emoji:'🌧️' },
  82: { desc:'Chubascos fuertes',      emoji:'🌧️' },
  85: { desc:'Nevada con viento',      emoji:'🌨️' },
  86: { desc:'Tormenta de nieve',      emoji:'❄️' },
  95: { desc:'Tormenta eléctrica',     emoji:'⛈️' },
  96: { desc:'Tormenta con granizo',   emoji:'⛈️' },
  99: { desc:'Tormenta severa',        emoji:'⛈️' },
};
function wmo(code) {
  const keys = Object.keys(WMO).map(Number).sort((a,b)=>a-b);
  let k = keys[0];
  for (const kk of keys) { if (kk <= code) k = kk; else break; }
  return WMO[k] || { desc:'Variable', emoji:'🌡️' };
}

// ── CARDINAL ─────────────────────────────────────────────────────────────────
const DIRS = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSO','SO','OSO','O','ONO','NO','NNO'];
function degToCardinal(d) { return DIRS[Math.round(d/22.5)%16]; }

// ── STATE ─────────────────────────────────────────────────────────────────────
let currentCountry = 'ar';
let currentCity = null;
let chart1 = null;
let chart2 = null;
let windyLayer = 'wind';

function setWindyLayer(layer, btn) {
  windyLayer = layer;
  document.querySelectorAll('.windy-layer-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  if (currentCity) updateWindyMap(currentCity);
}

function updateWindyMap(city) {
  const iframe = document.getElementById('windy-iframe');
  if (!iframe) return;
  const zoom = city.lat < -65 ? 4 : city.lat < -50 ? 5 : 6;
  iframe.src = `https://embed.windy.com/embed2.html?lat=${city.lat}&lon=${city.lon}&detailLat=${city.lat}&detailLon=${city.lon}&zoom=${zoom}&level=surface&overlay=${windyLayer}&product=ecmwf&isolines=pressure&menu=&message=true&marker=true&metricWind=km%2Fh&metricTemp=%C2%B0C`;
}

// ── INIT ─────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  // fecha
  const now = new Date();
  const dias = ['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'];
  const meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
  document.getElementById('fecha-display').textContent =
    `${dias[now.getDay()]}, ${now.getDate()} de ${meses[now.getMonth()]} de ${now.getFullYear()} · Patagonia Argentina y Chilena`;

  // URL param — window.__CLIMA_CIUDAD_DEFAULT permite que las páginas shell
  // fuercen una ciudad sin depender del query string
  const params = new URLSearchParams(location.search);
  const ciudadParam = window.__CLIMA_CIUDAD_DEFAULT || params.get('ciudad') || 'bariloche';
  const paisParam   = window.__CLIMA_PAIS_DEFAULT   || params.get('pais')   || 'ar';
  currentCountry = paisParam === 'cl' ? 'cl' : paisParam === 'ant' ? 'ant' : 'ar';

  renderCityGrid();
  const city = [...CITIES.ar, ...CITIES.cl].find(c => c.id === ciudadParam) || CITIES.ar[0];
  selectCity(city);

  // hamburger
  const btn = document.getElementById('hamburger-btn');
  const nav = document.getElementById('nav-links');
  if (btn && nav) {
    btn.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      btn.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open);
    });
    document.addEventListener('click', e => {
      if (!btn.contains(e.target) && !nav.contains(e.target)) {
        nav.classList.remove('open');
        btn.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }
});

// ── SELECTOR ─────────────────────────────────────────────────────────────────
function switchCountry(cc) {
  currentCountry = cc;
  document.getElementById('tab-ar').classList.toggle('active', cc==='ar');
  document.getElementById('tab-cl').classList.toggle('active', cc==='cl');
  document.getElementById('tab-ant').classList.toggle('active', cc==='ant');
  renderCityGrid();
}

function renderCityGrid() {
  const grid = document.getElementById('city-grid');
  grid.innerHTML = '';
  CITIES[currentCountry].forEach(city => {
    const btn = document.createElement('button');
    btn.className = 'city-btn' + (currentCity && currentCity.id === city.id ? ' active' : '');
    btn.textContent = city.name;
    btn.onclick = () => selectCity(city);
    grid.appendChild(btn);
  });
}

function selectCity(city) {
  currentCity = city;
  // detect country
  const cc = CITIES.cl.find(c=>c.id===city.id) ? 'cl'
           : CITIES.ant.find(c=>c.id===city.id) ? 'ant'
           : 'ar';
  // update URL
  history.replaceState(null,'',`?ciudad=${city.id}&pais=${cc}`);
  // SEO: update title, description, canonical y H1 por ciudad
  const _seoTitle = `Clima ${city.name} hoy — Pronóstico 7 días · GLOBALpatagonia`;
  const _seoDesc  = `Clima y pronóstico del tiempo en ${city.name} (${city.region}) para hoy y los próximos 7 días. Temperatura, viento, nieve, UV y meteograma 48h.`;
  const _seoUrl   = `https://globalpatagonia.org/clima.html?ciudad=${city.id}&pais=${cc}`;
  document.title = _seoTitle;
  document.querySelector('meta[name="description"]').content = _seoDesc;
  document.querySelector('meta[property="og:title"]').content = _seoTitle;
  document.querySelector('meta[property="og:description"]').content = _seoDesc;
  document.querySelector('meta[name="twitter:title"]').content = _seoTitle;
  document.querySelector('meta[name="twitter:description"]').content = _seoDesc;
  // Canonical y og:url: solo se actualizan en clima.html, no en shells de ciudad
  if (!window.__CLIMA_SKIP_CANONICAL_UPDATE) {
    document.querySelector('link[rel="canonical"]').href = _seoUrl;
    document.querySelector('meta[property="og:url"]').content = _seoUrl;
  }
  const _h1 = document.getElementById('clima-h1');
  if (_h1) _h1.textContent = `El Tiempo en ${city.name}`;
  // switch tab if needed
  if (cc !== currentCountry) {
    currentCountry = cc;
    document.getElementById('tab-ar').classList.toggle('active', cc==='ar');
    document.getElementById('tab-cl').classList.toggle('active', cc==='cl');
    document.getElementById('tab-ant').classList.toggle('active', cc==='ant');
    renderCityGrid();
  }
  document.querySelectorAll('.city-btn').forEach(b => b.classList.toggle('active', b.textContent === city.name));
  loadWeather(city);
}

// ── FETCH ─────────────────────────────────────────────────────────────────────
async function loadWeather(city) {
  showLoading(`Cargando ${city.name}...`);
  try {
    const hourly = 'temperature_2m,apparent_temperature,precipitation_probability,precipitation,snowfall,weathercode,cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,visibility,windspeed_10m,windspeed_80m,windspeed_120m,windgusts_10m,cape,freezinglevel_height,relativehumidity_2m,surface_pressure,dewpoint_2m,winddirection_10m';
    const daily  = 'weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,uv_index_max,precipitation_sum,precipitation_probability_max,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant,snowfall_sum';
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${city.lat}&longitude=${city.lon}&hourly=${hourly}&daily=${daily}&current_weather=true&timezone=auto&wind_speed_unit=kmh&forecast_days=7`;
    const res = await fetch(url);
    if (!res.ok) {
      const err = await res.json().catch(()=>({}));
      throw new Error(err.reason || `HTTP ${res.status}`);
    }
    const data = await res.json();
    renderAll(city, data);
  } catch(e) {
    console.error('Open-Meteo error:', e.message);
    showError(e.message);
  }
}

function showLoading(msg) {
  document.getElementById('loading').style.display='block';
  document.getElementById('loading-text').textContent = msg || 'Cargando...';
  document.getElementById('error-state').style.display='none';
  document.getElementById('current-section').style.display='none';
  document.getElementById('forecast-section').style.display='none';
  document.getElementById('pro-section').style.display='none';
}
function showError(msg) {
  document.getElementById('loading').style.display='none';
  const el = document.getElementById('error-state');
  el.innerHTML = `⚠️ No se pudieron obtener datos. Verificá tu conexión e intentá de nuevo.${msg ? `<br><small style="opacity:.5">${msg}</small>` : ''}`;
  el.style.display='block';
}
function showData() {
  document.getElementById('loading').style.display='none';
  document.getElementById('error-state').style.display='none';
  document.getElementById('current-section').style.display='block';
  document.getElementById('forecast-section').style.display='block';
  document.getElementById('pro-section').style.display='block';
}

// ── RENDER ALL ────────────────────────────────────────────────────────────────
function renderAll(city, data) {
  const cw = data.current_weather;
  const cwIdx = Math.max(0, data.hourly.time.indexOf(cw.time));

  renderCurrent(city, data, cwIdx);
  renderForecast(data);
  updateWindyMap(city);
  renderMeteogram(data, cwIdx);
  renderAltitudeTable(data, cwIdx);
  renderMetrics(data, cwIdx);
  renderRisk(data, cwIdx);
  showData();
}

// ── CURRENT ───────────────────────────────────────────────────────────────────
function renderCurrent(city, data, idx) {
  const cw = data.current_weather;
  const h = data.hourly;
  const w = wmo(cw.weathercode);

  document.getElementById('cc-location').textContent  = `${city.name} · ${city.region}`;
  document.getElementById('cc-emoji').textContent      = w.emoji;
  document.getElementById('cc-temp').innerHTML         = `${Math.round(cw.temperature)}<sup>°C</sup>`;
  document.getElementById('cc-apparent').textContent   = `Sensación: ${Math.round(h.apparent_temperature[idx])}°C`;
  document.getElementById('cc-desc').textContent       = w.desc;
  document.getElementById('cc-humidity').textContent   = `${h.relativehumidity_2m[idx]}%`;
  document.getElementById('cc-pressure').textContent   = `${Math.round(h.surface_pressure[idx])} hPa ${pressureTrend(h.surface_pressure, idx)}`;
  document.getElementById('cc-dewpoint').textContent   = `${Math.round(h.dewpoint_2m[idx])}°C`;
  const vis = h.visibility[idx];
  document.getElementById('cc-visibility').textContent = vis >= 10000 ? '>10 km' : `${(vis/1000).toFixed(1)} km`;

  const wd = cw.winddirection;
  const arrowRot = (wd + 180) % 360;
  document.getElementById('cc-wind-arrow').style.transform = `rotate(${arrowRot}deg)`;
  document.getElementById('cc-wind-speed').textContent = Math.round(cw.windspeed);
  document.getElementById('cc-wind-dir').textContent   = `Desde el ${degToCardinal(wd)}`;
  const gust = h.windgusts_10m[idx];
  document.getElementById('cc-wind-gust').textContent  = gust > cw.windspeed + 5 ? `Ráfagas hasta ${Math.round(gust)} km/h` : '';
}

function pressureTrend(pressures, idx) {
  if (idx < 3) return '';
  const diff = pressures[idx] - pressures[idx-3];
  if (diff > 2) return '↑';
  if (diff < -2) return '↓';
  return '→';
}

// ── FORECAST 7D ───────────────────────────────────────────────────────────────
function renderForecast(data) {
  const d = data.daily;
  const strip = document.getElementById('forecast-strip');
  strip.innerHTML = '';
  const diasCortos = ['Dom','Lun','Mar','Mié','Jue','Vie','Sáb'];
  d.time.forEach((t, i) => {
    const date = new Date(t + 'T12:00:00');
    const dayName = i === 0 ? 'HOY' : i === 1 ? 'MÑN' : diasCortos[date.getDay()];
    const w = wmo(d.weathercode[i]);
    const precip = d.precipitation_probability_max[i] || 0;
    const snow = d.snowfall_sum[i] > 0.5;
    const uv = d.uv_index_max[i];
    const card = document.createElement('div');
    card.className = 'fc-card';
    card.innerHTML = `
      <div class="fc-day">${dayName}</div>
      <span class="fc-emoji">${w.emoji}</span>
      <div class="fc-temps">${Math.round(d.temperature_2m_max[i])}° <span class="fc-tmin">/ ${Math.round(d.temperature_2m_min[i])}°</span></div>
      <div class="fc-wind">💨 ${Math.round(d.windspeed_10m_max[i])} km/h</div>
      ${precip > 20 ? `<div class="fc-precip">💧 ${precip}%</div>` : ''}
      ${snow ? `<div class="fc-snow">❄️ ${d.snowfall_sum[i].toFixed(1)} cm</div>` : ''}
      ${uv >= 4 ? `<div class="fc-uv">UV ${Math.round(uv)}</div>` : ''}
    `;
    strip.appendChild(card);
  });
}

// ── METEOGRAM ─────────────────────────────────────────────────────────────────
function renderMeteogram(data, cwIdx) {
  const h = data.hourly;
  const N = 48;
  const start = cwIdx;
  const slice = (arr) => arr.slice(start, start + N);

  const times   = slice(h.time);
  const temps   = slice(h.temperature_2m);
  const wind10  = slice(h.windspeed_10m);
  const wind80  = slice(h.windspeed_80m);
  const precips = slice(h.precipitation);
  const clouds  = slice(h.cloudcover);

  const now = new Date();
  const labels = times.map(t => {
    const dt = new Date(t);
    const hh = dt.getHours();
    const d = dt.getDate();
    const todayD = now.getDate();
    const prefix = d === todayD ? 'Hoy' : d === todayD+1 ? 'Mañ' : dt.toLocaleDateString('es-AR',{weekday:'short'});
    return (hh === 0 || hh === 6 || hh === 12 || hh === 18) ? `${prefix} ${hh}h` : '';
  });

  if (chart1) { chart1.destroy(); chart1=null; }
  if (chart2) { chart2.destroy(); chart2=null; }

  const cloudPlugin = {
    id: 'cloudBg',
    beforeDraw(chart) {
      const { ctx, chartArea: ca, scales } = chart;
      if (!ca) return;
      clouds.forEach((cc, i) => {
        const x0 = scales.x.getPixelForValue(i);
        const x1 = i < clouds.length-1 ? scales.x.getPixelForValue(i+1) : ca.right;
        const alpha = (cc||0) / 100 * 0.22;
        ctx.fillStyle = `rgba(170,200,220,${alpha})`;
        ctx.fillRect(x0, ca.top, x1-x0, ca.bottom-ca.top);
      });
    }
  };

  const ctx1 = document.getElementById('meteogram-chart').getContext('2d');
  const maxWind = Math.max(...wind10, ...wind80.filter(v=>v!=null)) * 1.15 || 60;
  chart1 = new Chart(ctx1, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Temp °C',
          data: temps,
          borderColor: '#f4845a',
          backgroundColor: 'rgba(244,132,90,0.08)',
          borderWidth: 2.5,
          pointRadius: 0,
          tension: 0.35,
          yAxisID: 'yTemp',
          fill: true,
        },
        {
          label: 'Viento 10m km/h',
          data: wind10,
          borderColor: '#7aadcc',
          backgroundColor: 'rgba(122,173,204,0.12)',
          borderWidth: 2,
          pointRadius: 0,
          tension: 0.3,
          yAxisID: 'yWind',
          fill: true,
        },
        {
          label: 'Viento 80m km/h',
          data: wind80,
          borderColor: '#5a8db5',
          backgroundColor: 'transparent',
          borderWidth: 1.5,
          borderDash: [5,4],
          pointRadius: 0,
          tension: 0.3,
          yAxisID: 'yWind',
        },
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      interaction: { mode:'index', intersect:false },
      plugins: {
        legend: { display:false },
        tooltip: {
          backgroundColor: 'rgba(28,45,61,0.95)',
          titleColor: '#8ab8d4',
          bodyColor: '#eee',
          padding: 12,
          callbacks: {
            title: (items) => {
              const i = items[0].dataIndex;
              return times[i] ? new Date(times[i]).toLocaleString('es-AR',{weekday:'short',day:'numeric',hour:'2-digit',minute:'2-digit'}) : '';
            },
            label: (item) => {
              const u = item.datasetIndex===0 ? '°C' : ' km/h';
              return ` ${item.dataset.label.split(' ')[0]}: ${Math.round(item.raw)}${u}`;
            }
          }
        }
      },
      scales: {
        x: {
          ticks: { color:'rgba(255,255,255,.55)', font:{ size:10 }, maxRotation:0, autoSkip:false },
          grid: { color:'rgba(255,255,255,.07)' },
        },
        yTemp: {
          type:'linear', position:'left',
          ticks: { color:'#f4845a', font:{size:10}, callback:v=>`${v}°` },
          grid: { color:'rgba(255,255,255,.07)' },
          title: { display:true, text:'°C', color:'#f4845a', font:{size:10} },
        },
        yWind: {
          type:'linear', position:'right',
          min:0, max: maxWind,
          ticks: { color:'#7aadcc', font:{size:10}, callback:v=>`${v}` },
          grid: { display:false },
          title: { display:true, text:'km/h', color:'#7aadcc', font:{size:10} },
        },
      }
    },
    plugins: [cloudPlugin]
  });

  const ctx2 = document.getElementById('precip-chart').getContext('2d');
  const maxPrecip = Math.max(...precips) || 1;
  chart2 = new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Precip mm',
        data: precips,
        backgroundColor: precips.map(v => v > 5 ? 'rgba(50,100,200,0.85)' : 'rgba(80,140,210,0.65)'),
        borderWidth: 0,
        borderRadius: 2,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: { display:false },
        tooltip: {
          backgroundColor:'rgba(28,45,61,0.95)',
          titleColor:'#8ab8d4',
          bodyColor:'#eee',
          padding:8,
          callbacks: {
            title:(items)=>{
              const i=items[0].dataIndex;
              return times[i] ? new Date(times[i]).toLocaleString('es-AR',{weekday:'short',day:'numeric',hour:'2-digit',minute:'2-digit'}) : '';
            },
            label:(item)=>` Lluvia: ${item.raw.toFixed(1)} mm`
          }
        }
      },
      scales: {
        x: {
          ticks: { color:'rgba(255,255,255,.45)', font:{size:9}, maxRotation:0, autoSkip:false },
          grid: { color:'rgba(255,255,255,.05)' },
        },
        y: {
          min:0,
          suggestedMax: Math.max(maxPrecip*1.3, 3),
          ticks: { color:'rgba(255,255,255,.5)', font:{size:9}, callback:v=>`${v}mm` },
          grid: { color:'rgba(255,255,255,.05)' },
          title: { display:true, text:'mm', color:'rgba(255,255,255,.5)', font:{size:9} },
        }
      }
    }
  });
}

// ── ALTITUDE TABLE ────────────────────────────────────────────────────────────
function renderAltitudeTable(data, cwIdx) {
  const h = data.hourly;
  const n6 = Math.min(6, data.hourly.time.length - cwIdx);
  const avg = (arr, from, len) => {
    const vals = arr.slice(from, from+len).filter(v=>v!=null);
    return vals.length ? vals.reduce((a,b)=>a+b,0)/vals.length : null;
  };
  const maxOf = (arr, from, len) => {
    const vals = arr.slice(from, from+len).filter(v=>v!=null);
    return vals.length ? Math.max(...vals) : null;
  };

  const levels = [
    { name:'10 m', ref:'Superficie', windKey:'windspeed_10m', gustKey:'windgusts_10m', color:'#7aadcc' },
    { name:'80 m', ref:'~Arbolado / pasos montañosos', windKey:'windspeed_80m', gustKey:null, color:'#5a8db5' },
    { name:'120 m', ref:'Crestas expuestas / vuelo', windKey:'windspeed_120m', gustKey:null, color:'#3a6d95' },
  ];
  const maxWind = Math.max(
    ...levels.map(l => avg(h[l.windKey], cwIdx, n6) || 0)
  ) || 1;

  const tbody = document.getElementById('alt-table-body');
  tbody.innerHTML = '';
  levels.forEach(l => {
    const spd = avg(h[l.windKey], cwIdx, n6);
    const gust = l.gustKey ? maxOf(h[l.gustKey], cwIdx, n6) : null;
    const pct = spd ? Math.min(100, (spd/maxWind)*100) : 0;
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td class="alt-name">${l.name}</td>
      <td style="color:#888;font-size:11px">${l.ref}</td>
      <td><strong style="color:${spd>80?'#b03a2e':spd>50?'#e8a020':l.color}">${spd!=null?Math.round(spd)+' km/h':'—'}</strong></td>
      <td class="wind-bar-cell">
        <div class="wind-bar-bg"><div class="wind-bar-fill" style="width:${pct}%;background:${l.color}"></div></div>
      </td>
      <td style="color:#888;font-size:12px">${gust!=null?'≤ '+Math.round(gust)+' km/h':'—'}</td>
    `;
    tbody.appendChild(tr);
  });
}

// ── METRICS GRID ──────────────────────────────────────────────────────────────
function renderMetrics(data, cwIdx) {
  const h = data.hourly;
  const d48 = Math.min(48, h.time.length - cwIdx);
  const d24 = Math.min(24, d48);

  const slice48 = (k) => h[k].slice(cwIdx, cwIdx+d48).filter(v=>v!=null);
  const slice24 = (k) => h[k].slice(cwIdx, cwIdx+d24).filter(v=>v!=null);
  const maxArr = (arr) => arr.length ? Math.max(...arr) : null;
  const minArr = (arr) => arr.length ? Math.min(...arr) : null;
  const sumArr = (arr) => arr.reduce((a,b)=>a+b,0);

  const maxGust    = maxArr(slice48('windgusts_10m'));
  const maxCAPE    = maxArr(slice48('cape'));
  const freezeH    = h.freezinglevel_height[cwIdx];
  const minVis     = minArr(slice24('visibility'));
  const totalPrecip= sumArr(slice48('precipitation'));
  const totalSnow  = sumArr(slice48('snowfall'));
  const uvMax      = maxArr(data.daily.uv_index_max ? [data.daily.uv_index_max[0]] : [0]);
  const maxWind80  = maxArr(slice48('windspeed_80m'));

  const metrics = [
    {
      icon:'💨', label:'Ráfaga máx. (48h)',
      value: maxGust!=null ? Math.round(maxGust) : '—',
      unit:'km/h',
      sub: maxGust>80?'⚠️ Viento extremo':maxGust>50?'Viento fuerte':'Normal',
      alert: maxGust>80?'rojo':maxGust>50?'amarillo':''
    },
    {
      icon:'🏔️', label:'Viento en altura (80m)',
      value: maxWind80!=null ? Math.round(maxWind80) : '—',
      unit:'km/h',
      sub:'Máximo 48h en cresta',
      alert: maxWind80>80?'rojo':maxWind80>50?'amarillo':''
    },
    {
      icon:'🧊', label:'Nivel de congelamiento',
      value: freezeH!=null ? Math.round(freezeH) : '—',
      unit:'m',
      sub:'Isoterma 0°C actual',
      alert:''
    },
    {
      icon:'⚡', label:'CAPE máx. (48h)',
      value: maxCAPE!=null ? Math.round(maxCAPE) : '—',
      unit:'J/kg',
      sub: maxCAPE>1500?'⚠️ Alto riesgo convectivo':maxCAPE>500?'Potencial tormenta':'Estable',
      alert: maxCAPE>1500?'amarillo':''
    },
    {
      icon:'🌧️', label:'Precipitación total (48h)',
      value: totalPrecip.toFixed(1),
      unit:'mm',
      sub: totalPrecip>30?'Lluvia intensa':totalPrecip>10?'Lluvia moderada':'Escasa',
      alert: totalPrecip>30?'amarillo':''
    },
    {
      icon:'❄️', label:'Nieve total (48h)',
      value: totalSnow>0 ? totalSnow.toFixed(1) : '0',
      unit:'cm',
      sub: totalSnow>20?'⚠️ Nevada intensa':totalSnow>5?'Nevada moderada':'Sin nieve',
      alert: totalSnow>20?'amarillo':''
    },
    {
      icon:'👁️', label:'Visibilidad mín. (24h)',
      value: minVis!=null ? (minVis<10000?(minVis/1000).toFixed(1):'>10') : '—',
      unit:'km',
      sub: minVis<1000?'⚠️ Muy reducida':minVis<5000?'Reducida':'Buena',
      alert: minVis<1000?'rojo':minVis<5000?'amarillo':''
    },
    {
      icon:'☀️', label:'UV máx. hoy',
      value: uvMax!=null ? Math.round(uvMax) : '—',
      unit:'índice',
      sub: uvMax>=8?'Muy alto':uvMax>=6?'Alto':uvMax>=3?'Moderado':'Bajo',
      alert:''
    },
  ];

  const grid = document.getElementById('metrics-grid');
  grid.innerHTML = '';
  metrics.forEach(m => {
    const card = document.createElement('div');
    card.className = 'metric-card' + (m.alert?' alert-'+m.alert:'');
    card.innerHTML = `
      <div class="metric-icon">${m.icon}</div>
      <div class="metric-label">${m.label}</div>
      <div class="metric-value">${m.value} <span class="metric-unit">${m.unit}</span></div>
      <div class="metric-sub">${m.sub}</div>
    `;
    grid.appendChild(card);
  });
}

// ── RISK ASSESSMENT ───────────────────────────────────────────────────────────
function renderRisk(data, cwIdx) {
  const h = data.hourly;
  const d48 = Math.min(48, h.time.length - cwIdx);
  const d24 = Math.min(24, d48);

  const maxGust = Math.max(...h.windgusts_10m.slice(cwIdx,cwIdx+d48).filter(v=>v!=null), 0);
  const minVis  = Math.min(...h.visibility.slice(cwIdx,cwIdx+d24).filter(v=>v!=null), 99999);
  const maxCAPE = Math.max(...h.cape.slice(cwIdx,cwIdx+d48).filter(v=>v!=null), 0);
  const tempMin = Math.min(...h.temperature_2m.slice(cwIdx,cwIdx+d48).filter(v=>v!=null), 99);
  const totalSnow = h.snowfall.slice(cwIdx,cwIdx+d48).filter(v=>v!=null).reduce((a,b)=>a+b,0);

  let level = 'verde';
  const reasons = [];

  if (maxGust > 100) { level='rojo'; reasons.push(`Ráfagas extremas: ${Math.round(maxGust)} km/h — condiciones de huracán patagónico`); }
  else if (maxGust > 70) { if(level!=='rojo') level='rojo'; reasons.push(`Viento muy fuerte: ${Math.round(maxGust)} km/h en ráfagas`); }
  else if (maxGust > 50) { if(level==='verde') level='amarillo'; reasons.push(`Viento fuerte: ${Math.round(maxGust)} km/h en ráfagas`); }

  if (minVis < 500) { level='rojo'; reasons.push(`Visibilidad prácticamente nula: ${Math.round(minVis)} m`); }
  else if (minVis < 2000) { if(level!=='rojo') level='rojo'; reasons.push(`Visibilidad muy reducida: ${(minVis/1000).toFixed(1)} km`); }
  else if (minVis < 5000) { if(level==='verde') level='amarillo'; reasons.push(`Visibilidad reducida: ${(minVis/1000).toFixed(1)} km`); }

  if (totalSnow > 25) { if(level!=='rojo') level='rojo'; reasons.push(`Nevada intensa: ${totalSnow.toFixed(0)} cm en 48h`); }
  else if (totalSnow > 10) { if(level==='verde') level='amarillo'; reasons.push(`Nevada moderada: ${totalSnow.toFixed(1)} cm`); }

  if (maxCAPE > 1500) { if(level==='verde') level='amarillo'; reasons.push(`Alto potencial convectivo: CAPE ${Math.round(maxCAPE)} J/kg`); }

  if (tempMin < -5 && maxGust > 30) { if(level==='verde') level='amarillo'; reasons.push(`Riesgo de tormenta de nieve y congelamiento`); }

  const msgs = {
    verde:    { title:'Condiciones favorables', emoji:'✅', sub:'Sin alertas para las próximas 48 horas.' },
    amarillo: { title:'Precaución recomendada', emoji:'⚠️', sub:'' },
    rojo:     { title:'Condiciones adversas', emoji:'🔴', sub:'' },
  };
  const msg = msgs[level];

  const el = document.getElementById('risk-card');
  el.innerHTML = `
    <div class="risk-card ${level}">
      <div class="risk-dot ${level}">${msg.emoji}</div>
      <div>
        <div class="risk-title">${msg.title}</div>
        <div class="risk-reasons">${reasons.length ? reasons.join(' · ') : msg.sub}</div>
      </div>
    </div>
  `;
}

// ── SERVICE WORKER ─────────────────────────────────────────────────────────────
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js').catch(()=>{});
  });
}

// ── TOP BAR TEMPS ─────────────────────────────────────────────────────────────
(function() {
  const KEY = 'gp_topbar_v1', TTL = 30 * 60 * 1000;
  const cities = [
    { name:'Bariloche',   lat:-41.133, lon:-71.310 },
    { name:'Neuquén',     lat:-38.952, lon:-68.059 },
    { name:'Pta. Arenas', lat:-53.164, lon:-70.917 },
    { name:'Pto. Montt',  lat:-41.469, lon:-72.942 },
  ];
  function emoji(c) {
    if (c===0) return '☀️'; if (c<=2) return '🌤'; if (c===3) return '☁️';
    if (c<=48) return '🌫'; if (c<=67) return '🌧'; if (c<=77) return '❄️';
    if (c<=82) return '🌦'; if (c>=95) return '⛈'; return '🌡';
  }
  function update(data) {
    const el = document.getElementById('topbar-temps');
    if (el) el.textContent = data.map(d => `${d.emoji} ${d.name} ${Math.round(d.t)}°`).join(' · ');
  }
  window.addEventListener('load', async () => {
    try {
      const cached = localStorage.getItem(KEY);
      if (cached) { const { ts, data } = JSON.parse(cached); if (Date.now()-ts < TTL) { update(data); return; } }
      const results = await Promise.all(cities.map(c =>
        fetch(`https://api.open-meteo.com/v1/forecast?latitude=${c.lat}&longitude=${c.lon}&current_weather=true&timezone=auto`).then(r=>r.json())
      ));
      const data = results.map((r,i) => ({ name:cities[i].name, t:r.current_weather.temperature, emoji:emoji(r.current_weather.weathercode) }));
      localStorage.setItem(KEY, JSON.stringify({ ts:Date.now(), data }));
      update(data);
    } catch(e) {}
  });
})();
