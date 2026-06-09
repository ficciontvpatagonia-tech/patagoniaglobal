#!/usr/bin/env python3
"""Genera las variantes EN/PT/中文 del informe de submarinos:
- notas/{id}-en.html, -pt.html, -zh.html (clonando la página ES con texto traducido,
  switcher de idiomas, hreflang)
- inyecta switcher + hreflang + CSS en la página ES
- agrega titulo_/bajada_/cuerpo_ {en,pt,zh} a propios.json
- agrega las 3 URLs al sitemap.xml
"""
import json, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NID = "20260609-propio-malvinas-submarinos"
ES_PATH = f"{BASE}/notas/{NID}.html"
TODAY = "2026-06-09"

# ───────────────────────── strings ES exactos (objetivos de reemplazo) ─────────────────────────
ES_TITLE = "Reino Unido sin submarinos de ataque: sin defensa ni disuasión en Malvinas"
ES_BAJADA = ('Por primera vez en décadas, toda la flota de cazadores nucleares clase Astute de la Royal Navy '
             'está atracada por fallas de mantenimiento. Sin su principal arma de combate en el Atlántico Sur, '
             'Londres ya no puede sostener con credibilidad su discurso de "defensa inquebrantable" del '
             'archipiélago ocupado. Desde la Patagonia, una grieta que la diplomacia argentina tiene derecho a señalar.')
ES_BAJADA_TRUNC = ('Por primera vez en décadas, toda la flota de cazadores nucleares clase Astute de la Royal Navy '
                   'está atracada por fallas de mantenimiento. Sin su principal…')
ES_SOV = "Soberanía"
ES_FIG_ALT = "El crucero ARA General Belgrano hundiéndose tras el ataque del submarino británico HMS Conqueror en 1982"
ES_FIG_CAP = "El ARA General Belgrano, hundido por el submarino británico HMS Conqueror el 2 de mayo de 1982."

# bloques de cuerpo (exactos, como en la estática)
ES_BODY = [
 '<p>No es una especulación ni un rumor de redes sociales. La información fue revelada por <strong>The Mail on Sunday</strong> y replicada por The Telegraph, LBC y Daily Mail: por primera vez, la flota de submarinos de ataque de la Royal Navy —los cazadores nucleares clase Astute— se encuentra completamente inmovilizada en puerto.</p>',
 '<h3>Toda la flota de ataque, atracada</h3>',
 '<p>Los <strong>cinco submarinos operativos</strong> de la clase —HMS Astute, Ambush, Artful, Audacious y Anson— están amarrados, sometidos a mantenimiento y reparaciones. Un sexto, el HMS Agamemnon, fue incorporado a fines de 2025 pero sigue en pruebas de mar, y el séptimo, el HMS Achilles, todavía se construye en Barrow-in-Furness. El resultado es inédito: el Reino Unido no tiene hoy ningún submarino de ataque disponible para desplegar.</p>',
 '<p>La causa, según ex altos mandos británicos, es estructural: años de recortes presupuestarios, falta de diques secos y una crisis de personal especializado. El ship-lift de la base de Faslane lleva más de un año inoperante y las obras en Devonport reducen cuántas unidades pueden repararse a la vez. <strong>Lord West</strong>, ex jefe de la Royal Navy, calificó la situación de "inaceptable" y "muy preocupante". El ex comandante de submarino Ryan Ramsey fue más crudo ante The Telegraph: el Reino Unido, dijo, "luce desdentado".</p>',
 '<p>Cada uno de estos cazadores desplaza 7.400 toneladas, mide 97 metros, navega impulsado por un reactor nuclear Rolls-Royce y carga torpedos pesados Spearfish y misiles de crucero Tomahawk. En teoría, es una de las armas más sofisticadas del arsenal británico. Hoy, ninguna está en condiciones de hacerse a la mar.</p>',
 '<h3>Un vacío estratégico en el Atlántico Sur</h3>',
 '<p>Cuatro décadas después, el tablero se invirtió. No hay un solo submarino de ataque británico en condiciones de patrullar el Atlántico Sur. Los lanzamisiles Trident de la clase Vanguard siguen operativos, pero quedaron sin la escolta que esos cazadores les proporcionaban. La misma desprotección alcanza a la base aérea de Monte Agradable (Mount Pleasant) y a las aguas que rodean las Islas Malvinas.</p>',
 '<p>La pregunta surge sola: si Londres no puede siquiera desplegar sus principales activos navales de combate, ¿con qué sostiene su discurso de "defensa inquebrantable" del territorio que ocupa?</p>',
 '<h3>Una crisis anunciada</h3>',
 '<p>El problema no es un hecho aislado. Décadas de recortes, una industria naval en decadencia y la falta de tripulantes calificados arrastraron a la Royal Navy a su peor momento operativo en mucho tiempo. Ya en enero de 2026 había trascendido que solo <strong>tres de sus seis destructores</strong> Type 45 estaban en servicio.</p>',
 '<p>El Ministerio de Defensa se limitó a señalar que "se está trabajando en un plan de recuperación del mantenimiento". El First Sea Lord, almirante Sir Gwyn Jenkins, lo lanzó el <strong>15 de enero de 2026</strong> con una meta modesta: devolver al menos tres Astute a alta disponibilidad antes de fin de año. No ofreció plazos ni garantías sobre cuándo volverá a flote la flota completa.</p>',
 '<h3>Qué significa para el reclamo argentino</h3>',
 '<p>Conviene ser claro: desde la perspectiva argentina, esto no abre ninguna oportunidad militar. Ningún análisis serio sostiene que el país tenga hoy la capacidad logística, naval o aérea para una reconquista armada, y esa tampoco es la política de Estado que impulsa la diplomacia nacional.</p>',
 '<p>El verdadero impacto es político y simbólico. Durante décadas, el Reino Unido justificó su negativa a negociar con el argumento de que las islas estaban protegidas por una fuerza "moderna y creíble". Ese relato se resquebraja cuando todos sus submarinos de combate están fuera de servicio al mismo tiempo. En los foros internacionales donde se discute la Cuestión Malvinas queda expuesta una contradicción incómoda: Londres exige respeto por la autodeterminación de los kelpers, pero no puede garantizar la defensa efectiva del territorio que administra.</p>',
 '<h3>Conclusión</h3>',
 '<p>El dato es verificable y sus consecuencias, concretas: la Royal Navy atraviesa una etapa en la que su brazo submarino —su herramienta de proyección más temida— simplemente no está disponible.</p>',
 '<p>Para el reclamo argentino de soberanía, no es una invitación a la aventura militar, sino una confirmación de que el poder británico tiene límites y grietas. La diplomacia nacional cuenta ahora con un hecho objetivo para cuestionar la supuesta "garantía de defensa" que Londres esgrime cada vez que se niega a sentarse a negociar.</p>',
 '<p>Desde la Patagonia, atentos a una crisis que desnuda las debilidades de una potencia que alguna vez dominó todos los mares.</p>',
]
# P5 (con clearfix) va aparte porque en la estática lleva class="clearfix"
ES_P5_STATIC = '<p class="clearfix">En 1982, el HMS Conqueror —un submarino nuclear británico— hundió al crucero <strong>ARA General Belgrano</strong> y forzó a toda la flota argentina a replegarse a puerto por el resto de la guerra. Aquel episodio convirtió a la amenaza submarina en la carta más temida del Reino Unido para sostener el control militar del archipiélago.</p>'
ES_SOURCE = '<p style="font-size:13px;color:#888;font-style:italic;margin-top:32px">Informe elaborado con información de The Mail on Sunday, The Telegraph, LBC y declaraciones de ex autoridades de la Royal Navy. Junio de 2026.</p>'
ES_FUENTE = 'Esta nota fue elaborada con información de <strong>GLOBALpatagonia</strong>.'
ES_FUENTE_LABEL = 'Fuente original:'
ES_RELTITLE = 'También te puede interesar'
ES_VOLVER = '← Inicio'
ES_VERCOMPLETO = '← Más noticias en GLOBALpatagonia'

# ───────────────────────── traducciones ─────────────────────────
EN = {
 "title":"United Kingdom without attack submarines: no defense or deterrence in the Falklands",
 "bajada":'For the first time in decades, the Royal Navy\'s entire fleet of Astute-class nuclear hunter-killer submarines is docked due to maintenance failures. Without its main combat asset in the South Atlantic, London can no longer credibly sustain its rhetoric of an "unwavering defense" of the occupied archipelago. From Patagonia, a crack that Argentine diplomacy has every right to point out.',
 "bajada_trunc":"For the first time in decades, the Royal Navy's entire fleet of Astute-class nuclear hunter-killer submarines is docked due to maintenance failures…",
 "sov":"Sovereignty",
 "fig_alt":"The cruiser ARA General Belgrano sinking after the attack by the British submarine HMS Conqueror in 1982",
 "fig_cap":"The ARA General Belgrano, sunk by the British submarine HMS Conqueror on 2 May 1982.",
 "fuente":"This article was prepared with information from <strong>GLOBALpatagonia</strong>.",
 "fuente_label":"Original source:",
 "reltitle":"You might also be interested in",
 "volver":"← Home",
 "vercompleto":"← More news on GLOBALpatagonia",
 "body":[
  '<p>This is not speculation or a social-media rumor. The information was revealed by <strong>The Mail on Sunday</strong> and echoed by The Telegraph, LBC and the Daily Mail: for the first time, the Royal Navy\'s fleet of attack submarines —the Astute-class nuclear hunters— is completely immobilized in port.</p>',
  '<h3>The entire attack fleet, in dock</h3>',
  '<p>The class\'s <strong>five operational submarines</strong> —HMS Astute, Ambush, Artful, Audacious and Anson— are moored, undergoing maintenance and repairs. A sixth, HMS Agamemnon, was commissioned in late 2025 but is still in sea trials, and the seventh, HMS Achilles, is still under construction at Barrow-in-Furness. The result is unprecedented: the United Kingdom currently has no attack submarine available to deploy.</p>',
  '<p>According to former senior British commanders, the cause is structural: years of budget cuts, a shortage of dry docks and a crisis of specialized personnel. The ship-lift at the Faslane base has been out of service for more than a year, and the upgrade works at Devonport reduce how many boats can be repaired at once. <strong>Lord West</strong>, a former head of the Royal Navy, called the situation "unacceptable" and "very worrying." Former submarine commander Ryan Ramsey was blunter to The Telegraph: the United Kingdom, he said, "looks toothless."</p>',
  '<p>Each of these hunters displaces 7,400 tons, measures 97 meters, is driven by a Rolls-Royce nuclear reactor and carries heavy Spearfish torpedoes and Tomahawk cruise missiles. In theory, it is one of the most sophisticated weapons in the British arsenal. Today, not one is in any condition to put to sea.</p>',
  '<h3>A strategic vacuum in the South Atlantic</h3>',
  '<p>Four decades later, the board has flipped. There is not a single British attack submarine in condition to patrol the South Atlantic. The Vanguard-class Trident missile submarines remain operational, but they are left without the escort those hunters used to provide. The same exposure reaches RAF Mount Pleasant and the waters surrounding the Falkland Islands (Malvinas).</p>',
  '<p>The question arises on its own: if London cannot even deploy its main naval combat assets, on what does it sustain its rhetoric of an "unwavering defense" of the territory it occupies?</p>',
  '<h3>A crisis foretold</h3>',
  '<p>The problem is not an isolated event. Decades of cuts, a declining naval industry and a shortage of qualified crews have dragged the Royal Navy to its worst operational moment in a long time. As early as January 2026 it had emerged that only <strong>three of its six</strong> Type 45 destroyers were in service.</p>',
  '<p>The Ministry of Defence merely stated that "work is underway on a maintenance recovery plan." The First Sea Lord, Admiral Sir Gwyn Jenkins, launched it on <strong>15 January 2026</strong> with a modest goal: to return at least three Astutes to high readiness before the end of the year. He offered no timelines or guarantees as to when the full fleet will be back afloat.</p>',
  '<h3>What it means for Argentina\'s claim</h3>',
  '<p>To be clear: from the Argentine perspective, this opens no military opportunity. No serious analysis holds that the country today has the logistical, naval or air capability for an armed reconquest, nor is that the state policy that national diplomacy pursues.</p>',
  '<p>The real impact is political and symbolic. For decades, the United Kingdom justified its refusal to negotiate with the argument that the islands were protected by a "modern and credible" force. That narrative cracks when all of its combat submarines are out of service at the same time. In the international forums where the Malvinas Question is debated, an uncomfortable contradiction is exposed: London demands respect for the self-determination of the islanders, yet cannot guarantee the effective defense of the territory it administers.</p>',
  '<h3>Conclusion</h3>',
  '<p>The fact is verifiable and its consequences concrete: the Royal Navy is going through a phase in which its submarine arm —its most feared instrument of power projection— is simply unavailable.</p>',
  '<p>For Argentina\'s sovereignty claim, this is not an invitation to military adventure, but a confirmation that British power has limits and cracks. National diplomacy now has an objective fact with which to question the supposed "guarantee of defense" that London brandishes each time it refuses to sit down and negotiate.</p>',
  '<p>From Patagonia, watching closely a crisis that lays bare the weaknesses of a power that once ruled every sea.</p>',
 ],
 "p5":'In 1982, HMS Conqueror —a British nuclear submarine— sank the cruiser <strong>ARA General Belgrano</strong> and forced the entire Argentine fleet to withdraw to port for the rest of the war. That episode turned the submarine threat into the United Kingdom\'s most feared card for maintaining military control of the archipelago.',
 "source":'<p style="font-size:13px;color:#888;font-style:italic;margin-top:32px">Report prepared with information from The Mail on Sunday, The Telegraph, LBC and statements by former Royal Navy officials. June 2026.</p>',
 "htmllang":"en","ogloc":"en_US","inlang":"en",
}

PT = {
 "title":"Reino Unido sem submarinos de ataque: sem defesa nem dissuasão nas Malvinas",
 "bajada":'Pela primeira vez em décadas, toda a frota de caçadores nucleares da classe Astute da Royal Navy está atracada por falhas de manutenção. Sem sua principal arma de combate no Atlântico Sul, Londres já não pode sustentar com credibilidade seu discurso de "defesa inabalável" do arquipélago ocupado. Da Patagônia, uma brecha que a diplomacia argentina tem o direito de apontar.',
 "bajada_trunc":'Pela primeira vez em décadas, toda a frota de caçadores nucleares da classe Astute da Royal Navy está atracada por falhas de manutenção. Sem sua principal…',
 "sov":"Soberania",
 "fig_alt":"O cruzador ARA General Belgrano afundando após o ataque do submarino britânico HMS Conqueror em 1982",
 "fig_cap":"O ARA General Belgrano, afundado pelo submarino britânico HMS Conqueror em 2 de maio de 1982.",
 "fuente":"Esta matéria foi elaborada com informações de <strong>GLOBALpatagonia</strong>.",
 "fuente_label":"Fonte original:",
 "reltitle":"Você também pode se interessar",
 "volver":"← Início",
 "vercompleto":"← Mais notícias no GLOBALpatagonia",
 "body":[
  '<p>Não é especulação nem boato de redes sociais. A informação foi revelada pelo <strong>The Mail on Sunday</strong> e replicada por The Telegraph, LBC e Daily Mail: pela primeira vez, a frota de submarinos de ataque da Royal Navy —os caçadores nucleares da classe Astute— encontra-se completamente imobilizada no porto.</p>',
  '<h3>Toda a frota de ataque, atracada</h3>',
  '<p>Os <strong>cinco submarinos operacionais</strong> da classe —HMS Astute, Ambush, Artful, Audacious e Anson— estão amarrados, em manutenção e reparos. Um sexto, o HMS Agamemnon, foi incorporado no fim de 2025, mas segue em testes de mar, e o sétimo, o HMS Achilles, ainda está em construção em Barrow-in-Furness. O resultado é inédito: o Reino Unido não tem hoje nenhum submarino de ataque disponível para enviar.</p>',
  '<p>Segundo ex-altos comandantes britânicos, a causa é estrutural: anos de cortes orçamentários, falta de docas secas e uma crise de pessoal especializado. O ship-lift da base de Faslane está fora de serviço há mais de um ano, e as obras em Devonport reduzem quantas unidades podem ser reparadas ao mesmo tempo. <strong>Lord West</strong>, ex-chefe da Royal Navy, classificou a situação como "inaceitável" e "muito preocupante". O ex-comandante de submarino Ryan Ramsey foi mais duro ao The Telegraph: o Reino Unido, disse, "parece desdentado".</p>',
  '<p>Cada um desses caçadores desloca 7.400 toneladas, mede 97 metros, é movido por um reator nuclear Rolls-Royce e carrega torpedos pesados Spearfish e mísseis de cruzeiro Tomahawk. Em tese, é uma das armas mais sofisticadas do arsenal britânico. Hoje, nenhum está em condições de ir ao mar.</p>',
  '<h3>Um vácuo estratégico no Atlântico Sul</h3>',
  '<p>Quatro décadas depois, o tabuleiro se inverteu. Não há um único submarino de ataque britânico em condições de patrulhar o Atlântico Sul. Os submarinos lançadores de mísseis Trident, da classe Vanguard, seguem operacionais, mas ficaram sem a escolta que esses caçadores lhes proporcionavam. A mesma desproteção alcança a base aérea de Mount Pleasant e as águas que cercam as Ilhas Malvinas.</p>',
  '<p>A pergunta surge sozinha: se Londres não pode sequer enviar seus principais ativos navais de combate, com o que sustenta seu discurso de "defesa inabalável" do território que ocupa?</p>',
  '<h3>Uma crise anunciada</h3>',
  '<p>O problema não é um fato isolado. Décadas de cortes, uma indústria naval em decadência e a falta de tripulantes qualificados arrastaram a Royal Navy ao seu pior momento operacional em muito tempo. Já em janeiro de 2026 havia transpirado que apenas <strong>três dos seis</strong> contratorpedeiros Type 45 estavam em serviço.</p>',
  '<p>O Ministério da Defesa limitou-se a afirmar que "trabalha-se em um plano de recuperação da manutenção". O First Sea Lord, almirante Sir Gwyn Jenkins, lançou-o em <strong>15 de janeiro de 2026</strong> com uma meta modesta: devolver pelo menos três Astute à alta disponibilidade antes do fim do ano. Não ofereceu prazos nem garantias sobre quando a frota completa voltará à água.</p>',
  '<h3>O que significa para a reivindicação argentina</h3>',
  '<p>Convém ser claro: da perspectiva argentina, isso não abre nenhuma oportunidade militar. Nenhuma análise séria sustenta que o país tenha hoje a capacidade logística, naval ou aérea para uma reconquista armada, e essa tampouco é a política de Estado que a diplomacia nacional impulsiona.</p>',
  '<p>O verdadeiro impacto é político e simbólico. Por décadas, o Reino Unido justificou sua recusa em negociar com o argumento de que as ilhas estavam protegidas por uma força "moderna e confiável". Esse relato se desfaz quando todos os seus submarinos de combate estão fora de serviço ao mesmo tempo. Nos foros internacionais onde se discute a Questão das Malvinas fica exposta uma contradição incômoda: Londres exige respeito pela autodeterminação dos kelpers, mas não pode garantir a defesa efetiva do território que administra.</p>',
  '<h3>Conclusão</h3>',
  '<p>O dado é verificável e suas consequências, concretas: a Royal Navy atravessa uma etapa em que seu braço submarino —sua ferramenta de projeção mais temida— simplesmente não está disponível.</p>',
  '<p>Para a reivindicação argentina de soberania, não é um convite à aventura militar, mas uma confirmação de que o poder britânico tem limites e brechas. A diplomacia nacional conta agora com um fato objetivo para questionar a suposta "garantia de defesa" que Londres ostenta cada vez que se nega a negociar.</p>',
  '<p>Da Patagônia, atentos a uma crise que desnuda as fraquezas de uma potência que um dia dominou todos os mares.</p>',
 ],
 "p5":'Em 1982, o HMS Conqueror —um submarino nuclear britânico— afundou o cruzador <strong>ARA General Belgrano</strong> e obrigou toda a frota argentina a recuar ao porto pelo resto da guerra. Aquele episódio transformou a ameaça submarina na carta mais temida do Reino Unido para manter o controle militar do arquipélago.',
 "source":'<p style="font-size:13px;color:#888;font-style:italic;margin-top:32px">Reportagem elaborada com informações de The Mail on Sunday, The Telegraph, LBC e declarações de ex-autoridades da Royal Navy. Junho de 2026.</p>',
 "htmllang":"pt-BR","ogloc":"pt_BR","inlang":"pt-BR",
}

ZH = {
 "title":"英国无攻击型潜艇：在马尔维纳斯群岛既无防御也无威慑",
 "bajada":'几十年来，英国皇家海军的整支机敏级（Astute）核动力攻击潜艇舰队首次因维护故障全部停靠港内。失去了在南大西洋的主要作战力量，伦敦再也无法令人信服地维持其对被占群岛"坚定不移的防御"的说辞。从巴塔哥尼亚看，这是阿根廷外交有权指出的一道裂痕。',
 "bajada_trunc":'几十年来，英国皇家海军的整支机敏级核动力攻击潜艇舰队首次因维护故障全部停靠港内。失去了在南大西洋的主要作战力量……',
 "sov":"主权",
 "fig_alt":"1982年，阿根廷巡洋舰贝尔格拉诺将军号在英国潜艇HMS Conqueror袭击后沉没",
 "fig_cap":"贝尔格拉诺将军号（ARA General Belgrano），于1982年5月2日被英国潜艇HMS Conqueror击沉。",
 "fuente":"本文依据<strong>GLOBALpatagonia</strong>的信息整理而成。",
 "fuente_label":"原始来源：",
 "reltitle":"您可能还感兴趣",
 "volver":"← 首页",
 "vercompleto":"← 更多 GLOBALpatagonia 新闻",
 "body":[
  '<p>这并非猜测，也不是社交媒体上的谣言。该消息由<strong>《星期日邮报》（The Mail on Sunday）</strong>披露，并被《电讯报》、LBC和《每日邮报》转载：英国皇家海军的攻击型潜艇舰队——机敏级核动力猎杀潜艇——首次完全停摆于港口。</p>',
  '<h3>整支攻击舰队停靠在港</h3>',
  '<p>该级别的<strong>五艘现役潜艇</strong>——HMS Astute、Ambush、Artful、Audacious和Anson——均已系泊，正在接受维护和修理。第六艘HMS Agamemnon于2025年底服役，但仍在海试；第七艘HMS Achilles仍在巴罗因弗内斯（Barrow-in-Furness）建造中。结果前所未有：英国目前没有任何可供部署的攻击型潜艇。</p>',
  '<p>据英国前高级指挥官称，原因是结构性的：多年的预算削减、干船坞短缺以及专业人员危机。法斯莱恩（Faslane）基地的潜艇升降系统已停用一年多，而德文波特（Devonport）的升级工程减少了同时可维修的艇数。皇家海军前负责人<strong>韦斯特勋爵（Lord West）</strong>称这一状况"不可接受"且"令人非常担忧"。前潜艇指挥官瑞安·拉姆齐（Ryan Ramsey）对《电讯报》说得更直白：他说，英国"看上去毫无牙齿"。</p>',
  '<p>每艘这样的猎杀潜艇排水量达7400吨，长97米，由劳斯莱斯核反应堆驱动，配备重型"长矛鱼"（Spearfish）鱼雷和"战斧"（Tomahawk）巡航导弹。理论上，它是英国武库中最先进的武器之一。如今，没有一艘能够出海。</p>',
  '<h3>南大西洋的战略真空</h3>',
  '<p>四十年后，棋局逆转。没有一艘英国攻击型潜艇能够在南大西洋巡逻。携带三叉戟（Trident）导弹的前卫级（Vanguard）潜艇仍在服役，但失去了这些猎杀潜艇曾经提供的护航。同样的暴露也波及蒙特普莱森特（Mount Pleasant）空军基地以及马尔维纳斯群岛周边海域。</p>',
  '<p>问题不言自明：如果伦敦连主要的海军作战力量都无法部署，它又凭什么维持对其占领领土"坚定不移的防御"的说辞？</p>',
  '<h3>一场早有预兆的危机</h3>',
  '<p>这一问题并非孤立事件。数十年的削减、衰落的造船工业以及合格船员的短缺，将皇家海军拖入了长期以来最糟糕的作战状态。早在2026年1月就已传出，其六艘45型驱逐舰中只有<strong>三艘</strong>在役。</p>',
  '<p>国防部仅表示"正在制定一项维护恢复计划"。第一海务大臣、海军上将格温·詹金斯爵士（Sir Gwyn Jenkins）于<strong>2026年1月15日</strong>启动该计划，目标却很有限：在年底前让至少三艘机敏级潜艇恢复高度战备。他没有提供整支舰队何时重新下水的时间表或保证。</p>',
  '<h3>这对阿根廷主权主张意味着什么</h3>',
  '<p>需要明确的是：从阿根廷的角度看，这并未带来任何军事机会。没有任何严肃分析认为该国如今具备武力收复的后勤、海军或空中能力，这也不是国家外交所推行的国策。</p>',
  '<p>真正的影响是政治性和象征性的。数十年来，英国以这些岛屿受到一支"现代且可信"的力量保护为由，拒绝谈判。当其所有作战潜艇同时退出服役时，这套说辞便出现裂痕。在讨论马尔维纳斯问题的国际论坛上，一个令人尴尬的矛盾暴露无遗：伦敦要求尊重岛民的自决权，却无法保证对其所管理领土的有效防御。</p>',
  '<h3>结语</h3>',
  '<p>事实可以核实，其后果也很具体：皇家海军正处于这样一个阶段——其潜艇力量，这一最令人畏惧的力量投射工具，根本无法使用。</p>',
  '<p>对于阿根廷的主权主张而言，这并非一份诉诸军事冒险的邀请，而是再次印证英国的力量存在极限与裂缝。每当伦敦拒绝坐下来谈判时，国家外交如今便有了一个客观事实，去质疑伦敦所标榜的所谓"防御保证"。</p>',
  '<p>从巴塔哥尼亚，我们密切关注这场危机——它暴露了一个曾经称霸所有海洋的强国的虚弱。</p>',
 ],
 "p5":'1982年，英国核潜艇HMS Conqueror击沉了巡洋舰<strong>贝尔格拉诺将军号</strong>，迫使整支阿根廷舰队在战争余下时间撤回港口。那一事件使潜艇威胁成为英国维持对该群岛军事控制最令人畏惧的王牌。',
 "source":'<p style="font-size:13px;color:#888;font-style:italic;margin-top:32px">本报道依据《星期日邮报》、《电讯报》、LBC以及皇家海军前官员的声明整理而成。2026年6月。</p>',
 "htmllang":"zh-Hans","ogloc":"zh_CN","inlang":"zh-Hans",
}

LANGS = {"en":EN, "pt":PT, "zh":ZH}

# ───────────────────────── helpers ─────────────────────────
def hreflang_block():
    u = lambda s: f"https://globalpatagonia.org/notas/{NID}{s}.html"
    return (f'  <link rel="alternate" hreflang="es" href="{u("")}"/>\n'
            f'  <link rel="alternate" hreflang="en" href="{u("-en")}"/>\n'
            f'  <link rel="alternate" hreflang="pt" href="{u("-pt")}"/>\n'
            f'  <link rel="alternate" hreflang="zh-Hans" href="{u("-zh")}"/>\n'
            f'  <link rel="alternate" hreflang="x-default" href="{u("")}"/>\n')

def switcher_block(active):
    def a(code, suf, label):
        cls = ' class="active"' if code == active else ''
        return f'      <a href="{NID}{suf}.html"{cls}>{label}</a>'
    return ('    <div class="lang-switcher">\n'
            + a("es","","🇦🇷 ES") + "\n"
            + a("en","-en","🇬🇧 EN") + "\n"
            + a("pt","-pt","🇧🇷 PT") + "\n"
            + a("zh","-zh","🇨🇳 中文") + "\n"
            + '    </div>\n')

LANG_CSS = (
  "    .lang-switcher{display:flex;gap:8px;margin:14px 0 24px;align-items:center;flex-wrap:wrap;}\n"
  "    .lang-switcher a{display:inline-flex;align-items:center;gap:4px;padding:5px 12px;border:1.5px solid #c8d4dc;border-radius:20px;font-size:11px;font-weight:700;letter-spacing:0.5px;text-decoration:none;color:#3a5a7a;background:#fff;transition:all 0.2s;}\n"
  "    .lang-switcher a:hover,.lang-switcher a.active{background:var(--verde);color:white;border-color:var(--verde);}\n"
)

def build_translated(es_html, L, T):
    c = es_html
    # 1) texto: bajada (trunc -> quot -> esc), título, soberanía, figura, cuerpo
    c = c.replace(ES_BAJADA_TRUNC, T["bajada_trunc"])
    c = c.replace(ES_BAJADA.replace('"','&quot;'), T["bajada"].replace('"','&quot;'))
    c = c.replace(ES_BAJADA.replace('"','\\"'),     T["bajada"].replace('"','\\"'))
    c = c.replace(ES_TITLE, T["title"])
    c = c.replace(ES_FIG_ALT, T["fig_alt"]).replace(ES_FIG_CAP, T["fig_cap"])
    c = c.replace(ES_P5_STATIC, '<p class="clearfix">'+T["p5"]+'</p>')
    for es_b, t_b in zip(ES_BODY, T["body"]):
        c = c.replace(es_b, t_b)
    c = c.replace(ES_SOURCE, T["source"])
    c = c.replace(ES_FUENTE, T["fuente"]).replace(ES_FUENTE_LABEL, T["fuente_label"])
    c = c.replace(ES_RELTITLE, T["reltitle"])
    c = c.replace('class="volver">'+ES_VOLVER, 'class="volver">'+T["volver"])
    c = c.replace('class="ver-completo">'+ES_VERCOMPLETO, 'class="ver-completo">'+T["vercompleto"])
    c = c.replace(ES_SOV, T["sov"])
    # 1b) quitar hreflang + switcher heredados de la base ES (evita duplicados)
    c = re.sub(r'\s*<link rel="alternate" hreflang="[^"]*" href="[^"]*"/>', '', c)
    c = re.sub(r'\s*<div class="lang-switcher">.*?</div>\n', '\n', c, count=1, flags=re.S)
    # 2) self-id -> -L (canonical, og:url, json-ld url) ANTES de meter hreflang/switcher
    c = c.replace(f"{NID}.html", f"{NID}-{L}.html")
    # 3) lang / inLanguage / og:locale
    c = c.replace('<html lang="es">', f'<html lang="{T["htmllang"]}">')
    c = c.replace('"inLanguage": "es"', f'"inLanguage": "{T["inlang"]}"')
    # 4) hreflang (URLs fijas correctas) tras canonical
    c = re.sub(r'(<link rel="canonical"[^>]*/>)', lambda m: m.group(1)+"\n"+hreflang_block().rstrip("\n"), c, count=1)
    # 5) switcher antes de la imagen principal
    c = c.replace('    <img class="nota-imagen"', switcher_block(L)+'    <img class="nota-imagen"', 1)
    return c

def cuerpo_field(T):
    """Cuerpo para propios.json (sin figura, P5 sin clearfix)."""
    parts = list(T["body"])
    parts.insert(6, '<p>'+T["p5"]+'</p>')   # P5 va tras el h3 'vacío estratégico' (índice 5)
    parts.append(T["source"])
    return "\n\n".join(parts)

# ───────────────────────── 1. ES: CSS + hreflang + switcher ─────────────────────────
es = open(ES_PATH, encoding="utf-8").read()
if ".lang-switcher{" not in es:
    es = es.replace("  </style>", LANG_CSS + "  </style>", 1)
if 'hreflang="en"' not in es:
    es = re.sub(r'(<link rel="canonical"[^>]*/>)', lambda m: m.group(1)+"\n"+hreflang_block().rstrip("\n"), es, count=1)
if 'class="lang-switcher"' not in es:
    es = es.replace('    <img class="nota-imagen"', switcher_block("es")+'    <img class="nota-imagen"', 1)
open(ES_PATH, "w", encoding="utf-8").write(es)
print("ES: switcher + hreflang + CSS inyectados")

# ───────────────────────── 2. páginas traducidas ─────────────────────────
for L, T in LANGS.items():
    out = build_translated(es, L, T)
    # checks anti-residuo
    assert T["title"] in out, f"{L}: título no insertado"
    assert ES_TITLE not in out, f"{L}: quedó el título ES"
    assert "Conclusión" not in out, f"{L}: quedó el h3 'Conclusión'"
    assert f'<html lang="{T["htmllang"]}">' in out, f"{L}: lang no cambiado"
    path = f"{BASE}/notas/{NID}-{L}.html"
    open(path, "w", encoding="utf-8").write(out)
    print(f"{L}: {os.path.basename(path)} generada")

# ───────────────────────── 3. propios.json: campos _en/_pt/_zh ─────────────────────────
PROP = f"{BASE}/propios.json"
data = json.load(open(PROP, encoding="utf-8"))
for n in data:
    if n.get("id") == NID:
        for L, T in LANGS.items():
            n[f"titulo_{L}"] = T["title"]
            n[f"bajada_{L}"] = T["bajada"]
            n[f"cuerpo_{L}"] = cuerpo_field(T)
        break
json.dump(data, open(PROP, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("propios.json: titulo/bajada/cuerpo _en/_pt/_zh agregados")

# ───────────────────────── 4. sitemap: 3 variantes ─────────────────────────
SM = f"{BASE}/sitemap.xml"
sm = open(SM, encoding="utf-8").read()
add = ""
for L in ("en","pt","zh"):
    loc = f"https://globalpatagonia.org/notas/{NID}-{L}.html"
    if loc not in sm:
        add += (f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{TODAY}</lastmod>\n"
                f"    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n")
if add:
    sm = sm.replace("</urlset>", add + "</urlset>")
    open(SM, "w", encoding="utf-8").write(sm)
    print("sitemap.xml: variantes agregadas")
else:
    print("sitemap.xml: variantes ya presentes")

print("LISTO.")
