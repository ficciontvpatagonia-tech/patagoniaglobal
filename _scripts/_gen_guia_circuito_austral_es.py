#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera notas/guia-circuito-austral.html (ES) a partir de la estructura de guia-esquel.html.
Preview local: NO publica. Cuerpo = lista de bloques; head/pie se heredan de Esquel."""
import re, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
esq = open(f"{BASE}/notas/guia-esquel.html", encoding="utf-8").read()

SLUG = "guia-circuito-austral"
TITLE = "Circuito Austral: 12 días de El Calafate a Ushuaia por Argentina y Chile — GLOBALpatagonia"
DESC = ("Itinerario de 12 días por la Patagonia austral en dos países: El Calafate, Torres del Paine, Puerto Natales, Punta Arenas y Ushuaia. Día por día, cómo moverse entre tramos, cruces de frontera y consejos prácticos.")
HERO = "fotos/CIUDADES/calafate-glaciar-tempanos-aereo.webp"
HERO_ABS = "https://globalpatagonia.org/" + HERO

# ---- cabeza: reemplazos sobre la de Esquel
head = esq[:esq.index('<div class="hero">')]
head = head.replace("Esquel: guía de viaje — La puerta de la Patagonia — GLOBALpatagonia", TITLE)
head = re.sub(r'Esquel es una ciudad tranquila[^"]*?Trevelin\.', DESC, head)
head = head.replace("guia-esquel", SLUG)
head = head.replace("https://globalpatagonia.org/fotos/CIUDADES/esquel-trochita-nieve.webp", HERO_ABS)
head = head.replace("https://globalpatagonia.org/fotos/CIUDADES/esquel-trochita-nieve.jpg", HERO_ABS)
head = head.replace('"@type":"TouristDestination","name":"Esquel"', '"@type":"TouristTrip","name":"Circuito Austral: El Calafate, Torres del Paine, Punta Arenas y Ushuaia"')
head = head.replace('es_AR', 'es_AR')
# CSS extra: mapa y tabla
extra_css = """
    .mapa-wrap{margin:8px 0 8px;background:white;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.07);overflow:hidden;}
    .mapa-wrap img{width:100%;height:auto;display:block;}
    .mapa-cap{font-size:12px;color:#7a7a7a;font-style:italic;padding:10px 16px 12px;}
    .tabla-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;}
    .gp-tabla{width:100%;border-collapse:collapse;background:white;border-radius:6px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.07);font-size:14px;}
    .gp-tabla th{background:var(--verde);color:white;text-align:left;padding:12px 14px;font-size:12px;letter-spacing:1px;text-transform:uppercase;}
    .gp-tabla td{padding:12px 14px;border-bottom:1px solid #e8e5e0;vertical-align:top;line-height:1.5;color:#2a2a2a;}
    .gp-tabla tr:last-child td{border-bottom:none;}
    .gp-tabla td:first-child{font-weight:700;color:var(--verde);}
    .aviso-salud{background:#fff7e6;border:1px solid #f0d9a8;border-left:6px solid #e59500;border-radius:6px;padding:22px 24px;margin-top:6px;box-shadow:0 2px 8px rgba(0,0,0,0.05);}
    .aviso-salud h3{font-family:'Playfair Display',serif;font-size:20px;color:#7a4a00;margin-bottom:10px;}
    .aviso-salud p{font-size:15px;line-height:1.7;color:#3a3a3a;margin:0 0 10px;}
    .aviso-salud ul{margin:6px 0 12px 20px;}
    .aviso-salud li{font-size:15px;line-height:1.65;color:#3a3a3a;margin-bottom:6px;}
    .aviso-salud .fin{font-size:13px;color:#7a5a20;margin:10px 0 0;}
    .nota-oficial{font-size:13px;color:#5a6070;background:#e9f1f6;border-left:4px solid #8ab8d4;padding:12px 16px;border-radius:3px;margin-top:14px;line-height:1.6;}
"""
head = head.replace("  </style>", extra_css + "  </style>", 1)

def img(src, alt, pos=None):
    st = f' style="object-position:{pos};"' if pos else ""
    return f'<div class="foto-ratio"><img src="../fotos/CIUDADES/{src}" alt="{alt}" loading="lazy"{st}/></div>'
def item(src, alt, h, p):
    return f'''    <div class="guia-item">
      {img(src, alt)}
      <div class="guia-item-body">
        <h3>{h}</h3>
        <p>{p}</p>
      </div>
    </div>
'''

def itemnoimg(h, p, extra=""):
    return f'''    <div class="guia-item guia-item-noimg">
      <h3>{h}</h3>
      <p>{p}</p>{extra}
    </div>
'''

hero = f'''<div class="hero">
  <img src="../{HERO}" alt="El glaciar Perito Moreno con témpanos azules sobre el Lago Argentino, primera parada del Circuito Austral"/>
  <div class="hero-overlay">
    <div class="hero-tag">🗺️ Guía de viaje · Recorrido</div>
    <div class="hero-titulo">Circuito Austral</div>
    <div class="hero-tagline">12 días de los glaciares al fin del mundo, por Argentina y Chile</div>
  </div>
</div>

<div class="container">
  <a href="../" class="volver">← Inicio</a>
    <div class="lang-switcher">
      <a href="{SLUG}.html" class="active">🇦🇷 ES</a>
      <a href="{SLUG}-en.html">🇬🇧 EN</a>
      <a href="{SLUG}-pt.html">🇧🇷 PT</a>
      <a href="{SLUG}-zh.html">🇨🇳 中文</a>
    </div>

  <p class="guia-intro">Un solo viaje, dos países y cinco paradas: el glaciar Perito Moreno en El Calafate, las torres de granito de Torres del Paine, Puerto Natales, Punta Arenas sobre el estrecho de Magallanes y Ushuaia, la ciudad más austral del mundo. Son 12 días de recorrido por tierra, con dos cruces de frontera, que van bajando hacia el sur hasta llegar al final del continente. Se puede hacer en bus o en auto alquilado: se retira en El Calafate y se devuelve en Ushuaia, o al revés.</p>

  <!-- RESUMEN -->
  <div class="guia-seccion">
    <h2>El recorrido, día por día</h2>
    <div class="tabla-scroll">
      <table class="gp-tabla">
        <thead><tr><th>Días</th><th>Parada</th><th>Qué hacer</th><th>Traslado</th></tr></thead>
        <tbody>
          <tr><td>1 a 3</td><td>El Calafate 🇦🇷</td><td>Glaciar Perito Moreno, pasarelas y navegación; laguna Nimez</td><td>Llegada en avión</td></tr>
          <tr><td>4</td><td>Puerto Natales 🇨🇱</td><td>Llegada y preparación para el parque</td><td>Bus con cruce de frontera, 4 a 7 h</td></tr>
          <tr><td>5 a 7</td><td>Torres del Paine 🇨🇱</td><td>Lago Pehoé, Base de las Torres, glaciar Grey</td><td>Bus o excursión desde Puerto Natales</td></tr>
          <tr><td>8</td><td>Punta Arenas 🇨🇱</td><td>Ciudad sobre el estrecho de Magallanes</td><td>Bus, unas 3 h</td></tr>
          <tr><td>9</td><td>Punta Arenas 🇨🇱</td><td>Excursión a una pingüinera (en temporada) y paseo por el centro</td><td>—</td></tr>
          <tr><td>10</td><td>En ruta a Ushuaia</td><td>Cruce del Estrecho en transbordador y frontera en San Sebastián</td><td>Bus, 10 a 12 h</td></tr>
          <tr><td>11 y 12</td><td>Ushuaia 🇦🇷</td><td>Parque Nacional Tierra del Fuego y navegación por el canal Beagle</td><td>Regreso en avión</td></tr>
        </tbody>
      </table>
    </div>
    <div class="nota-oficial">Si querés hacer el circuito W de Torres del Paine (4 a 5 días), sumá esos días a la parte chilena: este itinerario incluye la Base de las Torres, que se hace en un día.</div>
  </div>

  <!-- MAPA -->
  <div class="guia-seccion">
    <h2>El mapa del recorrido</h2>
    <div class="mapa-wrap">
      <img src="../fotos/CIUDADES/circuito-austral-mapa.webp" alt="Mapa del Circuito Austral: El Calafate, Torres del Paine, Puerto Natales, Punta Arenas y Ushuaia, con la ruta y los cruces de frontera" loading="lazy"/>
      <div class="mapa-cap">Mapa propio de GLOBALpatagonia con datos de OpenStreetMap. Las rutas siguen los caminos principales; el cruce del Estrecho de Magallanes se hace en transbordador. Los rombos marcan los cruces de frontera.</div>
    </div>
  </div>

  <!-- DISTANCIAS -->
  <div class="guia-seccion">
    <h2>Distancias entre paradas</h2>
    <div class="tabla-scroll">
      <table class="gp-tabla">
        <thead><tr><th>Tramo</th><th>Distancia aprox.</th><th>Tiempo aprox.</th><th>Cómo</th></tr></thead>
        <tbody>
          <tr><td>El Calafate → Puerto Natales</td><td>350 km</td><td>4 a 7 h</td><td>Bus, con cruce de frontera</td></tr>
          <tr><td>Puerto Natales → Torres del Paine</td><td>110 km</td><td>2 h</td><td>Bus o auto, hasta la portería Laguna Amarga</td></tr>
          <tr><td>Puerto Natales → Punta Arenas</td><td>250 km</td><td>3 h</td><td>Bus</td></tr>
          <tr><td>Punta Arenas → Ushuaia</td><td>600 km</td><td>10 a 12 h</td><td>Bus, con transbordador en el Estrecho y frontera en San Sebastián</td></tr>
          <tr><td>Recorrido total por tierra</td><td>1.200 km</td><td>—</td><td>De El Calafate a Ushuaia, sin la excursión a Torres del Paine</td></tr>
        </tbody>
      </table>
    </div>
    <div class="nota-oficial">Distancias medidas sobre los caminos principales del mapa y redondeadas; los tiempos incluyen controles de frontera y espera del transbordador. El clima y la temporada pueden cambiarlos: confirmá siempre con la empresa de bus.</div>
  </div>

  <!-- CUÁNDO IR -->
  <div class="guia-seccion">
    <h2>¿Cuándo ir?</h2>
    <div class="cuando-grid">
      <div class="cuando-card">
        <div class="mes">Nov · Dic</div>
        <div class="titulo-cuando">Comienzo de temporada</div>
        <p>Días largos, menos gente y precios más bajos. Algunos servicios recién abren y el viento ya es fuerte en el parque.</p>
      </div>
      <div class="cuando-card">
        <div class="mes">Ene · Feb</div>
        <div class="titulo-cuando">Pleno verano</div>
        <p>El mejor clima y todos los servicios abiertos, pero es temporada alta: conviene reservar vuelos, buses y alojamiento con mucha anticipación.</p>
      </div>
      <div class="cuando-card">
        <div class="mes">Mar · Abr</div>
        <div class="titulo-cuando">Otoño: colores y calma</div>
        <p>Bosques rojizos y menos visitantes. Hay menos salidas de buses y la pingüinera ya no está activa.</p>
      </div>
    </div>
    <div class="nota-oficial">Fuera de la temporada de verano muchos servicios reducen sus frecuencias o no operan, sobre todo el bus entre Punta Arenas y Ushuaia y los barcos. En invierno, además, el circuito W y la Base de las Torres exigen un guía habilitado por CONAF.</div>
  </div>

  <!-- LAS PARADAS -->
  <div class="guia-seccion">
    <h2>Las cinco paradas</h2>
{item("calafate-glaciar-frente-hielo.webp", "Frente de hielo del glaciar Perito Moreno en El Calafate", "Días 1 a 3 · El Calafate", "Es la puerta del Parque Nacional Los Glaciares, Patrimonio de la Humanidad de la UNESCO. El Perito Moreno se ve desde las pasarelas, en barco o caminando sobre el hielo. Quedan tiempo y energía para la laguna Nimez y para el pueblo. <a href='guia-calafate.html'>Ver la guía de El Calafate →</a>")}
{item("torres-del-paine-base-torres-laguna.webp", "Laguna turquesa a los pies de las torres de granito de Torres del Paine", "Días 5 a 7 · Torres del Paine", "Tres días alcanzan para lo esencial: un día para los miradores del lago Pehoé y los guanacos, otro para la caminata a la Base de las Torres (8 a 10 horas) y otro para el glaciar Grey. <a href='guia-torres-del-paine.html'>Ver la guía de Torres del Paine →</a>")}
{item("puerto-natales-costanera-aerea.webp", "Vista aérea de la costanera de Puerto Natales sobre el seno Última Esperanza", "Día 4 y 8 · Puerto Natales", "Es la base para el parque, a unos 110 km: hostales, restaurantes y tiendas de equipo. Sirve de escala en la ida y la vuelta. Está sobre el seno Última Esperanza, con vistas a los canales y a las montañas del fondo.")}
{item("punta-arenas-cementerio-cipreses.webp", "Cipreses podados en forma de arco y una cruz blanca en el Cementerio Municipal de Punta Arenas", "Días 8 y 9 · Punta Arenas", "La mayor ciudad del estrecho de Magallanes, con una costanera de casas de colores y una plaza central de aire señorial. Desde acá salen las excursiones a las pingüineras, que funcionan solo en temporada: consultá fechas y reservá antes de viajar.")}
{item("ushuaia-ciudad-montana.webp", "Ushuaia entre las montañas y el canal Beagle", "Días 11 y 12 · Ushuaia", "La ciudad más austral del mundo, entre la cordillera y el canal Beagle. Dos días dan para el Parque Nacional Tierra del Fuego y para navegar el canal, con lobos marinos y faros. <a href='guia-ushuaia.html'>Ver la guía de Ushuaia →</a>")}
  </div>

  <!-- GASTRONOMÍA -->
  <div class="guia-seccion">
    <h2>Qué comer en el camino</h2>
{item("calafate-cordero-estofado.webp", "Cordero patagónico estofado, plato típico de El Calafate", "Cordero patagónico", "El plato de toda la ruta, al asador o estofado. Se come en El Calafate, en Puerto Natales y en Ushuaia, y en las estancias se sirve con el asado a la vista. Para el postre, buscá los dulces y helados de calafate, la baya que da nombre al pueblo.")}
{item("ushuaia-centolla-entera.webp", "Centolla entera, el marisco más buscado del extremo sur", "Centolla", "La reina del Beagle y del estrecho de Magallanes. Se pide en Punta Arenas, en Puerto Natales y sobre todo en Ushuaia, al natural o gratinada. Es un plato caro: consultá el precio antes de pedir.")}
{item("ushuaia-cordero-asador.webp", "Cordero fueguino asado al asador en Ushuaia", "Cordero fueguino y pescados del Beagle", "En Ushuaia el cordero se asa a la cruz, y también hay trucha, merluza negra y mariscos de las aguas frías del canal. Una cena así es el cierre natural de este viaje.")}
    <div class="comer-grid">
      <div class="comer-item">
        <div class="comer-item-body">
          <h4>Cerveza artesanal</h4>
          <div class="comer-dir">El Calafate · Puerto Natales · Ushuaia</div>
          <p>Cada pueblo tiene su cervecería. Es una buena parada después de una caminata larga.</p>
        </div>
      </div>
      <div class="comer-item">
        <div class="comer-item-body">
          <h4>Pisco sour y vinos chilenos</h4>
          <div class="comer-dir">Puerto Natales · Punta Arenas</div>
          <p>Del lado chileno, el pisco sour acompaña casi cualquier mesa. Los vinos del Valle Central se encuentran en todas las cartas.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- OTRAS ATRACCIONES -->
  <div class="guia-seccion">
    <h2>Otras atracciones en cada parada</h2>
{item("calafate-pueblo-aereo.webp", "Vista aérea de El Calafate sobre la costa del Lago Argentino", "El Calafate: más allá del glaciar", "Caminá por la reserva Laguna Nimez, a pocos minutos del centro, para ver flamencos y aves de laguna. El Glaciarium, un museo del hielo sobre la ruta al glaciar, y las estancias donde se ve la esquila y se prueba el asado completan una jornada sin glaciar.")}
{item("chalten-fitz-roy-atardecer.webp", "El cerro Fitz Roy iluminado al atardecer en El Chaltén", "Excursión opcional: El Chaltén", "Si tenés un día extra, El Chaltén está a unas tres horas de El Calafate y es la capital argentina del trekking, al pie del Fitz Roy. Funciona como excursión de un día o con una noche.")}
{item("cueva-del-milodon-interior.webp", "Interior de la cueva del Milodón con la boca abierta hacia el paisaje de Última Esperanza", "Puerto Natales: la cueva del Milodón", "A unos 25 km al norte de Puerto Natales, en la cueva del Milodón se encontraron restos de un perezoso gigante de hace miles de años. Es una visita corta, de media jornada, que suma a un día de descanso entre caminatas.")}
{item("punta-arenas-fuerte-bulnes.webp", "Casas de madera y capilla del Fuerte Bulnes frente al estrecho de Magallanes", "Punta Arenas: Fuerte Bulnes", "A unos 55 km al sur de la ciudad, sobre el estrecho, está el Fuerte Bulnes, fundado en 1843: el primer asentamiento chileno en la zona. Lo que se visita hoy es una reconstrucción, con casas de madera, capilla y empalizada, y un buen paseo de medio día por la costa.")}
{item("punta-arenas-isla-magdalena-pinguinos.webp", "Una visitante fotografía pingüinos de Magallanes en la isla Magdalena", "Punta Arenas: pingüinos y ciudad", "En temporada, las pingüineras de Seno Otway o de la isla Magdalena, a la que se llega en barco, son la excursión más buscada. En la ciudad alcanzan dos horas para la plaza Muñoz Gamero, el Cementerio Municipal y el mirador del cerro de la Cruz. Las salidas dependen del clima y del calendario: reservá con anticipación.")}
{item("ushuaia-tren-fin-del-mundo.webp", "El Tren del Fin del Mundo, una locomotora a vapor roja con vagones verdes, avanza entre la nieve en Tierra del Fuego", "Ushuaia: el Tren del Fin del Mundo", "Una locomotora a vapor recorre un tramo de la antigua ruta del presidio, entre bosques de lenga y el río Pipo, dentro del Parque Nacional Tierra del Fuego. Es un paseo de unas dos horas, muy pedido: reservá con anticipación en temporada alta.")}
{item("ushuaia-beagle-faro-eclaireures.webp", "Faro Les Éclaireurs en el canal Beagle, cerca de Ushuaia", "Ushuaia: canal y museos", "La navegación por el Beagle llega al faro Les Éclaireurs y a las islas de lobos marinos y cormoranes. En tierra están el Museo del Fin del Mundo y el antiguo presidio, hoy museo marítimo y penal. Con tiempo, el glaciar Martial se alcanza en una caminata corta desde la ciudad.")}
{item("ushuaia-laguna-esmeralda.webp", "Laguna Esmeralda entre montañas cerca de Ushuaia", "Laguna Esmeralda", "Una caminata de media jornada por turbales y bosque de lengas hasta una laguna de agua turquesa al pie del glaciar. Es la excursión más recomendada para quien llega con ganas de caminar, pero no con muchas fuerzas.")}
    <div class="nota-oficial">Las excursiones con barco o a pingüineras y los trenes turísticos funcionan en temporada y dependen del clima. Reservá con anticipación y confirmá horarios y precios con cada operador.</div>
  </div>

  <!-- CÓMO MOVERSE -->
  <div class="guia-seccion">
    <h2>Cómo moverse entre tramos: en bus</h2>
    <div class="llegar-grid">
      <div class="llegar-item">
        <div class="icono">🚌</div>
        <h4>El Calafate – Puerto Natales</h4>
        <p>Bus con cruce de frontera: entre 4 y 7 horas según la empresa y la demora en el control. En temporada alta hay varias salidas diarias; fuera de temporada, menos y no todos los días.</p>
      </div>
      <div class="llegar-item">
        <div class="icono">🚌</div>
        <h4>Puerto Natales – Punta Arenas</h4>
        <p>Unos 250 km, alrededor de 3 horas. Hay muchas salidas diarias en verano y menos en invierno. Se compra en la terminal o en línea.</p>
      </div>
      <div class="llegar-item">
        <div class="icono">⛴️</div>
        <h4>Punta Arenas – Ushuaia</h4>
        <p>El tramo más largo: de 10 a 12 horas de bus, con cruce del Estrecho de Magallanes en transbordador (unos 20 minutos) y control de frontera en San Sebastián. Las empresas no salen todos los días y el transbordador depende del clima.</p>
      </div>
      <div class="llegar-item">
        <div class="icono">✈️</div>
        <h4>Alternativa en avión</h4>
        <p>Si el tiempo apremia, se puede volar entre Punta Arenas y Ushuaia o desde El Calafate hacia el resto del país, y reservar el bus solo para los tramos más cortos. Los vuelos cambian por temporada: verificá antes de armar el viaje.</p>
      </div>
    </div>
{item("estrecho-magallanes-barcaza-embarque.webp", "Un auto embarca en la barcaza que cruza el Estrecho de Magallanes hacia Tierra del Fuego", "El cruce del Estrecho de Magallanes", "Para llegar a Tierra del Fuego hay que cruzar el Estrecho en una barcaza, en el paso de Primera Angostura, entre Punta Delgada y Bahía Azul. Embarca buses, autos y camiones, y el cruce dura unos 20 minutos. Si hay mucho viento, se demora o se suspende: por eso conviene dejar margen en la jornada.")}
    <div class="nota-oficial"><strong>Frontera:</strong> este recorrido cruza dos veces entre Argentina y Chile: al ir de El Calafate a Puerto Natales y al ir de Punta Arenas a Ushuaia. Llevá el pasaporte (o el documento habilitado para tu nacionalidad) y no cargues frutas, carnes, lácteos ni semillas frescas al pasar a Chile: se controlan y se decomisan. Verificá siempre requisitos, horarios y estado de los pasos en los sitios oficiales antes de salir.</div>
  </div>

  <!-- EN AUTO -->
  <div class="guia-seccion">
    <h2>Hacerlo en auto alquilado</h2>
    <p class="guia-intro" style="margin-bottom:14px;">La alternativa más libre: retirar el vehículo en El Calafate y devolverlo en Ushuaia, o hacerlo al revés. <strong>Es posible, pero con condiciones.</strong> Las dos ciudades están en Argentina, y las empresas piden que el auto vuelva a Argentina; lo difícil es el cruce a Chile y la autorización para hacerlo.</p>
    <div class="llegar-grid">
      <div class="llegar-item">
        <div class="icono">📄</div>
        <h4>Permiso para cruzar a Chile</h4>
        <p>Es obligatorio y se pide a la empresa con anticipación: Hertz exige al menos 72 horas, con copia del pasaporte y del carnet. Hace falta una autorización notarial, el seguro válido en los dos países y los papeles del vehículo. Sin permiso, el seguro puede quedar anulado.</p>
      </div>
      <div class="llegar-item">
        <div class="icono">🚗</div>
        <h4>No todas las empresas ni todos los autos</h4>
        <p>Según las guías de viaje, Hertz, Localiza y Europcar autorizan el cruce, con cargo; Budget lo decide caso por caso y la mayoría de las empresas locales no lo permite. En Hertz, los modelos económicos chicos no pueden cruzar y la flota habilitada en Ushuaia es limitada.</p>
      </div>
      <div class="llegar-item">
        <div class="icono">🏁</div>
        <h4>Devolver en otra ciudad</h4>
        <p>Entre El Calafate y Ushuaia hay un cargo por devolución en otra ciudad que no figura en las tarifas publicadas: pedí el precio total por escrito antes de reservar. Devolver el auto fuera de Argentina tiene multas de miles de dólares en Hertz.</p>
      </div>
      <div class="llegar-item">
        <div class="icono">⛽</div>
        <h4>Lo que se suma</h4>
        <p>Combustible, peajes y el transbordador del Estrecho (se paga aparte), y el seguro completo, recomendable en ripio: un parabrisas puede costar entre 300 y 800 dólares.</p>
      </div>
    </div>
    <h3 style="font-family:'Playfair Display',serif;font-size:20px;color:var(--verde);margin:26px 0 10px;">¿Camioneta o auto común?</h3>
    <div class="tabla-scroll">
      <table class="gp-tabla">
        <thead><tr><th>Vehículo</th><th>Por día · temporada baja</th><th>Por día · verano</th><th>12 días en verano</th><th>Para quién</th></tr></thead>
        <tbody>
          <tr><td>Auto económico</td><td>USD 40 a 55</td><td>USD 65 a 85</td><td>USD 780 a 1.020</td><td>Ciudad y rutas asfaltadas, pero suele no poder cruzar a Chile</td></tr>
          <tr><td>SUV compacta</td><td>USD 60 a 80</td><td>USD 95 a 130</td><td>USD 1.140 a 1.560</td><td>La mejor relación para este recorrido: asfalto, algo de ripio y viento</td></tr>
          <tr><td>SUV mediana</td><td>USD 90 a 120</td><td>USD 140 a 180</td><td>USD 1.680 a 2.160</td><td>Más espacio y comodidad para cuatro personas</td></tr>
          <tr><td>Camioneta 4x4</td><td>USD 110 a 150</td><td>USD 170 a 220</td><td>USD 2.040 a 2.640</td><td>Invierno, caminos de ripio y salidas del camino principal</td></tr>
        </tbody>
      </table>
    </div>
    <div class="nota-oficial"><strong>Cuánto sumar.</strong> A esos valores hay que agregar el permiso de cruce a Chile: en Hertz, USD 190 si se retira en El Calafate y una estimación de USD 330 si se retira en Ushuaia, sin impuestos; otras empresas cobran menos. El seguro completo suma entre USD 15 y 30 por día, y el cargo por devolver en otra ciudad se cotiza por separado. Los precios son orientativos de enero 2026 (PatagoniaHub y Hertz Argentina) y cambian mucho por temporada y por empresa: reservá con meses de anticipación, que puede ahorrar entre un 20 y un 30 por ciento.</div>
    <div class="nota-oficial"><strong>Nuestra recomendación:</strong> casi todo el recorrido principal es asfalto: la camioneta 4x4 solo se justifica en invierno o si vas a salir de las rutas principales. Para el verano, una SUV compacta alcanza, cruza a Chile con permiso y consume menos. Los caminos dentro de Torres del Paine son de ripio y con viento lateral fuerte.</div>
  </div>

  <!-- CONSEJOS -->
  <div class="guia-seccion">
    <h2>Consejos prácticos</h2>
    <div class="consejo-grid">
      <div class="consejo-item" style="grid-column:1/-1;">Hacete un control médico antes de viajar y entrená con anticipación si vas a caminar en Torres del Paine. Mirá el aviso al final de la guía: <strong>Exigencia física y preparación</strong>.</div>
      <div class="consejo-item">Reservá primero lo que se agota: alojamiento en Torres del Paine, entradas al parque (pasesparques.cl) y los barcos al glaciar.</div>
      <div class="consejo-item">Dejá un día de margen antes de cualquier vuelo de regreso: los buses largos y el transbordador pueden demorarse por el viento.</div>
      <div class="consejo-item">Llevá algo de efectivo en pesos argentinos y chilenos, sobre todo en el parque y en pueblos chicos.</div>
      <div class="consejo-item">Armá la valija en capas: en un mismo día podés pasar de sol a viento helado. Un impermeable liviano no puede faltar.</div>
      <div class="consejo-item">Confirmá horarios, paso fronterizo y fechas de apertura en las fuentes oficiales y con las empresas de bus: cambian cada temporada.</div>
    </div>
  </div>

  <!-- EXIGENCIA Y PREPARACIÓN -->
  <div class="guia-seccion">
    <h2>Exigencia física y preparación</h2>
    <div class="aviso-salud">
      <h3>⚠️ Antes de reservar, evaluá si estás en condiciones</h3>
      <p>Este recorrido combina muchas horas de viaje por tierra con caminatas en Torres del Paine: la Base de las Torres lleva entre 8 y 10 horas, con subida por piedra, viento fuerte y clima que cambia rápido. Los servicios médicos están lejos de varios tramos.</p>
      <ul>
        <li><strong>Hacete un control médico completo antes de viajar</strong> y consultá si tu estado de salud es adecuado para caminatas largas y para tantas horas de viaje. Es especialmente importante si tenés problemas cardíacos o de presión, respiratorios, de rodillas o columna, diabetes, o si tomás medicación.</li>
        <li><strong>Entrená con anticipación:</strong> caminatas largas con mochila y escaleras o cuestas durante varias semanas antes del viaje.</li>
        <li><strong>Considerá ir con guía habilitado</strong> para las caminatas, sobre todo si no tenés experiencia o si viajás en invierno.</li>
        <li><strong>Contratá un seguro de viaje con cobertura médica y de rescate</strong> que incluya trekking.</li>
        <li><strong>Escuchá a tu cuerpo:</strong> si no te sentís bien, descansá o volvé. El viaje no se acaba.</li>
      </ul>
      <p class="fin">Esta guía es informativa y no reemplaza la opinión de un médico ni de un guía profesional. Cada persona debe evaluar su propio estado y el de quienes viajen con ella.</p>
    </div>
  </div>

  <div class="relacionadas">
    <div class="relacionadas-titulo">También te puede interesar</div>
    <div class="relacionadas-grid">
      <a class="rel-card" href="/notas/guia-calafate.html">
        <img class="rel-img" src="https://globalpatagonia.org/fotos/CIUDADES/Calafate.webp" alt="El Calafate"/>
        <div class="rel-body"><div class="rel-tag">Guías</div><div class="rel-titulo">El Calafate: la puerta al Glaciar Perito Moreno</div></div>
      </a>
      <a class="rel-card" href="/notas/guia-torres-del-paine.html">
        <img class="rel-img" src="https://globalpatagonia.org/fotos/CIUDADES/torres-del-paine-hero.webp" alt="Torres del Paine"/>
        <div class="rel-body"><div class="rel-tag">Guías</div><div class="rel-titulo">Torres del Paine: guía de viaje — Circuitos W y O, glaciares y fauna</div></div>
      </a>
      <a class="rel-card" href="/notas/guia-ushuaia.html">
        <img class="rel-img" src="https://globalpatagonia.org/fotos/CIUDADES/ushuaia-laguna-esmeralda.webp" alt="Ushuaia"/>
        <div class="rel-body"><div class="rel-tag">Guías</div><div class="rel-titulo">Ushuaia: donde el mundo termina y la aventura empieza</div></div>
      </a>
    </div>
  </div>

  <div class="compartir-bloque" id="compartir-bloque"></div>
  <a href="../#sec-turismo" class="ver-mas">← Más guías en GLOBALpatagonia</a>
</div>

'''
tail = esq[esq.index('<div class="divider-footer">'):]
out = head + hero + tail
open(f"{BASE}/notas/{SLUG}.html", "w", encoding="utf-8").write(out)
print(f"OK notas/{SLUG}.html", len(out))
