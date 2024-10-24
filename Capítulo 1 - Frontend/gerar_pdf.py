from fpdf import FPDF

def criar_pdf(titulo_pdf, conteudo):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.add_page()
    
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 10, "RESUMO DO MÓDULO\n" + titulo_pdf, align='C')
    pdf.ln(2)  
    
    pdf.set_line_width(0.5)
    pdf.line(10, 33, 200, 33)
    pdf.ln(10)

    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, conteudo)
    
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    nome_arquivo = titulo_pdf.replace(" ", "_") + ".pdf"
    pdf.output(nome_arquivo)

titulo = "O Pilar do Planejamento no DevQuest"
conteudo = """Introdução
O planejamento é um dos pilares mais importantes para quem deseja evoluir rapidamente na carreira de desenvolvimento de software. Infelizmente, muitas vezes, ele é negligenciado. Neste capítulo, vamos explicar por que um bom planejamento é essencial e como ele pode ser a chave para seu sucesso.
Um ditado interessante, que resume bem essa questão, diz que não adianta ser o corredor mais rápido se você estiver correndo na direção errada. Muitos iniciantes estão cheios de vontade, mas acabam investindo seu tempo e energia em áreas que não trarão o retorno esperado.

---------

Por Que o Planejamento é Essencial?
A falta de planejamento é uma das principais razões pelas quais muitos perdem tempo no início de suas carreiras. Imagine começar a aprender uma linguagem de programação sem saber onde ela será aplicada ou se há vagas no mercado para iniciantes nessa área. Sem uma visão clara e um planejamento bem estruturado, muitos correm o risco de seguir por um caminho que não trará os resultados desejados.

---------

O Pulo Direto para a Prática
É comum ver pessoas querendo pular diretamente para a parte prática, o famoso "mão na massa". Mas, assim como tocar uma música sem aprender os acordes ou a posição correta dos dedos em um instrumento musical, isso pode se tornar um desafio muito maior sem uma base sólida. Entender a base é o que permitirá que você progrida de forma mais consistente e eficiente.

---------

Seguindo a Bússola Certa
No início da carreira, seguir uma "bússola" é essencial. No DevQuest, fornecemos a direção e as ferramentas que você precisa para atingir seu objetivo de conseguir um emprego na área de desenvolvimento em até 7 meses.

---------

Por Que Focar no Desenvolvimento Web?
O desenvolvimento web é uma excelente área para começar, especialmente porque possui uma curva de aprendizado mais suave e oferece oportunidades reais de aplicação prática desde o início. O mercado está aquecido, e você poderá começar a aplicar o que está aprendendo em projetos que serão úteis para os primeiros empregos.

---------

Exposição a Tecnologias
É importante se expor desde agora às tecnologias que vamos estudar ao longo do curso. Isso significa ouvir podcasts, assistir a vídeos no YouTube e ler artigos sobre as ferramentas e linguagens que estamos aprendendo. Mesmo que você ainda não entenda tudo, começar a ouvir termos e jargões ajudará seu cérebro a se familiarizar com esses conceitos.

---------

Frontend e Backend: Entendendo as Diferenças
No desenvolvimento web, há duas grandes áreas: frontend e backend. O frontend é responsável pela parte visual de um site ou sistema, a interface com a qual o usuário interage. Já o backend cuida de toda a lógica que acontece por trás dos panos, como o processamento de dados e a comunicação com bancos de dados.

---------

Conclusão
Neste capítulo, discutimos a importância do planejamento e por que ele é essencial para sua jornada no DevQuest. Defina seus objetivos, siga as orientações e prepare-se para uma carreira de sucesso!
"""

criar_pdf(titulo, conteudo)
