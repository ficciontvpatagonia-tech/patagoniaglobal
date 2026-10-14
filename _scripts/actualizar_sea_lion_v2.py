#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Reemplaza el informe Sea Lion / Tribunal del Mar por la v2 (aprobada por Marto 14/10/2026):
# actualiza la entrada en propios.json (ES/EN/PT/ZH). Las páginas se regeneran con
# _gen_variantes_malvinas_tribunal_mar_sea_lion.py (borrando antes las 4 notas/*.html).
import json, os

BASE = "/Users/jm/Desktop/CLAUDCODE/GLOBAL PATAGONIA"
BID = "20261014-propio-malvinas-tribunal-mar-sea-lion"

DATELINE = '<p style="font-size:.85rem;letter-spacing:.05em;text-transform:uppercase;color:#7aadcc;font-weight:600;margin-bottom:1.2rem">{}</p>'

def img_block(src, alt, cap):
    return ('<div style="margin:2rem 0"><img src="' + src + '" alt="' + alt +
            '" loading="lazy" decoding="async" style="width:100%;border-radius:6px;display:block">'
            '<div style="font-size:.8rem;color:#777;margin-top:.45rem">' + cap + '</div></div>')

def quote(txt):
    return ('<blockquote style="border-left:4px solid #7aadcc;margin:2rem 0;'
            'padding:.4rem 0 .4rem 1.4rem;font-size:1.25rem;line-height:1.5;'
            f'font-style:italic">{txt}</blockquote>')

IMG = "fotos/malvinas-plataforma-sea-lion.webp"

# ---- ES: se toma del borrador aprobado (mismo texto que vio Marto en el preview) ----
src = open(f"{BASE}/_scripts/_borrador_sea_lion_v2_preview.py", encoding="utf-8").read()
seg = src[src.index("cuerpo = "):src.index("page = f")]
ns = {"DATELINE": DATELINE.format("Malvinas — Informe GLOBALpatagonia"), "img_block": img_block, "quote": quote, "IMG": IMG}
exec(seg, ns)
cuerpo = ns["cuerpo"].replace('<p style="font-size:.85rem;color:#777">', '<p style="font-size:.85rem;color:#777;margin-top:-1rem">')
fuentes_es = "Fuentes: Página12, <em>The Guardian</em> (vía Página12), Infobae, Perfil, La Gaceta, Informe Digital, Rosario3, Splash247."

# ============================== ENGLISH ==============================
cuerpo_en = "\n\n".join([
    DATELINE.format("Malvinas — GLOBALpatagonia Report"),

    "<p>The fight over Malvinas (Falklands) oil has moved from diplomatic notes to international courts. The Argentine government took the United Kingdom to the International Tribunal for the Law of the Sea, in Hamburg, to stop <strong>Sea Lion</strong>, the first major oil project in the islands' waters. Hours later, London announced it will legally shield the companies operating it and asked Interpol to reject Argentine arrest requests linked to the project.</p>",

    "<h3>What Argentina asked for</h3>",

    "<p>The request is part of the arbitration the government opened on September 28 under the United Nations Convention on the Law of the Sea. That day the UK was given two weeks to halt activity; the deadline expired on October 12 without a favourable answer, and on the 13th Argentina asked the Tribunal for <strong>provisional measures</strong> with four specific demands:</p>",

    "<ul><li><strong>Sea Lion:</strong> that the UK prevent the start or continuation of hydrocarbon exploitation in the North Malvinas Basin.</li>"
    "<li><strong>Exploration data:</strong> that it not use information gathered during exploration to Argentina's detriment.</li>"
    "<li><strong>Marine environment:</strong> that it not hinder compliance with the Convention's environmental obligations.</li>"
    "<li><strong>New permits:</strong> that it refrain from measures that aggravate the dispute, in particular new exploitation authorisations.</li></ul>",

    "<p>Filing the request does not suspend the project: the Tribunal must decide whether to grant the measures. In the ARA Libertad frigate case in 2012 it ruled in about a month, so a first decision could come in November, though no date is confirmed.</p>",

    img_block(IMG, "Sea Lion offshore platform in the South Atlantic",
              "The Sea Lion platform, the project in the North Malvinas Basin that Argentina wants to stop. Photo: file."),

    "<p>Foreign Minister Pablo Quirno presented the strategy as “unprecedented” and said it is “the first time Argentina has gone to arbitration on this issue,” with a “peaceful intention of resolving a dispute that is at its heart.” That is true of the arbitration; not of pressuring the oil companies — previous governments had already done that.</p>",

    "<h3>What had already been tried</h3>",

    "<p>Pressure on companies operating in Malvinas has a history of more than a decade:</p>",

    "<ul><li><strong>2011:</strong> a law restricting hydrocarbon activity in the area without Argentine authorisation.</li>"
    "<li><strong>2012:</strong> the operations of five oil companies were declared illegal.</li>"
    "<li><strong>2013:</strong> criminal penalties were toughened.</li>"
    "<li><strong>2015:</strong> companies exploring in the area were reported and court-ordered attachments of more than US$156 million were obtained.</li></ul>",

    "<p>What is different now is the setting: an international tribunal and a project that already has an investment decision and production planned for 2028.</p>",

    "<h3>London shields its companies</h3>",

    "<p>The British response had three parts. First, it reaffirmed its backing for Sea Lion's development and cleared its continuation. That authorisation runs through Foreign Secretary Ed Miliband, whose consent is required for certain hydrocarbon licences in the archipelago under the 1994 Falkland Islands Offshore Minerals Ordinance. London holds that the islanders have the right to develop their natural resources, and that this right is part of its position on self-determination.</p>",

    "<p>Second, it activated its <em>Protection of Trading Interests</em> legislation, which lets it bar companies and individuals under British jurisdiction from complying with foreign laws — in this case, Argentine ones — that impose sanctions or restrictions on those operating in Malvinas. In practice, Navitas and Rockhopper will keep operating despite the sanctions pushed by Buenos Aires.</p>",

    "<p>Third, it wrote to Interpol. According to <em>The Guardian</em>, the UK argues that the “red notices” requested by Argentina “should be considered politically motivated” and describes them as “an attempt to intimidate people and companies from operating in the Malvinas.” Interpol replied that it will respect Article 3 of its constitution, which bars it from intervening in matters of a political character.</p>",

    quote("“Sea Lion could triple the archipelago's GDP, but Milei has promised to block it.”"),

    '<p style="font-size:.85rem;color:#777;margin-top:-1rem">British government argument, according to the letter to Interpol cited by <em>The Guardian</em>.</p>',

    "<h3>The companies and the timeline</h3>",

    "<p>Sea Lion is operated by Israel's <strong>Navitas Petroleum</strong> (65%), with Britain's <strong>Rockhopper Exploration</strong> (35%) as partner; Rockhopper discovered the field in 2010. The plan calls for eleven subsea wells tied to a floating production unit. Development drilling is scheduled for 2027, first oil for the first quarter of 2028, and capacity of up to 180,000 barrels a day. On October 7, Rockhopper announced a US$44 million investment in its share of the company that owns that unit.</p>",

    "<p>Argentine pressure already has one concrete effect: according to the Presidency, Halliburton confirmed its subsidiaries will not provide services to the project. Navitas acknowledged it is replacing two contractors, though it says it expects no material impact.</p>",

    "<h3>The British contradiction</h3>",

    "<p>The decision also opened an internal rift in the UK. The Conservative Party's energy spokesman, Andrew Bowie, welcomed the authorisation but challenged the Labour government:</p>",

    quote("“Why is Ed Miliband, the man who blocked drilling in the North Sea, willing to allow it in the South Atlantic but not off the coast of Scotland?”"),

    "<p>In the North Sea, the British government has for now pushed to halt new oil and gas exploration. In the South Atlantic, by contrast, it backs a new field.</p>",

    "<h3>What is really at stake</h3>",

    "<p>The Law of the Sea Tribunal does not settle sovereignty disputes, and that is the main legal obstacle to Argentina's strategy: the Convention gives it no general jurisdiction over who owns a territory. That is why the filing relies on concrete obligations over resources, the environment and the parties' conduct while the dispute remains open.</p>",

    "<p>Even so, the move carries clear political and economic weight: it takes Sea Lion to an international forum, exposes the companies to reputational and financial risk, and forces London to show how much it is willing to spend — in laws, in diplomacy and in letters to Interpol — to sustain the project. The Tribunal's decision, expected in the coming weeks, will set the course of the oil dispute in the South Atlantic.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Sources: Página12, <em>The Guardian</em> (via Página12), Infobae, Perfil, La Gaceta, Informe Digital, Rosario3, Splash247.</p>',
])

# ============================== PORTUGUÊS ==============================
cuerpo_pt = "\n\n".join([
    DATELINE.format("Malvinas — Relatório GLOBALpatagonia"),

    "<p>A disputa pelo petróleo das Malvinas passou das notas diplomáticas para os tribunais internacionais. O governo argentino levou o Reino Unido ao Tribunal Internacional do Direito do Mar, em Hamburgo, para frear o <strong>Sea Lion</strong>, o primeiro grande projeto petrolífero em águas das ilhas. Horas depois, Londres anunciou que blindará legalmente as empresas que o operam e pediu à Interpol que rejeite os pedidos de prisão argentinos ligados ao projeto.</p>",

    "<h3>O que a Argentina pediu</h3>",

    "<p>O pedido faz parte da arbitragem que o governo iniciou em 28 de setembro sob a Convenção das Nações Unidas sobre o Direito do Mar. Naquele dia, o Reino Unido recebeu um prazo de duas semanas para interromper as atividades; o prazo venceu em 12 de outubro sem resposta favorável e, no dia 13, a Argentina pediu ao Tribunal <strong>medidas provisórias</strong> com quatro reclamações concretas:</p>",

    "<ul><li><strong>Sea Lion:</strong> que o Reino Unido impeça o início ou a continuação da exploração de hidrocarbonetos na Bacia Malvinas Norte.</li>"
    "<li><strong>Dados de exploração:</strong> que não use em prejuízo da Argentina as informações obtidas durante as explorações.</li>"
    "<li><strong>Meio marinho:</strong> que não obstrua o cumprimento das obrigações ambientais da Convenção.</li>"
    "<li><strong>Novas licenças:</strong> que não adote medidas que agravem a controvérsia, em particular novas autorizações de exploração.</li></ul>",

    "<p>Apresentar o pedido não suspende o projeto: o Tribunal deve decidir se concede as medidas. No caso da Fragata Libertad, em 2012, decidiu em cerca de um mês, de modo que uma primeira definição poderia sair em novembro, embora não haja data confirmada.</p>",

    img_block(IMG, "Plataforma offshore do Sea Lion no Atlântico Sul",
              "A plataforma do Sea Lion, o projeto na Bacia Malvinas Norte que a Argentina quer frear. Foto: arquivo."),

    "<p>O chanceler Pablo Quirno apresentou a estratégia como “inédita” e disse que é “a primeira vez que a Argentina recorre a uma arbitragem sobre este tema”, com a “intenção pacífica de resolver uma disputa que está em seu coração”. É verdade quanto à arbitragem; não quanto a pressionar as petroleiras: governos anteriores já o haviam feito.</p>",

    "<h3>O que já tinha sido tentado</h3>",

    "<p>A pressão sobre as empresas que operam nas Malvinas tem antecedentes de mais de uma década:</p>",

    "<ul><li><strong>2011:</strong> lei que restringe a atividade de hidrocarbonetos na zona sem autorização argentina.</li>"
    "<li><strong>2012:</strong> as operações de cinco petroleiras foram declaradas ilegais.</li>"
    "<li><strong>2013:</strong> endureceram-se as sanções penais.</li>"
    "<li><strong>2015:</strong> denunciaram-se empresas que exploravam na zona e obtiveram-se embargos judiciais de mais de 156 milhões de dólares.</li></ul>",

    "<p>A diferença agora é o cenário: um tribunal internacional e um projeto que já tem decisão de investimento e produção prevista para 2028.</p>",

    "<h3>Londres blinda suas empresas</h3>",

    "<p>A resposta britânica teve três peças. Primeiro, ratificou seu apoio ao desenvolvimento do Sea Lion e habilitou sua continuidade. Essa autorização passa pelo secretário de Relações Exteriores, Ed Miliband, cujo consentimento é necessário para certas licenças de hidrocarbonetos no arquipélago, segundo a Portaria de Minerais Offshore das Malvinas de 1994. Londres sustenta que os habitantes das ilhas têm direito a desenvolver seus recursos naturais, e que essa faculdade faz parte de sua posição sobre a autodeterminação.</p>",

    "<p>Segundo, ativou a legislação de <em>Proteção de Interesses Comerciais</em>, que lhe permite proibir empresas e pessoas sob jurisdição britânica de cumprir leis estrangeiras —neste caso, as argentinas— que imponham sanções ou restrições a quem opera nas Malvinas. Na prática, Navitas e Rockhopper seguirão operando apesar das sanções impulsionadas por Buenos Aires.</p>",

    "<p>Terceiro, escreveu à Interpol. Segundo informou o <em>The Guardian</em>, o Reino Unido sustenta que as “notificações vermelhas” solicitadas pela Argentina “devem ser consideradas motivadas por razões políticas” e as descreve como “uma tentativa de intimidar pessoas e empresas para que não operem nas Malvinas”. A Interpol respondeu que respeitará o artigo 3 de seu estatuto, que a proíbe de intervir em assuntos de caráter político.</p>",

    quote("“O Sea Lion poderia triplicar o PIB do arquipélago, mas Milei prometeu bloqueá-lo.”"),

    '<p style="font-size:.85rem;color:#777;margin-top:-1rem">Argumento do governo britânico, segundo a carta à Interpol citada pelo <em>The Guardian</em>.</p>',

    "<h3>As empresas e o calendário</h3>",

    "<p>O Sea Lion é operado pela israelense <strong>Navitas Petroleum</strong> (65%), com a britânica <strong>Rockhopper Exploration</strong> (35%) como sócia; a Rockhopper descobriu o campo em 2010. O plano prevê onze poços submarinos conectados a uma unidade flutuante de produção. A perfuração de desenvolvimento está prevista para 2027, o primeiro petróleo para o primeiro trimestre de 2028 e uma capacidade de até 180.000 barris por dia. Em 7 de outubro, a Rockhopper anunciou um investimento de 44 milhões de dólares em sua participação na sociedade dona dessa unidade.</p>",

    "<p>A pressão argentina já tem um primeiro efeito concreto: segundo a Presidência, a Halliburton confirmou que suas filiais não prestarão serviços ao projeto. A Navitas reconheceu que está substituindo dois contratados, embora diga não esperar impacto material.</p>",

    "<h3>A contradição britânica</h3>",

    "<p>A decisão também abriu uma fissura interna no Reino Unido. O responsável por Energia do Partido Conservador, Andrew Bowie, celebrou a autorização, mas questionou o governo trabalhista:</p>",

    quote("“Por que Ed Miliband, o homem que bloqueou as perfurações no Mar do Norte, está disposto a permiti-las no Atlântico Sul, mas não na costa da Escócia?”"),

    "<p>No Mar do Norte, o governo britânico impulsionou por ora a suspensão de novas explorações de petróleo e gás. No Atlântico Sul, em contrapartida, respalda um campo novo.</p>",

    "<h3>O que realmente está em jogo</h3>",

    "<p>O Tribunal do Direito do Mar não resolve disputas de soberania, e esse é o principal obstáculo jurídico da estratégia argentina: a Convenção não lhe dá competência geral sobre quem é dono de um território. Por isso o pedido se apoia em obrigações concretas sobre recursos, meio ambiente e conduta das partes enquanto a controvérsia segue aberta.</p>",

    "<p>Ainda assim, o movimento tem peso político e econômico evidente: leva o Sea Lion a um foro internacional, expõe as empresas a risco reputacional e financeiro e obriga Londres a mostrar quanto está disposta a gastar —em leis, em diplomacia e em cartas à Interpol— para sustentar o projeto. A decisão do Tribunal, esperada para as próximas semanas, definirá o rumo da disputa petrolífera no Atlântico Sul.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Fontes: Página12, <em>The Guardian</em> (via Página12), Infobae, Perfil, La Gaceta, Informe Digital, Rosario3, Splash247.</p>',
])

# ============================== 中文 ==============================
cuerpo_zh = "\n\n".join([
    DATELINE.format("马尔维纳斯 — GLOBALpatagonia 深度报道"),

    "<p>围绕马尔维纳斯石油的争端,已从外交照会走向国际法庭。阿根廷政府将英国诉至设在汉堡的国际海洋法法庭,要求叫停<strong>海狮(Sea Lion)</strong>项目——这是群岛海域首个大型石油开发项目。数小时后,伦敦宣布将在法律上为运营该项目的企业提供“护盾”,并请求国际刑警组织驳回阿根廷就该项目提出的拘捕请求。</p>",

    "<h3>阿根廷提出了什么</h3>",

    "<p>该申请是政府9月28日依据《联合国海洋法公约》启动的仲裁程序的一部分。当天英国被给予两周时间停止相关活动;期限于10月12日届满,英国未作出有利答复,13日阿根廷向法庭申请<strong>临时措施</strong>,提出四项具体诉求:</p>",

    "<ul><li><strong>海狮项目:</strong>要求英国阻止在马尔维纳斯北部盆地开始或继续开采油气。</li>"
    "<li><strong>勘探数据:</strong>要求英国不得以损害阿根廷的方式使用勘探期间获得的信息。</li>"
    "<li><strong>海洋环境:</strong>要求英国不得妨碍公约所规定的环境义务的履行。</li>"
    "<li><strong>新许可:</strong>要求英国不得采取加剧争端的措施,尤其是新的开采授权。</li></ul>",

    "<p>提出申请并不会使项目暂停:法庭须决定是否批准这些措施。在2012年“自由号”护卫舰案中,法庭大约一个月即作出裁决,因此首份裁定可能在11月出炉,但尚无确定日期。</p>",

    img_block(IMG, "南大西洋上的海狮海上平台",
              "海狮平台——阿根廷希望叫停的马尔维纳斯北部盆地项目。图片:资料图。"),

    "<p>外长巴勃罗·基尔诺(Pablo Quirno)称这一策略“史无前例”,表示这是“阿根廷首次就此问题诉诸仲裁”,“和平地解决一场关乎国家核心的争端”。就仲裁而言确实如此;但就向石油公司施压而言并非如此——此前的历届政府早已这样做过。</p>",

    "<h3>此前已经尝试过的做法</h3>",

    "<p>对在马尔维纳斯作业的企业施压,已有十多年的历史:</p>",

    "<ul><li><strong>2011年:</strong>通过法律,限制未经阿根廷许可在该海域开展油气活动。</li>"
    "<li><strong>2012年:</strong>宣布五家石油公司的作业非法。</li>"
    "<li><strong>2013年:</strong>加重刑事处罚。</li>"
    "<li><strong>2015年:</strong>起诉在该海域勘探的企业,并取得超过1.56亿美元的司法查封。</li></ul>",

    "<p>如今的不同在于舞台:一个国际法庭,以及一个已作出投资决定、预计2028年投产的项目。</p>",

    "<h3>伦敦为企业撑腰</h3>",

    "<p>英国的回应分为三步。首先,重申对海狮项目开发的支持,并允许其继续推进。该授权须经外交大臣埃德·米利班德(Ed Miliband)同意——根据1994年《马尔维纳斯近海矿产条例》,群岛上的某些油气许可须取得其同意。伦敦坚称,岛民有权开发自身的自然资源,这一权利是其自决立场的一部分。</p>",

    "<p>其次,启动《保护贸易利益法》,该法允许禁止英国管辖下的公司和个人遵守外国法律——此处即阿根廷法律——对在马尔维纳斯作业者施加的制裁或限制。实际上,这意味着Navitas和Rockhopper将不顾布宜诺斯艾利斯推动的制裁继续作业。</p>",

    "<p>第三,致函国际刑警组织。据《卫报》(<em>The Guardian</em>)报道,英国认为阿根廷申请的“红色通缉令”“应被视为出于政治动机”,并称其是“企图恐吓个人和企业不要在马尔维纳斯作业”。国际刑警组织回应称,将遵守其章程第3条,该条禁止其介入具有政治性质的事务。</p>",

    quote("“海狮项目可能使群岛的GDP翻三倍,但米莱已承诺要阻止它。”"),

    '<p style="font-size:.85rem;color:#777;margin-top:-1rem">英国政府的论点,据《卫报》援引的致国际刑警组织信函。</p>',

    "<h3>企业与时间表</h3>",

    "<p>海狮项目由以色列的<strong>Navitas Petroleum</strong>(65%)担任作业者,英国的<strong>Rockhopper Exploration</strong>(35%)为合作伙伴;Rockhopper于2010年发现该油田。计划包括十一口水下油井,连接至一艘浮式生产装置。开发钻井预计2027年进行,首批原油预计2028年第一季度产出,产能最高可达每日18万桶。10月7日,Rockhopper宣布向持有该装置的公司投入4,400万美元以增持其份额。</p>",

    "<p>阿根廷的施压已产生第一个具体效果:据总统府称,哈里伯顿(Halliburton)确认其子公司不会为该项目提供服务。Navitas则承认正在更换两家承包商,但称预计不会产生重大影响。</p>",

    "<h3>英国的自相矛盾</h3>",

    "<p>这一决定也在英国内部引发裂痕。保守党能源事务发言人安德鲁·鲍伊(Andrew Bowie)对授权表示欢迎,但质疑工党政府:</p>",

    quote("“为什么阻止北海钻探的埃德·米利班德,愿意允许在南大西洋钻探,却不允许在苏格兰近海钻探?”"),

    "<p>在北海,英国政府目前推动叫停新的油气勘探;而在南大西洋,却支持一个新油田。</p>",

    "<h3>真正的利害所在</h3>",

    "<p>海洋法法庭并不裁决主权争端,这正是阿根廷策略面临的主要法律障碍:公约并未赋予其对领土归属的一般管辖权。因此,此次申请围绕争端未决期间各方在资源、环境和行为方面的具体义务展开。</p>",

    "<p>即便如此,此举仍具有明显的政治与经济分量:它把海狮项目带上国际舞台,使相关企业面临声誉和财务风险,并迫使伦敦表明为维持该项目愿意付出多大代价——无论是立法、外交,还是写给国际刑警组织的信函。法庭预计在未来几周内作出的决定,将左右南大西洋石油争端的走向。</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">来源:Página12、《卫报》(经Página12转引)、Infobae、Perfil、La Gaceta、Informe Digital、Rosario3、Splash247。</p>',
])

# ---- Actualizar entrada ----
P = f"{BASE}/propios.json"
propios = json.load(open(P, encoding="utf-8"))
e = next(p for p in propios if p["id"] == BID)

e["bajada"] = ("Buenos Aires pidió medidas urgentes en Hamburgo para frenar Sea Lion, el primer gran proyecto petrolero "
               "en aguas de Malvinas. Londres respondió con una ley que protege a las empresas y una carta a Interpol. "
               "Qué pidió cada lado y qué puede pasar.")
e["bajada_en"] = ("Buenos Aires asked for urgent measures in Hamburg to stop Sea Lion, the first major oil project in Malvinas waters. "
                  "London responded with a law protecting the companies and a letter to Interpol. What each side wants and what could happen.")
e["bajada_pt"] = ("Buenos Aires pediu medidas urgentes em Hamburgo para frear o Sea Lion, o primeiro grande projeto petrolífero em águas das Malvinas. "
                  "Londres respondeu com uma lei que protege as empresas e uma carta à Interpol. O que pediu cada lado e o que pode acontecer.")
e["bajada_zh"] = "布宜诺斯艾利斯在汉堡请求紧急措施,以叫停马尔维纳斯海域首个大型石油项目“海狮”。伦敦则以一部保护企业的法律和一封致国际刑警组织的信函作答。双方诉求各是什么,接下来可能发生什么。"
e["cuerpo"], e["cuerpo_en"], e["cuerpo_pt"], e["cuerpo_zh"] = cuerpo, cuerpo_en, cuerpo_pt, cuerpo_zh
e["imagen_keywords"] = "malvinas sea lion plataforma petrolera tribunal del mar hamburgo interpol navitas rockhopper"

json.dump(propios, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK — entrada v2 en propios.json")
