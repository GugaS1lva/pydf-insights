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
    pdf.multi_cell(0, 10, conteudo)
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    
    nome_arquivo = re.sub(r'[\\/*?:"<>|]', "", titulo_pdf.replace(" ", "_")) + ".pdf"
    pdf.output(nome_arquivo)

titulo = "Unidades de Medida Absoluta"
conteudo = """As unidades de medida absolutas são fixas, o que significa que não mudam de acordo com o tamanho da tela ou do elemento pai. A mais comum é o pixel (px), que representa um ponto físico na tela.
Por exemplo, definir a largura de um elemento em pixels cria um tamanho fixo que não será redimensionado conforme o tamanho da tela:

div {
  width: 300px; /* Largura fixa de 300 pixels */
}

A desvantagem das medidas absolutas, como o pixel, é que elas não são responsivas, ou seja, podem causar problemas de visualização em dispositivos com telas menores, como smartphones.
"""

criar_pdf(titulo, conteudo)
