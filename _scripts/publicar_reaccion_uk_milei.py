#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Publica el informe "Reino Unido responde a Milei por Malvinas"
# en propios.json (modelo: publicar_malvinas_eeuu_otan.py)
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

IMG_PORTADA = "fotos/malvinas-milei-discurso-gabinete-2026.webp"
IMG_STANLEY = "fotos/puerto-argentino-stanley-aereo.webp"
IMG_PLATAFORMA = "fotos/plataforma-petrolera-offshore-atardecer.webp"

# ============================== ESPAÑOL ==============================
cuerpo = "\n\n".join([
    DATELINE.format("Malvinas — Informe GLOBALpatagonia"),

    "<p>BUENOS AIRES. El jueves, en un mensaje por cadena nacional flanqueado por su gabinete, el presidente argentino Javier Milei volvió a poner a las Malvinas en el centro de la agenda: firmó un DNU que amplía los recursos del Ministerio de Defensa, anunció la construcción de una base naval en Ushuaia y confirmó que las empresas con operaciones de hidrocarburos en la plataforma continental en disputa quedarán excluidas del RIGI, el régimen de incentivos para grandes inversiones. “Los isleños no tienen derecho a la autodeterminación”, afirmó, en la misma línea con la que también cuestionó lo que calificó como “múltiples crisis de carácter migratorio, demográfico y económico” del Reino Unido. La primera respuesta oficial, a cargo del secretario de Defensa Wes Streeting, llegó horas después y fue tajante: los isleños “eligen ser británicos” y el Reino Unido “no negociará la soberanía”.</p>",

    "<p>LONDRES. Pero la onda expansiva del discurso recién empezaba. En las horas siguientes, la reacción se extendió a la política, los mercados y la prensa británica en su conjunto: desde la respuesta oficial, monolítica y previsible, hasta un desplome en las acciones de las petroleras que operan en el archipiélago, pasando por una cobertura mediática que osciló entre el sensacionalismo, el alarmismo y el ataque político al gobierno laborista.</p>",

    img_block(IMG_STANLEY, "Vista aérea de Puerto Argentino/Stanley",
              "Puerto Argentino/Stanley, la capital de las islas en disputa, en el centro de la escalada diplomática."),

    "<h3>La respuesta oficial: “Inquebrantable”</h3>",

    "<p>La posición del gobierno británico no dejó espacio para matices. El canciller Ed Miliband, del ala izquierda del gobierno laborista de Andy Burnham, fue tajante:</p>",

    quote("“La posición británica sobre las Malvinas es inquebrantable. Las islas son británicas y seguirán siéndolo porque eso es lo que quieren los isleños. El derecho a la autodeterminación es inviolable, se asienta en el derecho internacional y lo vamos a sostener”."),

    "<p>El ministro de Defensa, Wes Streeting, más cercano al ala derecha del partido, coincidió en el fondo pero añadió una lectura política:</p>",

    quote("“El discurso de Milei tiene mucho más que ver con la política interna de Argentina que con las islas Malvinas”."),

    "<p>Desde la oposición, la lideresa conservadora Kemi Badenoch, admiradora confesa de Margaret Thatcher al igual que Milei, subió el tono con un espíritu más confrontativo:</p>",

    quote("“El Reino Unido no se rinde ante patoteros. Si Milei quiere un país fuerte, debería reconstruir su economía, no amenazar a otros”."),

    "<h3>El impacto en los mercados</h3>",

    img_block(IMG_PLATAFORMA, "Plataforma petrolera offshore al atardecer",
              "Las petroleras que operan licencias en la cuenca norte de Malvinas fueron las primeras en sentir el golpe en sus acciones."),

    "<p>Más allá de las palabras, los mercados financieros reaccionaron con inmediatez. En la bolsa de Tel Aviv, las acciones de la israelí Navitas Petroleum —que controla el 65% de la explotación en la cuenca norte de las islas a través de una subsidiaria en el Reino Unido— cayeron un 4,5%. En Londres, el desplome fue aún más pronunciado: Rockhopper Exploration, dueña del 35% restante, y Borders & Southern, que también opera en la zona, experimentaron caídas del 15% cada una.</p>",

    "<h3>La prensa británica: entre el alarmismo y la política interna</h3>",

    "<p>La cobertura mediática fue, como titula el propio análisis, “curioser and curioser”, en un guiño a Alicia en el país de las maravillas. El tono de entusiasmo que alguna vez despertó el Milei “fanático de Margaret Thatcher, simpatizante de la autodeterminación de los isleños y amante de la motosierra” dio paso a la indignación.</p>",

    "<p><strong>Los tabloides fueron los más virulentos:</strong></p>",

    "<p><strong>Sky News</strong>, de Rupert Murdoch, abrió con un alarmista “¿Va Argentina a invadir las islas nuevamente?”, acompañado de una toma del discurso de Milei flanqueado por todo su gabinete, para luego vincular la escalada con el petróleo y la intervención de Donald Trump.</p>",

    "<p><strong>The Sun</strong> convocó a sus lectores con una encuesta del día: “¿Tenemos que ser mucho más enérgicos en nuestro rechazo de Argentina?”, ofreciendo un voucher de 100 libras entre los participantes.</p>",

    "<p>El <strong>Daily Mail</strong> aprovechó el discurso para atacar al gobierno laborista: “Argentina está apostando otra vez a las Falklands porque el laborismo es débil”, haciéndose eco de la reacción del partido ultraderechista Reform UK, de Nigel Farage.</p>",

    "<p>El <strong>Daily Express</strong> tituló que “las tensiones explotan con la respuesta del Reino Unido a la amenaza bélica de Milei”.</p>",

    "<p>Un aspecto destacado por la mayoría de los tabloides fue el pasaje en el que Milei habla de las “múltiples crisis de carácter migratorio, demográfico y económico” que enfrenta el Reino Unido, un discurso que, paradójicamente, sintoniza con la cobertura diaria que estos mismos medios hacen del gobierno laborista.</p>",

    "<p><strong>Los medios más ponderados intentaron aportar sensatez:</strong></p>",

    "<p>La <strong>BBC</strong> puso el foco en la situación interna argentina y la incongruencia entre la posición previa de Milei respecto a las islas y la actual, en un momento en que “su popularidad está cayendo en picada”.</p>",

    "<p><strong>The Guardian</strong> vinculó el giro de Milei con una presión de Donald Trump, que “se la tiene jurada al gobierno laborista desde que Keir Starmer se hizo el difícil con lo de darle todo el apoyo militar que quería para su aventura en Irán”. El matutino también recordó que “Milei siempre se describió como un gran admirador de Margaret Thatcher” y que su interés por la soberanía es “muy reciente”, coincidiendo con el momento en que Estados Unidos comenzó a reconsiderar su posición.</p>",

    "<p>El <strong>Daily Telegraph</strong>, por su parte, se movió hacia posiciones más cercanas a Nigel Farage y tituló parafraseando a Milei: “Argentina va a prevalecer sobre una decadente Gran Bretaña”, con un subtítulo que subrayaba que el presidente argentino “dice que el Reino Unido es un país en crisis al anunciar planes para imponer sanciones a la explotación petrolera en las Malvinas”.</p>",

    "<h3>Análisis</h3>",

    "<p>La cobertura británica refleja, en su conjunto, una lectura que prioriza la coyuntura política interna de Argentina —y las propias disputas domésticas del Reino Unido— por encima de una genuina preocupación por el conflicto de soberanía. Como señala el análisis, las palabras de Milei y las de los jugadores argentinos tras el mundial pueden ser similares, pero “su significado fue radicalmente distinto”. Lo que queda en evidencia es que, para el establishment británico, las Malvinas siguen siendo un tema cerrado, y cualquier revisión de esa posición es leída, ante todo, como un acto de política interna argentina.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Fuentes: Sky News, The Sun, Daily Mail, Daily Express, BBC, The Guardian, The Daily Telegraph.</p>',
])

# ============================== ENGLISH ==============================
cuerpo_en = "\n\n".join([
    DATELINE.format("Malvinas — GLOBALpatagonia Report"),

    "<p>BUENOS AIRES. On Thursday, in a nationally broadcast address flanked by his cabinet, Argentine President Javier Milei put Malvinas (the Falkland Islands) back at the center of the agenda: he signed a decree expanding the Defence Ministry's resources, announced the construction of a naval base in Ushuaia, and confirmed that companies with hydrocarbon operations on the disputed continental shelf will be excluded from RIGI, the incentive scheme for large investments. “The islanders have no right to self-determination,” he said, in the same address in which he also criticized what he called the UK's “multiple migratory, demographic and economic crises.” The first official response, from Defence Secretary Wes Streeting, came hours later and was blunt: the islanders “choose to be British” and the UK “will not negotiate sovereignty.”</p>",

    "<p>LONDON. But the speech's shockwaves were only getting started. In the hours that followed, the reaction spread to politics, the markets and the British press as a whole: from an official response that was monolithic and predictable, to a plunge in the shares of the oil companies operating in the archipelago, to media coverage that swung between sensationalism, alarmism and political attacks on the Labour government.</p>",

    img_block(IMG_STANLEY, "Aerial view of Stanley/Puerto Argentino",
              "Stanley/Puerto Argentino, the capital of the disputed islands, at the center of the diplomatic escalation."),

    "<h3>The official response: “Unshakeable”</h3>",

    "<p>The British government's position left no room for nuance. Foreign Secretary Ed Miliband, from the left wing of Andy Burnham's Labour government, was blunt:</p>",

    quote("“Britain's position on the Falklands is unshakeable. The islands are British and will remain so because that is what the islanders want. The right to self-determination is inviolable, it is grounded in international law, and we will uphold it.”"),

    "<p>Defence Secretary Wes Streeting, closer to the party's right flank, agreed in substance but added a political read:</p>",

    quote("“Milei's speech has far more to do with Argentina's domestic politics than with the Falkland Islands.”"),

    "<p>From the opposition, Conservative leader Kemi Badenoch, a self-declared admirer of Margaret Thatcher just like Milei, struck a more combative tone:</p>",

    quote("“Britain does not bow to bullies. If Milei wants a strong country, he should rebuild his economy, not threaten others.”"),

    "<h3>The impact on the markets</h3>",

    img_block(IMG_PLATAFORMA, "Offshore oil platform at dusk",
              "The oil companies holding licenses in Malvinas' northern basin were the first to feel the hit to their shares."),

    "<p>Beyond the rhetoric, financial markets reacted immediately. On the Tel Aviv stock exchange, shares of Israel's Navitas Petroleum — which controls 65% of the exploration in the islands' northern basin through a UK subsidiary — fell 4.5%. In London, the drop was even steeper: Rockhopper Exploration, which owns the remaining 35%, and Borders &amp; Southern, which also operates in the area, each saw their shares fall 15%.</p>",

    "<h3>The British press: between alarmism and domestic politics</h3>",

    "<p>Media coverage was, to borrow the analysis's own description, “curiouser and curiouser” — a nod to Alice in Wonderland. The enthusiasm once sparked by a Milei cast as “a Thatcher fanatic, a supporter of the islanders' self-determination and a chainsaw-wielding libertarian” gave way to outrage.</p>",

    "<p><strong>The tabloids were the most virulent:</strong></p>",

    "<p><strong>Sky News</strong>, owned by Rupert Murdoch, opened with an alarmist “Is Argentina about to invade the islands again?”, paired with footage of Milei's speech flanked by his entire cabinet, before linking the escalation to oil and to Donald Trump's involvement.</p>",

    "<p><strong>The Sun</strong> rallied its readers with its poll of the day: “Do we need to be much tougher in standing up to Argentina?”, offering a £100 voucher to participants.</p>",

    "<p>The <strong>Daily Mail</strong> used the speech to attack the Labour government: “Argentina is chancing its arm over the Falklands again because Labour is weak,” echoing the reaction of Nigel Farage's hard-right Reform UK.</p>",

    "<p>The <strong>Daily Express</strong> ran with “tensions explode as UK hits back at Milei's war threat.”</p>",

    "<p>One passage highlighted by most of the tabloids was the moment Milei spoke of the “multiple migratory, demographic and economic crises” facing the UK — a line that, ironically, echoes these same outlets' own daily coverage of the Labour government.</p>",

    "<p><strong>The more measured outlets tried to bring some perspective:</strong></p>",

    "<p>The <strong>BBC</strong> focused on Argentina's domestic situation and the inconsistency between Milei's previous stance on the islands and his current one, at a moment when “his approval ratings are in freefall.”</p>",

    "<p><strong>The Guardian</strong> linked Milei's shift to pressure from Donald Trump, who “has had it in for the Labour government ever since Keir Starmer played hardball over giving him all the military support he wanted for his Iran adventure.” The paper also noted that “Milei has always described himself as a great admirer of Margaret Thatcher” and that his sudden interest in sovereignty is “very recent,” coinciding with the moment the United States began reconsidering its position.</p>",

    "<p>The <strong>Daily Telegraph</strong>, for its part, moved closer to Nigel Farage's line, running a headline paraphrasing Milei: “Argentina will prevail over a declining Britain,” with a subhead noting that the Argentine president “says the UK is a country in crisis as he announces plans to sanction oil exploration in the Falklands.”</p>",

    "<h3>Analysis</h3>",

    "<p>Taken together, British coverage reflects a reading that prioritizes Argentina's domestic political moment — and the UK's own internal disputes — over any genuine concern for the sovereignty dispute. As the analysis notes, Milei's words and those of the Argentine footballers after the World Cup may sound similar, but “their meaning was radically different.” What emerges is that, for the British establishment, Malvinas remains a closed matter, and any revisiting of that position is read, above all, as an act of Argentine domestic politics.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Sources: Sky News, The Sun, Daily Mail, Daily Express, BBC, The Guardian, The Daily Telegraph.</p>',
])

# ============================== PORTUGUÊS ==============================
cuerpo_pt = "\n\n".join([
    DATELINE.format("Malvinas — Relatório GLOBALpatagonia"),

    "<p>BUENOS AIRES. Na quinta-feira, em um pronunciamento em cadeia nacional cercado por seu gabinete, o presidente argentino Javier Milei voltou a colocar as Malvinas no centro da agenda: assinou um decreto que amplia os recursos do Ministério da Defesa, anunciou a construção de uma base naval em Ushuaia e confirmou que as empresas com operações de hidrocarbonetos na plataforma continental em disputa ficarão excluídas do RIGI, o regime de incentivos para grandes investimentos. “Os ilhéus não têm direito à autodeterminação”, afirmou, na mesma linha em que também questionou o que classificou como “múltiplas crises de caráter migratório, demográfico e econômico” do Reino Unido. A primeira resposta oficial, do secretário de Defesa Wes Streeting, veio horas depois e foi taxativa: os ilhéus “escolhem ser britânicos” e o Reino Unido “não vai negociar a soberania”.</p>",

    "<p>LONDRES. Mas a onda de choque do discurso ainda estava só começando. Nas horas seguintes, a reação se estendeu à política, aos mercados e à imprensa britânica como um todo: da resposta oficial, monolítica e previsível, a um tombo nas ações das petrolíferas que operam no arquipélago, passando por uma cobertura da imprensa que oscilou entre o sensacionalismo, o alarmismo e o ataque político ao governo trabalhista.</p>",

    img_block(IMG_STANLEY, "Vista aérea de Porto Argentino/Stanley",
              "Porto Argentino/Stanley, a capital das ilhas em disputa, no centro da escalada diplomática."),

    "<h3>A resposta oficial: “Inabalável”</h3>",

    "<p>A posição do governo britânico não deixou espaço para nuances. O chanceler Ed Miliband, da ala esquerda do governo trabalhista de Andy Burnham, foi taxativo:</p>",

    quote("“A posição britânica sobre as Malvinas é inabalável. As ilhas são britânicas e continuarão sendo, porque é isso que os ilhéus querem. O direito à autodeterminação é inviolável, está fundamentado no direito internacional e vamos sustentá-lo.”"),

    "<p>O ministro da Defesa, Wes Streeting, mais próximo da ala direita do partido, concordou no fundo, mas acrescentou uma leitura política:</p>",

    quote("“O discurso de Milei tem muito mais a ver com a política interna da Argentina do que com as Malvinas.”"),

    "<p>Da oposição, a líder conservadora Kemi Badenoch, admiradora confessa de Margaret Thatcher assim como Milei, subiu o tom com um espírito mais confrontador:</p>",

    quote("“O Reino Unido não se curva a valentões. Se Milei quer um país forte, deveria reconstruir sua economia, não ameaçar os outros.”"),

    "<h3>O impacto nos mercados</h3>",

    img_block(IMG_PLATAFORMA, "Plataforma petrolífera offshore ao entardecer",
              "As petrolíferas com licenças na bacia norte das Malvinas foram as primeiras a sentir o golpe em suas ações."),

    "<p>Além das palavras, os mercados financeiros reagiram de imediato. Na bolsa de Tel Aviv, as ações da israelense Navitas Petroleum —que controla 65% da exploração na bacia norte das ilhas através de uma subsidiária no Reino Unido— caíram 4,5%. Em Londres, o tombo foi ainda mais acentuado: Rockhopper Exploration, dona dos 35% restantes, e Borders &amp; Southern, que também opera na região, tiveram quedas de 15% cada uma.</p>",

    "<h3>A imprensa britânica: entre o alarmismo e a política interna</h3>",

    "<p>A cobertura da imprensa foi, como diz a própria análise, “curioser and curioser”, em uma referência a Alice no País das Maravilhas. O tom de entusiasmo que um dia despertou o Milei “fanático por Margaret Thatcher, simpatizante da autodeterminação dos ilhéus e amante da motosserra” deu lugar à indignação.</p>",

    "<p><strong>Os tabloides foram os mais virulentos:</strong></p>",

    "<p>A <strong>Sky News</strong>, de Rupert Murdoch, abriu com um alarmista “A Argentina vai invadir as ilhas de novo?”, acompanhado de imagens do discurso de Milei cercado por todo o seu gabinete, para depois vincular a escalada ao petróleo e à intervenção de Donald Trump.</p>",

    "<p>O <strong>The Sun</strong> convocou seus leitores com a enquete do dia: “Precisamos ser muito mais duros na nossa rejeição à Argentina?”, oferecendo um vale de 100 libras entre os participantes.</p>",

    "<p>O <strong>Daily Mail</strong> aproveitou o discurso para atacar o governo trabalhista: “A Argentina está apostando de novo nas Falklands porque o trabalhismo é fraco”, ecoando a reação do partido ultradireitista Reform UK, de Nigel Farage.</p>",

    "<p>O <strong>Daily Express</strong> estampou que “as tensões explodem com a resposta do Reino Unido à ameaça bélica de Milei”.</p>",

    "<p>Um trecho destacado pela maioria dos tabloides foi a passagem em que Milei fala das “múltiplas crises de caráter migratório, demográfico e econômico” que o Reino Unido enfrenta — um discurso que, paradoxalmente, sintoniza com a cobertura diária que esses mesmos veículos fazem do governo trabalhista.</p>",

    "<p><strong>Os veículos mais ponderados tentaram trazer bom senso:</strong></p>",

    "<p>A <strong>BBC</strong> colocou o foco na situação interna argentina e na incoerência entre a posição anterior de Milei sobre as ilhas e a atual, em um momento em que “sua popularidade está em queda livre”.</p>",

    "<p>O <strong>The Guardian</strong> associou a guinada de Milei a uma pressão de Donald Trump, que “está de marcação cerrada com o governo trabalhista desde que Keir Starmer bancou o difícil na hora de dar todo o apoio militar que ele queria para sua aventura no Irã”. O jornal também lembrou que “Milei sempre se descreveu como um grande admirador de Margaret Thatcher” e que seu interesse pela soberania é “muito recente”, coincidindo com o momento em que os Estados Unidos começaram a reconsiderar sua posição.</p>",

    "<p>O <strong>Daily Telegraph</strong>, por sua vez, se aproximou das posições de Nigel Farage e estampou, parafraseando Milei: “A Argentina vai prevalecer sobre uma Grã-Bretanha em decadência”, com um subtítulo destacando que o presidente argentino “diz que o Reino Unido é um país em crise ao anunciar planos de sancionar a exploração de petróleo nas Malvinas”.</p>",

    "<h3>Análise</h3>",

    "<p>A cobertura britânica reflete, no conjunto, uma leitura que prioriza a conjuntura política interna da Argentina —e as próprias disputas domésticas do Reino Unido— acima de uma preocupação genuína com o conflito de soberania. Como aponta a análise, as palavras de Milei e as dos jogadores argentinos após a Copa do Mundo podem ser parecidas, mas “seu significado foi radicalmente diferente”. Fica evidente que, para o establishment britânico, as Malvinas seguem sendo um tema encerrado, e qualquer revisão dessa posição é lida, antes de tudo, como um ato de política interna argentina.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Fontes: Sky News, The Sun, Daily Mail, Daily Express, BBC, The Guardian, The Daily Telegraph.</p>',
])

# ============================== 中文 ==============================
cuerpo_zh = "\n\n".join([
    DATELINE.format("马尔维纳斯 — GLOBALpatagonia 深度报道"),

    "<p>布宜诺斯艾利斯。周四，阿根廷总统哈维尔·米莱在全国电视讲话中，由内阁成员陪同，再次将马尔维纳斯群岛问题推上议程中心：他签署了一项扩大国防部资源的行政令，宣布将在乌斯怀亚建设一座海军基地，并确认在存在主权争议的大陆架上从事油气开采业务的企业将被排除在“大型投资激励制度”（RIGI）之外。“岛民没有自决权，”他表示，并在同一讲话中批评英国正面临“移民、人口和经济等多重危机”。国防大臣韦斯·斯特里廷数小时后作出的首个官方回应态度强硬：岛民“选择做英国人”，英国“不会就主权进行谈判”。</p>",

    "<p>伦敦。但这场讲话引发的冲击波才刚刚开始扩散。在随后的几个小时里，反应蔓延至政治、市场以及整个英国媒体：从千篇一律、可预见的官方回应，到在群岛运营的石油公司股价暴跌，再到在耸人听闻、危言耸听与对工党政府的政治攻击之间摇摆不定的媒体报道。</p>",

    img_block(IMG_STANLEY, "斯坦利港/阿根廷港鸟瞰",
              "斯坦利港/阿根廷港，这座存在主权争议的群岛首府，如今成为外交升级的焦点。"),

    "<h3>官方回应：“不可动摇”</h3>",

    "<p>英国政府的立场没有留下任何模糊空间。来自安迪·伯纳姆工党政府左翼的外交大臣埃德·米利班德态度强硬：</p>",

    quote("“英国在马尔维纳斯（福克兰）问题上的立场不可动摇。这些岛屿是英国的，并将继续如此，因为这是岛民的意愿。自决权不可侵犯，它植根于国际法，我们将坚持这一立场。”"),

    "<p>更偏向该党右翼的国防大臣韦斯·斯特里廷在实质上表示认同，但加入了政治层面的解读：</p>",

    quote("“米莱的讲话更多与阿根廷国内政治有关，而非马尔维纳斯群岛本身。”"),

    "<p>在野党方面，保守党领袖凯米·巴德诺赫——和米莱一样，是玛格丽特·撒切尔的公开崇拜者——则以更具对抗性的姿态提高了调门：</p>",

    quote("“英国不会向恃强凌弱者低头。如果米莱想要一个强大的国家，他应该重建自己的经济，而不是威胁别人。”"),

    "<h3>对市场的冲击</h3>",

    img_block(IMG_PLATAFORMA, "黄昏中的海上石油平台",
              "在马尔维纳斯北部海域持有开采许可的石油公司，是最先感受到股价冲击的一批。"),

    "<p>除了言辞交锋，金融市场也立即作出反应。在特拉维夫证券交易所，以色列纳维塔斯石油公司（Navitas Petroleum）——通过其英国子公司控制着群岛北部海域65%的开采权——股价下跌4.5%。在伦敦，跌幅更为剧烈：持有剩余35%权益的洛克霍珀勘探公司（Rockhopper Exploration），以及同样在该海域运营的Borders &amp; Southern公司，股价均下跌15%。</p>",

    "<h3>英国媒体：在耸人听闻与国内政治之间</h3>",

    "<p>正如该分析报道所言，媒体报道呈现出“越来越奇怪”（curioser and curioser）的态势，这是对《爱丽丝梦游仙境》的戏仿。曾经让人们对“撒切尔的狂热崇拜者、支持岛民自决、热爱电锯”的米莱抱有热情的氛围，如今已让位于愤怒。</p>",

    "<p><strong>各小报的反应最为激烈：</strong></p>",

    "<p>鲁珀特·默多克旗下的<strong>天空新闻</strong>（Sky News）以耸人听闻的标题开场——“阿根廷会再次入侵群岛吗？”——并配上米莱在全体内阁陪同下发表讲话的画面，随后将这场升级与石油以及唐纳德·特朗普的介入联系起来。</p>",

    "<p><strong>《太阳报》</strong>（The Sun）以当日民调号召读者参与：“我们是否应该在反对阿根廷的立场上更加强硬？”，并向参与者提供100英镑代金券。</p>",

    "<p><strong>《每日邮报》</strong>（Daily Mail）借讲话之机攻击工党政府：“阿根廷之所以再次在福克兰问题上冒险，是因为工党软弱”，呼应了奈杰尔·法拉奇领导的极右翼政党“改革党”（Reform UK）的反应。</p>",

    "<p><strong>《每日快报》</strong>（Daily Express）的标题是：“随着英国对米莱战争威胁作出回应，紧张局势全面爆发”。</p>",

    "<p>大多数小报都特别提到米莱讲话中提及英国正面临“移民、人口和经济等多重危机”的段落——具有讽刺意味的是，这与这些媒体自己日常报道工党政府时的论调如出一辙。</p>",

    "<p><strong>较为持重的媒体则试图带来一些理性的视角：</strong></p>",

    "<p><strong>BBC</strong>将焦点放在阿根廷国内局势上，指出米莱此前对群岛问题的立场与如今的立场之间存在矛盾，而此时“他的支持率正在自由落体式下跌”。</p>",

    "<p><strong>《卫报》</strong>（The Guardian）将米莱态度的转变与唐纳德·特朗普的施压联系在一起，称特朗普“自基尔·斯塔默在伊朗军事行动问题上没有痛快答应给予他想要的全部军事支持后，就一直对工党政府怀恨在心”。该报还指出，“米莱一直自称是玛格丽特·撒切尔的崇拜者”，而他对主权问题的兴趣“是最近才出现的”，恰好与美国开始重新考虑其立场的时间相吻合。</p>",

    "<p><strong>《每日电讯报》</strong>（Daily Telegraph）则更靠近奈杰尔·法拉奇的立场，以戏仿米莱的方式打出标题：“阿根廷将战胜正在衰落的英国”，副标题则强调，这位阿根廷总统“在宣布计划制裁马尔维纳斯石油开采活动的同时，称英国是一个陷入危机的国家”。</p>",

    "<h3>分析</h3>",

    "<p>总体来看，英国媒体的报道反映出一种解读倾向：相较于对主权争端的真正关切，它们更看重阿根廷的国内政治局势——以及英国自身的内部纷争。正如该分析所指出的，米莱的言论与世界杯后阿根廷球员的言论或许听起来相似，但“其含义却截然不同”。这也表明，对英国建制派而言，马尔维纳斯问题仍是一个已经“盖棺定论”的议题，而任何对这一立场的重新审视，首先都会被解读为阿根廷国内政治的一次表态。</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">资料来源：天空新闻、《太阳报》、《每日邮报》、《每日快报》、BBC、《卫报》、《每日电讯报》。</p>',
])

FECHA_META = "4 de septiembre de 2026 · J. Martineau"

nueva_entrada = {
    "id": "20260904-propio-reaccion-uk-milei",
    "titulo": "Reino Unido responde a Milei por Malvinas",
    "bajada": "El discurso de Milei sobre Malvinas desató en el Reino Unido un rechazo oficial “inquebrantable”, un desplome bursátil de las petroleras y una tormenta mediática.",
    "cuerpo": cuerpo,
    "titulo_en": "The UK Responds to Milei Over Malvinas",
    "bajada_en": "Milei's speech on Malvinas triggered an “unshakeable” official rejection in the UK, a stock plunge for oil companies, and a media storm.",
    "cuerpo_en": cuerpo_en,
    "titulo_pt": "Reino Unido responde a Milei sobre as Malvinas",
    "bajada_pt": "O discurso de Milei sobre as Malvinas provocou no Reino Unido uma rejeição oficial “inabalável”, um tombo nas ações das petrolíferas e uma tempestade midiática.",
    "cuerpo_pt": cuerpo_pt,
    "titulo_zh": "英国回应米莱的马尔维纳斯讲话",
    "bajada_zh": "米莱有关马尔维纳斯的讲话在英国引发了“不可动摇”的官方回应、石油公司股价暴跌，以及一场媒体风暴。",
    "cuerpo_zh": cuerpo_zh,
    "tag": "🇦🇷 Malvinas",
    "categoria": "malvinas|politica|internacional",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "malvinas",
    "imagen": IMG_PORTADA,
    "imagen_keywords": "malvinas milei discurso reino unido petroleras bolsa prensa britanica",
    "hashtags_en": "#Malvinas #Falklands #Milei #UK",
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
