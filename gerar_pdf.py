from fpdf import FPDF
import re

def criar_pdf(titulo_pdf, conteudo):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 10, "RESUMO DA AULA\n" + titulo_pdf, align='C')
    pdf.ln(2)
    pdf.set_line_width(0.5)
    pdf.line(10, 33, 200, 33)
    pdf.ln(10)
    
    pdf.set_font('Arial', '', 12)
    conteudo = conteudo.replace("—", "-").replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    pdf.multi_cell(0, 10, conteudo)
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    
    nome_arquivo = re.sub(r'[\\/*?:"<>|]', "", titulo_pdf.replace(" ", "_")) + ".pdf"
    pdf.output(nome_arquivo)

titulo = "Flexbox: Estruturação de Layouts Flexíveis"
conteudo = """Flexbox: Estruturação de Layouts Flexíveis
O Flexbox é uma das ferramentas mais poderosas e flexíveis para construir layouts CSS. Ele permite distribuir o espaço entre os itens e controlar seu alinhamento de maneira eficiente, mesmo em layouts responsivos e dinâmicos.
Conceitos-chave:
display: flex; — Define um contêiner flexível e transforma seus filhos em itens flexíveis.
justify-content — Controla o alinhamento horizontal.
align-items — Controla o alinhamento vertical.
Exemplo:

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

Aqui, todos os itens dentro do .container serão centralizados vertical e horizontalmente. Flexbox é especialmente útil para criar layouts de colunas e alinhar elementos dentro de um contêiner."""

criar_pdf(titulo, conteudo)
