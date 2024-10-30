from fpdf import FPDF
import re

def remover_caracteres_especiais(texto):
    texto = texto.replace("—", "-").replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    return texto

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
    conteudo = remover_caracteres_especiais(conteudo)
    pdf.multi_cell(0, 10, conteudo)
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    
    nome_arquivo = re.sub(r'[\\/*?:"<>|]', "", titulo_pdf.replace(" ", "_")) + ".pdf"
    pdf.output(nome_arquivo)

titulo = "Centralizando Elementos no CSS"
conteudo = """Centralizando Elementos no CSS
Centralizar elementos é uma necessidade comum no design de interfaces. Existem várias técnicas para isso no CSS, cada uma adequada para um tipo específico de elemento.
Centralização de Texto com text-align: Para centralizar texto dentro de um bloco, use:

.texto {
  text-align: center;
}

Centralização com margin: auto: Para centralizar blocos, como divs, defina um valor fixo de largura e aplique margin: auto:

.bloco {
  width: 300px;
  margin: 0 auto;
}

Centralização com position e transform: Para centralizar elementos verticalmente, use position em conjunto com transform:

.caixa {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

Essa técnica é útil para elementos que precisam ser posicionados de maneira exata no centro da tela.
Centralização com Flexbox: Embora flexbox seja um assunto mais avançado, vale a pena mencioná-lo como a forma mais simples e poderosa de centralizar elementos horizontal e verticalmente ao mesmo tempo:

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

Cada método tem suas vantagens e desvantagens, e escolher o mais apropriado depende do contexto e do tipo de elemento a ser centralizado.
"""

criar_pdf(titulo, conteudo)
