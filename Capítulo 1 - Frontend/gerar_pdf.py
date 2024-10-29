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

titulo = "Criando Sua Primeira Página HTML"
conteudo = """Criando Sua Primeira Página HTML
Agora que você já conhece os principais elementos do HTML, vamos criar sua primeira página HTML completa. A estrutura básica da página será a seguinte:

Organização das pastas:
Crie uma pasta chamada curso-devquest.
Dentro dessa pasta, crie uma subpasta chamada modulo-html.
Nessa subpasta, crie um arquivo chamado index.html.

Criando o arquivo index.html:

Estrutura inicial:

<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha Primeira Página HTML</title>
  </head>
  <body>
    <h1>Minha Primeira Página HTML</h1>
    <p>Bem-vindo à minha primeira página web criada com HTML!</p>
  </body>
</html>

Agora você tem uma estrutura básica de página HTML. Quando carregada em um navegador, você verá o título na aba e o conteúdo da página visível, como o título e o parágrafo.

Automatizando com o Emmet: O Emmet é uma ferramenta poderosa integrada ao VS Code que permite criar código HTML rapidamente com abreviações. Por exemplo, se você digitar html:5 e pressionar Tab, o Emmet cria automaticamente toda a estrutura HTML básica para você.

Com esses conhecimentos, você agora é capaz de criar páginas simples com listas, tabelas, e formatação básica de texto, além de usar o Emmet para agilizar seu processo de desenvolvimento. Na próxima etapa, avançaremos para trabalhar com formulários e outros elementos interativos, que permitirão criar páginas mais dinâmicas e funcionais.
"""

criar_pdf(titulo, conteudo)
