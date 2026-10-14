#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Publica el informe "Argentina fue al Tribunal del Mar y Londres blindó a sus petroleras"
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

IMG_PORTADA = "fotos/malvinas-plataforma-sea-lion.webp"
FECHA_META = "14 de octubre de 2026 · J. Martineau"

# ============================== ESPAÑOL ==============================
cuerpo = "\n\n".join([
    DATELINE.format("Malvinas — Informe GLOBALpatagonia"),

    "<p>La disputa por el petróleo de Malvinas pasó de las notas diplomáticas a los tribunales internacionales. El 13 de octubre, la Argentina presentó ante el Tribunal Internacional del Derecho del Mar, en Hamburgo, un pedido de <strong>medidas provisionales</strong> para frenar Sea Lion, el primer gran proyecto petrolero en aguas de las islas. Casi en simultáneo, Londres dejó claro que va a proteger a las empresas que lo llevan adelante.</p>",

    "<h3>Qué pidió la Argentina</h3>",

    "<p>El pedido es parte del arbitraje que el Gobierno inició el 28 de septiembre bajo la Convención de las Naciones Unidas sobre el Derecho del Mar. Ese día se le dio al Reino Unido un plazo de dos semanas para detener las actividades; el plazo venció el 12 de octubre sin respuesta favorable. La presentación se apoya en el artículo 290 de la Convención y plantea cuatro reclamos concretos:</p>",

    '<ul><li><strong>Sea Lion:</strong> que el Reino Unido impida el inicio o la continuación de la explotación de hidrocarburos en la Cuenca Malvinas Norte.</li>'
    '<li><strong>Datos de exploración:</strong> que no use en perjuicio de la Argentina la información obtenida durante las exploraciones.</li>'
    '<li><strong>Medio marino:</strong> que no obstaculice el cumplimiento de las obligaciones de protección ambiental de la Convención.</li>'
    '<li><strong>Nuevos permisos:</strong> que no adopte medidas que agraven la controversia, en particular nuevas autorizaciones de explotación.</li></ul>',

    "<p>Es importante entender el alcance: presentar el pedido no suspende el proyecto. Es el Tribunal el que ahora debe decidir si concede las medidas y en qué términos. En el caso de la Fragata Libertad, en 2012, resolvió en alrededor de un mes, por lo que una primera definición podría conocerse en noviembre, aunque no hay fecha confirmada.</p>",

    img_block(IMG_PORTADA, "Plataforma offshore de Sea Lion en el Atlántico Sur",
              "La plataforma de Sea Lion, el proyecto en la Cuenca Malvinas Norte que la Argentina quiere frenar. Foto: archivo."),

    "<h3>Londres blinda a sus empresas</h3>",

    "<p>La respuesta británica fue rápida. El Gobierno rechazó el planteo argentino, sostuvo que las actividades están amparadas por las licencias emitidas por las autoridades de las islas —que en septiembre fueron extendidas por cinco años— y anunció que recurrirá a su legislación de <em>Protección de Intereses Comerciales</em>, una norma que permite impedir que empresas británicas cumplan sanciones o regulaciones extraterritoriales de otros países.</p>",

    "<p>En el Parlamento, la ministra para los Territorios de Ultramar, Uma Kumaran, fue directa: el reclamo argentino “no invalida las licencias emitidas por el gobierno de las islas”. Y advirtió que, si la situación continúa, Londres podría tomar medidas adicionales que, según dijo, “serán legales, serán proporcionales y serán contundentes”.</p>",

    "<h3>Las empresas y el calendario</h3>",

    "<p>Sea Lion es operado por la israelí <strong>Navitas Petroleum</strong> (65%), con la británica <strong>Rockhopper Exploration</strong> (35%) como socia; Rockhopper descubrió el yacimiento en 2010. El plan contempla once pozos submarinos conectados a una unidad flotante de producción. Las perforaciones de desarrollo están previstas para 2027 y el primer petróleo comercial para el primer trimestre de 2028. El 7 de octubre, Rockhopper anunció una inversión de 44 millones de dólares en su participación en la sociedad dueña de esa unidad.</p>",

    "<p>Del lado argentino, la presión ya tiene un primer efecto concreto: según informó la Presidencia, Halliburton confirmó que sus filiales no prestarán servicios al proyecto. Navitas, por su parte, reconoció que está reemplazando a dos contratistas, aunque dice que no espera un impacto material.</p>",

    "<h3>Qué está realmente en juego</h3>",

    "<p>El Tribunal del Mar no resuelve disputas de soberanía, y ese es el principal obstáculo jurídico de la estrategia argentina: la Convención no le da competencia general sobre quién es dueño de un territorio. Por eso el planteo evita discutir la soberanía y se apoya en obligaciones concretas sobre recursos, ambiente y conducta de las partes mientras la controversia sigue abierta.</p>",

    "<p>Aun así, el movimiento tiene un valor político y económico evidente: lleva el tema Sea Lion a un foro internacional, expone a las empresas a un riesgo reputacional y financiero, y obliga a Londres a mostrar cuánto está dispuesto a gastar para sostener el proyecto. La decisión del Tribunal, que se espera para las próximas semanas, marcará el rumbo de la disputa petrolera en el Atlántico Sur.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Fuentes: Página12, Infobae, Perfil, La Gaceta, Informe Digital, Rosario3, Splash247, Rio Times.</p>',
])

# ============================== ENGLISH ==============================
cuerpo_en = "\n\n".join([
    DATELINE.format("Malvinas — GLOBALpatagonia Report"),

    "<p>The fight over Malvinas (Falklands) oil has moved from diplomatic notes to international courts. On October 13, Argentina asked the International Tribunal for the Law of the Sea, in Hamburg, for <strong>provisional measures</strong> to stop Sea Lion, the first major oil project in the islands' waters. Almost simultaneously, London made clear it will protect the companies behind it.</p>",

    "<h3>What Argentina asked for</h3>",

    "<p>The request is part of the arbitration the government opened on September 28 under the United Nations Convention on the Law of the Sea. That day the United Kingdom was given two weeks to halt activity; the deadline expired on October 12 without a favourable answer. The filing relies on Article 290 of the Convention and makes four specific demands:</p>",

    '<ul><li><strong>Sea Lion:</strong> that the UK prevent the start or continuation of hydrocarbon exploitation in the North Malvinas Basin.</li>'
    '<li><strong>Exploration data:</strong> that it not use information gathered during exploration to Argentina\'s detriment.</li>'
    '<li><strong>Marine environment:</strong> that it not hinder compliance with the Convention\'s environmental protection obligations.</li>'
    '<li><strong>New permits:</strong> that it refrain from measures that aggravate the dispute, in particular new exploitation authorisations.</li></ul>',

    "<p>It is important to understand the scope: filing the request does not suspend the project. The Tribunal must now decide whether to grant the measures and on what terms. In the ARA Libertad frigate case in 2012 it ruled in about a month, so a first decision could come in November, though no date is confirmed.</p>",

    img_block(IMG_PORTADA, "Sea Lion offshore platform in the South Atlantic",
              "The Sea Lion platform, the project in the North Malvinas Basin that Argentina wants to stop. Photo: file."),

    "<h3>London shields its companies</h3>",

    "<p>The British response was swift. The government rejected Argentina's move, argued that the activity is covered by licences issued by the islands' authorities — extended for five years in September — and announced it will use its <em>Protection of Trading Interests</em> legislation, a law that allows it to stop British companies from complying with other countries' extraterritorial sanctions or regulations.</p>",

    "<p>In Parliament, Overseas Territories minister Uma Kumaran was blunt: the Argentine claim “does not invalidate the licences issued by the islands' government.” She warned that, if the situation continues, London could take further measures that, she said, “will be lawful, will be proportionate and will be forceful.”</p>",

    "<h3>The companies and the timeline</h3>",

    "<p>Sea Lion is operated by Israel's <strong>Navitas Petroleum</strong> (65%), with Britain's <strong>Rockhopper Exploration</strong> (35%) as partner; Rockhopper discovered the field in 2010. The plan calls for eleven subsea wells tied to a floating production unit. Development drilling is scheduled for 2027 and first commercial oil for the first quarter of 2028. On October 7, Rockhopper announced a US$44 million investment in its share of the company that owns that unit.</p>",

    "<p>On the Argentine side, the pressure already has one concrete effect: according to the Presidency, Halliburton confirmed its subsidiaries will not provide services to the project. Navitas, for its part, acknowledged it is replacing two contractors, though it says it expects no material impact.</p>",

    "<h3>What is really at stake</h3>",

    "<p>The Law of the Sea Tribunal does not settle sovereignty disputes, and that is the main legal obstacle to Argentina's strategy: the Convention gives it no general jurisdiction over who owns a territory. That is why the filing avoids debating sovereignty and relies on concrete obligations over resources, the environment and the parties' conduct while the dispute remains open.</p>",

    "<p>Even so, the move has clear political and economic value: it takes Sea Lion to an international forum, exposes the companies to reputational and financial risk, and forces London to show how much it is willing to spend to sustain the project. The Tribunal's decision, expected in the coming weeks, will set the course of the oil dispute in the South Atlantic.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Sources: Página12, Infobae, Perfil, La Gaceta, Informe Digital, Rosario3, Splash247, Rio Times.</p>',
])

# ============================== PORTUGUÊS ==============================
cuerpo_pt = "\n\n".join([
    DATELINE.format("Malvinas — Relatório GLOBALpatagonia"),

    "<p>A disputa pelo petróleo das Malvinas passou das notas diplomáticas para os tribunais internacionais. Em 13 de outubro, a Argentina apresentou ao Tribunal Internacional do Direito do Mar, em Hamburgo, um pedido de <strong>medidas provisórias</strong> para frear o Sea Lion, o primeiro grande projeto petrolífero em águas das ilhas. Quase ao mesmo tempo, Londres deixou claro que vai proteger as empresas que o levam adiante.</p>",

    "<h3>O que a Argentina pediu</h3>",

    "<p>O pedido faz parte da arbitragem que o governo iniciou em 28 de setembro sob a Convenção das Nações Unidas sobre o Direito do Mar. Naquele dia, o Reino Unido recebeu um prazo de duas semanas para interromper as atividades; o prazo venceu em 12 de outubro sem resposta favorável. A apresentação se apoia no artigo 290 da Convenção e traz quatro reclamações concretas:</p>",

    '<ul><li><strong>Sea Lion:</strong> que o Reino Unido impeça o início ou a continuação da exploração de hidrocarbonetos na Bacia Malvinas Norte.</li>'
    '<li><strong>Dados de exploração:</strong> que não use em prejuízo da Argentina as informações obtidas durante as explorações.</li>'
    '<li><strong>Meio marinho:</strong> que não obstrua o cumprimento das obrigações de proteção ambiental da Convenção.</li>'
    '<li><strong>Novas licenças:</strong> que não adote medidas que agravem a controvérsia, em particular novas autorizações de exploração.</li></ul>',

    "<p>É importante entender o alcance: apresentar o pedido não suspende o projeto. Cabe agora ao Tribunal decidir se concede as medidas e em que termos. No caso da Fragata Libertad, em 2012, decidiu em cerca de um mês, de modo que uma primeira definição poderia sair em novembro, embora não haja data confirmada.</p>",

    img_block(IMG_PORTADA, "Plataforma offshore do Sea Lion no Atlântico Sul",
              "A plataforma do Sea Lion, o projeto na Bacia Malvinas Norte que a Argentina quer frear. Foto: arquivo."),

    "<h3>Londres blinda suas empresas</h3>",

    "<p>A resposta britânica foi rápida. O governo rejeitou a iniciativa argentina, sustentou que as atividades estão amparadas por licenças emitidas pelas autoridades das ilhas —prorrogadas por cinco anos em setembro— e anunciou que recorrerá à sua legislação de <em>Proteção de Interesses Comerciais</em>, norma que permite impedir que empresas britânicas cumpram sanções ou regulações extraterritoriais de outros países.</p>",

    "<p>No Parlamento, a ministra para os Territórios Ultramarinos, Uma Kumaran, foi direta: o reclamo argentino “não invalida as licenças emitidas pelo governo das ilhas”. E advertiu que, se a situação continuar, Londres poderá tomar medidas adicionais que, segundo disse, “serão legais, serão proporcionais e serão contundentes”.</p>",

    "<h3>As empresas e o calendário</h3>",

    "<p>O Sea Lion é operado pela israelense <strong>Navitas Petroleum</strong> (65%), com a britânica <strong>Rockhopper Exploration</strong> (35%) como sócia; a Rockhopper descobriu o campo em 2010. O plano prevê onze poços submarinos conectados a uma unidade flutuante de produção. A perfuração de desenvolvimento está prevista para 2027 e o primeiro petróleo comercial para o primeiro trimestre de 2028. Em 7 de outubro, a Rockhopper anunciou um investimento de 44 milhões de dólares em sua participação na sociedade dona dessa unidade.</p>",

    "<p>Do lado argentino, a pressão já tem um primeiro efeito concreto: segundo a Presidência, a Halliburton confirmou que suas filiais não prestarão serviços ao projeto. A Navitas, por sua vez, reconheceu que está substituindo dois contratados, embora diga não esperar impacto material.</p>",

    "<h3>O que realmente está em jogo</h3>",

    "<p>O Tribunal do Direito do Mar não resolve disputas de soberania, e esse é o principal obstáculo jurídico da estratégia argentina: a Convenção não lhe dá competência geral sobre quem é dono de um território. Por isso o pedido evita discutir a soberania e se apoia em obrigações concretas sobre recursos, meio ambiente e conduta das partes enquanto a controvérsia segue aberta.</p>",

    "<p>Ainda assim, o movimento tem valor político e econômico evidente: leva o tema Sea Lion a um foro internacional, expõe as empresas a risco reputacional e financeiro e obriga Londres a mostrar quanto está disposta a gastar para sustentar o projeto. A decisão do Tribunal, esperada para as próximas semanas, definirá o rumo da disputa petrolífera no Atlântico Sul.</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">Fontes: Página12, Infobae, Perfil, La Gaceta, Informe Digital, Rosario3, Splash247, Rio Times.</p>',
])

# ============================== 中文 ==============================
cuerpo_zh = "\n\n".join([
    DATELINE.format("马尔维纳斯 — GLOBALpatagonia 深度报道"),

    "<p>围绕马尔维纳斯石油的争端,已从外交照会走向国际法庭。10月13日,阿根廷向设在汉堡的国际海洋法法庭提出<strong>临时措施</strong>申请,要求叫停海狮(Sea Lion)项目——这是群岛海域首个大型石油开发项目。几乎同时,伦敦明确表示将保护参与该项目的企业。</p>",

    "<h3>阿根廷提出了什么</h3>",

    "<p>该申请是政府9月28日依据《联合国海洋法公约》启动的仲裁程序的一部分。当天英国被给予两周时间停止相关活动;期限于10月12日届满,英国未作出有利答复。申请以公约第290条为依据,提出四项具体诉求:</p>",

    "<ul><li><strong>海狮项目:</strong>要求英国阻止在马尔维纳斯北部盆地开始或继续开采油气。</li>"
    "<li><strong>勘探数据:</strong>要求英国不得以损害阿根廷的方式使用勘探期间获得的信息。</li>"
    "<li><strong>海洋环境:</strong>要求英国不得妨碍公约所规定的环境保护义务的履行。</li>"
    "<li><strong>新许可:</strong>要求英国不得采取加剧争端的措施,尤其是新的开采授权。</li></ul>",

    "<p>需要明确其效力:提出申请并不会使项目暂停。法庭现在须决定是否批准这些措施及其范围。在2012年“自由号”护卫舰案中,法庭大约一个月即作出裁决,因此首份裁定可能在11月出炉,但尚无确定日期。</p>",

    img_block(IMG_PORTADA, "南大西洋上的海狮海上平台",
              "海狮平台——阿根廷希望叫停的马尔维纳斯北部盆地项目。图片:资料图。"),

    "<h3>伦敦为企业撑腰</h3>",

    "<p>英国的回应迅速。英国政府驳回阿根廷的主张,称相关活动受群岛当局颁发的许可证保护(该许可证已于9月延长五年),并宣布将动用其《保护贸易利益法》——该法允许阻止英国企业遵守其他国家的域外制裁或监管规定。</p>",

    "<p>在议会中,海外领地事务大臣乌玛·库马兰(Uma Kumaran)态度直接:阿根廷的主张“并不使群岛政府颁发的许可证失效”。她还警告说,如果局势持续,伦敦可能采取进一步措施,她表示这些措施“将合法、将相称,而且将是强有力的”。</p>",

    "<h3>企业与时间表</h3>",

    "<p>海狮项目由以色列的<strong>Navitas Petroleum</strong>(65%)担任作业者,英国的<strong>Rockhopper Exploration</strong>(35%)为合作伙伴;Rockhopper于2010年发现该油田。计划包括十一口水下油井,连接至一艘浮式生产装置。开发钻井预计2027年进行,首批商业原油预计2028年第一季度产出。10月7日,Rockhopper宣布向持有该装置的公司投入4,400万美元以增持其份额。</p>",

    "<p>在阿根廷一方,施压已产生第一个具体效果:据总统府称,哈里伯顿(Halliburton)确认其子公司不会为该项目提供服务。Navitas则承认正在更换两家承包商,但称预计不会产生重大影响。</p>",

    "<h3>真正的利害所在</h3>",

    "<p>海洋法法庭并不裁决主权争端,这正是阿根廷策略面临的主要法律障碍:公约并未赋予其对领土归属的一般管辖权。因此,此次申请回避主权问题,而是围绕争端未决期间各方在资源、环境和行为方面的具体义务展开。</p>",

    "<p>即便如此,此举仍具有明显的政治与经济价值:它把海狮项目带上国际舞台,使相关企业面临声誉和财务风险,并迫使伦敦表明为维持该项目愿意付出多大代价。法庭预计在未来几周内作出的决定,将左右南大西洋石油争端的走向。</p>",

    '<p style="font-size:.85rem;color:#888;margin-top:2rem">来源:Página12、Infobae、Perfil、La Gaceta、Informe Digital、Rosario3、Splash247、Rio Times。</p>',
])

nueva_entrada = {
    "id": "20261014-propio-malvinas-tribunal-mar-sea-lion",
    "titulo": "Argentina fue al Tribunal del Mar y Londres blindó a sus petroleras",
    "bajada": "Buenos Aires pidió medidas urgentes en Hamburgo para frenar Sea Lion, el primer gran proyecto petrolero en aguas de Malvinas. El Reino Unido respondió activando una ley para proteger a las empresas. Qué pidió cada lado y qué puede pasar.",
    "cuerpo": cuerpo,
    "titulo_en": "Argentina took Malvinas (Falklands) oil to the Law of the Sea Tribunal — and London shielded its oil companies",
    "bajada_en": "Buenos Aires asked for urgent measures in Hamburg to stop Sea Lion, the first major oil project in Malvinas waters. The UK responded by invoking a law to protect the companies. What each side wants and what could happen.",
    "cuerpo_en": cuerpo_en,
    "titulo_pt": "Argentina foi ao Tribunal do Mar e Londres blindou suas petroleiras",
    "bajada_pt": "Buenos Aires pediu medidas urgentes em Hamburgo para frear o Sea Lion, o primeiro grande projeto petrolífero em águas das Malvinas. O Reino Unido respondeu acionando uma lei para proteger as empresas. O que pediu cada lado e o que pode acontecer.",
    "cuerpo_pt": cuerpo_pt,
    "titulo_zh": "阿根廷将马尔维纳斯石油争端诉诸海洋法法庭,伦敦为石油企业撑腰",
    "bajada_zh": "布宜诺斯艾利斯在汉堡请求紧急措施,以叫停马尔维纳斯海域首个大型石油项目“海狮”。英国则启动法律保护相关企业。双方诉求各是什么,接下来可能发生什么。",
    "cuerpo_zh": cuerpo_zh,
    "tag": "🇦🇷 Malvinas",
    "categoria": "malvinas|politica|internacional|energia",
    "fuente": "GLOBALpatagonia",
    "autor": "J. Martineau",
    "propio": True,
    "url_original": "",
    "pais": "malvinas",
    "imagen": IMG_PORTADA,
    "imagen_keywords": "malvinas sea lion plataforma petrolera tribunal del mar hamburgo navitas rockhopper",
    "hashtags_en": "#Malvinas #Falklands #SeaLion #Oil #ITLOS",
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
