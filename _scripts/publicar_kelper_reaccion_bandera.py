#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Publica el informe "La reacción kelper y británica a la bandera de Malvinas"
# en propios.json (modelo: publicar_argentina_inglaterra.py)
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

def quote(txt):
    return ('<blockquote style="border-left:4px solid #7aadcc;margin:2rem 0;'
            'padding:.4rem 0 .4rem 1.4rem;font-size:1.25rem;line-height:1.5;'
            f'font-style:italic">{txt}</blockquote>')

IMG_CARTEL = "fotos/malvinas-cartel-bienvenida-islas.webp"
IMG_BANDERA = "fotos/bandera-malvinas-atlanta.webp"
IMG_PARLAMENTO = "fotos/malvinas-parlamento-britanico.webp"

# ============================== ESPAÑOL ==============================
cuerpo = "\n\n".join([
    DATELINE.format("Malvinas — Informe GLOBALpatagonia"),

    "<p>La bandera con la leyenda “Las Malvinas son argentinas” que los jugadores de la Selección desplegaron en Atlanta el 15 de julio, tras vencer 2-1 a Inglaterra en la semifinal del Mundial, no se apagó con el pitido final. Semanas después, mientras la FIFA todavía delibera qué hacer, la carta que un grupo de legisladores de las islas le envió al organismo es la prueba de que en las islas y en Londres el gesto sigue doliendo.</p>",

    "<h3>La carta de los isleños a la FIFA</h3>",

    "<p>El semanario <em>Penguin News</em>, el diario de las islas, reveló que miembros de la Asamblea Legislativa de Malvinas (MLA) escribieron una carta abierta a la FIFA pidiendo sanciones disciplinarias contra los jugadores argentinos. La calificaron de “insensitive” —insensible— y argumentaron:</p>",

    quote("“It is the avowed policy of the Falkland Islands Government that we do not wish to see politics being brought into sport”<br><span style=\"font-size:.95rem;opacity:.75;font-style:normal\">(“Es política declarada del Gobierno de las Islas Falkland que no deseamos ver que la política se introduzca en el deporte”)</span>"),

    "<p>El argumento de los legisladores apela, una vez más, a la autodeterminación: la voluntad de la población isleña de seguir siendo un Territorio Británico de Ultramar. Es el mismo argumento que se repite desde el referéndum de 2013, cuando el 99,8% de los votantes —menos de 1.400 personas— eligió mantener el vínculo con la Corona.</p>",

    img_block(IMG_CARTEL, "Cartel de bienvenida en las Islas Malvinas",
              "Así se presentan las islas a quien llega: apenas unos 3.500 habitantes, a 463 kilómetros de la costa patagónica, que se definen como territorio británico."),

    img_block(IMG_BANDERA, "Jugadores argentinos con la bandera 'Las Malvinas son Argentinas' en Atlanta",
              "El cartel que los jugadores argentinos desplegaron en el campo del Mercedes-Benz Stadium de Atlanta, tras el 2-1 a Inglaterra."),

    "<h3>Habla el gobierno británico</h3>",

    "<p>El reclamo no se quedó en las islas. El vocero del primer ministro británico, Keir Starmer, salió a marcar posición ante la prensa:</p>",

    quote("“The World Cup might not be ours, but the Falkland Islands definitely are”<br><span style=\"font-size:.95rem;opacity:.75;font-style:normal\">(“El Mundial puede que no sea nuestro, pero las Islas Falkland definitivamente sí lo son”)</span>"),

    "<p>Y agregó la fórmula de siempre: “Self-determination rests with the islanders and our commitment to the Falklands will never waver” (“La autodeterminación recae en los isleños y nuestro compromiso con las Falklands nunca flaqueará”).</p>",

    "<p>Horas después, el secretario de Negocios, Peter Kyle, fue más lejos en una entrevista con <strong>BBC Breakfast</strong>. Calificó la conducta de los jugadores de “entirely inappropriate” (enteramente inapropiada) y pidió a la FIFA investigar “thoroughly” lo que definió como una “egregious violation” —una violación flagrante— del reglamento del torneo.</p>",

    img_block(IMG_PARLAMENTO, "Cámara de los Comunes del Parlamento británico",
              "El Parlamento británico, donde el reclamo por la bandera llegó hasta la vocería del primer ministro."),

    "<h3>El veterano que pidió mano dura</h3>",

    "<p>Entre las voces que más resonaron en la prensa británica estuvo la de <strong>Simon Weston</strong>, veterano de la Guerra de Malvinas de 1982, sobreviviente del ataque al buque <em>Sir Galahad</em>. Weston reclamó que la FIFA actúe:</p>",

    quote("“FIFA have to do something. We can't wear a poppy on our international jerseys because they say that's a political symbol”<br><span style=\"font-size:.95rem;opacity:.75;font-style:normal\">(“La FIFA tiene que hacer algo. Nosotros no podemos usar una amapola en nuestras camisetas de la selección porque dicen que es un símbolo político”)</span>"),

    "<p>Y remató: los jugadores “just have to be more respectful and obey the rules. Obey the rules for no politics brought into sport” (“solo tienen que ser más respetuosos y obedecer las reglas. Obedecer las reglas de que no se meta la política en el deporte”).</p>",

    "<p>La comparación de Weston —la amapola (<em>poppy</em>) que en el Reino Unido conmemora a los caídos en guerra, y que la propia FIFA restringió en partidos internacionales por considerarla un símbolo político— fue retomada por buena parte de la prensa deportiva británica como el argumento más citado contra la bandera argentina.</p>",

    "<h3>Lo que los diarios no pudieron dejar de escribir</h3>",

    "<p>Ahí está la paradoja que más le duele a Londres: para explicar por qué se enojaron, buena parte de los medios británicos tuvo que hacer lo que llevan décadas evitando —contarle a su propia audiencia qué son las Malvinas, por qué Argentina las reclama y qué pasó en 1982. El <strong>Daily Mail</strong> confirmó que la FIFA, presidida por Gianni Infantino, esperaría al final del torneo para resolver cualquier sanción, de modo que el caso siguiera abierto sobre la cabeza de la Selección incluso mientras jugaba la final. <strong>Sky Sports</strong> detalló que el expediente disciplinario de la FIFA no se limitaba a la bandera: incluía además cánticos discriminatorios, fallas de protocolo de seguridad y objetos arrojados a la cancha en distintos partidos del torneo. Y <strong>Yahoo News UK</strong> reprodujo, palabra por palabra, la respuesta del gobierno británico.</p>",

    "<p>Ninguno de esos artículos pudo escribir sobre la bandera sin escribir, aunque fuera en una línea, la palabra “Malvinas” —o “Falklands”, del lado británico— seguida de la explicación de una guerra de 74 días: 255 soldados británicos, 649 argentinos y tres isleños muertos en 1982. Esa es, exactamente, la visibilidad que la diplomacia tradicional no consigue.</p>",

    "<h3>El contrapunto que nadie esperaba: Washington</h3>",

    "<p>Mientras Londres pedía sanciones, la Casa Blanca hizo lo contrario. El enlace del gobierno de Donald Trump para el Mundial salió a respaldar el derecho de los jugadores argentinos a manifestarse, invocando la libertad de expresión, y rechazó los pedidos británicos de castigo. El detalle no fue menor para la prensa británica, acostumbrada a contar con Washington como aliado automático en cualquier disputa con Buenos Aires.</p>",

    "<h3>Milei, del otro lado del mostrador</h3>",

    "<p>Desde Argentina, el presidente Javier Milei calificó la celebración de los jugadores como “perfectly valid” (perfectamente válida), y dijo que el mensaje “reflects a sentiment shared by all Argentinians” (refleja un sentimiento que comparten todos los argentinos). Aun así, anticipó que esperaba que la FIFA terminara sancionando al equipo con una multa: “the players get carried away by their emotions, they act on impulse, and that will likely lead to discussions about a fine” (los jugadores se dejan llevar por sus emociones, actúan por impulso, y eso probablemente derive en una discusión sobre una multa).</p>",

    "<h3>La FIFA, todavía sin fallo</h3>",

    "<p>A casi un mes del episodio, y semanas después de la final —que Argentina perdió 1-0 ante España en el MetLife Stadium—, la FIFA no resolvió el caso. El comité disciplinario abrió expediente por varias infracciones, incluida la pancarta, y dio a las partes la posibilidad de presentar su posición antes de fallar. El antecedente más citado es 2014, cuando la FIFA multó a la AFA con 20.000 libras por una pancarta idéntica. Todo indica que el desenlace, otra vez, será una multa y no una sanción deportiva.</p>",

    "<p>Para quienes miramos esto desde la Patagonia —la puerta de embarque hacia el Atlántico Sur, la región que ve pasar a los isleños rumbo a Malvinas por el vuelo mensual desde Río Gallegos— hay una lectura que sobrevive a cualquier multa que termine fijando la FIFA. Durante semanas, un primer ministro, un secretario de Estado, un veterano de guerra y toda la prensa británica tuvieron que decir en voz alta, y explicar, la palabra que Londres prefiere mantener fuera de la agenda. Los legisladores de las islas le escribieron a la FIFA para pedir que castigue a los jugadores argentinos. Pero, sin proponérselo, confirmaron con esa carta lo que ya era evidente en cada portada: la bandera cumplió su cometido.</p>",
])

# ============================== ENGLISH ==============================
cuerpo_en = "\n\n".join([
    DATELINE.format("Malvinas — GLOBALpatagonia Report"),

    "<p>The banner reading “Las Malvinas son argentinas” (“The Malvinas are Argentine”) that Argentina's players unfurled in Atlanta on July 15, after beating England 2-1 in the World Cup semifinal, did not fade with the final whistle. Weeks later, while FIFA still deliberates what to do, a letter that a group of Malvinas (Falklands) lawmakers sent to the governing body is proof that on the islands — and in Britain — the gesture still stings.</p>",

    "<h3>The islanders' letter to FIFA</h3>",

    "<p>The islands' weekly newspaper, <em>Penguin News</em>, revealed that members of the Falkland Islands Legislative Assembly (MLA) wrote an open letter to FIFA calling for disciplinary action against the Argentine players. They called it “insensitive” and argued:</p>",

    quote("“It is the avowed policy of the Falkland Islands Government that we do not wish to see politics being brought into sport”"),

    "<p>The lawmakers' argument invokes self-determination once again: the will of the island population to remain a British Overseas Territory. It is the same argument repeated since the 2013 referendum, when 99.8% of voters — fewer than 1,400 people — chose to keep the link with the Crown.</p>",

    img_block(IMG_CARTEL, "Welcome sign on the Malvinas Islands",
              "This is how the islands present themselves to visitors: barely 3,500 residents, 463 kilometres off the Patagonian coast, who define themselves as British territory."),

    img_block(IMG_BANDERA, "Argentine players with the banner reading 'Las Malvinas son Argentinas' in Atlanta",
              "The sign Argentina's players unfurled on the pitch at Mercedes-Benz Stadium in Atlanta, after beating England 2-1."),

    "<h3>The British government responds</h3>",

    "<p>The claim did not stay on the islands. The spokesperson for British Prime Minister Keir Starmer took a public stand:</p>",

    quote("“The World Cup might not be ours, but the Falkland Islands definitely are”"),

    "<p>And added the usual formula: “Self-determination rests with the islanders and our commitment to the Falklands will never waver.”</p>",

    "<p>Hours later, Business Secretary Peter Kyle went further in an interview with <strong>BBC Breakfast</strong>. He called the players' conduct “entirely inappropriate” and urged FIFA to “thoroughly” investigate what he described as an “egregious violation” of the tournament's rules.</p>",

    img_block(IMG_PARLAMENTO, "The House of Commons at the British Parliament",
              "The British Parliament, where the row over the banner reached all the way to the Prime Minister's spokesperson."),

    "<h3>The veteran who demanded a tough response</h3>",

    "<p>Among the voices that echoed loudest in the British press was that of <strong>Simon Weston</strong>, a veteran of the 1982 Falklands War and a survivor of the attack on the <em>Sir Galahad</em>. Weston demanded FIFA take action:</p>",

    quote("“FIFA have to do something. We can't wear a poppy on our international jerseys because they say that's a political symbol”"),

    "<p>And he added that the players “just have to be more respectful and obey the rules. Obey the rules for no politics brought into sport.”</p>",

    "<p>Weston's comparison — the poppy that in the United Kingdom commemorates the war dead, and which FIFA itself has restricted at international matches for being a political symbol — was picked up by much of the British sports press as the most-quoted argument against the Argentine banner.</p>",

    "<h3>What the papers couldn't avoid writing</h3>",

    "<p>That is the paradox that stings London the most: to explain why they were angry, much of the British media had to do what it has spent decades avoiding — telling its own audience what Malvinas is, why Argentina claims it, and what happened in 1982. The <strong>Daily Mail</strong> confirmed that FIFA, under president Gianni Infantino, would wait until the end of the tournament to resolve any punishment, keeping the case hanging over the team even as it played the final. <strong>Sky Sports</strong> reported that FIFA's disciplinary file was not limited to the banner: it also covered discriminatory chants, security and protocol failures, and objects thrown onto the pitch at several matches. And <strong>Yahoo News UK</strong> reproduced the British government's response word for word.</p>",

    "<p>None of those articles could write about the banner without writing, even if only in one line, the word “Malvinas” — or “Falklands”, on the British side — followed by an explanation of a 74-day war: 255 British soldiers, 649 Argentines and three islanders killed in 1982. That is exactly the visibility that traditional diplomacy cannot achieve.</p>",

    "<h3>The counterpoint nobody expected: Washington</h3>",

    "<p>While London called for sanctions, the White House did the opposite. Donald Trump's liaison for the World Cup came out in support of the Argentine players' right to express themselves, invoking freedom of expression, and rejected British calls for punishment. It was not a small detail for the British press, used to counting on Washington as an automatic ally in any dispute with Buenos Aires.</p>",

    "<h3>Milei, on the other side of the counter</h3>",

    "<p>From Argentina, President Javier Milei described the players' celebration as “perfectly valid”, saying the message “reflects a sentiment shared by all Argentinians.” Still, he predicted FIFA would end up fining the team: “the players get carried away by their emotions, they act on impulse, and that will likely lead to discussions about a fine.”</p>",

    "<h3>FIFA, still without a ruling</h3>",

    "<p>Nearly a month after the incident, and weeks after the final — which Argentina lost 1-0 to Spain at MetLife Stadium — FIFA has not resolved the case. The disciplinary committee opened a file over several alleged breaches, including the banner, and gave the parties a chance to state their position before ruling. The most-cited precedent is 2014, when FIFA fined the Argentine Football Association £20,000 for an identical banner. Everything points, once again, to a fine rather than a sporting sanction.</p>",

    "<p>For those of us watching from Patagonia — the gateway to the South Atlantic, the region that sees islanders pass through on the monthly flight from Río Gallegos to Malvinas — there is a reading that survives whatever fine FIFA ends up setting. For weeks, a prime minister, a cabinet secretary, a war veteran and the entire British press had to say out loud, and explain, the word London prefers to keep off the agenda. The islands' lawmakers wrote to FIFA to ask that the Argentine players be punished. But, without meaning to, that letter confirmed what was already obvious on every front page: the banner did its job.</p>",
])

# ============================== PORTUGUÊS ==============================
cuerpo_pt = "\n\n".join([
    DATELINE.format("Malvinas — Relatório GLOBALpatagonia"),

    "<p>A bandeira com a frase “Las Malvinas son argentinas” (“As Malvinas são argentinas”) que os jogadores da Seleção ergueram em Atlanta no dia 15 de julho, após vencer a Inglaterra por 2 a 1 na semifinal da Copa, não se apagou com o apito final. Semanas depois, enquanto a FIFA ainda delibera sobre o que fazer, a carta que um grupo de legisladores das ilhas enviou ao órgão é a prova de que, nas ilhas e em Londres, o gesto ainda incomoda.</p>",

    "<h3>A carta dos ilhéus à FIFA</h3>",

    "<p>O semanário <em>Penguin News</em>, o jornal das ilhas, revelou que membros da Assembleia Legislativa das Malvinas (MLA) escreveram uma carta aberta à FIFA pedindo sanções disciplinares contra os jogadores argentinos. Classificaram o gesto de “insensitive” —insensível— e argumentaram:</p>",

    quote("“It is the avowed policy of the Falkland Islands Government that we do not wish to see politics being brought into sport”<br><span style=\"font-size:.95rem;opacity:.75;font-style:normal\">(“É política declarada do Governo das Ilhas Falkland que não desejamos ver a política ser trazida para o esporte”)</span>"),

    "<p>O argumento dos legisladores apela, mais uma vez, à autodeterminação: a vontade da população das ilhas de continuar sendo um Território Britânico Ultramarino. É o mesmo argumento repetido desde o referendo de 2013, quando 99,8% dos eleitores —menos de 1.400 pessoas— optaram por manter o vínculo com a Coroa.</p>",

    img_block(IMG_CARTEL, "Placa de boas-vindas nas Ilhas Malvinas",
              "É assim que as ilhas se apresentam a quem chega: apenas cerca de 3.500 habitantes, a 463 quilômetros da costa patagônica, que se definem como território britânico."),

    img_block(IMG_BANDERA, "Jogadores argentinos com a bandeira 'Las Malvinas son Argentinas' em Atlanta",
              "A faixa que os jogadores argentinos exibiram no gramado do Mercedes-Benz Stadium, em Atlanta, após o 2 a 1 sobre a Inglaterra."),

    "<h3>Fala o governo britânico</h3>",

    "<p>O reclamo não ficou restrito às ilhas. O porta-voz do primeiro-ministro britânico, Keir Starmer, saiu para marcar posição diante da imprensa:</p>",

    quote("“The World Cup might not be ours, but the Falkland Islands definitely are”<br><span style=\"font-size:.95rem;opacity:.75;font-style:normal\">(“A Copa do Mundo pode não ser nossa, mas as Ilhas Falkland definitivamente são”)</span>"),

    "<p>E acrescentou a fórmula de sempre: “Self-determination rests with the islanders and our commitment to the Falklands will never waver” (“A autodeterminação está nas mãos dos ilhéus, e nosso compromisso com as Falklands jamais vacilará”).</p>",

    "<p>Horas depois, o secretário de Negócios, Peter Kyle, foi mais longe em entrevista à <strong>BBC Breakfast</strong>. Classificou a conduta dos jogadores como “entirely inappropriate” (inteiramente inapropriada) e pediu que a FIFA investigasse “thoroughly” o que definiu como uma “egregious violation” —uma violação flagrante— do regulamento do torneio.</p>",

    img_block(IMG_PARLAMENTO, "Câmara dos Comuns do Parlamento britânico",
              "O Parlamento britânico, onde o reclamo pela bandeira chegou até o porta-voz do primeiro-ministro."),

    "<h3>O veterano que pediu mão dura</h3>",

    "<p>Entre as vozes que mais ressoaram na imprensa britânica esteve a de <strong>Simon Weston</strong>, veterano da Guerra das Malvinas de 1982, sobrevivente do ataque ao navio <em>Sir Galahad</em>. Weston exigiu que a FIFA agisse:</p>",

    quote("“FIFA have to do something. We can't wear a poppy on our international jerseys because they say that's a political symbol”<br><span style=\"font-size:.95rem;opacity:.75;font-style:normal\">(“A FIFA precisa fazer alguma coisa. Nós não podemos usar uma papoula em nossas camisas da seleção porque dizem que é um símbolo político”)</span>"),

    "<p>E completou: os jogadores “just have to be more respectful and obey the rules. Obey the rules for no politics brought into sport” (“só precisam ser mais respeitosos e obedecer às regras. Obedecer à regra de que a política não entra no esporte”).</p>",

    "<p>A comparação de Weston —a papoula (<em>poppy</em>) que no Reino Unido homenageia os mortos em guerra, e que a própria FIFA restringiu em partidas internacionais por considerá-la um símbolo político— foi repetida por boa parte da imprensa esportiva britânica como o argumento mais citado contra a bandeira argentina.</p>",

    "<h3>O que os jornais não puderam deixar de escrever</h3>",

    "<p>Aí está o paradoxo que mais incomoda Londres: para explicar por que se irritaram, boa parte da mídia britânica teve que fazer o que evita há décadas —contar à própria audiência o que são as Malvinas, por que a Argentina as reivindica e o que aconteceu em 1982. O <strong>Daily Mail</strong> confirmou que a FIFA, presidida por Gianni Infantino, esperaria o fim do torneio para resolver qualquer sanção, mantendo o caso em aberto sobre a Seleção mesmo enquanto ela disputava a final. A <strong>Sky Sports</strong> detalhou que o processo disciplinar da FIFA não se limitava à bandeira: incluía também cânticos discriminatórios, falhas de protocolo de segurança e objetos arremessados ao gramado em diferentes partidas do torneio. E a <strong>Yahoo News UK</strong> reproduziu, palavra por palavra, a resposta do governo britânico.</p>",

    "<p>Nenhuma dessas matérias conseguiu escrever sobre a bandeira sem escrever, ainda que em uma linha, a palavra “Malvinas” —ou “Falklands”, do lado britânico— seguida da explicação de uma guerra de 74 dias: 255 soldados britânicos, 649 argentinos e três ilhéus mortos em 1982. Essa é, exatamente, a visibilidade que a diplomacia tradicional não consegue.</p>",

    "<h3>O contraponto que ninguém esperava: Washington</h3>",

    "<p>Enquanto Londres pedia sanções, a Casa Branca fez o contrário. O elo do governo de Donald Trump para a Copa saiu em defesa do direito dos jogadores argentinos de se manifestar, invocando a liberdade de expressão, e rejeitou os pedidos britânicos de punição. O detalhe não foi pequeno para a imprensa britânica, acostumada a contar com Washington como aliado automático em qualquer disputa com Buenos Aires.</p>",

    "<h3>Milei, do outro lado do balcão</h3>",

    "<p>Da Argentina, o presidente Javier Milei classificou a celebração dos jogadores como “perfectly valid” (perfeitamente válida), e disse que a mensagem “reflects a sentiment shared by all Argentinians” (reflete um sentimento compartilhado por todos os argentinos). Ainda assim, previu que a FIFA acabaria multando a equipe: “the players get carried away by their emotions, they act on impulse, and that will likely lead to discussions about a fine” (os jogadores se deixam levar pelas emoções, agem por impulso, e isso provavelmente vai gerar uma discussão sobre uma multa).</p>",

    "<h3>A FIFA, ainda sem decisão</h3>",

    "<p>A quase um mês do episódio, e semanas após a final —que a Argentina perdeu por 1 a 0 para a Espanha no MetLife Stadium—, a FIFA não resolveu o caso. O comitê disciplinar abriu processo por várias infrações, incluída a faixa, e deu às partes a possibilidade de apresentar sua posição antes de decidir. O antecedente mais citado é 2014, quando a FIFA multou a AFA em 20 mil libras por uma faixa idêntica. Tudo indica que o desfecho, mais uma vez, será uma multa, e não uma sanção esportiva.</p>",

    "<p>Para quem observa isso a partir da Patagônia —o portão de embarque para o Atlântico Sul, a região que vê os ilhéus passarem rumo às Malvinas pelo voo mensal saído de Río Gallegos— há uma leitura que sobrevive a qualquer multa que a FIFA venha a fixar. Durante semanas, um primeiro-ministro, um secretário de Estado, um veterano de guerra e toda a imprensa britânica tiveram que dizer em voz alta, e explicar, a palavra que Londres prefere manter fora da pauta. Os legisladores das ilhas escreveram à FIFA para pedir que os jogadores argentinos fossem punidos. Mas, sem querer, confirmaram com essa carta o que já era evidente em cada capa de jornal: a bandeira cumpriu seu papel.</p>",
])

# ============================== 中文 ==============================
cuerpo_zh = "\n\n".join([
    DATELINE.format("马尔维纳斯 — GLOBALpatagonia 深度报道"),

    "<p>7月15日，阿根廷队在亚特兰大以2比1击败英格兰、晋级世界杯半决赛之后，球员们展示的那面写着“Las Malvinas son argentinas”（“马尔维纳斯属于阿根廷”）的旗帜，并没有随着终场哨声而平息。数周之后，就在国际足联仍在商议如何处置之际，一群群岛议员写给该机构的信，恰恰证明了这一举动仍然刺痛着群岛和伦敦两边。</p>",

    "<h3>岛民写给国际足联的信</h3>",

    "<p>群岛的周报《企鹅新闻》（<em>Penguin News</em>）披露，马尔维纳斯立法议会（MLA）的多名成员联名写信给国际足联，要求对阿根廷球员实施纪律处罚。他们称这一举动“insensitive”——缺乏体谅——并辩称：</p>",

    quote("“It is the avowed policy of the Falkland Islands Government that we do not wish to see politics being brought into sport”<br><span style=\"font-size:.95rem;opacity:.75;font-style:normal\">（“福克兰群岛政府一贯的政策是，我们不希望看到政治被带入体育运动”）</span>"),

    "<p>议员们的论点再次诉诸自决权：岛上居民希望继续作为英国海外领地的意愿。这与2013年公投以来反复出现的论调如出一辙——当时99.8%的投票者（不到1400人）选择继续与英国王室保持联系。</p>",

    img_block(IMG_CARTEL, "马尔维纳斯群岛上的欢迎标牌",
              "这就是群岛向来访者展示自己的方式：仅约3500名居民，距离巴塔哥尼亚海岸463公里，自我定位为英国领土。"),

    img_block(IMG_BANDERA, "阿根廷球员在亚特兰大展示写有'Las Malvinas son Argentinas'的旗帜",
              "阿根廷球员在亚特兰大梅赛德斯-奔驰体育场的草坪上展开的那面旗帜，就在2比1战胜英格兰之后。"),

    "<h3>英国政府发声</h3>",

    "<p>这一诉求没有止步于群岛。英国首相基尔·斯塔默的发言人公开表明立场：</p>",

    quote("“The World Cup might not be ours, but the Falkland Islands definitely are”<br><span style=\"font-size:.95rem;opacity:.75;font-style:normal\">（“世界杯或许不属于我们，但福克兰群岛绝对属于我们”）</span>"),

    "<p>并补上了那句一贯的说法：“Self-determination rests with the islanders and our commitment to the Falklands will never waver”（“自决权掌握在岛民手中，我们对福克兰群岛的承诺永远不会动摇”）。</p>",

    "<p>几个小时后，商业大臣彼得·凯尔在接受<strong>BBC Breakfast</strong>采访时表态更为强硬。他称球员的行为“entirely inappropriate”（完全不恰当），并要求国际足联“thoroughly”（彻底）调查他所说的“egregious violation”——对赛事规则的严重违反。</p>",

    img_block(IMG_PARLAMENTO, "英国议会下议院",
              "英国议会——这场围绕旗帜的争议，一路闹到了首相发言人的办公桌前。"),

    "<h3>要求严惩的老兵</h3>",

    "<p>在英国媒体上回响最大的声音之一，来自1982年马岛战争老兵、“加拉哈德爵士”号（<em>Sir Galahad</em>）袭击事件幸存者<strong>西蒙·韦斯顿</strong>。韦斯顿要求国际足联采取行动：</p>",

    quote("“FIFA have to do something. We can't wear a poppy on our international jerseys because they say that's a political symbol”<br><span style=\"font-size:.95rem;opacity:.75;font-style:normal\">（“国际足联必须有所作为。我们的国家队球衣上都不能戴虞美人花，因为他们说那是一种政治符号”）</span>"),

    "<p>他还补充说，球员们“just have to be more respectful and obey the rules. Obey the rules for no politics brought into sport”（“只需要更懂得尊重，遵守规则。遵守不把政治带入体育的规则”）。</p>",

    "<p>韦斯顿的类比——虞美人花（<em>poppy</em>）在英国是纪念阵亡将士的符号，而国际足联自己也曾以政治符号为由，在国际比赛中限制佩戴虞美人花——被英国体育媒体广泛引用，成为反对阿根廷旗帜最常被提及的论据。</p>",

    "<h3>报纸不得不写下的内容</h3>",

    "<p>这正是最让伦敦难堪的悖论：为了解释他们为何愤怒，相当一部分英国媒体不得不做他们几十年来一直回避的事情——向自己的读者解释什么是马尔维纳斯、阿根廷为何主张对其拥有主权，以及1982年到底发生了什么。<strong>《每日邮报》</strong>证实，由詹尼·因凡蒂诺执掌的国际足联将等到赛事结束后再处理任何处罚，这意味着即便阿根廷队打进决赛，这桩案子也一直悬在球队头上。<strong>天空体育</strong>披露，国际足联的纪律调查并不局限于那面旗帜：还涉及歧视性口号、安保和流程失误，以及本届赛事多场比赛中被扔进场内的物品。<strong>英国雅虎新闻</strong>则一字不差地转载了英国政府的回应。</p>",

    "<p>没有一篇报道能绕开这面旗帜，而不写下——哪怕只有一行——“马尔维纳斯”这个词，或英国一方所说的“福克兰”，紧跟着的，是对一场持续74天的战争的解释：255名英国士兵、649名阿根廷人和3名岛民在1982年丧生。这恰恰是传统外交手段无法企及的曝光度。</p>",

    "<h3>没人预料到的对立面：华盛顿</h3>",

    "<p>就在伦敦要求制裁之际，白宫的态度截然相反。特朗普政府派驻世界杯的联络人公开表态，支持阿根廷球员表达自身立场的权利，援引言论自由，并拒绝了英国方面的处罚要求。对于习惯了在与布宜诺斯艾利斯的任何争端中把华盛顿视为天然盟友的英国媒体来说，这个细节分量不小。</p>",

    "<h3>米莱：站在柜台的另一边</h3>",

    "<p>在阿根廷这一边，总统哈维尔·米莱将球员的庆祝方式称为“perfectly valid”（完全正当），并表示这一表态“reflects a sentiment shared by all Argentinians”（反映了所有阿根廷人共有的情感）。尽管如此，他也预料国际足联最终会对球队处以罚款：“the players get carried away by their emotions, they act on impulse, and that will likely lead to discussions about a fine”（球员们被情绪裹挟，出于一时冲动行事，这很可能会引发关于罚款的讨论）。</p>",

    "<h3>国际足联，仍未作出裁决</h3>",

    "<p>事件发生近一个月后，决赛结束数周后——阿根廷在决赛中于大都会人寿体育场以0比1不敌西班牙——国际足联仍未就此案作出裁决。纪律委员会已就多项涉嫌违规（包括这面旗帜）立案调查，并给予各方在裁决前陈述立场的机会。被引用最多的先例是2014年，国际足联曾就一面几乎一模一样的旗帜，对阿根廷足协处以2万英镑罚款。种种迹象表明，这一次的结局很可能同样是罚款，而非体育层面的处罚。</p>",

    "<p>对我们这些从巴塔哥尼亚观察这一切的人来说——这里是通往南大西洋的门户，是岛民们每月搭乘从里奥加耶戈斯出发的航班前往马尔维纳斯时途经的地方——无论国际足联最终开出多少罚款，都有一层意义不会随之消失。数周以来，一位首相、一位内阁大臣、一位战争老兵，以及整个英国媒体界，都不得不大声说出、并解释伦敦宁愿束之高阁的那个词。群岛的议员们写信给国际足联，要求惩罚阿根廷球员。但他们大概没有想到，这封信恰恰印证了每一个头版早已显而易见的事实：这面旗帜，达到了它的目的。</p>",
])

FECHA_META = "15 de agosto de 2026 · J. Martineau"

nueva_entrada = {
    "id": "20260815-propio-kelper-reaccion-bandera",
    "titulo": "La reacción kelper y británica a la bandera de Malvinas",
    "bajada": "Los legisladores de las islas le escribieron a la FIFA. El gobierno inglés salió a responder. Un ministro habló en la BBC. Y hasta un veterano de la guerra de 1982 pidió sanciones. Repasamos, con nombres y citas textuales, cómo se vivió en Gran Bretaña la bandera que los jugadores argentinos alzaron en Atlanta.",
    "cuerpo": cuerpo,
    "titulo_en": "How Britain and the Falkland Islanders Reacted to the Malvinas (Falklands) Banner",
    "bajada_en": "The islands' lawmakers wrote to FIFA. The British government answered back. A minister spoke on the BBC. And a veteran of the 1982 war called for sanctions. We go through it — names and direct quotes — to see how Britain lived through the banner Argentina's players raised in Atlanta.",
    "cuerpo_en": cuerpo_en,
    "titulo_pt": "A reação kelper e britânica à bandeira das Malvinas",
    "bajada_pt": "Os legisladores das ilhas escreveram à FIFA. O governo britânico respondeu. Um ministro falou na BBC. E até um veterano da guerra de 1982 pediu sanções. Repassamos, com nomes e citações textuais, como a Grã-Bretanha viveu a bandeira que os jogadores argentinos ergueram em Atlanta.",
    "cuerpo_pt": cuerpo_pt,
    "titulo_zh": "岛民与英国政府:马尔维纳斯旗帜引发的怒火",
    "bajada_zh": "群岛的议员给国际足联写了信。英国政府作出回应。一位大臣在BBC发声。就连一位1982年战争的老兵也要求制裁。我们通过真实姓名和直接引语，回顾英国如何面对阿根廷球员在亚特兰大高举的那面旗帜。",
    "cuerpo_zh": cuerpo_zh,
    "tag": "🇦🇷 Malvinas",
    "categoria": "malvinas|politica|mundial|internacional",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "malvinas",
    "imagen": IMG_BANDERA,
    "imagen_keywords": "malvinas bandera kelper falklands mundial 2026 seleccion argentina inglaterra fifa",
    "hashtags_en": "#Malvinas #Falklands #Argentina #WorldCup2026 #FIFA",
    "meta": FECHA_META,
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
