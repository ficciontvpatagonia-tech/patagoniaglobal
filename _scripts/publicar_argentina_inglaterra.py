#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Publica el informe "Más que un partido: Argentina e Inglaterra, una semifinal
# con 649 historias que no se olvidan" en propios.json
# (modelo: publicar_malvinas_calamar.py)
import json

BASE = "/Users/jm/Desktop/CLAUDCODE/GLOBAL PATAGONIA"
PROPIOS = f"{BASE}/propios.json"
HISTORIAL = f"{BASE}/propios_historial.json"
MAX_ACTIVOS = 7

DATELINE = '<p style="font-size:.85rem;letter-spacing:.05em;text-transform:uppercase;color:#7aadcc;font-weight:600;margin-bottom:1.2rem">{}</p>'

def img_block(src, alt, cap):
    return ('<div style="margin:2rem 0"><img src="' + src + '" alt="' + alt +
            '" loading="lazy" decoding="async" style="width:100%;border-radius:6px;display:block">'
            '<div style="font-size:.8rem;color:#777;margin-top:.45rem">' + cap + '</div></div>')

def video_v(vid):
    return ('<div style="margin:2rem auto;max-width:380px"><iframe width="100%" height="640" '
            f'src="https://www.youtube.com/embed/{vid}" frameborder="0" allowfullscreen '
            'style="border-radius:8px"></iframe></div>')

def video_h(vid):
    return ('<div style="margin:2rem 0"><iframe width="100%" height="400" '
            f'src="https://www.youtube.com/embed/{vid}" frameborder="0" allowfullscreen '
            'style="border-radius:8px"></iframe></div>')

def quote(txt):
    return ('<blockquote style="border-left:4px solid #7aadcc;margin:2rem 0;'
            'padding:.4rem 0 .4rem 1.4rem;font-size:1.25rem;line-height:1.5;'
            f'font-style:italic">{txt}</blockquote>')

def ficha(instancia, eq1, fl1, eq2, fl2, detalle):
    return ('<div style="background:#1c2d3d;color:#fff;border-radius:10px;padding:1.5rem 1.2rem;margin:1.5rem 0 1.8rem;text-align:center">'
            '<div style="background:#fff;border-radius:10px;padding:.7rem 1.1rem .5rem;display:inline-block;margin-bottom:1rem">'
            '<img src="fotos/mundial-2026-emblema-poster.webp" alt="Copa Mundial FIFA 2026" style="height:88px;display:block"></div>'
            f'<div><span style="display:inline-block;background:#7aadcc;color:#0e1a26;font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:.3rem .9rem;border-radius:4px;margin-bottom:1rem">{instancia}</span></div>'
            '<div style="display:flex;align-items:center;justify-content:center;gap:1.2rem;margin-bottom:1rem">'
            f'<div style="display:flex;flex-direction:column;align-items:center;gap:.3rem;min-width:110px"><span style="font-size:3.2rem;line-height:1">{fl1}</span><span style="font-weight:800;font-size:1.15rem;letter-spacing:.04em">{eq1}</span></div>'
            '<span style="font-weight:900;font-size:1.5rem;color:#7aadcc">VS</span>'
            f'<div style="display:flex;flex-direction:column;align-items:center;gap:.3rem;min-width:110px"><span style="font-size:3.2rem;line-height:1">{fl2}</span><span style="font-weight:800;font-size:1.15rem;letter-spacing:.04em">{eq2}</span></div></div>'
            f'<div style="font-size:.95rem;line-height:1.9;color:#dce6ef">{detalle}</div></div>')

FL_AR = "🇦🇷"
FL_EN = "🏴󠁧󠁢󠁥󠁮󠁧󠁿"

IMG_PIBES = "fotos/pibes-soldados-malvinas-1982.webp"
IMG_THATCHER = "fotos/margaret-thatcher-1982.webp"
IMG_BELGRANO = "fotos/ara-general-belgrano-1982.webp"
IMG_DIEGO = "fotos/maradona-copa-mexico-1986.webp"
IMG_SOLDADOS = "fotos/soldados-fusiles-malvinas-1982.webp"
IMG_DARWIN = "fotos/cementerio-darwin-malvinas.webp"

VID_HINCHADA = "box97yugSPU"
VID_MILEI = "ApOHtoy30Gw"
VID_GOL = "JqbEZJ5r0rk"

# ============================== ESPAÑOL ==============================
cuerpo = "\n\n".join([
    DATELINE.format("Mundial 2026 — Informe GLOBALpatagonia"),

    ficha("Semifinal · Copa Mundial FIFA 2026", "ARGENTINA", FL_AR, "INGLATERRA", FL_EN,
          "<strong>Miércoles 15 de julio</strong> · 16:00 hora argentina<br>Mercedes-Benz Stadium · Atlanta, Estados Unidos"),

    "<p>La semifinal del Mundial 2026 entre Argentina e Inglaterra se jugará este miércoles 15 de julio a las 16 (hora argentina) en el Mercedes-Benz Stadium de Atlanta. Pero para los argentinos, y especialmente para nuestra Patagonia, este partido comenzó a jugarse hace mucho tiempo. Mucho antes de que la pelota ruede en el césped estadounidense.</p>",

    "<h3>El grito que une generaciones.</h3>",

    "<p>“El que no salta es un inglés”. El canto resuena en cada estadio, en cada celebración, en cada rincón donde haya un argentino alentando a la Selección. Pero, ¿saben realmente los más jóvenes por qué hay que saltar para ser ingleses?</p>",

    video_v(VID_HINCHADA),

    "<p>La respuesta no está en el presente. Está en las Islas Malvinas, a 463 kilómetros de la costa patagónica. Está en 1982, cuando 649 argentinos perdieron la vida en una guerra que el Reino Unido, bajo el liderazgo de Margaret Thatcher, llevó adelante para mantener la ocupación de un territorio que no le pertenece.</p>",

    "<p>Para las nuevas generaciones, el grito “el que no salta es un inglés” ha trascendido su origen inmediato. Muchos jóvenes lo entonan con fervor, pero ¿comprenden el peso histórico de esas palabras? La canción popular “Muchachos, ahora nos volvimos a ilusionar” se encargó de plantar una bandera: “En Argentina nací, tierra de Diego y Lionel, de los pibes de Malvinas que jamás olvidaré”. Esa frase convirtió a la canción en mucho más que un himno de cancha.</p>",

    "<p>Como explicó Juan Carlos Parodi, presidente del Centro de Excombatientes de Ushuaia, la canción ayudó a mantener vivo un sentimiento compartido y abrió la puerta a una reflexión más profunda sobre la historia, la memoria y el significado de la causa Malvinas para las nuevas generaciones. El grito, entonces, no es solo un desafío futbolístico: es un recordatorio de que hay una historia que no se negocia.</p>",

    img_block(IMG_PIBES, "Jóvenes soldados argentinos en las Islas Malvinas, 1982",
              "“Los pibes de Malvinas que jamás olvidaré”: jóvenes soldados argentinos en las islas, 1982."),

    "<h3>Thatcher, Milei y la polémica que no cierra</h3>",

    "<p>En medio de esta previa cargada de historia, las declaraciones del presidente Javier Milei han sumado un capítulo controversial. Milei ha manifestado en varias oportunidades su admiración por Margaret Thatcher, la ex primera ministra británica que condujo al Reino Unido durante el conflicto de 1982 y ordenó el hundimiento del ARA General Belgrano, donde murieron 323 argentinos.</p>",

    img_block(IMG_THATCHER, "Margaret Thatcher, primera ministra británica durante la guerra de Malvinas",
              "Margaret Thatcher, la primera ministra británica que condujo la guerra de 1982."),

    "<p>“Ella fue brillante”, afirmó el mandatario en una entrevista con la BBC, y reforzó su postura al sostener que no ve problema en valorar a quien fue adversaria en la guerra: “Hubo una guerra y a nosotros nos tocó perder”. Incluso llegó a definir a Thatcher como una de “las grandes líderes de la historia de la humanidad”.</p>",

    video_v(VID_MILEI),

    img_block(IMG_BELGRANO, "El ARA General Belgrano hundiéndose, 2 de mayo de 1982",
              "El ARA General Belgrano, hundido el 2 de mayo de 1982 fuera de la zona de exclusión: 323 argentinos murieron en el Atlántico Sur."),

    "<p>Estas declaraciones, particularmente sensibles en la Patagonia por el peso histórico de la guerra, han generado un fuerte rechazo. Excombatientes y dirigentes políticos cuestionaron que esa admiración “atenta contra el reclamo legítimo” de soberanía argentina y la consideran un agravio a la memoria de quienes participaron del conflicto. La valoración positiva de Thatcher rompe con un consenso histórico en Argentina respecto de Malvinas, una causa que suele unificar al arco político.</p>",

    "<h3>La mano de Dios y el gol del siglo</h3>",

    img_block(IMG_DIEGO, "Diego Maradona con la Copa del Mundo, México 1986",
              "Maradona y la Copa del Mundo en el Azteca: la consagración de México 1986."),

    "<p>No se puede hablar de Argentina e Inglaterra en los Mundiales sin mencionar aquel 22 de junio de 1986 en el Estadio Azteca de México. Diego Armando Maradona, con la “Mano de Dios” primero y el “Gol del Siglo” después, selló una victoria que los argentinos interpretaron como mucho más que un triunfo deportivo.</p>",

    video_h(VID_GOL),

    "<p>Como explica el historiador Carlos Sebastián Ciccone, especialista en el estudio de la construcción de identidades nacionales a través del deporte: “Hay un sentir nacional que aumenta cuando juega con la selección y que hace que aflore un conflicto que sigue muy presente en el país”. Argentina lleva en el alma tres M: Maradona, Messi y las Malvinas.</p>",

    "<p>El fútbol, como máxima expresión de la cultura popular, despierta pasiones que a menudo se entrelazan con la identidad nacional. Y cuando el rival es Inglaterra, esa identidad se vuelve más consciente, más militante.</p>",

    "<h3>El deporte no es la guerra</h3>",

    "<p>A horas del partido, la Federación de Veteranos de Guerra “2 de Abril” emitió un comunicado titulado “El sentimiento malvinero no se negocia: la memoria se defiende en cada cancha”. Los excombatientes pidieron diferenciar la semifinal del reclamo por la soberanía de las Islas Malvinas y llamaron a mantener viva la memoria “sin xenofobia ni odio”.</p>",

    "<p>Fueron categóricos:</p>",

    quote("“El deporte no es la guerra. El partido de semifinales es un evento deportivo de alcance mundial, no una revancha armada ni una compensación histórica. La soberanía se defiende en los foros internacionales, con la diplomacia, la verdad histórica y el reclamo pacífico e irrenunciable que dicta nuestra Constitución Nacional”."),

    "<p>“Que el fútbol sea un puente para malvinizar y para recordar al mundo que nuestro reclamo sigue más vigente que nunca. La pelota rueda, el orgullo por nuestros colores se multiplica, pero la memoria permanece intacta”, concluyeron.</p>",

    img_block(IMG_SOLDADOS, "Soldados argentinos en las Islas Malvinas, 1982",
              "Soldados argentinos en Malvinas, 1982. “La memoria se defiende en cada cancha”, dicen hoy los veteranos."),

    "<h3>Un abrazo que cruza océanos</h3>",

    "<p>El fervor por la Selección Argentina no conoce fronteras. A 17.000 kilómetros de distancia, en Bangladesh, miles de fanáticos salen a las calles con camisetas celestes y blancas, muchos con la casaca número 10 de Lionel Messi, subidos a camiones entre banderas y cánticos.</p>",

    "<p>¿Por qué Bangladesh ama tanto a Argentina? La respuesta está en 1982, cuando Bangladesh respaldó a la Argentina en los foros internacionales durante la Guerra de Malvinas. Y en 1986, el triunfo de la Selección con la “Mano de Dios” selló un amor que perdura hasta hoy. El conflicto con la Corona británica fue clave para construir ese vínculo emocional, junto con la figura de Maradona y los recientes éxitos de Messi.</p>",

    "<p>Irlanda, otro país históricamente perjudicado por el Reino Unido, también encuentra en la camiseta argentina un símbolo de resistencia. Y no son los únicos. En cada rincón del mundo donde el colonialismo británico dejó heridas abiertas, hay alguien que el miércoles saltará con Argentina para no ser un inglés.</p>",

    "<h3>La pelota rueda, la memoria queda</h3>",

    "<p>Este miércoles en Atlanta, cuando los 70 mil espectadores del Mercedes-Benz Stadium coreen “el que no salta es un inglés”, cuando los jugadores argentinos salten al ritmo de ese grito ancestral, cuando la pelota ruede y el partido comience, no estará en juego solo un pase a la final.</p>",

    img_block(IMG_DARWIN, "Cementerio argentino de Darwin, Islas Malvinas",
              "El cementerio argentino de Darwin, en las Islas Malvinas, donde descansan los caídos de 1982."),

    "<p>Estará en juego la memoria de 649 héroes que quedaron en las islas y en las aguas del Atlántico Sur. Estará en juego la soberanía de un territorio que nos pertenece. Estará en juego, como dice el historiador Ciccone, un conflicto que “sigue muy presente en el país” y que “siempre se visibiliza en el fútbol”.</p>",

    "<p>Porque, como bien lo dijeron los veteranos, el deporte no es la guerra. Pero el fútbol, cuando Argentina e Inglaterra se enfrentan, es el escenario donde una nación entera recuerda quién es y de dónde viene.</p>",

    "<p>Que la pelota ruede. Que la memoria permanezca. Y que el miércoles, todos los que saltemos, lo hagamos por los pibes de Malvinas que jamás olvidaremos. ¡Que viva Argentina, que viva el deporte!</p>",
])

# ============================== ENGLISH ==============================
cuerpo_en = "\n\n".join([
    DATELINE.format("2026 World Cup — GLOBALpatagonia Report"),

    ficha("Semifinal · FIFA World Cup 2026", "ARGENTINA", FL_AR, "ENGLAND", FL_EN,
          "<strong>Wednesday, July 15</strong> · 4:00 p.m. Argentina time (3:00 p.m. in Atlanta)<br>Mercedes-Benz Stadium · Atlanta, United States"),

    "<p>The 2026 World Cup semifinal between Argentina and England will be played this Wednesday, July 15, at 4 p.m. Argentina time at Mercedes-Benz Stadium in Atlanta. But for Argentines — and especially for our Patagonia — this match began long ago. Long before the ball rolls on American turf.</p>",

    "<h3>The chant that unites generations</h3>",

    "<p>“El que no salta es un inglés” — “whoever doesn’t jump is an Englishman”. The chant echoes in every stadium, in every celebration, in every corner where an Argentine is cheering for the national team. But do the youngest fans really know why not jumping makes you English?</p>",

    video_v(VID_HINCHADA),

    "<p>The answer is not in the present. It lies in the Malvinas Islands, 463 kilometres off the Patagonian coast. It lies in 1982, when 649 Argentines lost their lives in a war that the United Kingdom, under Margaret Thatcher’s leadership, waged to maintain its occupation of a territory that does not belong to it.</p>",

    "<p>For the new generations, the chant has transcended its immediate origin. Many young people sing it with fervour — but do they grasp the historical weight of those words? The popular song “Muchachos, ahora nos volvimos a ilusionar” planted a flag: “In Argentina I was born, land of Diego and Lionel, of the boys of Malvinas I will never forget.” That line turned the song into far more than a stadium anthem.</p>",

    "<p>As Juan Carlos Parodi, president of the Ushuaia War Veterans Centre, explained, the song helped keep a shared feeling alive and opened the door to a deeper reflection on history, memory and the meaning of the Malvinas cause for the new generations. The chant, then, is not merely a footballing taunt: it is a reminder that there is a history that is not up for negotiation.</p>",

    img_block(IMG_PIBES, "Young Argentine soldiers in the Malvinas Islands, 1982",
              "“The boys of Malvinas I will never forget”: young Argentine soldiers on the islands, 1982."),

    "<h3>Thatcher, Milei and a controversy that will not close</h3>",

    "<p>Amid this history-laden build-up, statements by President Javier Milei have added a controversial chapter. Milei has repeatedly expressed his admiration for Margaret Thatcher, the former British prime minister who led the United Kingdom during the 1982 conflict and ordered the sinking of the ARA General Belgrano, in which 323 Argentines died.</p>",

    img_block(IMG_THATCHER, "Margaret Thatcher, British prime minister during the Malvinas war",
              "Margaret Thatcher, the British prime minister who led the 1982 war."),

    "<p>“She was brilliant,” the president said in a BBC interview, standing his ground: he sees no problem in praising a wartime adversary — “There was a war, and it fell to us to lose it.” He even went so far as to call Thatcher one of “the great leaders in the history of humanity”.</p>",

    video_v(VID_MILEI),

    img_block(IMG_BELGRANO, "The ARA General Belgrano sinking, May 2, 1982",
              "The ARA General Belgrano, sunk on May 2, 1982, outside the exclusion zone: 323 Argentines died in the South Atlantic."),

    "<p>Those statements, especially sensitive in Patagonia because of the war’s historical weight, have drawn strong rejection. Veterans and political leaders argued that such admiration “undermines the legitimate claim” to Argentine sovereignty and consider it an affront to the memory of those who took part in the conflict. Praising Thatcher breaks with a historical consensus in Argentina around Malvinas — a cause that usually unites the entire political spectrum.</p>",

    "<h3>The Hand of God and the Goal of the Century</h3>",

    img_block(IMG_DIEGO, "Diego Maradona with the World Cup trophy, Mexico 1986",
              "Maradona and the World Cup at the Azteca: the consecration of Mexico 1986."),

    "<p>It is impossible to speak of Argentina and England at World Cups without recalling June 22, 1986, at Mexico City’s Azteca Stadium. Diego Armando Maradona — with the “Hand of God” first and the “Goal of the Century” later — sealed a victory that Argentines read as much more than a sporting triumph.</p>",

    video_h(VID_GOL),

    "<p>As historian Carlos Sebastián Ciccone, a specialist in the construction of national identities through sport, explains: “There is a national feeling that swells when the national team plays, and it brings to the surface a conflict that remains very much alive in the country.” Argentina carries three Ms in its soul: Maradona, Messi and the Malvinas.</p>",

    "<p>Football, as the highest expression of popular culture, stirs passions that often intertwine with national identity. And when the rival is England, that identity becomes more conscious, more militant.</p>",

    "<h3>Sport is not war</h3>",

    "<p>Hours before the match, the “2 de Abril” War Veterans Federation issued a statement titled “The Malvinas feeling is not negotiable: memory is defended on every pitch”. The veterans asked that the semifinal be kept separate from the claim to sovereignty over the Malvinas Islands and called for keeping memory alive “without xenophobia or hatred”.</p>",

    "<p>They were categorical:</p>",

    quote("“Sport is not war. The semifinal is a sporting event of global reach, not an armed rematch nor a historical compensation. Sovereignty is defended in international forums, with diplomacy, historical truth and the peaceful, unrenounceable claim mandated by our National Constitution.”"),

    "<p>“May football be a bridge to keep Malvinas present, and to remind the world that our claim is more alive than ever. The ball rolls, the pride in our colours multiplies, but memory remains intact,” they concluded.</p>",

    img_block(IMG_SOLDADOS, "Argentine soldiers in the Malvinas Islands, 1982",
              "Argentine soldiers in Malvinas, 1982. “Memory is defended on every pitch,” the veterans say today."),

    "<h3>An embrace across oceans</h3>",

    "<p>Passion for the Argentine national team knows no borders. Seventeen thousand kilometres away, in Bangladesh, thousands of fans take to the streets in sky-blue and white shirts — many wearing Lionel Messi’s number 10 — riding on trucks amid flags and chants.</p>",

    "<p>Why does Bangladesh love Argentina so much? The answer lies in 1982, when Bangladesh backed Argentina in international forums during the Malvinas War. And in 1986, the national team’s triumph with the “Hand of God” sealed a love that endures to this day. The conflict with the British Crown was key to building that emotional bond, together with the figure of Maradona and Messi’s recent triumphs.</p>",

    "<p>Ireland, another country historically wronged by the United Kingdom, also finds in the Argentine shirt a symbol of resistance. And they are not alone. In every corner of the world where British colonialism left open wounds, someone will jump with Argentina on Wednesday so as not to be an Englishman.</p>",

    "<h3>The ball rolls, memory remains</h3>",

    "<p>This Wednesday in Atlanta, when the 70,000 spectators at Mercedes-Benz Stadium chant “el que no salta es un inglés”, when the Argentine players jump to the rhythm of that ancestral cry, when the ball rolls and the match begins, far more than a place in the final will be at stake.</p>",

    img_block(IMG_DARWIN, "Argentine cemetery at Darwin, Malvinas Islands",
              "The Argentine cemetery at Darwin, in the Malvinas Islands, where the fallen of 1982 rest."),

    "<p>At stake will be the memory of 649 heroes who remained on the islands and in the waters of the South Atlantic. At stake will be the sovereignty of a territory that belongs to us. At stake, as historian Ciccone says, will be a conflict that “remains very much alive in the country” and that “always becomes visible in football”.</p>",

    "<p>Because, as the veterans rightly said, sport is not war. But football, when Argentina and England meet, is the stage on which an entire nation remembers who it is and where it comes from.</p>",

    "<p>Let the ball roll. Let memory remain. And on Wednesday, may all of us who jump do so for the boys of Malvinas we will never forget. Long live Argentina, long live sport!</p>",
])

# ============================== PORTUGUÊS ==============================
cuerpo_pt = "\n\n".join([
    DATELINE.format("Copa do Mundo 2026 — Relatório GLOBALpatagonia"),

    ficha("Semifinal · Copa do Mundo FIFA 2026", "ARGENTINA", FL_AR, "INGLATERRA", FL_EN,
          "<strong>Quarta-feira, 15 de julho</strong> · 16h no horário argentino<br>Mercedes-Benz Stadium · Atlanta, Estados Unidos"),

    "<p>A semifinal da Copa do Mundo de 2026 entre Argentina e Inglaterra será disputada nesta quarta-feira, 15 de julho, às 16h (horário argentino), no Mercedes-Benz Stadium, em Atlanta. Mas para os argentinos — e especialmente para a nossa Patagônia — esta partida começou a ser jogada há muito tempo. Muito antes de a bola rolar no gramado americano.</p>",

    "<h3>O grito que une gerações</h3>",

    "<p>“El que no salta es un inglés” — “quem não pula é um inglês”. O canto ressoa em cada estádio, em cada celebração, em cada canto onde haja um argentino torcendo pela Seleção. Mas será que os mais jovens sabem realmente por que é preciso pular para não ser inglês?</p>",

    video_v(VID_HINCHADA),

    "<p>A resposta não está no presente. Está nas Ilhas Malvinas, a 463 quilômetros da costa patagônica. Está em 1982, quando 649 argentinos perderam a vida em uma guerra que o Reino Unido, sob a liderança de Margaret Thatcher, levou adiante para manter a ocupação de um território que não lhe pertence.</p>",

    "<p>Para as novas gerações, o grito transcendeu sua origem imediata. Muitos jovens o entoam com fervor, mas será que compreendem o peso histórico dessas palavras? A canção popular “Muchachos, ahora nos volvimos a ilusionar” tratou de fincar uma bandeira: “Na Argentina nasci, terra de Diego e Lionel, dos garotos das Malvinas que jamais esquecerei”. Essa frase transformou a canção em muito mais que um hino de arquibancada.</p>",

    "<p>Como explicou Juan Carlos Parodi, presidente do Centro de Ex-Combatentes de Ushuaia, a canção ajudou a manter vivo um sentimento compartilhado e abriu a porta para uma reflexão mais profunda sobre a história, a memória e o significado da causa Malvinas para as novas gerações. O grito, portanto, não é apenas um desafio futebolístico: é um lembrete de que há uma história que não se negocia.</p>",

    img_block(IMG_PIBES, "Jovens soldados argentinos nas Ilhas Malvinas, 1982",
              "“Os garotos das Malvinas que jamais esquecerei”: jovens soldados argentinos nas ilhas, 1982."),

    "<h3>Thatcher, Milei e a polêmica que não se fecha</h3>",

    "<p>Em meio a essa véspera carregada de história, as declarações do presidente Javier Milei somaram um capítulo controverso. Milei manifestou em várias oportunidades sua admiração por Margaret Thatcher, a ex-primeira-ministra britânica que conduziu o Reino Unido durante o conflito de 1982 e ordenou o afundamento do ARA General Belgrano, onde morreram 323 argentinos.</p>",

    img_block(IMG_THATCHER, "Margaret Thatcher, primeira-ministra britânica durante a guerra das Malvinas",
              "Margaret Thatcher, a primeira-ministra britânica que conduziu a guerra de 1982."),

    "<p>“Ela foi brilhante”, afirmou o mandatário em entrevista à BBC, reforçando sua postura ao sustentar que não vê problema em valorizar quem foi adversária na guerra: “Houve uma guerra e a nós coube perder”. Chegou inclusive a definir Thatcher como uma das “grandes líderes da história da humanidade”.</p>",

    video_v(VID_MILEI),

    img_block(IMG_BELGRANO, "O ARA General Belgrano afundando, 2 de maio de 1982",
              "O ARA General Belgrano, afundado em 2 de maio de 1982 fora da zona de exclusão: 323 argentinos morreram no Atlântico Sul."),

    "<p>Essas declarações, particularmente sensíveis na Patagônia pelo peso histórico da guerra, geraram forte rejeição. Ex-combatentes e dirigentes políticos questionaram que essa admiração “atenta contra a reivindicação legítima” de soberania argentina e a consideram um agravo à memória de quem participou do conflito. A valorização positiva de Thatcher rompe com um consenso histórico na Argentina a respeito das Malvinas, uma causa que costuma unificar todo o arco político.</p>",

    "<h3>A mão de Deus e o gol do século</h3>",

    img_block(IMG_DIEGO, "Diego Maradona com a taça da Copa do Mundo, México 1986",
              "Maradona e a taça da Copa no Azteca: a consagração do México 1986."),

    "<p>Não se pode falar de Argentina e Inglaterra em Copas do Mundo sem mencionar aquele 22 de junho de 1986 no Estádio Azteca, no México. Diego Armando Maradona, com a “Mão de Deus” primeiro e o “Gol do Século” depois, selou uma vitória que os argentinos interpretaram como muito mais que um triunfo esportivo.</p>",

    video_h(VID_GOL),

    "<p>Como explica o historiador Carlos Sebastián Ciccone, especialista no estudo da construção de identidades nacionais através do esporte: “Há um sentir nacional que aumenta quando a seleção joga e que faz aflorar um conflito que segue muito presente no país”. A Argentina leva na alma três M: Maradona, Messi e as Malvinas.</p>",

    "<p>O futebol, como máxima expressão da cultura popular, desperta paixões que muitas vezes se entrelaçam com a identidade nacional. E quando o rival é a Inglaterra, essa identidade se torna mais consciente, mais militante.</p>",

    "<h3>O esporte não é a guerra</h3>",

    "<p>A poucas horas da partida, a Federação de Veteranos de Guerra “2 de Abril” emitiu um comunicado intitulado “O sentimento malvinense não se negocia: a memória se defende em cada campo”. Os ex-combatentes pediram para diferenciar a semifinal da reivindicação pela soberania das Ilhas Malvinas e conclamaram a manter viva a memória “sem xenofobia nem ódio”.</p>",

    "<p>Foram categóricos:</p>",

    quote("“O esporte não é a guerra. A partida das semifinais é um evento esportivo de alcance mundial, não uma revanche armada nem uma compensação histórica. A soberania se defende nos foros internacionais, com a diplomacia, a verdade histórica e a reivindicação pacífica e irrenunciável que dita a nossa Constituição Nacional”."),

    "<p>“Que o futebol seja uma ponte para ‘malvinizar’ e para lembrar ao mundo que a nossa reivindicação segue mais vigente do que nunca. A bola rola, o orgulho pelas nossas cores se multiplica, mas a memória permanece intacta”, concluíram.</p>",

    img_block(IMG_SOLDADOS, "Soldados argentinos nas Ilhas Malvinas, 1982",
              "Soldados argentinos nas Malvinas, 1982. “A memória se defende em cada campo”, dizem hoje os veteranos."),

    "<h3>Um abraço que cruza oceanos</h3>",

    "<p>O fervor pela Seleção Argentina não conhece fronteiras. A 17.000 quilômetros de distância, em Bangladesh, milhares de torcedores saem às ruas com camisas celestes e brancas, muitos com a camisa 10 de Lionel Messi, em cima de caminhões, entre bandeiras e cânticos.</p>",

    "<p>Por que Bangladesh ama tanto a Argentina? A resposta está em 1982, quando Bangladesh apoiou a Argentina nos foros internacionais durante a Guerra das Malvinas. E em 1986, o triunfo da Seleção com a “Mão de Deus” selou um amor que perdura até hoje. O conflito com a Coroa britânica foi chave para construir esse vínculo emocional, junto com a figura de Maradona e os êxitos recentes de Messi.</p>",

    "<p>A Irlanda, outro país historicamente prejudicado pelo Reino Unido, também encontra na camisa argentina um símbolo de resistência. E não são os únicos. Em cada canto do mundo onde o colonialismo britânico deixou feridas abertas, há alguém que na quarta-feira vai pular com a Argentina para não ser um inglês.</p>",

    "<h3>A bola rola, a memória fica</h3>",

    "<p>Nesta quarta-feira em Atlanta, quando os 70 mil espectadores do Mercedes-Benz Stadium entoarem “el que no salta es un inglés”, quando os jogadores argentinos pularem ao ritmo desse grito ancestral, quando a bola rolar e a partida começar, não estará em jogo apenas uma vaga na final.</p>",

    img_block(IMG_DARWIN, "Cemitério argentino de Darwin, Ilhas Malvinas",
              "O cemitério argentino de Darwin, nas Ilhas Malvinas, onde descansam os caídos de 1982."),

    "<p>Estará em jogo a memória de 649 heróis que ficaram nas ilhas e nas águas do Atlântico Sul. Estará em jogo a soberania de um território que nos pertence. Estará em jogo, como diz o historiador Ciccone, um conflito que “segue muito presente no país” e que “sempre se visibiliza no futebol”.</p>",

    "<p>Porque, como bem disseram os veteranos, o esporte não é a guerra. Mas o futebol, quando Argentina e Inglaterra se enfrentam, é o palco onde uma nação inteira lembra quem é e de onde vem.</p>",

    "<p>Que a bola role. Que a memória permaneça. E que na quarta-feira, todos os que pularmos, o façamos pelos garotos das Malvinas que jamais esqueceremos. Que viva a Argentina, que viva o esporte!</p>",
])

# ============================== 中文 ==============================
cuerpo_zh = "\n\n".join([
    DATELINE.format("2026世界杯 — GLOBALpatagonia 深度报道"),

    ficha("半决赛 · 2026国际足联世界杯", "阿根廷", FL_AR, "英格兰", FL_EN,
          "<strong>7月15日 星期三</strong> · 阿根廷时间16:00<br>梅赛德斯-奔驰体育场 · 美国亚特兰大"),

    "<p>2026年世界杯半决赛，阿根廷对英格兰，将于本周三7月15日阿根廷时间16点在亚特兰大的梅赛德斯-奔驰体育场开球。但对阿根廷人——尤其是对我们巴塔哥尼亚人——来说，这场比赛早在很久以前就开始了。远在皮球于美国草坪上滚动之前。</p>",

    "<h3>连结几代人的呐喊</h3>",

    "<p>“El que no salta es un inglés”——“不跳的人就是英国佬”。这句歌声回荡在每一座球场、每一场庆祝、每一个有阿根廷人为国家队呐喊的角落。但最年轻的一代真的知道，为什么不跳就成了英国人吗？</p>",

    video_v(VID_HINCHADA),

    "<p>答案不在当下。答案在距巴塔哥尼亚海岸463公里的马尔维纳斯群岛。答案在1982年——那一年，649名阿根廷人在一场战争中失去了生命；那场战争，是英国在玛格丽特·撒切尔的领导下，为维持对一片不属于它的领土的占领而发动的。</p>",

    "<p>对新一代人来说，这句呐喊早已超越了它最初的语境。许多年轻人满怀热情地唱着它，但他们理解这些词句的历史分量吗？流行歌曲《Muchachos，我们再次燃起希望》插下了一面旗帜：“我生在阿根廷，迭戈和梅西的土地，还有我永远不会忘记的马尔维纳斯的孩子们。”这句歌词让这首歌远远超越了球场助威曲。</p>",

    "<p>正如乌斯怀亚老兵中心主席胡安·卡洛斯·帕罗迪所解释的，这首歌帮助一种共同的情感延续下去，也打开了一扇门，让新一代人更深入地思考历史、记忆以及马尔维纳斯事业的意义。因此，这句呐喊不只是足球场上的挑衅：它提醒着人们，有一段历史没有商量的余地。</p>",

    img_block(IMG_PIBES, "1982年马尔维纳斯群岛上的阿根廷年轻士兵",
              "“我永远不会忘记的马尔维纳斯的孩子们”：1982年，群岛上的阿根廷年轻士兵。"),

    "<h3>撒切尔、米莱与未了的争议</h3>",

    "<p>在这场承载历史的赛前氛围中，总统哈维尔·米莱的言论增添了一个争议章节。米莱多次表达对玛格丽特·撒切尔的钦佩——这位英国前首相在1982年冲突期间领导英国，并下令击沉贝尔格拉诺将军号巡洋舰，323名阿根廷人因此丧生。</p>",

    img_block(IMG_THATCHER, "马尔维纳斯战争期间的英国首相玛格丽特·撒切尔",
              "玛格丽特·撒切尔，指挥1982年战争的英国首相。"),

    "<p>“她非常杰出”，这位总统在接受BBC采访时说，并进一步坚称，赞赏一位战争中的对手没有问题：“打了一场仗，输的是我们。”他甚至把撒切尔定义为“人类历史上最伟大的领导人”之一。</p>",

    video_v(VID_MILEI),

    img_block(IMG_BELGRANO, "1982年5月2日正在沉没的贝尔格拉诺将军号",
              "贝尔格拉诺将军号，1982年5月2日在禁航区之外被击沉：323名阿根廷人葬身南大西洋。"),

    "<p>这些言论因战争的历史分量而在巴塔哥尼亚尤为敏感，引发了强烈反对。老兵和政界人士抨击这种钦佩“损害了阿根廷主权的正当诉求”，并认为这是对参战者记忆的冒犯。对撒切尔的正面评价，打破了阿根廷在马尔维纳斯问题上的历史共识——这一事业通常能让整个政治光谱团结一致。</p>",

    "<h3>上帝之手与世纪进球</h3>",

    img_block(IMG_DIEGO, "1986年墨西哥世界杯，马拉多纳捧起大力神杯",
              "马拉多纳与世界杯奖杯在阿兹特克球场：1986年墨西哥的加冕时刻。"),

    "<p>谈论世界杯上的阿根廷与英格兰，不可能不提1986年6月22日墨西哥阿兹特克球场的那一天。迭戈·阿曼多·马拉多纳，先以“上帝之手”、后以“世纪进球”，锁定了一场在阿根廷人眼中远不止于体育的胜利。</p>",

    video_h(VID_GOL),

    "<p>正如专门研究体育与国家认同建构的历史学家卡洛斯·塞巴斯蒂安·奇科内所解释的：“国家队比赛时，民族情感会高涨，让一个在这个国家依然鲜活的冲突浮出水面。”阿根廷的灵魂里装着三个M：马拉多纳（Maradona）、梅西（Messi）和马尔维纳斯（Malvinas）。</p>",

    "<p>足球作为大众文化的最高表达，唤起的激情常常与民族认同交织在一起。而当对手是英格兰时，这种认同变得更加自觉，也更加坚定。</p>",

    "<h3>体育不是战争</h3>",

    "<p>比赛前数小时，“四月二日”战争老兵联合会发表了一份题为《马尔维纳斯情感没有商量余地：记忆要在每一块球场上捍卫》的声明。老兵们呼吁将这场半决赛与马尔维纳斯群岛主权诉求区分开来，并呼吁让记忆延续，“不要仇外，不要仇恨”。</p>",

    "<p>他们的态度斩钉截铁：</p>",

    quote("“体育不是战争。这场半决赛是一场全球性的体育盛事，不是武装复仇，也不是历史补偿。主权要在国际场合捍卫，靠外交、靠历史真相、靠我们国家宪法所规定的和平且不可放弃的诉求。”"),

    "<p>“愿足球成为一座桥梁，让马尔维纳斯被铭记，让世界记得我们的诉求比以往任何时候都更有生命力。皮球滚动，我们为自己颜色感到的骄傲成倍增长，但记忆完好无损”，他们总结道。</p>",

    img_block(IMG_SOLDADOS, "1982年马尔维纳斯群岛上的阿根廷士兵",
              "1982年，马尔维纳斯群岛上的阿根廷士兵。老兵们今天说：“记忆要在每一块球场上捍卫。”"),

    "<h3>跨越大洋的拥抱</h3>",

    "<p>对阿根廷国家队的热爱没有国界。在17,000公里之外的孟加拉国，成千上万的球迷身穿蓝白球衣走上街头——许多人穿着莱昂内尔·梅西的10号战袍——爬上卡车，在旗帜与歌声中游行。</p>",

    "<p>孟加拉国为什么如此热爱阿根廷？答案在1982年：马尔维纳斯战争期间，孟加拉国在国际场合声援了阿根廷。而在1986年，国家队凭“上帝之手”夺冠，让这份爱延续至今。与英国王室的冲突，加上马拉多纳的形象和梅西近年的成就，是构建这种情感纽带的关键。</p>",

    "<p>爱尔兰——另一个在历史上深受英国之害的国家——同样在阿根廷球衣中找到了抵抗的象征。他们并不孤单。在世界上每一个被英国殖民主义留下未愈伤口的角落，都会有人在周三与阿根廷一起跳起来，不做英国佬。</p>",

    "<h3>皮球滚动，记忆长存</h3>",

    "<p>本周三在亚特兰大，当梅赛德斯-奔驰体育场的七万名观众齐声高唱“el que no salta es un inglés”，当阿根廷球员随着这古老的呐喊跳跃，当皮球滚动、比赛开始，赌上的绝不只是一张决赛门票。</p>",

    img_block(IMG_DARWIN, "马尔维纳斯群岛达尔文阿根廷军人公墓",
              "马尔维纳斯群岛的达尔文阿根廷军人公墓，1982年的阵亡者长眠于此。"),

    "<p>赌上的，是留在群岛和南大西洋水域的649位英雄的记忆。赌上的，是一片属于我们的领土的主权。赌上的，正如历史学家奇科内所说，是一个“在这个国家依然鲜活”、并且“总是在足球中显现”的冲突。</p>",

    "<p>因为，正如老兵们所言，体育不是战争。但当阿根廷与英格兰相遇时，足球是一整个民族记起自己是谁、从哪里来的舞台。</p>",

    "<p>让皮球滚动。让记忆长存。愿周三所有跳起来的人，都是为了那些我们永远不会忘记的马尔维纳斯的孩子们而跳。阿根廷万岁，体育万岁！</p>",
])

nueva_entrada = {
    "id": "20260714-propio-argentina-inglaterra",
    "titulo": "Más que un partido: Argentina e Inglaterra, una semifinal con 649 historias que no se olvidan",
    "bajada": "El miércoles en Atlanta, la pelota rodará con el peso de cuatro décadas de historia. Porque cuando Argentina e Inglaterra se enfrentan en un Mundial, nunca es solo fútbol.",
    "cuerpo": cuerpo,
    "titulo_en": "More Than a Match: Argentina vs England, a Semifinal With 649 Stories That Are Never Forgotten",
    "bajada_en": "On Wednesday in Atlanta, the ball will roll under the weight of four decades of history. Because when Argentina and England meet at a World Cup, it is never just football.",
    "cuerpo_en": cuerpo_en,
    "titulo_pt": "Mais que um jogo: Argentina e Inglaterra, uma semifinal com 649 histórias que não se esquecem",
    "bajada_pt": "Na quarta-feira, em Atlanta, a bola vai rolar com o peso de quatro décadas de história. Porque quando Argentina e Inglaterra se enfrentam em uma Copa do Mundo, nunca é só futebol.",
    "cuerpo_pt": cuerpo_pt,
    "titulo_zh": "不只是一场比赛：阿根廷对英格兰，一场承载649段记忆的半决赛",
    "bajada_zh": "周三在亚特兰大，滚动的皮球将承载四十年历史的重量。因为当阿根廷与英格兰在世界杯相遇时，从来不只是足球。",
    "cuerpo_zh": cuerpo_zh,
    "tag": "⚽ Mundial 2026",
    "categoria": "deportes|malvinas|mundial|identidad",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "argentina",
    "imagen": "fotos/mano-de-dios-azteca-1986.webp",
    "imagen_keywords": "argentina inglaterra mundial semifinal malvinas maradona seleccion",
    "hashtags_en": "#Argentina #England #WorldCup2026 #Malvinas #Maradona #Messi",
    "meta": "14 de Julio de 2026 · J. Martineau",
    "excluir_feed": True,
    "galeria": []
}

with open(PROPIOS, "r", encoding="utf-8") as f:
    propios = json.load(f)

with open(HISTORIAL, "r", encoding="utf-8") as f:
    historial = json.load(f)

if any(p["id"] == nueva_entrada["id"] for p in propios):
    raise SystemExit("Ya existe ese id en propios.json — abortando.")

if len(propios) >= MAX_ACTIVOS:
    mas_antiguo = propios.pop()
    historial.insert(0, mas_antiguo)
    print(f"Movido al historial: {mas_antiguo['id']}")

propios.insert(0, nueva_entrada)
print(f"Nuevo informe en propios[0]: {nueva_entrada['id']}")
print(f"Total activos: {len(propios)}")

with open(PROPIOS, "w", encoding="utf-8") as f:
    json.dump(propios, f, ensure_ascii=False, indent=2)

with open(HISTORIAL, "w", encoding="utf-8") as f:
    json.dump(historial, f, ensure_ascii=False, indent=2)

print("OK — propios.json y propios_historial.json actualizados.")
