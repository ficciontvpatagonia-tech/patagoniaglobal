#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publica la guía C4 Parque de Nieve en Turismo en Patagonia (turismo.json)
con cuerpo completo en historial.json + traducciones EN/PT/ZH embebidas.
Luego _scripts/_gen_variantes_c4.py genera las 4 páginas estáticas."""
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NID = "c4-parque-nieve-2026"
IMG = "fotos/DEPORTES/CENTROS_SKY/"

CSS = "<style>.ski-table{width:100%;border-collapse:collapse;margin:24px 0 8px;font-size:14px;border-radius:6px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.08)}.ski-table thead tr{background:#1c2d3d;color:#fff;text-align:left}.ski-table thead th{padding:12px 16px;font-weight:700;font-size:11px;letter-spacing:1px;text-transform:uppercase}.ski-table tbody tr:nth-child(even){background:#fff}.ski-table tbody tr:nth-child(odd){background:#f7f5f0}.ski-table tbody td{padding:11px 16px;color:#2a2a2a;border-bottom:1px solid #e8e5e0}.ski-table td strong{color:#1c2d3d}.c4-card{display:flex;gap:18px;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 2px 10px rgba(28,45,61,.1);margin:22px 0}.c4-card img{width:38%;object-fit:cover;min-height:220px}.c4-card .c4-body{padding:18px 18px 18px 0;flex:1}.c4-card h4{font-family:'Playfair Display',serif;color:#1c2d3d;font-size:18px;margin:0 0 8px}.c4-chips{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}.c4-chip{background:#f0ede8;border:1px solid #7aadcc;color:#1c2d3d;font-size:12px;font-weight:600;padding:3px 10px;border-radius:20px}.c4-nota{background:#fff8ec;border-left:4px solid #8c6b4a;padding:14px 18px;border-radius:0 8px 8px 0;font-size:15px;margin:22px 0}.c4-quote{font-family:'Playfair Display',serif;font-size:19px;color:#1c2d3d;font-style:italic;border-left:4px solid #8c6b4a;padding:6px 0 6px 18px;margin:26px 0}.c4-quote span{display:block;font-family:Inter,sans-serif;font-size:12px;font-style:normal;color:#888;margin-top:6px}.c4-g2{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:22px 0}.c4-g2 img{width:100%;height:260px;object-fit:cover;border-radius:8px}.c4-foto{width:100%;border-radius:8px;margin:6px 0 2px}.c4-cred{font-size:12px;color:#888;margin-bottom:14px}@media(max-width:640px){.c4-card{flex-direction:column}.c4-card img{width:100%}.c4-card .c4-body{padding:16px}.c4-g2{grid-template-columns:1fr}}</style>"


def card(img, alt, titulo, chips, texto):
    ch = "".join(f'<span class="c4-chip">{c}</span>' for c in chips)
    return (f'<div class="c4-card"><img src="{IMG}{img}" alt="{alt}" loading="lazy">'
            f'<div class="c4-body"><h4>{titulo}</h4><div class="c4-chips">{ch}</div>'
            f'<p style="font-size:15px;margin:0">{texto}</p></div></div>')


def tabla(headers, filas):
    th = "".join(f"<th>{h}</th>" for h in headers)
    tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in f) + "</tr>" for f in filas)
    return f'<table class="ski-table"><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>'


# ============================== ESPAÑOL ==============================
cuerpo_es = "\n\n".join([
    CSS,
    "<p>Aprender a esquiar tiene un enemigo silencioso: el primer día. Todos los inviernos, miles de personas suben al cerro Chapelco decididas a probar por primera vez y se encuentran con pistas colapsadas, esquiadores expertos pasando a toda velocidad al lado, alquileres agotados y precios de centro internacional. Muchos vuelven a casa sin ganas de intentarlo de nuevo. Lo que casi nadie sabe es que <b>600 metros antes de llegar a la base</b>, sobre la misma Ruta Provincial 19, hay un lugar diseñado exactamente para que ese primer día salga bien.</p>",
    "<p><b>C4 Parque de Nieve</b> es el primer parque de invierno de San Martín de los Andes orientado <b>exclusivamente a principiantes</b>. Acá nadie baja a toda velocidad: todo el parque está pensado para el que se calza los esquíes por primera vez. Está al pie del cerro C4, dentro del territorio de la <b>comunidad mapuche Curruhuinca</b>, en pleno Parque Nacional Lanín, y en 2026 encara su <b>sexta temporada</b> — seis inviernos consecutivos haciendo una sola cosa: enseñar a esquiar.</p>",
    "<h3>Por qué es la mejor opción para arrancar</h3>",
    "<p>El que aprende en un centro de esquí grande paga dos veces: el pase diario (que aprovecha a medias, porque el principiante pasa el día en la pista de iniciación) y la clase aparte. En C4 la lógica es la inversa — <b>la clase incluye el acceso a la pista</b> y todo el entorno juega a favor del que recién empieza:</p>",
    tabla(["El problema del primer día", "Cómo lo resuelve C4"], [
        ["Miedo a las pendientes y a la velocidad", "Pistas suaves diseñadas para iniciación, sin esquiadores expertos cruzando"],
        ["Pagar pase de centro grande para usar solo la pista escuela", "La clase para principiantes ya incluye el acceso a pista, desde $105.000"],
        ["Instructores saturados en temporada alta", "Escuela propia dedicada únicamente a primeros pasos y progresión"],
        ["El segundo día, ¿ya estoy para el cerro grande?", "Clases de progresión para afirmar giros y frenadas antes de pasar a Chapelco"],
        ["La familia que no esquía se aburre y pasa frío", "Snowtubing desde los 4 años, raquetas y refugio con fuego para los acompañantes"],
    ]),
    "<h3>La ficha rápida</h3>",
    tabla(["Dato", "Detalle"], [
        ["<strong>Ubicación</strong>", "Ruta Provincial 19, a 600 m de la base del cerro Chapelco y 4 km de la Ruta 40 (Camino de los Siete Lagos)"],
        ["<strong>Desde San Martín de los Andes</strong>", "~20 minutos en auto"],
        ["<strong>Temporada 2026</strong>", "Invierno — sexta temporada del parque"],
        ["<strong>Ideal para</strong>", "Primer contacto con el esquí o snowboard, familias con chicos"],
        ["<strong>Edad mínima snowtubing</strong>", "4 años"],
        ["<strong>Reserva</strong>", "15% de anticipo online — 10% de descuento pagando el saldo en efectivo"],
    ]),
    "<h3>Qué se puede hacer</h3>",
    card("c4-parque-nieve-clase.webp", "Clase de esquí para principiantes en C4 Parque de Nieve",
         "⛷ Esquí y snowboard: los primeros pasos", ["Desde $105.000", "Incluye acceso a pista", "Instructores propios"],
         "Clases para quienes nunca se calzaron una tabla o esquíes, en pendientes pensadas para aprender sin sustos. También hay clases de <b>progresión</b> para el segundo o tercer día, cuando el desafío es afirmar giros y frenadas antes de animarse al cerro grande."),
    card("c4-parque-nieve-tubing.webp", "Snowtubing en C4 Parque de Nieve",
         "🛷 Snowtubing: la estrella de los chicos", ["Desde $40.000", "Desde los 4 años"],
         "Bajadas en enormes donas inflables por canaletas de nieve. Es la actividad más pedida por las familias: no requiere ninguna técnica, solo ganas de gritar en la bajada. Los más chicos pueden compartir la dona con un adulto."),
    card("c4-parque-nieve-bosque-lenga.webp", "Bosque nevado de lengas en el cordón Chapelco",
         "🥾 Raquetas por el bosque", ["Caminatas guiadas", "Bosque de lengas"],
         "Caminatas con raquetas por el bosque nevado y las laderas del cordón Chapelco. La opción para los que no esquían pero quieren la postal del invierno andino en silencio, lejos de los medios de elevación."),
    "<h3>Cuánto cuesta (temporada 2026)</h3>",
    tabla(["Actividad", "Precio", "Incluye"], [
        ["Clase de esquí principiantes", "Desde $105.000", "Acceso a pista"],
        ["Clase de snowboard principiantes", "Desde $105.000", "Acceso a pista"],
        ["Clase de progresión (2º/3º día)", "$105.000", "Acceso a pista"],
        ["Snowtubing", "Desde $40.000", "Dona y canaleta"],
    ]),
    '<div class="c4-nota">💡 <b>El dato:</b> se reserva con un anticipo del 15% y el saldo se paga en el parque — <b>con 10% de descuento si es en efectivo</b>. Precios publicados por el parque a julio 2026; consultar equipo de alquiler por WhatsApp.</div>',
    "<h3>El refugio: fuego, chocolate y platos regionales</h3>",
    f'<img class="c4-foto" src="{IMG}c4-parque-nieve-refugio.webp" alt="Refugio de madera de C4 Parque de Nieve" loading="lazy"><div class="c4-cred">El refugio de madera, el corazón del parque. Fotos: C4 Parque de Nieve</div>',
    "<p>El centro de la vida social del parque es un <b>refugio de madera con el fuego siempre encendido</b>, donde se sirven chocolate caliente y platos regionales. Hay áreas de descanso para los acompañantes que prefieren mirar la nieve desde adentro — un detalle que los centros grandes suelen resolver con confiterías caras y llenas.</p>",
    '<div class="c4-quote">"Seguimos siendo el lugar ideal para dar los primeros pasos en la nieve, para quienes quieren tener su primer contacto con el esquí o el snowboard."<span>Fundador de C4 Parque de Nieve, a diario Río Negro</span></div>',
    "<h3>¿C4 o Chapelco?</h3>",
    tabla(["Tu situación", "Conviene"], [
        ["Nunca esquié / primer contacto con la nieve", "<strong>C4</strong> — pendientes suaves, clase incluida, sin multitudes"],
        ["Chicos menores de 6 años", "<strong>C4</strong> — snowtubing desde los 4 años y refugio a mano"],
        ["Segundo o tercer día de esquí", "<strong>C4</strong> (progresión) — y después sí, al cerro grande"],
        ["Ya esquío y quiero pistas largas", "<strong>Chapelco</strong> — 140 ha esquiables y medios de elevación"],
        ["Presupuesto ajustado", "<strong>C4</strong> — la jornada completa puede costar menos que un pase diario del centro grande"],
    ]),
    "<h3>Cómo llegar y contacto</h3>",
    "<p>Desde San Martín de los Andes se toma la Ruta 40 hacia el sur (Camino de los Siete Lagos) y a los pocos kilómetros se dobla en el acceso al cerro Chapelco (Ruta Provincial 19). El parque aparece <b>4 km después, a 600 metros antes de la base del cerro</b> — imposible perderse. Reservas y consultas por WhatsApp a través de <b>c4parquedenieve.com</b> · Instagram <b>@c4parquedenieve</b>.</p>",
    f'<div class="c4-g2"><img src="{IMG}c4-parque-nieve-familia.webp" alt="Familia en el snowtubing de C4 bajo la nevada" loading="lazy"><img src="{IMG}c4-parque-nieve-tubing.webp" alt="Bajada de snowtubing en C4 Parque de Nieve" loading="lazy"></div>',
    "<p><i>Con información de diario Río Negro y C4 Parque de Nieve.</i></p>",
])

# ============================== ENGLISH ==============================
cuerpo_en = "\n\n".join([
    CSS,
    "<p>Learning to ski has a silent enemy: the first day. Every winter, thousands of people head up Cerro Chapelco determined to try skiing for the first time — and run into packed slopes, expert skiers flying past them, sold-out rental gear and international-resort prices. Many go home never wanting to try again. What almost nobody knows is that <b>600 meters before the base of the mountain</b>, on the same Provincial Route 19, there is a place designed precisely so that first day goes well.</p>",
    "<p><b>C4 Parque de Nieve</b> (C4 Snow Park) is the first winter park in San Martín de los Andes, in Argentine Patagonia, aimed <b>exclusively at beginners</b>. Nobody speeds down these slopes: the whole park is built for people clipping into skis for the very first time. It sits at the foot of Cerro C4, on the land of the <b>Curruhuinca Mapuche community</b> inside Lanín National Park, and 2026 marks its <b>sixth season</b> — six consecutive winters doing one single thing: teaching people to ski.</p>",
    "<h3>Why it's the best place to start</h3>",
    "<p>Anyone who learns at a big ski resort pays twice: the daily lift pass (barely used, since beginners spend the day on the bunny slope) and the lesson on top. At C4 the logic is reversed — <b>the lesson includes access to the slope</b>, and the whole environment works in favor of the first-timer:</p>",
    tabla(["The first-day problem", "How C4 solves it"], [
        ["Fear of steep slopes and speed", "Gentle beginner-designed runs, with no expert skiers crossing through"],
        ["Paying full resort pass just to use the learners' slope", "The beginner lesson already includes slope access, from AR$105,000"],
        ["Overbooked instructors in high season", "In-house ski school dedicated only to first steps and progression"],
        ["Day two: am I ready for the big mountain?", "Progression lessons to lock in turns and stops before moving on to Chapelco"],
        ["The non-skiing family gets bored and cold", "Snow tubing from age 4, snowshoeing, and a lodge with a fire for companions"],
    ]),
    "<h3>Quick facts</h3>",
    tabla(["Fact", "Detail"], [
        ["<strong>Location</strong>", "Provincial Route 19, 600 m from the Cerro Chapelco base and 4 km from Route 40 (Seven Lakes Road)"],
        ["<strong>From San Martín de los Andes</strong>", "~20 minutes by car"],
        ["<strong>2026 season</strong>", "Winter (June–September) — the park's sixth season"],
        ["<strong>Best for</strong>", "First contact with skiing or snowboarding, families with kids"],
        ["<strong>Snow tubing minimum age</strong>", "4 years old"],
        ["<strong>Booking</strong>", "15% deposit online — 10% discount if you pay the balance in cash"],
    ]),
    "<h3>What you can do</h3>",
    card("c4-parque-nieve-clase.webp", "Beginner ski lesson at C4 Snow Park, San Martín de los Andes",
         "⛷ Skiing and snowboarding: first steps", ["From AR$105,000", "Slope access included", "In-house instructors"],
         "Lessons for people who have never put on skis or a board, on slopes designed for learning without fear. There are also <b>progression</b> lessons for day two or three, when the challenge is locking in turns and stops before taking on the big mountain."),
    card("c4-parque-nieve-tubing.webp", "Snow tubing at C4 Snow Park",
         "🛷 Snow tubing: the kids' favorite", ["From AR$40,000", "From age 4"],
         "Rides down snow chutes on giant inflatable donuts. It's the most requested family activity: no technique required, just the will to scream on the way down. The youngest kids can share a donut with an adult."),
    card("c4-parque-nieve-bosque-lenga.webp", "Snow-covered lenga forest on the Chapelco range",
         "🥾 Snowshoeing through the forest", ["Guided walks", "Lenga beech forest"],
         "Snowshoe walks through the snowy forest and the slopes of the Chapelco range. The option for those who don't ski but want the Andean winter postcard in silence, far from the ski lifts."),
    "<h3>How much it costs (2026 season)</h3>",
    tabla(["Activity", "Price", "Includes"], [
        ["Beginner ski lesson", "From AR$105,000", "Slope access"],
        ["Beginner snowboard lesson", "From AR$105,000", "Slope access"],
        ["Progression lesson (day 2/3)", "AR$105,000", "Slope access"],
        ["Snow tubing", "From AR$40,000", "Donut and chute"],
    ]),
    "<div class=\"c4-nota\">💡 <b>Good to know:</b> you book with a 15% deposit and pay the rest at the park — <b>with a 10% discount if you pay cash</b>. Prices published by the park as of July 2026; ask about rental gear via WhatsApp. Prices are in Argentine pesos — check our <a href=\"../cotizaciones.html\">live currency page</a> for today's exchange rate.</div>",
    "<h3>The lodge: fire, hot chocolate and regional dishes</h3>",
    f'<img class="c4-foto" src="{IMG}c4-parque-nieve-refugio.webp" alt="Wooden lodge at C4 Snow Park" loading="lazy"><div class="c4-cred">The wooden lodge, the heart of the park. Photos: C4 Parque de Nieve</div>',
    "<p>The social heart of the park is a <b>wooden lodge with a fire always burning</b>, serving hot chocolate and regional dishes. There are rest areas for companions who prefer to watch the snow from inside — a detail the big resorts usually solve with expensive, crowded cafeterias.</p>",
    '<div class="c4-quote">"We remain the ideal place to take your first steps in the snow, for anyone who wants their first contact with skiing or snowboarding."<span>Founder of C4 Parque de Nieve, to Río Negro newspaper</span></div>',
    "<h3>C4 or Chapelco?</h3>",
    tabla(["Your situation", "Best choice"], [
        ["Never skied / first contact with snow", "<strong>C4</strong> — gentle slopes, lesson included, no crowds"],
        ["Kids under 6", "<strong>C4</strong> — snow tubing from age 4 and the lodge close by"],
        ["Second or third day on skis", "<strong>C4</strong> (progression) — and then yes, the big mountain"],
        ["I already ski and want long runs", "<strong>Chapelco</strong> — 140 skiable hectares and full lift system"],
        ["Tight budget", "<strong>C4</strong> — a full day can cost less than a single day pass at the big resort"],
    ]),
    "<h3>Getting there and contact</h3>",
    "<p>From San Martín de los Andes take Route 40 south (the Seven Lakes Road) and after a few kilometers turn onto the Cerro Chapelco access road (Provincial Route 19). The park appears <b>4 km later, 600 meters before the mountain base</b> — impossible to miss. Bookings and inquiries via WhatsApp through <b>c4parquedenieve.com</b> · Instagram <b>@c4parquedenieve</b>.</p>",
    f'<div class="c4-g2"><img src="{IMG}c4-parque-nieve-familia.webp" alt="Family snow tubing at C4 under the snowfall" loading="lazy"><img src="{IMG}c4-parque-nieve-tubing.webp" alt="Snow tubing run at C4 Snow Park" loading="lazy"></div>',
    "<p><i>Sources: Río Negro newspaper and C4 Parque de Nieve.</i></p>",
])

# ============================== PORTUGUÊS ==============================
cuerpo_pt = "\n\n".join([
    CSS,
    "<p>Aprender a esquiar tem um inimigo silencioso: o primeiro dia. Todo inverno, milhares de pessoas sobem o Cerro Chapelco decididas a experimentar pela primeira vez — e encontram pistas lotadas, esquiadores experientes passando em alta velocidade do lado, aluguéis esgotados e preços de estação internacional. Muitos voltam para casa sem vontade de tentar de novo. O que quase ninguém sabe é que <b>600 metros antes de chegar à base</b>, na mesma Rota Provincial 19, existe um lugar desenhado exatamente para que esse primeiro dia dê certo.</p>",
    "<p>O <b>C4 Parque de Nieve</b> é o primeiro parque de inverno de San Martín de los Andes, na Patagônia argentina, voltado <b>exclusivamente para iniciantes</b>. Aqui ninguém desce em alta velocidade: o parque inteiro foi pensado para quem calça os esquis pela primeira vez. Fica ao pé do Cerro C4, dentro do território da <b>comunidade mapuche Curruhuinca</b>, em pleno Parque Nacional Lanín, e em 2026 encara sua <b>sexta temporada</b> — seis invernos consecutivos fazendo uma única coisa: ensinar a esquiar.</p>",
    "<h3>Por que é a melhor opção para começar</h3>",
    "<p>Quem aprende numa estação de esqui grande paga duas vezes: o passe diário (que aproveita pela metade, porque o iniciante passa o dia na pista de iniciação) e a aula à parte. No C4 a lógica é inversa — <b>a aula inclui o acesso à pista</b> e todo o ambiente joga a favor de quem está começando:</p>",
    tabla(["O problema do primeiro dia", "Como o C4 resolve"], [
        ["Medo das descidas e da velocidade", "Pistas suaves desenhadas para iniciação, sem esquiadores experientes cruzando"],
        ["Pagar passe de estação grande para usar só a pista escola", "A aula para iniciantes já inclui o acesso à pista, a partir de AR$ 105.000"],
        ["Instrutores lotados na alta temporada", "Escola própria dedicada só aos primeiros passos e à progressão"],
        ["No segundo dia, já estou pronto para a montanha grande?", "Aulas de progressão para firmar curvas e freadas antes de partir para o Chapelco"],
        ["A família que não esquia fica entediada e com frio", "Snow tubing a partir dos 4 anos, raquetes de neve e refúgio com lareira"],
    ]),
    "<h3>Ficha rápida</h3>",
    tabla(["Dado", "Detalhe"], [
        ["<strong>Localização</strong>", "Rota Provincial 19, a 600 m da base do Cerro Chapelco e 4 km da Rota 40 (Caminho dos Sete Lagos)"],
        ["<strong>De San Martín de los Andes</strong>", "~20 minutos de carro"],
        ["<strong>Temporada 2026</strong>", "Inverno (junho–setembro) — sexta temporada do parque"],
        ["<strong>Ideal para</strong>", "Primeiro contato com esqui ou snowboard, famílias com crianças"],
        ["<strong>Idade mínima snow tubing</strong>", "4 anos"],
        ["<strong>Reserva</strong>", "15% de sinal online — 10% de desconto pagando o saldo em dinheiro"],
    ]),
    "<h3>O que dá para fazer</h3>",
    card("c4-parque-nieve-clase.webp", "Aula de esqui para iniciantes no C4 Parque de Nieve",
         "⛷ Esqui e snowboard: os primeiros passos", ["A partir de AR$ 105.000", "Acesso à pista incluído", "Instrutores próprios"],
         "Aulas para quem nunca calçou uma prancha ou esquis, em descidas pensadas para aprender sem sustos. Também há aulas de <b>progressão</b> para o segundo ou terceiro dia, quando o desafio é firmar curvas e freadas antes de encarar a montanha grande."),
    card("c4-parque-nieve-tubing.webp", "Snow tubing no C4 Parque de Nieve",
         "🛷 Snow tubing: a estrela das crianças", ["A partir de AR$ 40.000", "A partir dos 4 anos"],
         "Descidas em enormes boias infláveis por canaletas de neve. É a atividade mais pedida pelas famílias: não exige nenhuma técnica, só vontade de gritar na descida. Os menores podem dividir a boia com um adulto."),
    card("c4-parque-nieve-bosque-lenga.webp", "Bosque nevado de lengas no cordão Chapelco",
         "🥾 Raquetes de neve pelo bosque", ["Caminhadas guiadas", "Bosque de lengas"],
         "Caminhadas com raquetes pelo bosque nevado e as encostas do cordão Chapelco. A opção para quem não esquia mas quer o cartão-postal do inverno andino em silêncio, longe dos meios de elevação."),
    "<h3>Quanto custa (temporada 2026)</h3>",
    tabla(["Atividade", "Preço", "Inclui"], [
        ["Aula de esqui iniciantes", "A partir de AR$ 105.000", "Acesso à pista"],
        ["Aula de snowboard iniciantes", "A partir de AR$ 105.000", "Acesso à pista"],
        ["Aula de progressão (2º/3º dia)", "AR$ 105.000", "Acesso à pista"],
        ["Snow tubing", "A partir de AR$ 40.000", "Boia e canaleta"],
    ]),
    '<div class="c4-nota">💡 <b>A dica:</b> a reserva é feita com 15% de sinal e o saldo se paga no parque — <b>com 10% de desconto se for em dinheiro</b>. Preços publicados pelo parque em julho de 2026; consulte o aluguel de equipamento pelo WhatsApp. Os preços são em pesos argentinos — veja o câmbio do dia na nossa <a href="../cotizaciones.html">página de cotações</a>.</div>',
    "<h3>O refúgio: lareira, chocolate quente e pratos regionais</h3>",
    f'<img class="c4-foto" src="{IMG}c4-parque-nieve-refugio.webp" alt="Refúgio de madeira do C4 Parque de Nieve" loading="lazy"><div class="c4-cred">O refúgio de madeira, o coração do parque. Fotos: C4 Parque de Nieve</div>',
    "<p>O centro da vida social do parque é um <b>refúgio de madeira com a lareira sempre acesa</b>, onde se servem chocolate quente e pratos regionais. Há áreas de descanso para os acompanhantes que preferem olhar a neve de dentro — um detalhe que as estações grandes costumam resolver com confeitarias caras e lotadas.</p>",
    '<div class="c4-quote">"Continuamos sendo o lugar ideal para dar os primeiros passos na neve, para quem quer ter o primeiro contato com o esqui ou o snowboard."<span>Fundador do C4 Parque de Nieve, ao jornal Río Negro</span></div>',
    "<h3>C4 ou Chapelco?</h3>",
    tabla(["Sua situação", "Vale mais a pena"], [
        ["Nunca esquiei / primeiro contato com a neve", "<strong>C4</strong> — descidas suaves, aula incluída, sem multidões"],
        ["Crianças menores de 6 anos", "<strong>C4</strong> — snow tubing a partir dos 4 anos e refúgio ao lado"],
        ["Segundo ou terceiro dia de esqui", "<strong>C4</strong> (progressão) — e depois sim, a montanha grande"],
        ["Já esquio e quero pistas longas", "<strong>Chapelco</strong> — 140 hectares esquiáveis e meios de elevação"],
        ["Orçamento apertado", "<strong>C4</strong> — o dia completo pode custar menos que um passe diário da estação grande"],
    ]),
    "<h3>Como chegar e contato</h3>",
    "<p>De San Martín de los Andes, pegue a Rota 40 rumo ao sul (Caminho dos Sete Lagos) e depois de poucos quilômetros entre no acesso ao Cerro Chapelco (Rota Provincial 19). O parque aparece <b>4 km depois, 600 metros antes da base da montanha</b> — impossível se perder. Reservas e consultas pelo WhatsApp em <b>c4parquedenieve.com</b> · Instagram <b>@c4parquedenieve</b>.</p>",
    f'<div class="c4-g2"><img src="{IMG}c4-parque-nieve-familia.webp" alt="Família no snow tubing do C4 sob a nevasca" loading="lazy"><img src="{IMG}c4-parque-nieve-tubing.webp" alt="Descida de snow tubing no C4 Parque de Nieve" loading="lazy"></div>',
    "<p><i>Com informações do jornal Río Negro e do C4 Parque de Nieve.</i></p>",
])

# ============================== 中文 ==============================
cuerpo_zh = "\n\n".join([
    CSS,
    "<p>学滑雪有一个无声的敌人：第一天。每年冬天，成千上万的人满怀期待登上查佩尔科山（Cerro Chapelco）想第一次尝试滑雪，迎接他们的却是拥挤的雪道、从身边飞驰而过的滑雪高手、租不到的装备和国际雪场级的价格。许多人回家后再也不想尝试。几乎没有人知道的是，<b>在距离雪场山脚600米处</b>，同一条19号省道旁，有一个专为让「第一天」顺利而设计的地方。</p>",
    "<p><b>C4雪地公园（C4 Parque de Nieve）</b>是阿根廷巴塔哥尼亚圣马丁德洛斯安第斯（San Martín de los Andes）第一个<b>专为初学者打造</b>的冬季公园。这里没有人高速滑降：整个公园都是为第一次穿上雪板的人设计的。公园位于C4山脚下，坐落在拉宁国家公园（Lanín National Park）内<b>库鲁温卡（Curruhuinca）马普切原住民社区</b>的土地上，2026年迎来<b>第六个雪季</b>——连续六个冬天只做一件事：教人滑雪。</p>",
    "<h3>为什么这里是入门的最佳选择</h3>",
    "<p>在大型雪场学滑雪要花两份钱：一份是日票（初学者整天待在练习道上，票几乎浪费），另一份是单独的课程费。C4的逻辑正好相反——<b>课程费已包含雪道使用</b>，而且整个环境都为初学者着想：</p>",
    tabla(["第一天的难题", "C4的解决方式"], [
        ["害怕坡度和速度", "专为入门设计的缓坡，没有高手从身边穿过"],
        ["花大雪场全价日票却只用练习道", "初学者课程已包含雪道使用，105,000阿根廷比索起"],
        ["旺季教练供不应求", "自有滑雪学校，只专注于入门和进阶教学"],
        ["第二天就能上大山了吗？", "进阶课程帮你巩固转弯和刹车，再去查佩尔科"],
        ["不滑雪的家人又冷又无聊", "4岁起可玩雪圈，还有雪鞋徒步和有壁炉的木屋"],
    ]),
    "<h3>速览信息</h3>",
    tabla(["项目", "详情"], [
        ["<strong>位置</strong>", "19号省道，距查佩尔科山脚600米，距40号国道（七湖公路）4公里"],
        ["<strong>从圣马丁德洛斯安第斯出发</strong>", "开车约20分钟"],
        ["<strong>2026雪季</strong>", "冬季（6月–9月）——公园第六个雪季"],
        ["<strong>适合</strong>", "第一次接触滑雪或单板的人、带孩子的家庭"],
        ["<strong>雪圈最低年龄</strong>", "4岁"],
        ["<strong>预订</strong>", "在线支付15%定金——现金支付余款可享9折"],
    ]),
    "<h3>可以玩什么</h3>",
    card("c4-parque-nieve-clase.webp", "C4雪地公园的初学者滑雪课",
         "⛷ 双板与单板：迈出第一步", ["105,000比索起", "含雪道使用", "自有教练"],
         "为从未穿过雪板的人开设的课程，在专为学习设计的缓坡上无惧起步。还有针对第二、三天的<b>进阶课程</b>，帮你在挑战大山之前巩固转弯和刹车。"),
    card("c4-parque-nieve-tubing.webp", "C4雪地公园的雪圈滑道",
         "🛷 雪圈：孩子们的最爱", ["40,000比索起", "4岁起"],
         "乘坐巨大的充气雪圈沿雪槽滑下。这是家庭游客最喜爱的项目：不需要任何技巧，只需要在滑下时放声尖叫。年龄最小的孩子可以和大人共乘一个雪圈。"),
    card("c4-parque-nieve-bosque-lenga.webp", "查佩尔科山脉被雪覆盖的南青冈森林",
         "🥾 雪鞋森林徒步", ["有向导陪同", "南青冈森林"],
         "穿上雪鞋，漫步在积雪的森林和查佩尔科山脉的山坡上。适合不滑雪、但想在宁静中欣赏安第斯冬季明信片美景的人，远离缆车的喧嚣。"),
    "<h3>价格（2026雪季）</h3>",
    tabla(["项目", "价格", "包含"], [
        ["初学者滑雪课", "105,000比索起", "雪道使用"],
        ["初学者单板课", "105,000比索起", "雪道使用"],
        ["进阶课程（第2/3天）", "105,000比索", "雪道使用"],
        ["雪圈", "40,000比索起", "雪圈和雪槽"],
    ]),
    '<div class="c4-nota">💡 <b>小贴士：</b>预订只需支付15%定金，余款到公园再付——<b>现金支付可享9折优惠</b>。价格为公园2026年7月公布；装备租赁请通过WhatsApp咨询。价格以阿根廷比索计。</div>',
    "<h3>木屋：炉火、热巧克力和地方菜肴</h3>",
    f'<img class="c4-foto" src="{IMG}c4-parque-nieve-refugio.webp" alt="C4雪地公园的木屋" loading="lazy"><div class="c4-cred">木屋是公园的心脏。图片：C4 Parque de Nieve</div>',
    "<p>公园社交生活的中心是一座<b>炉火常燃的木屋</b>，供应热巧克力和巴塔哥尼亚地方菜肴。木屋里还设有休息区，让陪同的家人可以在温暖的室内欣赏雪景——这个贴心细节，大雪场通常只能用昂贵又拥挤的餐厅来解决。</p>",
    '<div class="c4-quote">"我们始终是雪上初体验的理想之地，适合想第一次接触双板或单板滑雪的人。"<span>C4雪地公园创始人，接受《Río Negro》日报采访</span></div>',
    "<h3>选C4还是查佩尔科？</h3>",
    tabla(["你的情况", "更适合"], [
        ["从未滑过雪 / 第一次接触雪", "<strong>C4</strong>——缓坡、含课程、没有人潮"],
        ["6岁以下的孩子", "<strong>C4</strong>——4岁起玩雪圈，木屋就在旁边"],
        ["滑雪第二、三天", "<strong>C4</strong>（进阶课）——之后再去大山"],
        ["已会滑雪，想要长雪道", "<strong>查佩尔科</strong>——140公顷雪域和完整缆车系统"],
        ["预算有限", "<strong>C4</strong>——一整天的花费可能低于大雪场一张日票"],
    ]),
    "<h3>交通与联系方式</h3>",
    "<p>从圣马丁德洛斯安第斯沿40号国道向南行驶（七湖公路），几公里后转入查佩尔科山入口道路（19号省道）。<b>再行驶4公里，在距山脚600米处</b>即可看到公园——不可能错过。预订和咨询请通过<b>c4parquedenieve.com</b>的WhatsApp · Instagram <b>@c4parquedenieve</b>。</p>",
    f'<div class="c4-g2"><img src="{IMG}c4-parque-nieve-familia.webp" alt="雪中在C4玩雪圈的一家人" loading="lazy"><img src="{IMG}c4-parque-nieve-tubing.webp" alt="C4雪地公园的雪圈滑道" loading="lazy"></div>',
    "<p><i>资料来源：《Río Negro》日报及C4 Parque de Nieve。</i></p>",
])

entrada_historial = {
    "id": NID,
    "titulo": "C4 Parque de Nieve: una joya oculta para aprender a esquiar este 2026",
    "bajada": "A 600 metros de la base de Chapelco, el parque de nieve C4 es el secreto mejor guardado de San Martín de los Andes para dar los primeros pasos en el esquí o el snowboard: pendientes suaves, instructores dedicados solo a principiantes, snowtubing para los chicos y un refugio de madera con chocolate caliente — sin las multitudes ni los precios del centro grande.",
    "cuerpo": cuerpo_es,
    "tag": "⛷ Turismo",
    "categoria": "turismo",
    "fuente": "GLOBALpatagonia",
    "url_original": "https://c4parquedenieve.com/",
    "pais": "argentina",
    "imagen": f"{IMG}c4-parque-nieve-clase.webp",
    "fecha": "2026-07-05",
    "meta": "Guía · GLOBALpatagonia",
    "excluir_feed": True,
    "galeria": [],
    "titulo_en": "C4 Snow Park: a hidden gem to learn to ski in 2026",
    "bajada_en": "Just 600 meters from the Chapelco base, the C4 snow park is San Martín de los Andes' best-kept secret for your first days on skis or a snowboard: gentle slopes, beginner-only instructors, snow tubing for the kids and a wooden lodge with hot chocolate — without the crowds or the prices of the big resort.",
    "cuerpo_en": cuerpo_en,
    "titulo_pt": "C4 Parque de Nieve: uma joia escondida para aprender a esquiar em 2026",
    "bajada_pt": "A 600 metros da base do Chapelco, o parque de neve C4 é o segredo mais bem guardado de San Martín de los Andes para os primeiros passos no esqui ou no snowboard: descidas suaves, instrutores dedicados só a iniciantes, snow tubing para as crianças e um refúgio de madeira com chocolate quente — sem as multidões nem os preços da estação grande.",
    "cuerpo_pt": cuerpo_pt,
    "titulo_zh": "C4雪地公园：2026年学滑雪的隐藏瑰宝",
    "bajada_zh": "距查佩尔科雪场山脚仅600米，C4雪地公园是圣马丁德洛斯安第斯保守得最好的秘密：缓坡雪道、专教初学者的教练、供孩子玩的雪圈，还有供应热巧克力的木屋——没有大雪场的人潮和高价。",
    "cuerpo_zh": cuerpo_zh,
}

entrada_turismo = {
    "id": NID,
    "badge": "TURISMO",
    "titulo": entrada_historial["titulo"],
    "bajada": entrada_historial["bajada"],
    "imagen": entrada_historial["imagen"],
    "meta": "Guía · GLOBALpatagonia",
    "excluir_feed": True,
}

# --- turismo.json: insertar al inicio (slot principal), máx 7 ---
path_t = os.path.join(BASE, "turismo.json")
turismo = json.load(open(path_t, encoding="utf-8"))
turismo = [n for n in turismo if n.get("id") != NID]
turismo.insert(0, entrada_turismo)
while len(turismo) > 7:
    quitada = turismo.pop()
    print(f"Rotada fuera de turismo.json: {quitada['id']} (su página estática sigue viva)")
json.dump(turismo, open(path_t, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"turismo.json → {NID} en slot principal ({len(turismo)} activos)")

# --- historial.json: cuerpo completo al inicio ---
path_h = os.path.join(BASE, "historial.json")
historial = json.load(open(path_h, encoding="utf-8"))
historial = [n for n in historial if n.get("id") != NID]
historial.insert(0, entrada_historial)
json.dump(historial, open(path_h, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"historial.json → cuerpo completo + traducciones EN/PT/ZH ({len(historial)} notas)")
