#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Publica el informe "Argos Georgia: la tragedia que expone al Gobierno británico
# de las Islas Malvinas" (firma M. Galindo) en propios.json
# (modelo: publicar_malvinas_eeuu_otan.py). Texto ES = el entregado por Marto, sin cambios.
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


def map_block(src, alt, cap):
    # El mapa es vertical: se limita el ancho para que no ocupe toda la pantalla.
    return ('<div style="margin:2rem auto;max-width:460px"><img src="' + src + '" alt="' + alt +
            '" loading="lazy" decoding="async" style="width:100%;border-radius:6px;display:block">'
            '<div style="font-size:.8rem;color:#777;margin-top:.45rem">' + cap + '</div></div>')


IMG_PORTADA = "fotos/argos-georgia-buque.webp"
IMG_MAPA = "fotos/argos-georgia-mapa-atlantico-sur.webp"

# ============================== ESPAÑOL ==============================
bajada_es = ("En julio de 2024, un buque pesquero se hundió a unas 190 millas náuticas —casi 350 kilómetros— "
             "al este de Puerto Stanley, en las Islas Malvinas. Murieron 13 tripulantes. Dos años después, un "
             "informe oficial británico revela que la tragedia pudo evitarse: hubo fallas técnicas, negligencia "
             "en la emergencia y un retraso fatal en el pedido de auxilio. El hecho, casi desconocido en la "
             "Argentina, demuestra la imposibilidad del gobierno isleño de administrar con seguridad un espacio "
             "marítimo que no le pertenece.")

cuerpo = "\n\n".join([
    DATELINE.format("Malvinas — Informe GLOBALpatagonia"),
    "<p>Poco se sabe en la Argentina sobre lo que ocurrió con el Argos Georgia. La noticia tuvo una cobertura limitada en los grandes medios nacionales y el informe oficial de la Marine Accident Investigation Branch (MAIB) del Reino Unido —publicado 26 meses después del siniestro— pasó casi desapercibido para la opinión pública. Sin embargo, su importancia es mayúscula: no solo documenta la muerte de 13 personas, sino que expone una cadena de negligencias técnicas y operativas, y revela la fragilidad del control que el Gobierno británico de las Islas Malvinas ejerce sobre la actividad pesquera en el Atlántico Sur.</p>",
    "<h3>Qué pasó: la secuencia de una catástrofe</h3>",
    "<p>El Argos Georgia era un buque palangrero de 54 metros de eslora, abanderado en Santa Elena (un territorio británico de ultramar) y operado por la empresa Argos Froyanes Limited, de capitales anglo-noruegos. Navegaba desde Puerto Stanley hacia los caladeros de merluza negra próximos a Georgia del Sur con 27 tripulantes a bordo: diez españoles, ocho rusos, cinco indonesios, dos peruanos y dos uruguayos.</p>",
    map_block(IMG_MAPA, "Mapa del Atlántico Sur con la ubicación del hundimiento del Argos Georgia al este de las Islas Malvinas",
              "El Argos Georgia se hundió a unas 190 millas náuticas, casi 350 kilómetros, al este de Puerto Stanley."),
    "<p>El 22 de julio de 2024, alrededor de las 13:00 horas, la escotilla de halado de línea (line hauling hatch) del costado de estribor, que debería haber estado cerrada, “se abrió de forma inesperada”, permitiendo la entrada masiva de agua. El informe de la MAIB determina que el mecanismo de fijación manual de la compuerta “probablemente no se había aplicado” y que la tripulación no pudo cerrarla una vez abierta. Además, el mecanismo de accionamiento de la escotilla presentaba “una debilidad de diseño no identificada” y había sido modificado sin seguir un proceso de aprobación formal que permitiera detectar posibles deficiencias.</p>",
    "<p>El agua se propagó rápidamente porque las puertas estancas interiores estaban abiertas, una práctica que, según el informe, comprometió la estabilidad del buque. El Argos Georgia escoró progresivamente a estribor, perdió la propulsión y finalmente se hundió.</p>",
    "<h3>El retraso que costó vidas</h3>",
    "<p>Uno de los hallazgos más contundentes del informe es el relativo a la respuesta a la emergencia. La MAIB concluye que la tripulación no emitió una alerta formal de socorro (Mayday) en las primeras fases del siniestro. En su lugar, el capitán se comunicó primero a través de WhatsApp con otros barcos y con la empresa en tierra.</p>",
    "<p>Según la reconstrucción de los hechos, el agua comenzó a entrar alrededor de las 13:00, pero el capitán no alertó por WhatsApp hasta las 13:45. La alerta oficial de socorro no se emitió hasta casi las 15:30, es decir, casi dos horas y media después del inicio de la inundación. El informe señala que esta comunicación informal “redujo la comprensión inicial de la gravedad del evento” y retrasó la activación de una respuesta adecuada, ya que en tierra se creyó que la situación aún podía ser “controlada o estabilizada”.</p>",
    "<p>Este retraso, según la MAIB, “redujo la probabilidad de que los medios de rescate llegaran con luz diurna” y acortó drásticamente el margen operativo para una intervención eficaz. De los 27 tripulantes, 14 fueron rescatados con vida y 13 fallecieron, algunos durante el abandono del buque y otros en las balsas salvavidas, víctimas de la exposición al agua fría.</p>",
    "<h3>La sombra de la ilegalidad: licencias sin seguridad</h3>",
    "<p>El informe de la MAIB también dirigió una recomendación específica al Gobierno de las Islas Malvinas. Le instó a mejorar su capacidad de comunicaciones marítimas de búsqueda y rescate (SAR) para poder establecer un contacto “directo y fiable” con los buques en peligro dentro de su área de responsabilidad. Esta recomendación oficial confirma que el sistema de comunicaciones del centro coordinador de rescate isleño no fue lo suficientemente eficaz, un factor que, sumado al retraso en la alerta, contribuyó al desenlace fatal.</p>",
    "<p>Pero la crítica trasciende la respuesta a la emergencia. El Argos Georgia operaba bajo una licencia de pesca otorgada por las autoridades británicas de las Islas Malvinas. El buque era uno de los cuatro beneficiados por una extensión unilateral de licencias por parte de Gran Bretaña en el marco de la CCRVMA (Comisión para la Conservación de Recursos Vivos Marinos Antárticos), un proceso que, desde la perspectiva argentina, carece de toda legitimidad.</p>",
    "<p>El Gobierno argentino ha sido claro al respecto: las licencias que entrega el gobierno isleño son ilegales. Para pescar en las aguas que rodean las Malvinas, los buques deberían contar también con la autorización argentina, algo que no ocurre. Esta situación no es un detalle menor. Como señaló el experto en Atlántico Sur César Lerena, la actividad pesquera en la zona “quebranta no sólo la legislación argentina vigente (ley 24.922) sino también la Convención de las Naciones Unidas sobre el Derecho del Mar”, y le significa al país una pérdida anual de unas 250.000 toneladas de recursos pesqueros.</p>",
    "<h3>Un hecho silenciado que expone la fragilidad del control isleño</h3>",
    "<p>Pese a la magnitud de la tragedia y a las contundentes conclusiones del informe oficial, en la Argentina poco se sabe de lo ocurrido con el Argos Georgia. La noticia tuvo una cobertura limitada en los grandes medios nacionales, y el informe de la MAIB —publicado 26 meses después del siniestro— pasó casi desapercibido para la opinión pública. Sin embargo, su importancia es mayúscula, porque no solo documenta la muerte de 13 personas, sino que demuestra la imposibilidad del gobierno de las islas de hacer usufructo de ese espacio marítimo sin brindar las garantías mínimas de seguridad.</p>",
    "<p>La recomendación de la propia agencia británica al Gobierno de Malvinas para que mejore sus comunicaciones SAR es una admisión tácita de que el archipiélago no cuenta con los medios idóneos para coordinar un rescate de envergadura. La ausencia de un patrullero oceánico en la zona, la dependencia de buques pesqueros privados para las tareas de salvamento y el retraso en la activación del operativo revelan un sistema de administración pesquera que prioriza la recaudación por licencias por encima de la vida de los tripulantes.</p>",
    "<p>En otras palabras: el gobierno isleño se arroga el derecho de otorgar permisos de pesca en aguas en disputa, pero no puede garantizar la seguridad de quienes operan bajo esos permisos. La tragedia del Argos Georgia es la prueba más elocuente de que ese usufructo unilateral es, además de ilegal, insostenible desde el punto de vista humanitario.</p>",
    "<h3>Por qué es importante hoy</h3>",
    "<p>La tragedia del Argos Georgia es mucho más que un accidente marítimo. Es la evidencia más cruda de un sistema que prioriza la explotación de un recurso valioso —la merluza negra— por encima de la seguridad de las personas que lo extraen y de la legalidad internacional.</p>",
    "<p>El informe de la MAIB, conocido 26 meses después del siniestro, confirma que las fallas técnicas y la deficiente gestión de la emergencia fueron determinantes. Pero también deja al descubierto una pregunta incómoda: ¿puede un gobierno que otorga licencias de pesca en aguas en disputa garantizar la seguridad de quienes operan bajo esas licencias? La respuesta, a la luz de los hechos y de la recomendación oficial de la propia agencia británica, parece ser negativa.</p>",
    "<p>Para la Argentina, el caso refuerza una posición histórica: la explotación de los recursos del Atlántico Sur bajo un esquema de licencias unilateral no solo es ilegal, sino que además genera un entorno de riesgo para los trabajadores del mar. Mientras el Reino Unido y el gobierno isleño continúan administrando la pesquería sin un marco de cooperación con el Estado argentino, tragedias como la del Argos Georgia seguirán siendo una posibilidad latente.</p>",
    "<p>La memoria de los 13 tripulantes fallecidos exige algo más que un informe técnico. Exige una revisión profunda de un modelo que, hoy por hoy, sigue operando en la ilegalidad y sin las garantías mínimas de seguridad que cualquier actividad en el mar debería tener.</p>",
])

# ============================== ENGLISH ==============================
bajada_en = ("In July 2024, a fishing vessel sank some 190 nautical miles —almost 350 kilometres— east of Port Stanley, "
             "in the Malvinas Islands. Thirteen crew members died. Two years later, an official British report reveals "
             "that the tragedy could have been avoided: there were technical failures, negligence in the emergency and "
             "a fatal delay in calling for help. The case, almost unknown in Argentina, shows the inability of the "
             "island government to safely administer a maritime space that does not belong to it.")

cuerpo_en = "\n\n".join([
    DATELINE.format("Malvinas — GLOBALpatagonia Report"),
    "<p>Little is known in Argentina about what happened to the Argos Georgia. The news received limited coverage in the major national media, and the official report by the United Kingdom's Marine Accident Investigation Branch (MAIB) —published 26 months after the accident— went almost unnoticed by the public. Yet its importance is enormous: it not only documents the deaths of 13 people, but exposes a chain of technical and operational negligence, and reveals how fragile the control that the British Government of the Malvinas Islands exercises over fishing activity in the South Atlantic really is.</p>",
    "<h3>What happened: the sequence of a catastrophe</h3>",
    "<p>The Argos Georgia was a 54-metre longline fishing vessel, flagged in St Helena (a British overseas territory) and operated by Argos Froyanes Limited, a company with Anglo-Norwegian capital. She was sailing from Port Stanley to the Patagonian toothfish grounds near South Georgia with 27 crew on board: ten Spaniards, eight Russians, five Indonesians, two Peruvians and two Uruguayans.</p>",
    map_block(IMG_MAPA, "Map of the South Atlantic showing where the Argos Georgia sank, east of the Malvinas Islands",
              "The Argos Georgia sank some 190 nautical miles, almost 350 kilometres, east of Port Stanley."),
    "<p>On 22 July 2024, at around 13:00, the line hauling hatch on the starboard side, which should have been closed, “opened unexpectedly”, letting in a massive amount of water. The MAIB report concludes that the hatch's manual securing mechanism “had probably not been applied” and that the crew could not close it once open. In addition, the hatch's drive mechanism had “an unidentified design weakness” and had been modified without following a formal approval process that could have detected potential deficiencies.</p>",
    "<p>The water spread quickly because the internal watertight doors were open, a practice that, according to the report, compromised the vessel's stability. The Argos Georgia progressively heeled to starboard, lost propulsion and finally sank.</p>",
    "<h3>The delay that cost lives</h3>",
    "<p>One of the report's most damning findings concerns the emergency response. The MAIB concludes that the crew did not issue a formal distress alert (Mayday) in the early stages of the casualty. Instead, the captain first communicated through WhatsApp with other vessels and with the company ashore.</p>",
    "<p>According to the reconstruction of events, water began to enter at around 13:00, but the captain did not raise the alarm on WhatsApp until 13:45. The official distress alert was not issued until almost 15:30, nearly two and a half hours after the flooding began. The report notes that this informal communication “reduced the initial understanding of the seriousness of the event” and delayed the activation of an adequate response, since ashore it was believed the situation could still be “controlled or stabilised”.</p>",
    "<p>This delay, according to the MAIB, “reduced the likelihood of rescue assets arriving in daylight” and drastically shortened the operational margin for an effective intervention. Of the 27 crew, 14 were rescued alive and 13 died, some during the abandonment of the vessel and others in the liferafts, victims of exposure to cold water.</p>",
    "<h3>The shadow of illegality: licences without safety</h3>",
    "<p>The MAIB report also made a specific recommendation to the Government of the Malvinas Islands. It urged it to improve its maritime search and rescue (SAR) communications capability so as to establish “direct and reliable” contact with vessels in distress within its area of responsibility. This official recommendation confirms that the communications system of the island rescue coordination centre was not effective enough, a factor that, added to the delay in the alert, contributed to the fatal outcome.</p>",
    "<p>But the criticism goes beyond the emergency response. The Argos Georgia operated under a fishing licence granted by the British authorities of the Malvinas Islands. The vessel was one of four that benefited from a unilateral extension of licences by Great Britain within the framework of CCAMLR (the Commission for the Conservation of Antarctic Marine Living Resources), a process that, from the Argentine perspective, lacks any legitimacy.</p>",
    "<p>The Argentine Government has been clear on this: the licences issued by the island government are illegal. To fish in the waters surrounding the Malvinas, vessels should also hold Argentine authorisation, which they do not. This is no minor detail. As South Atlantic expert César Lerena has pointed out, fishing activity in the area “violates not only current Argentine legislation (Law 24,922) but also the United Nations Convention on the Law of the Sea”, and costs the country some 250,000 tonnes of fishery resources every year.</p>",
    "<h3>A silenced event that exposes the fragility of island control</h3>",
    "<p>Despite the magnitude of the tragedy and the forceful conclusions of the official report, little is known in Argentina about what happened to the Argos Georgia. The news received limited coverage in the major national media, and the MAIB report —published 26 months after the accident— went almost unnoticed by the public. Yet its importance is enormous, because it not only documents the deaths of 13 people, but shows the inability of the islands' government to exploit that maritime space without providing the minimum safety guarantees.</p>",
    "<p>The British agency's own recommendation to the Malvinas Government to improve its SAR communications is a tacit admission that the archipelago lacks the suitable means to coordinate a major rescue. The absence of an ocean-going patrol vessel in the area, the reliance on private fishing vessels for rescue tasks and the delay in activating the operation reveal a fisheries administration system that puts licence revenue above the lives of the crew.</p>",
    "<p>In other words: the island government arrogates to itself the right to grant fishing permits in disputed waters, but cannot guarantee the safety of those who operate under those permits. The Argos Georgia tragedy is the most eloquent proof that this unilateral exploitation is, besides being illegal, unsustainable from a humanitarian standpoint.</p>",
    "<h3>Why it matters today</h3>",
    "<p>The Argos Georgia tragedy is far more than a maritime accident. It is the rawest evidence of a system that puts the exploitation of a valuable resource —Patagonian toothfish— above the safety of the people who extract it and above international legality.</p>",
    "<p>The MAIB report, made public 26 months after the accident, confirms that technical failures and poor emergency management were decisive. But it also exposes an uncomfortable question: can a government that grants fishing licences in disputed waters guarantee the safety of those who operate under those licences? In light of the facts and of the British agency's own official recommendation, the answer appears to be no.</p>",
    "<p>For Argentina, the case reinforces a historic position: exploiting South Atlantic resources under a unilateral licensing scheme is not only illegal, but also creates a risky environment for seafarers. As long as the United Kingdom and the island government keep administering the fishery without a framework of cooperation with the Argentine State, tragedies like that of the Argos Georgia will remain a latent possibility.</p>",
    "<p>The memory of the 13 crew members who died demands more than a technical report. It demands a deep review of a model that, today, continues to operate illegally and without the minimum safety guarantees that any activity at sea should have.</p>",
])

# ============================== PORTUGUÊS ==============================
bajada_pt = ("Em julho de 2024, um navio pesqueiro afundou a cerca de 190 milhas náuticas —quase 350 quilômetros— "
             "a leste de Porto Stanley, nas Ilhas Malvinas. Morreram 13 tripulantes. Dois anos depois, um relatório "
             "oficial britânico revela que a tragédia poderia ter sido evitada: houve falhas técnicas, negligência na "
             "emergência e um atraso fatal no pedido de socorro. O fato, quase desconhecido na Argentina, demonstra "
             "a impossibilidade de o governo das ilhas administrar com segurança um espaço marítimo que não lhe pertence.")

cuerpo_pt = "\n\n".join([
    DATELINE.format("Malvinas — Relatório GLOBALpatagonia"),
    "<p>Pouco se sabe na Argentina sobre o que aconteceu com o Argos Georgia. A notícia teve cobertura limitada nos grandes meios nacionais e o relatório oficial da Marine Accident Investigation Branch (MAIB) do Reino Unido —publicado 26 meses após o sinistro— passou quase despercebido para a opinião pública. No entanto, sua importância é enorme: não apenas documenta a morte de 13 pessoas, como expõe uma cadeia de negligências técnicas e operacionais e revela a fragilidade do controle que o Governo britânico das Ilhas Malvinas exerce sobre a atividade pesqueira no Atlântico Sul.</p>",
    "<h3>O que aconteceu: a sequência de uma catástrofe</h3>",
    "<p>O Argos Georgia era um palangreiro de 54 metros de comprimento, com bandeira de Santa Helena (um território britânico ultramarino) e operado pela empresa Argos Froyanes Limited, de capitais anglo-noruegueses. Navegava de Porto Stanley rumo aos pesqueiros de merluza-negra próximos à Geórgia do Sul com 27 tripulantes a bordo: dez espanhóis, oito russos, cinco indonésios, dois peruanos e dois uruguaios.</p>",
    map_block(IMG_MAPA, "Mapa do Atlântico Sul com o local do naufrágio do Argos Georgia, a leste das Ilhas Malvinas",
              "O Argos Georgia afundou a cerca de 190 milhas náuticas, quase 350 quilômetros, a leste de Porto Stanley."),
    "<p>Em 22 de julho de 2024, por volta das 13h00, a escotilha de alagem de linha (line hauling hatch) do costado de boreste, que deveria estar fechada, “abriu-se inesperadamente”, permitindo a entrada maciça de água. O relatório da MAIB determina que o mecanismo manual de fixação da comporta “provavelmente não havia sido aplicado” e que a tripulação não conseguiu fechá-la depois de aberta. Além disso, o mecanismo de acionamento da escotilha apresentava “uma fraqueza de projeto não identificada” e havia sido modificado sem seguir um processo formal de aprovação que permitisse detectar possíveis deficiências.</p>",
    "<p>A água se propagou rapidamente porque as portas estanques internas estavam abertas, uma prática que, segundo o relatório, comprometeu a estabilidade do navio. O Argos Georgia adernou progressivamente para boreste, perdeu a propulsão e finalmente afundou.</p>",
    "<h3>O atraso que custou vidas</h3>",
    "<p>Uma das conclusões mais contundentes do relatório é a relativa à resposta à emergência. A MAIB conclui que a tripulação não emitiu um alerta formal de socorro (Mayday) nas primeiras fases do sinistro. Em vez disso, o capitão comunicou-se primeiro por WhatsApp com outros barcos e com a empresa em terra.</p>",
    "<p>Segundo a reconstrução dos fatos, a água começou a entrar por volta das 13h00, mas o capitão só alertou por WhatsApp às 13h45. O alerta oficial de socorro só foi emitido por volta das 15h30, ou seja, quase duas horas e meia depois do início da inundação. O relatório assinala que essa comunicação informal “reduziu a compreensão inicial da gravidade do evento” e atrasou a ativação de uma resposta adequada, já que em terra se acreditava que a situação ainda podia ser “controlada ou estabilizada”.</p>",
    "<p>Esse atraso, segundo a MAIB, “reduziu a probabilidade de que os meios de resgate chegassem com luz do dia” e encurtou drasticamente a margem operacional para uma intervenção eficaz. Dos 27 tripulantes, 14 foram resgatados com vida e 13 morreram, alguns durante o abandono do navio e outros nas balsas salva-vidas, vítimas da exposição à água fria.</p>",
    "<h3>A sombra da ilegalidade: licenças sem segurança</h3>",
    "<p>O relatório da MAIB também dirigiu uma recomendação específica ao Governo das Ilhas Malvinas. Instou-o a melhorar sua capacidade de comunicações marítimas de busca e salvamento (SAR) para poder estabelecer um contato “direto e confiável” com os navios em perigo dentro de sua área de responsabilidade. Essa recomendação oficial confirma que o sistema de comunicações do centro coordenador de resgate das ilhas não foi suficientemente eficaz, fator que, somado ao atraso no alerta, contribuiu para o desfecho fatal.</p>",
    "<p>Mas a crítica vai além da resposta à emergência. O Argos Georgia operava sob uma licença de pesca concedida pelas autoridades britânicas das Ilhas Malvinas. O navio era um dos quatro beneficiados por uma extensão unilateral de licenças por parte da Grã-Bretanha no âmbito da CCRVMA (Comissão para a Conservação dos Recursos Vivos Marinhos Antárticos), um processo que, da perspectiva argentina, carece de toda legitimidade.</p>",
    "<p>O Governo argentino tem sido claro a respeito: as licenças concedidas pelo governo das ilhas são ilegais. Para pescar nas águas que cercam as Malvinas, os navios deveriam contar também com a autorização argentina, o que não ocorre. Essa situação não é um detalhe menor. Como assinalou o especialista em Atlântico Sul César Lerena, a atividade pesqueira na zona “viola não apenas a legislação argentina vigente (lei 24.922), mas também a Convenção das Nações Unidas sobre o Direito do Mar”, e significa para o país uma perda anual de cerca de 250.000 toneladas de recursos pesqueiros.</p>",
    "<h3>Um fato silenciado que expõe a fragilidade do controle das ilhas</h3>",
    "<p>Apesar da magnitude da tragédia e das contundentes conclusões do relatório oficial, na Argentina pouco se sabe sobre o que ocorreu com o Argos Georgia. A notícia teve cobertura limitada nos grandes meios nacionais, e o relatório da MAIB —publicado 26 meses após o sinistro— passou quase despercebido para a opinião pública. No entanto, sua importância é enorme, porque não apenas documenta a morte de 13 pessoas, como demonstra a impossibilidade de o governo das ilhas usufruir desse espaço marítimo sem oferecer as garantias mínimas de segurança.</p>",
    "<p>A recomendação da própria agência britânica ao Governo das Malvinas para que melhore suas comunicações SAR é uma admissão tácita de que o arquipélago não conta com os meios idôneos para coordenar um resgate de grande envergadura. A ausência de uma patrulha oceânica na zona, a dependência de navios pesqueiros privados para as tarefas de salvamento e o atraso na ativação da operação revelam um sistema de administração pesqueira que prioriza a arrecadação por licenças acima da vida dos tripulantes.</p>",
    "<p>Em outras palavras: o governo das ilhas se arroga o direito de conceder permissões de pesca em águas em disputa, mas não pode garantir a segurança de quem opera sob essas permissões. A tragédia do Argos Georgia é a prova mais eloquente de que esse usufruto unilateral é, além de ilegal, insustentável do ponto de vista humanitário.</p>",
    "<h3>Por que é importante hoje</h3>",
    "<p>A tragédia do Argos Georgia é muito mais do que um acidente marítimo. É a evidência mais crua de um sistema que prioriza a exploração de um recurso valioso —a merluza-negra— acima da segurança das pessoas que o extraem e da legalidade internacional.</p>",
    "<p>O relatório da MAIB, conhecido 26 meses após o sinistro, confirma que as falhas técnicas e a deficiente gestão da emergência foram determinantes. Mas também deixa à mostra uma pergunta incômoda: pode um governo que concede licenças de pesca em águas em disputa garantir a segurança de quem opera sob essas licenças? A resposta, à luz dos fatos e da recomendação oficial da própria agência britânica, parece ser negativa.</p>",
    "<p>Para a Argentina, o caso reforça uma posição histórica: a exploração dos recursos do Atlântico Sul sob um esquema de licenças unilateral não é apenas ilegal, como também gera um ambiente de risco para os trabalhadores do mar. Enquanto o Reino Unido e o governo das ilhas continuarem administrando a pesqueira sem um marco de cooperação com o Estado argentino, tragédias como a do Argos Georgia seguirão sendo uma possibilidade latente.</p>",
    "<p>A memória dos 13 tripulantes falecidos exige algo mais do que um relatório técnico. Exige uma revisão profunda de um modelo que, hoje, segue operando na ilegalidade e sem as garantias mínimas de segurança que qualquer atividade no mar deveria ter.</p>",
])

# ============================== 中文 ==============================
bajada_zh = ("2024年7月，一艘渔船在马尔维纳斯群岛斯坦利港以东约190海里（近350公里）处沉没，13名船员遇难。两年后，英国官方报告披露，这场悲剧本可避免："
             "存在技术故障、紧急应对中的疏忽，以及求救上的致命延误。这一事件在阿根廷几乎无人知晓，却表明岛上政府无法安全管理一片并不属于它的海域。")

cuerpo_zh = "\n\n".join([
    DATELINE.format("马尔维纳斯 — GLOBALpatagonia 深度报道"),
    "<p>在阿根廷，人们对“阿尔戈斯·乔治亚”号（Argos Georgia）发生了什么知之甚少。这一消息在阿根廷主流媒体上的报道有限，英国海事事故调查局（MAIB）的官方报告——在事故发生26个月后才公布——也几乎没有引起公众注意。然而，它的重要性不容小觑：它不仅记录了13人的死亡，还揭示了一连串技术与操作上的疏忽，并暴露出英国马尔维纳斯群岛政府对南大西洋渔业活动的管控是多么脆弱。</p>",
    "<h3>发生了什么：一场灾难的经过</h3>",
    "<p>“阿尔戈斯·乔治亚”号是一艘54米长的延绳钓渔船，悬挂圣赫勒拿（英国海外领地）旗帜，由英挪合资的Argos Froyanes Limited公司运营。该船从斯坦利港出发，前往南乔治亚岛附近的犬牙鱼（巴塔哥尼亚犬牙鱼）渔场，船上共有27名船员：10名西班牙人、8名俄罗斯人、5名印度尼西亚人、2名秘鲁人和2名乌拉圭人。</p>",
    map_block(IMG_MAPA, "南大西洋地图，标出“阿尔戈斯·乔治亚”号在马尔维纳斯群岛以东的沉没位置",
              "“阿尔戈斯·乔治亚”号在斯坦利港以东约190海里（近350公里）处沉没。"),
    "<p>2024年7月22日13:00左右，右舷的起线舱口（line hauling hatch）本应处于关闭状态，却“意外开启”，大量海水涌入。MAIB报告认定，舱门的手动锁定装置“很可能没有锁上”，且舱口一旦打开，船员便无法将其关闭。此外，舱口的驱动机构存在“未被发现的设计缺陷”，并且曾在未经正式审批程序的情况下被改装，因而无法发现潜在隐患。</p>",
    "<p>由于内部水密门敞开，海水迅速蔓延；报告指出，这种做法损害了船舶的稳性。“阿尔戈斯·乔治亚”号逐渐向右舷倾斜，失去动力，最终沉没。</p>",
    "<h3>夺走生命的延误</h3>",
    "<p>报告中最有力的发现之一，是关于应急响应。MAIB得出结论：在事故初期，船员没有发出正式的遇险求救信号（Mayday）。相反，船长先是通过WhatsApp联系了其他船只和岸上的公司。</p>",
    "<p>根据事件重建，海水大约在13:00开始进入船体，但船长直到13:45才通过WhatsApp发出警报。正式的遇险警报直到接近15:30才发出，也就是进水开始近两个半小时之后。报告指出，这种非正式的联络“降低了对事态严重性的初步认识”，延误了适当响应的启动，因为岸上认为局势仍可以被“控制或稳定”。</p>",
    "<p>MAIB认为，这一延误“降低了救援力量在白天抵达的可能性”，并大幅压缩了有效施救的行动空间。27名船员中，14人获救生还，13人遇难，有的在弃船过程中，有的在救生筏上，死于低温海水的暴露。</p>",
    "<h3>非法的阴影：有许可，无安全</h3>",
    "<p>MAIB报告还向马尔维纳斯群岛政府提出了一项具体建议：敦促其提高海上搜救（SAR）通信能力，以便与其责任区内遇险船只建立“直接且可靠”的联系。这一官方建议证实，岛上救援协调中心的通信系统不够有效，再加上警报延误，促成了致命的结局。</p>",
    "<p>但批评不止于应急响应。“阿尔戈斯·乔治亚”号是凭英国马尔维纳斯群岛当局颁发的捕鱼许可证作业的。该船是英国在CCAMLR（南极海洋生物资源养护委员会）框架下单方面延长许可证的四艘船之一，而从阿根廷的角度看，这一程序毫无合法性可言。</p>",
    "<p>阿根廷政府对此态度明确：岛上政府颁发的许可证是非法的。要在马尔维纳斯周边海域捕鱼，船只还应获得阿根廷的授权，而这并未发生。这并非小事。正如南大西洋问题专家塞萨尔·莱雷纳（César Lerena）所指出的，该海域的捕捞活动“不仅违反阿根廷现行法律（第24.922号法），也违反《联合国海洋法公约》”，使阿根廷每年损失约25万吨渔业资源。</p>",
    "<h3>一起被沉默的事件，暴露了岛上管控的脆弱</h3>",
    "<p>尽管这场悲剧规模巨大，官方报告的结论也很有分量，但在阿根廷，人们对“阿尔戈斯·乔治亚”号的遭遇仍知之甚少。这一消息在阿根廷主流媒体上的报道有限，MAIB的报告——事故26个月后才公布——也几乎没有引起公众注意。然而，它的重要性不容小觑，因为它不仅记录了13人的死亡，还表明岛上政府根本无法在不提供最基本安全保障的情况下使用这片海域。</p>",
    "<p>英国这一机构亲自建议马尔维纳斯政府改善其SAR通信，这等于默认该群岛不具备协调大规模救援的适当手段。该海域没有远洋巡逻船，救援任务依赖私人渔船，行动启动又有延误，这些都暴露出一种渔业管理体系：把许可证收入置于船员生命之上。</p>",
    "<p>换句话说：岛上政府擅自在争议海域颁发捕鱼许可，却无法保证在这些许可下作业者的安全。“阿尔戈斯·乔治亚”号的悲剧最有力地证明，这种单方面的开发不仅非法，而且从人道角度也是不可持续的。</p>",
    "<h3>为什么今天仍然重要</h3>",
    "<p>“阿尔戈斯·乔治亚”号的悲剧远不止是一起海难。它是一个体制最赤裸的证据：这一体制把开发一种珍贵资源——犬牙鱼——置于捕捞者的安全和国际法之上。</p>",
    "<p>MAIB的报告在事故26个月后公之于众，证实技术故障和应急管理不善是决定性因素。但它也抛出了一个令人不安的问题：一个在争议海域颁发捕鱼许可证的政府，能否保证在这些许可下作业者的安全？鉴于事实和英国这一机构自身的官方建议，答案似乎是否定的。</p>",
    "<p>对阿根廷而言，此案强化了其一贯立场：在单方面许可制度下开发南大西洋资源，不仅非法，还给海员带来风险环境。只要英国和岛上政府继续在没有与阿根廷国家合作框架的情况下管理这片渔业，类似“阿尔戈斯·乔治亚”号的悲剧就仍可能再次发生。</p>",
    "<p>13名遇难船员的记忆，需要的不仅是一份技术报告。它要求对一种模式进行深入审视——这种模式至今仍在非法状态下运行，缺乏任何海上活动本应具备的最基本安全保障。</p>",
])

nueva_entrada = {
    "id": "20261027-propio-argos-georgia",
    "titulo": "Argos Georgia: la tragedia que expone al Gobierno británico de las Islas Malvinas",
    "bajada": bajada_es,
    "cuerpo": cuerpo,
    "titulo_en": "Argos Georgia: the tragedy that exposes the British Government of the Malvinas Islands",
    "bajada_en": bajada_en,
    "cuerpo_en": cuerpo_en,
    "titulo_pt": "Argos Georgia: a tragédia que expõe o Governo britânico das Ilhas Malvinas",
    "bajada_pt": bajada_pt,
    "cuerpo_pt": cuerpo_pt,
    "titulo_zh": "“阿尔戈斯·乔治亚”号：暴露英国马尔维纳斯群岛政府的悲剧",
    "bajada_zh": bajada_zh,
    "cuerpo_zh": cuerpo_zh,
    "tag": "🇦🇷 Malvinas",
    "categoria": "malvinas|pesca|internacional",
    "fuente": "GLOBALpatagonia",
    "autor": "M. Galindo",
    "propio": True,
    "url_original": "",
    "pais": "malvinas",
    "imagen": IMG_PORTADA,
    "imagen_keywords": "argos georgia buque palangrero naufragio malvinas merluza negra MAIB",
    "hashtags_en": "#Malvinas #ArgosGeorgia #Fishing #SouthAtlantic #MAIB",
    "meta": "Informe · GLOBALpatagonia",
    "fecha": "2026-10-27",
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
