import os
os.system("cls")
import time

def centralizar(texto):
    print(texto.center(180))

def boas_vindas():
    centralizar("Bem-vindo(a) ao programa")
    time.sleep(0.5)
    centralizar("✬ Voz Do Amanhã ✬")
    print("")
    time.sleep(1)
    centralizar("Pronto(a) para descobrir novos caminhos? Comece agora!")
    print("")
    time.sleep(1)
    centralizar("Descubra mais sobre seus interesses, habilidades e preferências através deste Teste Vocacional.")
    print("")
    time.sleep(1)
    centralizar("Agora responda as perguntas com sinceridade e veja quais áreas mais combinam com o seu perfil:")

def perguntas():
    time.sleep(1)
    centralizar("Instrução: Escolha a alternativa que mais se identifica. Não existe resposta certa ou errada.")
    time.sleep(0.5)
    print("")
    print("                                                                                         ╱")
    print("                                                                                        ╱")
    time.sleep(0.5)
    print("                                                                                       ╱")
    print("                                                                                      ╱")
    time.sleep(0.5)
    print("                                                                                     ╱")
    print("                                                                                    ╱")
    time.sleep(0.5)
    print("                                                                                  ⬋")
    time.sleep(0.5)
    respostas = []
    while len(respostas) < 50:
        numero = len(respostas) + 1
        if numero == 1:
            pergunta = input("1. Quando você recebe uma tarefa grande, normalmente prefere:\n"
                              "A) Pesquisar informações antes de começar.\n"
                              "B) Pensar em maneiras criativas de apresentar o resultado.\n"
                              "C) Organizar as etapas e definir prioridades.\n"
                              "D) Analisar os recursos e custos necessários.\n"
                              "E) Pensar em como as pessoas envolvidas podem colaborar.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 2:
            pergunta = input("2. Em um trabalho em grupo, você costuma assumir o papel de:\n"
                              "A) Pessoa responsável pela parte lógica e recursiva.\n"
                              "B) Pessoa que traz ideias diferentes.\n"
                              "C) Pessoa que organiza e coordena o trabalho.\n"
                              "D) Pessoa que promove as interações com compreensão/respeito mútuo na equipe.\n"
                              "E) Pessoa que pesquisa e reúne informações.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 3:
            pergunta = input("3. Qual atividade parece mais interessante?\n"
                              "A) Investigar uma história e produzir uma reportagem.\n"
                              "B) Criar uma campanha para uma marca.\n"
                              "C) Gerenciar uma empresa.\n"
                              "D) Analisar investimentos e resultados financeiros.\n"
                              "E) Selecionar e desenvolver funcionários.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 4:
            pergunta = input("4. Quando ocorre um conflito entre duas pessoas, você tende a:\n"
                              "A) Avaliar objetivamente os fatos envolvidos.\n"
                              "B) Conversar para encontrar uma forma de comunicação melhor.\n"
                              "C) Procurar uma solução prática.\n"
                              "D) Investigar o que realmente aconteceu.\n"
                              "E) Tentar entender os dois lados emocionalmente.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 5:
            pergunta = input("5. Qual matéria seria sua favorita?\n"
                              "A) Matemática.\n"
                              "B) Português.\n"
                              "C) Sociologia/Filosofia.\n"
                              "D) Artes.\n"
                              "E) Ciências.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 6:
            pergunta = input("6. Quais hobbies a seguir você costuma praticar/preferir?\n"
                              "A) Leitura e Escrita.\n"
                              "B) Dança e canto.\n"
                              "C) Jardinagem e Esportes.\n"
                              "D) Cozinhar e Viajar.\n"
                              "E) Fazer compras e usar redes sociais.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 7:
            pergunta = input("7. O que seria mais importante para você em uma carreira: \n"
                              "A) Estabilidade.\n"
                              "B) Reconhecimento.\n"
                              "C) Crescimento.\n"
                              "D) Salário.\n"
                              "E) Propósito.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 8:
            pergunta = input("8. Ao receber uma informação importante, você normalmente:\n"
                              "A) Verifica se ela é verdadeira e de onde veio.\n"
                              "B) Imagina maneiras diferentes de contar sobre ela\n"
                              "C) Pensa em como utilizá-la da melhor maneira.\n"
                              "D) Analisa suas possíveis e prováveis consequências lógicas.\n"
                              "E) Pensa em como ela pode afetar as pessoas envolvidas.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 9:
            pergunta = input("9. Qual dessas responsabilidades pessoais você acha melhor?\n"
                              "A) Cuidar do próprio dinheiro.\n"
                              "B) Escrever textos, mensagens ou anotações todos os dias.\n"
                              "C) Manter seus materiais, espaço ou objetos organizados.\n"
                              "D) Responder mensagens e manter conversas em dia.\n"
                              "E) Cuidar de alguém que não está se sentindo bem.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 10:
            pergunta = input("10. Com quais aspectos você se sente menos confortável trabalhando diariamente?\n"
                              "A) Matemática e Computadores.\n"
                              "B) Leitura e Escrita.\n"
                              "C) Empresas e Negócios.\n"
                              "D) Substâncias e Produção.\n"
                              "E) Pessoas e Conversas longas.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 11:
            pergunta = input("11. Você preferiria trabalhar de qual das seguintes maneiras?\n"
                              "A) Remotamente.\n"
                              "B) Viajando constantemente com horários flexíveis.\n"
                              "C) Em um único local com horários fixos bem estabelecidos.\n"
                              "D) Presencialmente.\n"
                              "E) Híbrido (Presencialmente e Remotamente).\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 12:
            pergunta = input("12. Se sua empresa estivesse com problemas internos, você priorizaria:\n"
                              "A) Pesquisar informações sobre o problema.\n"
                              "B) Elaborar uma nova estratégia de comunicação.\n"
                              "C) Analisar seus processos e propor melhorias.\n"
                              "D) Verificar os impactos referentes às finanças.\n"
                              "E) Conversar com os funcionários para entender certos problemas.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 13:
            pergunta = input("13. Qual ambiente de trabalho parece mais adequado para você?\n"
                              "A) Ambiente organizado, geralmente com atividades administrativas, planejamento, comunicação e uso de computadores.\n"
                              "B) Local mais voltado à criação, desenvolvimento de ideias, comunicação e produção de conteúdos.\n"
                              "C) Espaço voltado ao aprendizado, à troca de conhecimentos e ao acompanhamento de pessoas..\n"
                              "D) Espaço com contato frequente com pessoas, organização de atividades e prestação de serviços.\n"
                              "E) Local voltado ao cuidado, atendimento e acompanhamento das necessidades das pessoas.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 14:
            pergunta = input("14. Quando precisa convencer alguém sobre uma ideia, você:\n"
                              "A) Aponta dados e argumentos objetivos.\n"
                              "B) Apresenta uma narrativa envolvente.\n"
                              "C) Explica como a ideia pode melhorar situações.\n"
                              "D) Recorre a algum apelo visual relevante.\n"
                              "E) Demonstra como a ideia beneficiará as pessoas.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 15:
            pergunta = input("15. Quais dos seguintes gêneros você prefere consumir?\n"
                              "A) Documentários e Enredos Históricos.\n"
                              "B) Comédia e Aventura.\n"
                              "C) Suspense e Ação.\n"
                              "D) Ficção científica e Fantasia.\n"
                              "E) Drama e Romance.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 16:
            pergunta = input("16. Você se identifica mais com o papel de:\n"
                              "A) Pesquisador.\n"
                              "B) Comunicador.\n"
                              "C) Líder.\n"
                              "D) Desenvolvedor.\n"
                              "E) Assistente.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 17:
            pergunta = input("17. Se você recebesse uma grande quantidade de documentos, preferiria:\n"
                              "A) Procurar informações importantes neles.\n"
                              "B) Transformar as informações em um conteúdo interessante.\n"
                              "C) Organizar e classificar os documentos.\n"
                              "D) Identificar as relevâncias econõmicas e numéricas.\n"
                              "E) Analisar possíveis consequências informacionais.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 18:
            pergunta = input("18. Conseguiria trabalhar melhor sob qual extremo?\n"
                              "A) Sob isolamento total e sem ajuda de terceiros.\n"
                              "B) Sob o olhar julgamento de multidões..\n"
                              "C) Sob pressão momentânea e recorrente.\n"
                              "D) Sob prazos bastante apertados.\n"
                              "E) Sob constantes críticas construtivas e redirecionamentos.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 19:
            pergunta = input("19. Qual dilema parece mais fácil de resolver?\n"
                              "A) Você precisa escolher entre várias opções e não sabe qual é melhor.\n"
                              "B) Algo que você estava planejando dá errado de última hora.\n"
                              "C) Você percebe que esqueceu de fazer algo que tinha combinado.\n"
                              "D) Seu celular está quase sem bateria e você ainda precisa sair.\n"
                              "E) Você precisa resolver alguma coisa, mas não sabe por onde começar.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 20:
            pergunta = input("20. Dois familiares brigaram sério, o clima ficou tenso e ninguém sabe como resolver a situação. O que você faria?\n"
                              "A) Conversaria com todos para entender o que aconteceu antes de qualquer coisa.\n"
                              "B) Procuraria uma solução prática para ajudar a resolver o problema o mais rápido possível.\n"
                              "C) Daria espaço para as pessoas se acalmarem e evitaria me envolver diretamente.\n"
                              "D) Procuraria alguém de confiança para pedir orientação sobre como lidar com a situação.\n"
                              "E) Tentaria acalmar os envolvidos e ajudá-los a chegar a um acordo.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 21:
            pergunta = input("21. Qual desses desafios parece mais estimulante?\n"
                              "A) Estar em uma cidade desconhecida e precisar encontrar sozinho(a) um lugar específico, sem internet.\n"
                              "B) Encontrar um objeto desconhecido que parece ter alguma utilidade, mas sem saber para que serve.\n"
                              "C) Ficar responsável por organizar uma pequena atividade para um grupo de pessoas, mas com poucas instruções.\n"
                              "D) Receber uma quantia inesperada de dinheiro e precisar decidir como utilizá-la sem poder gastar tudo de uma vez.\n"
                              "E) Durante um passeio em grupo, acontecer um imprevisto e todos começarem a dar opiniões diferentes sobre o que fazer.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 22:
            pergunta = input("22. Se precisasse apresentar um projeto, você enfatizaria o uso de:\n"
                              "A) Gráficos e estatísticas.\n"
                              "B) Imagens e elementos visuais.\n"
                              "C) Apresentação de objetivos, etapas e resultados.\n"
                              "D) Narrativas para prender a atenção.\n"
                              "E) Explicação dos benefícios para as pessoas.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 23:
            pergunta = input("23. O que você faria se percebesse que um amigo está desmotivado?\n"
                              "A) Conversaria com ele para entender o que está acontecendo e tentaria ajudá-lo a encontrar uma solução.\n"
                              "B) Contaria alguma experiência ou ideia que pudesse ajudá-lo a enxergar a situação por outro ponto de vista.\n"
                              "C) Perguntaria quais são as dificuldades dele e ajudaria a organizar os próximos passos para resolver a situação.\n"
                              "D) Tentaria animá-lo propondo alguma atividade diferente para mudar um pouco o clima..\n"
                              "E) Ouviria com atenção, sem pressioná-lo, e procuraria entender como ele está se sentindo.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 24:
            pergunta = input("24. Qual/quais dos benefícios abaixo você preferiria?\n"
                              "A) Horário flexível\n"
                              "B) Viagens, eventos e experiências remuneradas\n"
                              "C) Trabalho remoto ou híbrido.\n"
                              "D) Cursos/capacitações pagos pela empresa\n"
                              "E) Plano de saúde e programas de bem-estar\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 25:
            pergunta = input("25. Quando você precisa aprender algo novo, seu método costuma ser:\n"
                              "A) Ler livros sobre o assunto e fazer profundas anotações.\n"
                              "B) Buscar por um aprendizado mais prático.\n"
                              "C) Organizar o conteúdo em etapas estruturadas e objetivas.\n"
                              "D) Analisar estatísticas e parte lógica do assunto.\n"
                              "E) Relacionar o conteúdo com situações reais e sociais.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 26:
            pergunta = input("26. Para você, seria melhor construir carreira em: \n"
                              "A) Órgão público.\n"
                              "B) Trabalhar por conta própria.\n"
                              "C) Uma grande empresa\n"
                              "D) Pequena empresa.\n"
                              "E) Instituição de ensino.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 27:
            pergunta = input("27. Se uma empresa lançasse um produto novo, você preferiria:\n"
                              "A) Estudar as reações e comportamento do público.\n"
                              "B) Criar a campanha de divulgação.\n"
                              "C) Planejar a estratégia de lançamento.\n"
                              "D) Analisar os custos e possíveis lucros.\n"
                              "E) Produzir conteúdos sobre o produto.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 28:
            pergunta = input("28. Qual costuma ser sua primeira ação ao fazer uma compra?\n"
                              "A) Pesquiso avaliações de outras pessoas.\n"
                              "B) Comparo os preços antes de escolher.\n"
                              "C) Analiso os prós e contras de cada opção.\n"
                              "D) Verifico meu orçamento antes de comprar.\n"
                              "E) Comparo a qualidade e o custo-benefício dos produtos.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 29:
            pergunta = input("29. Quando alguém apresenta uma opinião diferente da sua, você tende a:\n"
                              "A) Apresentar argumentos baseados em fatos.\n"
                              "B) Pensar em uma abordagem diferente sobre o assunto.\n"
                              "C) Optar por um lado de concordância em comum.\n"
                              "D) Observar os impactos das opiniões sobre o assunto.\n"
                              "E) Procurar entender os motivos da pessoa.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 30:
            pergunta = input("30. Qual atividade você gostaria de realizar em um projeto?\n"
                              "A) Pesquisar informações sobre o tema.\n"
                              "B) Criar o conceito visual.\n"
                              "C) Gerenciar as etapas e responsabilidades.\n"
                              "D) Analisar e organizar o orçamento.\n"
                              "E) Trabalhar diretamente com os participantes.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 31:
            pergunta = input("31. Sobre universidade e direcionamento profissional, qual proposta abaixo instiga mais seu interesse?\n"
                              "A) Um curso bastante teórico com diversas opções de especialização e de longa duração.\n"
                              "B) Um curso mais prática e objetivo com uma duração curta ou média.\n"
                              "C) Um curso longo porém objetivo e com perspectiva de crescimento profissional constante.\n"
                              "D) Um curso curto bastante específico com um alinhamento profissional direto. \n"
                              "E) Um curso de duração média/curta com liberdade de migração profissional durante os estudos ou carreira.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 32:
            pergunta = input("32. Imagine que você precise melhorar um serviço. O que faria primeiro?\n"
                              "A) Pesquisaria como o serviço funciona atualmente.\n"
                              "B) Criaria uma nova forma de apresentar o serviço.\n"
                              "C) Organizaria um plano de melhorias.\n"
                              "D) Analisaria os custos envolvidos.\n"
                              "E) Conversaria com os usuários.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 33:
            pergunta = input("33. Daqui a dez anos, você se vê: \n"
                              "A) Ocupando uma posição de responsabilidade, liderando projetos/equipes, com crescimento constante e assumindo novos desafios.\n"
                              "B) Trabalhando com atividades incomuns, desenvolvendo projetos pessoais e hobbies próprios com uma rotina profissional menos convencional.\n"
                              "C) Com casa própria, estabilidade financeira e bastante tempo para família/amigos.\n"
                              "D) Trabalhando por conta própria ou em um modelo flexível, com horários próprios e escolhendo em quais projetos trabalha.\n"
                              "E) Viajando algumas vezes ao ano, conhecendo lugares diferentes e com uma rotina mais imprevisível.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 34:
            pergunta = input("34. Qual dessas propostas mais te atrai? \n"
                              "A) Itaú te oferece trabalho para: Conferir dados, acompanhar resultados, organizar informações financeiras e auxiliar na análise de operações.\n"
                              "B) Canva te oferece trabalho para: Criar materiais visuais, desenvolver ideias, trabalhar com layouts e participar da criação de novos conteúdos.\n"
                              "C) Ambev te oferece trabalho para: Acompanhar resultados, organizar processos, analisar metas e auxiliar no planejamento de atividades.\n"
                              "D) Fleury te oferece trabalho para: Realizar ou acompanhar exames, organizar informações de pacientes, utilizar equipamentos e colaborar com a equipe de saúde.\n"
                              "E) Natura te oferece trabalho para: Apoiar colaboradores, organizar treinamentos, acompanhar equipes e auxiliar em processos de desenvolvimento.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 35:
            pergunta = input("35. A melhor opção de companhia profissional seria: \n"
                              "A) Computadores e aparelhos tecnológicos.\n"
                              "B) Livros e/ou papelada.\n"
                              "C) Natureza e/ou Arquiteturas.\n"
                              "D) Substâncias e/ou fórmulas.\n"
                              "E) Pessoas e/ou animais.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 36:
            pergunta = input("36. Em qual tipo de inteligência você costuma se destacar mais?\n"
                              "A) Inteligência acadêmica.\n"
                              "B) Inteligência criativa.\n"
                              "C) Inteligência financeira.\n"
                              "D) Inteligência social.\n"
                              "E) Inteligência emocional.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 37:
            pergunta = input("37. Ao organizar um evento, você se preocuparia principalmente com:\n"
                              "A) O planejamento geral do evento.\n"
                              "B) A apresentação e identidade visual do evento.\n"
                              "C) A divulgação do evento.\n"
                              "D) O orçamento do evento.\n"
                              "E) A experiência das pessoas no evento.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 38:
            pergunta = input("38. Qual dessas situações seria mais estimulante para você?\n"
                              "A) Descobrir algo que poucas pessoas conhecem.\n"
                              "B) Inventar algo esteticamente marcante.\n"
                              "C) Desenvolver uma solução para melhorar uma organização.\n"
                              "D) Encontrar uma maneira de aumentar/melhorar resultados.\n"
                              "E) Guiar alguém em uma importante tomada de decisão.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 39:
            pergunta = input("39. Quando você recebe um problema complexo, normalmente:\n"
                              "A) Separa o problema em partes.\n"
                              "B) Tenta uma abordagem menos convencional.\n"
                              "C) Procura entender as partes envolvidas.\n"
                              "D) Avalia possíveis resultados.\n"
                              "E) Recorre a analisar casos semelhantes.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 40:
            pergunta = input("40. Pior cenário possível para você: \n"
                              "A) Picada de cobra em um desconhecido(a) ao seu lado e você é o(a) único(a) por perto.\n"
                              "B) Um trabalho escolar manual que você passou dias fazendo é arruinado e você precisa refazer do zero.\n"
                              "C) Viajem que acaba saindo completamente do planejado.\n"
                              "D) Aniversário surpresa com várias grupos de pessoas diferentes com a atenção voltada a você.\n"
                              "E) Um discussão terrível ocorre na mesa ao lado em um restaurante e pedem para você intervir.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 41:
            pergunta = input("41. Seu carro quebrou no meio da estrada. Você: \n"
                              "A) Sentiria um pouco de raiva mas iria verificar o que aconteceu para achar uma forma de resolver o problema por conta própria.\n"
                              "B) Manteria a calma, analisaria as opções disponíveis e escolheria a alternativa mais segura.\n"
                              "C) Me apressaria em procurar um serviço de assistência ou alguém que pudesse resolver o problema rapidamente.\n"
                              "D) Surtaria um pouco primeiro mas logo aproveitaria a situação para improvisar uma solução até conseguir ajuda.\n"
                              "E) Ligaria nervosamente para alguém de confiança e pediria ajuda para decidir o que fazer.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 42:
            pergunta = input("42. Qual das abaixo você considera sua melhor qualidade: \n"
                              "A) Organização.\n"
                              "B) Criatividade.\n"
                              "C) Determinação.\n"
                              "D) Comunicação.\n"
                              "E) Empatia.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 43:
            pergunta = input("43. Imagine que você trabalhe em uma empresa. Qual atividade escolheria?\n"
                              "A) Controlar indicadores financeiros.\n"
                              "B) Produzir materiais de comunicação.\n"
                              "C) Elaborar estratégias de crescimento.\n"
                              "D) Criar projetos visuais.\n"
                              "E) Desenvolver ações para os funcionários.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 44:
            pergunta = input("44. Qual encontro parece você optaria por planejar?\n"
                              "A) Jantar em um restaurante novo.\n"
                              "B) Visita a uma exposição artística, literária ou cinematográfica.\n"
                              "C) Passeio ao ar livre.\n"
                              "D) Fazer uma pequena viagem a dois.\n"
                              "E) Ir a um evento, show ou apresentação.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 45:
            pergunta = input("45. Quando trabalha em algo importante, prefere:\n"
                              "A) Trabalhar com informações concretas.\n"
                              "B) Trabalhar com liberdade para desenvolvimento diversificado.\n"
                              "C) Trabalhar com metas e objetivos bem definidos.\n"
                              "D) Trabalhar analisando logística e resultados.\n"
                              "E) Trabalhar com a ajuda de outras pessoas.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 46:
            pergunta = input("46. Em um trabalho em grupo, sua maior contribuição seria:\n"
                              "A) Garantir bons resultados.\n"
                              "B) Encontrar novas ideias para incrementar o trabalho.\n"
                              "C) Catalogar as tarefas.\n"
                              "D) Desenvolver/coordenar as habilidades dos integrantes.\n"
                              "E) Manter uma boa comunicação entre todos.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 47:
            pergunta = input("47. Escolha um animal de estimação cujas responsabilidades e cuidados mais te agradem: \n"
                              "A) Peixe: Alimentação regular, limpeza do aquário e cuidados com o ambiente.\n"
                              "B) Pássaro: Limpeza da gaiola, interação e alguns momentos de liberdade.\n"
                              "C) Tartaruga: Limpeza do espaço e manutenção das condições adequadas do ambiente.\n"
                              "D) Gato: Cuidados básicos e bastante autonomia durante o dia.\n"
                              "E) Cachorro: Passeios constantes, treinamento comportamental e bastante interação.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 48:
            pergunta = input("48. Qual desses esportes você teria mais vontade de praticar?\n"
                              "A) Corrida.\n"
                              "B) Artes marciais\n"
                              "C) Futebol.\n"
                              "D) Natação.\n"
                              "E) Vôlei.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 49:
            pergunta = input("49. Se você tivesse que escolher viver a rotina profissional de um personagem, seria:\n"
                              "A) Hermione Granger.\n"
                              "B) Tony Stark.\n"
                              "C) Peter Parker.\n"
                              "D) Sherlock Holmes.\n"
                              "E) Meredith Grey.\n\n"
                              "Resposta: ").strip().upper()
        elif numero == 50:
            pergunta = input("50. Pensando no futuro, qual estrutura familiar mais lhe atrai?\n"
                              "A) Casal sem filhos - Parceiro(a), dividindo responsabilidades e visões de vida a dois.\n"
                              "B) Casal com pets - Parceiro(a) e Animais de estimação, uma vida alegre com companhia humana e animal.\n"
                              "C) Família tradicional - Parceiro(a), Filhos e Rotina familiar feliz e estável.\n"
                              "D) Vida solteira e independente - Morar sozinho(a), mantendo a própria privacidade e estilo de vida único.\n"
                              "E) Família grande - Com parceiro(a) ou sem, mas estando perto de familiares para conviver com estilo de comunidade.\n\n"
                              "Resposta: ").strip().upper()
        if pergunta not in ("A", "B", "C", "D", "E"):
            print("Resposta inválida: Por favor, informe apenas a letra da alternativa escolhida.")
            print("")
            continue
        respostas.append(pergunta)
        print("")
    return respostas

nomes_perfis = {"A": "Pesquisa e Investigação", "B": "Criatividade e Comunicação", "C": "Gestão e Organização", "D": "Lógica e Análise", "E": "Social e Empatia"}

def calcular_perfis(respostas):
    analisando_perfil = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for resposta in respostas:
        analisando_perfil[resposta] += 1
    perfil_principal = max(analisando_perfil, key=analisando_perfil.get)
    return analisando_perfil, perfil_principal

def calcular_areas(respostas):
    pontuacao = {"Pesquisa / Investigação": 0, "Criatividade / Comunicação": 0, "Gestão / Organização": 0, "Lógica / Análise": 0, "Social / Empatia": 0}
    relacao = {"A": "Pesquisa / Investigação", "B": "Criatividade / Comunicação", "C": "Gestão / Organização", "D": "Lógica / Análise", "E": "Social / Empatia"}
    for resposta in respostas:
        if resposta in relacao:
            perfil = relacao[resposta]
            pontuacao[perfil] += 1
    ranking = sorted(pontuacao.items(), key=lambda item: item[1], reverse=True)

    centralizar("🔍 A N A L I S A N D O 🔍")
    print("")
    time.sleep(1)
    centralizar("        🔍 5 🔍          ")
    print("")
    time.sleep(1)
    centralizar("        🔍 4 🔍          ")
    print("")
    time.sleep(1)
    centralizar("        🔍 3 🔍          ")
    print("")
    time.sleep(1)
    centralizar("        🔍 2🔍           ")
    print("")
    time.sleep(1) 
    centralizar("        🔍 1 🔍          ")
    print("")
    time.sleep(1)
    centralizar("🎊  C O N C L U Í D O  🎊 ")
    time.sleep(0.5)
    print("")
    centralizar("Agora cheque os resultados abaixo.")
    time.sleep(0.5)
    print("")
    centralizar("⬇️   H A B I L I D A D E S  ⬇️")
    time.sleep(0.5)
    print("")
    for perfil, pontos in ranking:
        centralizar(f"{perfil}: {pontos} pontos")
        print("")
        time.sleep(1)
    return pontuacao

def resultado(analisando_perfil, pontuacao_areas):
    perfil_principal = max(analisando_perfil, key=analisando_perfil.get)
    areas_ordenadas = sorted(pontuacao_areas.items(), key=lambda item: item[1], reverse=True)
    melhores_areas = areas_ordenadas[:3]
    print("")
    centralizar("⬇️   R E S U L T A D O  ⬇️")
    print("")
    centralizar(f"Seu perfil predominante é: ♕ {nomes_perfis[perfil_principal]} ♕")
    print("")
    time.sleep(1)

def conselho_final():
    print("")
    centralizar("⚠️  A T E N Ç Ã O  ⚠️")
    print("")
    centralizar("Independentemente de qualquer resultado, lembre-se de que o mais importante é:")
    centralizar("encontar um caminho que faça a ponte entre cérebro e coração.")
    centralizar("Escolher um curso ou carreira não precisa definir toda a sua vida.")
    centralizar("Use este momento para se conhecer, explorar possibilidades e descobrir")
    centralizar("caminhos que façam sentido para você!")
    #código feito por Sabrina Roberta 

boas_vindas()
respostas = perguntas()
analisando_perfil, perfil_principal = calcular_perfis(respostas)
pontuacao_areas = calcular_areas(respostas)
melhores_areas = resultado(analisando_perfil, pontuacao_areas)
conselho_final()