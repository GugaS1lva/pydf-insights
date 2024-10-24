from fpdf import FPDF

# Função para criar um PDF com formatações
def criar_pdf(titulo_pdf, conteudo):
    # Criando um objeto PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Adicionando uma página
    pdf.add_page()
    
    # Título principal
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 10, "RESUMO DA AULA\n" + titulo_pdf, align='C')
    pdf.ln(2)  # Adiciona um pequeno espaçamento
    
    # Linha horizontal após o título
    pdf.set_line_width(0.5)
    pdf.line(10, 33, 200, 33)
    pdf.ln(10)

    # Conteúdo do PDF
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, conteudo)

    # Linha horizontal no final
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    # Salvando o PDF com o nome escolhido
    nome_arquivo = titulo_pdf.replace(" ", "_") + ".pdf"
    pdf.output(nome_arquivo)

# Textos para o conteúdo do PDF
titulo = "O Pilar do Planejamento no DevQuest"
conteudo = """1.2 - O Pilar do Planejamento no DevQuest

Introdução
O planejamento é um dos pilares mais importantes para quem deseja evoluir rapidamente na carreira de desenvolvimento de software. Infelizmente, muitas vezes, ele é negligenciado. Neste capítulo, vamos explicar por que um bom planejamento é essencial e como ele pode ser a chave para seu sucesso.
Um ditado interessante, que resume bem essa questão, diz que não adianta ser o corredor mais rápido se você estiver correndo na direção errada. Muitos iniciantes estão cheios de vontade, mas acabam investindo seu tempo e energia em áreas que não trarão o retorno esperado.

Por Que o Planejamento é Essencial?
A falta de planejamento é uma das principais razões pelas quais muitos perdem tempo no início de suas carreiras. Imagine começar a aprender uma linguagem de programação sem saber onde ela será aplicada ou se há vagas no mercado para iniciantes nessa área. Sem uma visão clara e um planejamento bem estruturado, muitos correm o risco de seguir por um caminho que não trará os resultados desejados.
Nosso objetivo com o curso DevQuest é oferecer essa clareza para você desde o início. Queremos que você entenda o que deve ser aprendido, onde aplicar esse conhecimento e como otimizar seu tempo para alcançar o mercado de trabalho mais rapidamente.

O Pulo Direto para a Prática
É comum ver pessoas querendo pular diretamente para a parte prática, o famoso "mão na massa". Mas, assim como tocar uma música sem aprender os acordes ou a posição correta dos dedos em um instrumento musical, isso pode se tornar um desafio muito maior sem uma base sólida.
Entender a base é o que permitirá que você progrida de forma mais consistente e eficiente. No DevQuest, você tem mentores que te guiarão ao longo de todo o processo, fornecendo a orientação necessária para que seu aprendizado seja mais eficaz.

Seguindo a Bússola Certa
No início da carreira, seguir uma "bússola" é essencial. No DevQuest, fornecemos a direção e as ferramentas que você precisa para atingir seu objetivo de conseguir um emprego na área de desenvolvimento em até 7 meses. Conforme você ganha mais experiência, terá mais liberdade para improvisar, mas agora, o foco deve ser seguir as orientações e planejar com cuidado cada passo.

Por Que Focar no Desenvolvimento Web?
O desenvolvimento web é uma excelente área para começar, especialmente porque possui uma curva de aprendizado mais suave e oferece oportunidades reais de aplicação prática desde o início. O mercado está aquecido, e você poderá começar a aplicar o que está aprendendo em projetos que serão úteis para os primeiros empregos.
Muitas linguagens e áreas da programação são interessantes, mas podem não ser aplicáveis logo no início da sua carreira. Com o desenvolvimento web, você estará preparado para construir sites e sistemas rapidamente, habilidades que são diretamente utilizáveis em vagas de entrada no mercado de trabalho.

Exposição a Tecnologias
É importante se expor desde agora às tecnologias que vamos estudar ao longo do curso. Isso significa ouvir podcasts, assistir a vídeos no YouTube e ler artigos sobre as ferramentas e linguagens que estamos aprendendo.
Mesmo que você ainda não entenda tudo, começar a ouvir termos e jargões ajudará seu cérebro a se familiarizar com esses conceitos. Quando você os encontrar na prática, a compreensão será muito mais rápida e fácil. Além disso, essa prática de se expor constantemente pode até ajudar em entrevistas, mostrando que você está atualizado e comprometido com o aprendizado.

Frontend e Backend: Entendendo as Diferenças
No desenvolvimento web, há duas grandes áreas: frontend e backend. O frontend é responsável pela parte visual de um site ou sistema, a interface com a qual o usuário interage. As tecnologias mais comuns usadas no frontend são HTML, CSS e JavaScript.
Já o backend cuida de toda a lógica que acontece por trás dos panos, como o processamento de dados e a comunicação com bancos de dados. É o backend que garante que os dados enviados pelo usuário, por exemplo, sejam processados corretamente.

Por Que Começar Pelo Frontend?
Começar sua carreira pelo frontend pode ser uma estratégia eficiente. Mesmo que você deseje se especializar em backend no futuro, a base de frontend é essencial. O frontend e o backend são interdependentes, e entender como eles se comunicam te dará uma vantagem competitiva no mercado de trabalho.
O roadmap recomendado para desenvolvedores sugere que você comece pelo frontend com HTML, CSS e JavaScript antes de avançar para o backend. Isso tornará sua transição para projetos completos muito mais fácil e natural.

Estabelecendo Objetivos
Um dos primeiros passos para um planejamento eficiente é estabelecer metas claras. Pense em objetivos de curto e médio prazo. Por exemplo, um objetivo de curto prazo pode ser criar sua primeira página web com HTML e CSS em três semanas. Já um objetivo de médio prazo seria concluir o curso completo em três meses.
Esses marcos são essenciais para manter o foco e garantir que você esteja progredindo consistentemente. Nós estaremos aqui para guiá-lo em cada etapa, garantindo que você siga o caminho certo e atinja seus objetivos.

Conclusão
Neste capítulo, discutimos a importância do planejamento e por que ele é essencial para sua jornada no DevQuest. Com a base sólida de HTML, CSS e JavaScript, e um planejamento bem estruturado, você estará no caminho certo para entrar no mercado de trabalho rapidamente e com qualidade. Defina seus objetivos, siga as orientações e prepare-se para uma carreira de sucesso!
"""

# Criando o PDF com base no conteúdo fornecido
criar_pdf(titulo, conteudo)
