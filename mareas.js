(function () {
  var $ = function (id) { return document.getElementById(id); };
  var DATA = null, SEL = null;

  function ahoraLocal(zona) {
    // "YYYY-MM-DD HH:MM:SS" en la zona de la estación
    var s = new Date().toLocaleString('sv-SE', { timeZone: zona });
    return { fecha: s.slice(0, 10), min: parseInt(s.slice(11, 13), 10) * 60 + parseInt(s.slice(14, 16), 10) };
  }
  function aMin(hhmm) { return parseInt(hhmm.slice(0, 2), 10) * 60 + parseInt(hhmm.slice(3, 5), 10); }
  function fm(m) { return m.toFixed(2).replace('.', ','); }
  function dur(min) {
    var h = Math.floor(min / 60), m = min % 60;
    return h > 0 ? h + ' h ' + (m < 10 ? '0' : '') + m + ' min' : m + ' min';
  }
  function bandera(p) { return p === 'Chile' ? '🇨🇱' : '🇦🇷'; }

  function proximas(e, now) {
    // próximas extremas desde ahora (hoy y mañana)
    var lista = [];
    e.hoy.forEach(function (x) { lista.push({ x: x, min: aMin(x.hora) }); });
    e.manana.forEach(function (x) { lista.push({ x: x, min: aMin(x.hora) + 1440 }); });
    return lista.filter(function (l) { return l.min > now.min; });
  }

  function filas(tbody, items, now, marcarSiguiente) {
    var sig = marcarSiguiente ? proximas(SEL, now)[0] : null;
    tbody.innerHTML = '';
    if (!items.length) {
      tbody.innerHTML = '<tr><td colspan="3" style="color:#888">Marea muy pequeña en este puerto: casi no hay diferencia entre pleamar y bajamar. Mirá la altura real medida más abajo.</td></tr>';
      return;
    }
    items.forEach(function (x) {
      var m = aMin(x.hora), tr = document.createElement('tr');
      if (marcarSiguiente) {
        if (m <= now.min) tr.className = 'pasada';
        else if (sig && sig.x === x) tr.className = 'siguiente';
      }
      tr.innerHTML = '<td class="hora">' + x.hora + '</td>' +
        '<td class="tipo-' + x.tipo + '">' + (x.tipo === 'pleamar' ? '▲ Pleamar' : '▼ Bajamar') + '</td>' +
        '<td class="alt">' + fm(x.altura) + ' m</td>';
      tbody.appendChild(tr);
    });
  }

  function grafico(e, now) {
    var svg = $('mr-grafico'), W = 640, H = 300, L = 44, R = 14, T = 16, B = 30;
    var est = e.curva_hoy; // cada 30 min desde 00:00 local
    var obs = (e.observado || []).filter(function (o) { return o.t.slice(0, 10) === now.fecha; })
      .map(function (o) { return { m: aMin(o.t.slice(11, 16)), h: o.h }; });
    var ys = est.concat(obs.map(function (o) { return o.h; }));
    var lo = Math.floor(Math.min.apply(null, ys) * 2) / 2 - 0.25, hi = Math.ceil(Math.max.apply(null, ys) * 2) / 2 + 0.25;
    var X = function (m) { return L + (m / 1440) * (W - L - R); };
    var Y = function (h) { return T + (1 - (h - lo) / (hi - lo)) * (H - T - B); };
    var s = '';
    // grilla horizontal
    var paso = (hi - lo) > 4 ? 1 : 0.5;
    for (var v = Math.ceil(lo / paso) * paso; v <= hi; v += paso) {
      s += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + Y(v) + '" y2="' + Y(v) + '" stroke="#e8e4dc"/>' +
        '<text x="' + (L - 6) + '" y="' + (Y(v) + 4) + '" text-anchor="end" font-size="11" fill="#888">' + fm(v) + '</text>';
    }
    for (var h = 0; h <= 24; h += 3) {
      s += '<text x="' + X(h * 60) + '" y="' + (H - 10) + '" text-anchor="middle" font-size="11" fill="#888">' + (h < 10 ? '0' : '') + h + 'h</text>';
    }
    s += '<text x="12" y="' + (T + 4) + '" font-size="10" fill="#aaa" transform="rotate(-90 12 ' + (H / 2) + ')" text-anchor="middle">metros</text>';
    // estimada
    var d = est.map(function (h, i) { return (i ? 'L' : 'M') + X(i * 30).toFixed(1) + ' ' + Y(h).toFixed(1); }).join(' ');
    s += '<path d="' + d + '" fill="none" stroke="#1d6fa5" stroke-width="2.5" stroke-linejoin="round"/>';
    // observada
    if (obs.length > 1) {
      var d2 = obs.map(function (o, i) { return (i ? 'L' : 'M') + X(o.m).toFixed(1) + ' ' + Y(o.h).toFixed(1); }).join(' ');
      s += '<path d="' + d2 + '" fill="none" stroke="#d9822b" stroke-width="2.5" stroke-linejoin="round"/>';
    }
    // extremas
    e.hoy.forEach(function (x) {
      var m = aMin(x.hora), pl = x.tipo === 'pleamar';
      s += '<circle cx="' + X(m) + '" cy="' + Y(x.altura) + '" r="4" fill="' + (pl ? '#1d6fa5' : '#8c6b4a') + '"/>' +
        '<text x="' + X(m) + '" y="' + (Y(x.altura) + (pl ? -9 : 17)) + '" text-anchor="middle" font-size="11" font-weight="600" fill="#333">' + x.hora + '</text>';
    });
    // ahora
    s += '<line x1="' + X(now.min) + '" x2="' + X(now.min) + '" y1="' + T + '" y2="' + (H - B) + '" stroke="#c0392b" stroke-width="1.5" stroke-dasharray="4 3"/>';
    svg.innerHTML = s;
  }

  var CUAD = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSO','SO','OSO','O','ONO','NO','NNO'];
  var CUAD_N = { N:'Norte', NNE:'Nor-noreste', NE:'Noreste', ENE:'Este-noreste', E:'Este', ESE:'Este-sudeste', SE:'Sudeste', SSE:'Sud-sudeste', S:'Sur', SSO:'Sud-sudoeste', SO:'Sudoeste', OSO:'Oeste-sudoeste', O:'Oeste', ONO:'Oeste-noroeste', NO:'Noroeste', NNO:'Nor-noroeste' };
  function cuad(d) { return CUAD[Math.round(((d % 360) + 360) % 360 / 22.5) % 16]; }
  function nudos(kmh) { return Math.round(kmh / 1.852); }
  // dir = de dónde VIENE el viento; la flecha apunta hacia donde sopla
  function flecha(d) { return '<span class="mr-flecha" style="transform:rotate(' + (d + 180) + 'deg)">↑</span>'; }
  function claseRacha(r) { return r >= 60 ? 'v-fuerte' : r >= 40 ? 'v-ojo' : ''; }

  function viento(e, now) {
    var v = e.viento, box = $('mr-viento-ahora'), tb = document.querySelector('#mr-tabla-viento tbody');
    tb.innerHTML = '';
    if (!v) {
      box.innerHTML = '<div class="mr-v-nota" style="margin:0">Viento no disponible en este momento.</div>';
      return;
    }
    var a = v.actual, c = cuad(a.dir);
    var aviso = '';
    if (a.racha >= 60) aviso = '<span class="mr-chip aviso-vf">Rachas muy fuertes (' + nudos(a.racha) + ' nudos): extremar precauciones</span>';
    else if (a.racha >= 40) aviso = '<span class="mr-chip aviso-v">Rachas fuertes (' + nudos(a.racha) + ' nudos): precaución en el agua</span>';
    var brujula = '<svg class="mr-brujula" viewBox="0 0 100 100" aria-hidden="true">' +
      '<circle cx="50" cy="50" r="44" fill="#f7f5f0" stroke="#d8d2c6" stroke-width="2"/>' +
      '<text x="50" y="17" text-anchor="middle" font-size="11" font-weight="700" fill="#555">N</text>' +
      '<text x="50" y="93" text-anchor="middle" font-size="11" fill="#999">S</text>' +
      '<text x="91" y="54" text-anchor="middle" font-size="11" fill="#999">E</text>' +
      '<text x="9" y="54" text-anchor="middle" font-size="11" fill="#999">O</text>' +
      '<g transform="rotate(' + (a.dir + 180) + ' 50 50)"><path d="M50 22 L60 58 L50 50 L40 58 Z" fill="#1d6fa5"/><line x1="50" y1="50" x2="50" y2="76" stroke="#1d6fa5" stroke-width="3" stroke-linecap="round"/></g>' +
      '</svg>';
    box.innerHTML = '<div class="mr-v-ppal">' + brujula + '<div class="mr-v-dato">' +
      '<div class="cuad">' + c + ' <small>' + CUAD_N[c] + ' · ' + a.dir + '°</small></div>' +
      '<div class="vel">' + a.vel + ' km/h <small>· ' + nudos(a.vel) + ' nudos</small></div>' +
      '<div class="rac">Rachas ' + a.racha + ' km/h <small>· ' + nudos(a.racha) + ' nudos</small></div></div></div>' +
      (aviso ? '<div class="mr-chips">' + aviso + '</div>' : '') +
      '<div class="mr-v-nota">El cuadrante indica de dónde sopla el viento (viento del ' + CUAD_N[c] + '). La flecha apunta hacia donde va.</div>';

    // tabla: de la hora actual en adelante, cada 3 h (próximas 24 h)
    var hh = Math.floor(now.min / 60), mostradas = 0;
    var hoy = now.fecha;
    v.horas.forEach(function (x) {
      var hx = parseInt(x.h.slice(0, 2), 10);
      var abs = (x.f === hoy ? 0 : 24) + hx;
      if (abs < hh || abs > hh + 24 || (abs - hh) % 3 !== 0) return;
      var cx = cuad(x.dir), tr = document.createElement('tr');
      if (abs === hh) tr.className = 'v-actual';
      tr.innerHTML = '<td class="hora" style="font-size:15px">' + x.h + (x.f !== hoy ? ' <small style="color:#888;font-weight:400">mañana</small>' : '') + '</td>' +
        '<td>' + flecha(x.dir) + '<strong>' + cx + '</strong> <small style="color:#888">' + x.dir + '°</small></td>' +
        '<td class="alt">' + x.vel + ' km/h <small style="color:#888;font-weight:400">' + nudos(x.vel) + ' nd</small></td>' +
        '<td class="alt ' + claseRacha(x.racha) + '">' + x.racha + ' km/h <small style="font-weight:400">' + nudos(x.racha) + ' nd</small></td>';
      tb.appendChild(tr);
      mostradas++;
    });
  }

  function mostrar(cod) {
    SEL = DATA.estaciones.filter(function (x) { return x.codigo === cod; })[0];
    if (!SEL) return;
    var e = SEL, now = ahoraLocal(e.zona);
    try { history.replaceState(null, '', '#' + cod); } catch (_) {}
    document.querySelectorAll('#mr-puertos .city-btn').forEach(function (b) { b.classList.toggle('active', b.dataset.cod === cod); });

    $('mr-nombre').textContent = e.nombre;
    $('mr-sub').textContent = bandera(e.pais) + ' ' + e.pais + ' · ' + e.region + ' · hora local' + (e.actual ? '' : ' · estimación por modelo oceánico');

    // próxima marea
    var pr = proximas(e, now)[0];
    $('mr-prox').innerHTML = pr
      ? 'Próxima ' + (pr.x.tipo === 'pleamar' ? 'pleamar' : 'bajamar') + ' en ' + dur(pr.min - now.min) +
        '<b>' + pr.x.hora + ' · ' + fm(pr.x.altura) + ' m</b>'
      : 'Sin datos de próxima marea';

    filas(document.querySelector('#mr-tabla-hoy tbody'), e.hoy, now, true);
    filas(document.querySelector('#mr-tabla-man tbody'), e.manana, now, false);

    // chips: rango del día y viva/muerta
    var chips = '';
    if (e.hoy.length >= 2) {
      var hs = e.hoy.map(function (x) { return x.altura; });
      var rango = Math.max.apply(null, hs) - Math.min.apply(null, hs);
      var rm = e.rango_mes[1] - e.rango_mes[0];
      var r = rm > 0 ? rango / rm : 0;
      chips += '<span class="mr-chip">Diferencia del día: ' + fm(rango) + ' m</span>';
      if (r >= 0.8) chips += '<span class="mr-chip viva">Marea viva (grande): corrientes más fuertes</span>';
      else if (r <= 0.5) chips += '<span class="mr-chip muerta">Marea muerta (chica): corrientes más suaves</span>';
      else chips += '<span class="mr-chip">Marea intermedia</span>';
    }
    $('mr-chips').innerHTML = chips;

    grafico(e, now);
    viento(e, now);

    // altura real
    var sinReal = !e.actual;
    $('mr-titulo-real').textContent = sinReal ? 'Altura real del mar' : 'Altura real del mar — medida ahora';
    $('mr-leg-obs').style.display = sinReal ? 'none' : '';
    if (!e.actual) {
      $('mr-real').innerHTML = '<div class="m" style="grid-column:1/-1"><div class="k" style="margin:0 0 4px">Sin mareógrafo en este puerto</div>' +
        '<div class="n" style="font-size:13px">No hay un instrumento que mida la altura real del mar en ' + e.nombre + '. La marea que ves es una estimación de un modelo oceánico, con mayor margen de error (puede diferir 30 a 60 minutos y varios decímetros) que la de los puertos con medición real. Tomala como orientación.</div></div>';
      $('mr-puerto').style.display = '';
      return;
    }
    var a = e.actual, flecha = a.tendencia === 'subiendo' ? '▲' : a.tendencia === 'bajando' ? '▼' : '■';
    var estAhora = e.curva_hoy[Math.min(47, Math.round(now.min / 30))];
    var dif = a.altura - estAhora;
    var obsMax = Math.max.apply(null, (e.observado || []).map(function (o) { return o.h; }));
    var obsMin = Math.min.apply(null, (e.observado || []).map(function (o) { return o.h; }));
    $('mr-real').innerHTML =
      '<div class="m ' + a.tendencia + '"><div class="v">' + fm(a.altura) + ' <small>m</small></div><div class="k">Altura real ahora</div>' +
        '<div class="n">Medida a las ' + a.hora + ' (' + (a.edad_min > 90 ? 'hace ' + dur(a.edad_min) : 'tiempo real') + ')</div></div>' +
      '<div class="m ' + a.tendencia + '"><div class="v">' + flecha + ' <small style="font-size:19px;color:inherit">' + a.tendencia + '</small></div><div class="k">Tendencia última hora</div>' +
        '<div class="n">El mar está ' + a.tendencia + '</div></div>' +
      '<div class="m"><div class="v">' + (dif >= 0 ? '+' : '−') + fm(Math.abs(dif)) + ' <small>m</small></div><div class="k">Real vs. estimada</div>' +
        '<div class="n">' + (Math.abs(dif) < 0.15 ? 'Coincide con la estimación' : dif > 0 ? 'Más alto que lo estimado (viento/presión)' : 'Más bajo que lo estimado (viento/presión)') + '</div></div>' +
      '<div class="m"><div class="v">' + fm(obsMin) + ' – ' + fm(obsMax) + ' <small>m</small></div><div class="k">Mín. y máx. últimas 24 h</div>' +
        '<div class="n">Mediciones reales</div></div>';

    $('mr-puerto').style.display = '';
  }

  function resumen() {
    var tb = document.querySelector('#mr-resumen tbody');
    tb.innerHTML = '';
    DATA.estaciones.forEach(function (e) {
      var now = ahoraLocal(e.zona), pr = proximas(e, now);
      var pl = pr.filter(function (p) { return p.x.tipo === 'pleamar'; })[0];
      var ba = pr.filter(function (p) { return p.x.tipo === 'bajamar'; })[0];
      var f = function (p) {
        if (!p) return '—';
        return p.x.hora + (p.min >= 1440 ? ' (mañana)' : '') + ' · ' + fm(p.x.altura) + ' m';
      };
      var fl = !e.actual ? '' : e.actual.tendencia === 'subiendo' ? '▲ subiendo' : e.actual.tendencia === 'bajando' ? '▼ bajando' : '■ estable';
      var tr = document.createElement('tr');
      tr.className = 'puerto-link';
      tr.innerHTML = '<td><strong>' + bandera(e.pais) + ' ' + e.nombre + '</strong></td><td class="alt">' + (e.actual ? fm(e.actual.altura) + ' m' : '—') + '</td><td>' + (e.actual ? fl : 'modelo') + '</td><td>' + f(pl) + '</td><td>' + f(ba) + '</td>';
      tr.onclick = function () { mostrar(e.codigo); window.scrollTo({ top: 0, behavior: 'smooth' }); };
      tb.appendChild(tr);
    });
    $('mr-resumen-sec').style.display = '';
  }

  function init() {
    fetch('mareas.json?v=' + Math.floor(Date.now() / 600000))
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        DATA = d;
        $('mr-cargando').style.display = 'none';
        var cont = $('mr-puertos');
        d.estaciones.forEach(function (e) {
          var b = document.createElement('button');
          b.className = 'city-btn'; b.dataset.cod = e.codigo;
          b.textContent = bandera(e.pais) + ' ' + e.nombre;
          b.onclick = function () {
            mostrar(e.codigo);
            if (typeof gtag === 'function') gtag('event', 'mareas_puerto', { puerto: e.codigo });
          };
          cont.appendChild(b);
        });
        var gen = new Date(d.generado.replace('Z', ':00Z'));
        $('mr-fuente').textContent = 'Fuente: ' + d.fuente + '. Actualizado ' +
          gen.toLocaleString('es-AR', { dateStyle: 'short', timeStyle: 'short' }) + '.';
        var inicial = (location.hash || '').slice(1);
        if (!d.estaciones.some(function (e) { return e.codigo === inicial; })) inicial = d.estaciones[0].codigo;
        mostrar(inicial);
        resumen();
      })
      .catch(function () {
        $('mr-cargando').style.display = 'none';
        $('mr-error').style.display = '';
      });
  }
  init();
})();
