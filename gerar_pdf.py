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

titulo = "Variáveis no CSS"
conteudo = """Variáveis no CSS
As variáveis CSS são uma adição recente e poderosa que permite definir valores reutilizáveis no estilo. Elas facilitam a manutenção e permitem alterar valores de maneira centralizada.
Definindo variáveis:

:root {
  --cor-principal: #3498db;
  --tamanho-texto: 16px;
}

h1 {
  color: var(--cor-principal);
  font-size: var(--tamanho-texto);
}

As variáveis podem ser redefinidas em diferentes contextos, permitindo criar temas dinâmicos. O uso de variáveis facilita a atualização de estilos e garante consistência visual em grandes projetos."""

criar_pdf(titulo, conteudo)
