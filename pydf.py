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
    conteudo = re.sub(r'[^\x20-\x7E]+', ' ', conteudo)  # Remove caracteres não imprimíveis

    pdf.multi_cell(0, 10, conteudo)
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    
    nome_arquivo = re.sub(r'[\\/*?:"<>|]', "", titulo_pdf.replace(" ", "_")) + ".pdf"
    pdf.output(nome_arquivo)

titulo = "Tabelas"
conteudo = """As tabelas no HTML são usadas para organizar dados em linhas e colunas. Apesar de não serem mais usadas para estruturar layouts (como no passado), elas ainda são muito importantes para exibir dados tabulados de forma clara e organizada.
Estrutura básica de uma tabela:

<table>
  <tr>
    <th>Produto</th>
    <th>Cor</th>
    <th>Tamanho</th>
    <th>Preço</th>
    <th>Disponibilidade</th>
  </tr>
  <tr>
    <td>Camiseta</td>
    <td>Preta</td>
    <td>M</td>
    <td>R$ 50,00</td>
    <td>Em estoque</td>
  </tr>
  <tr>
    <td>Calça Jeans</td>
    <td>Azul</td>
    <td>P</td>
    <td>R$ 100,00</td>
    <td>Esgotado</td>
  </tr>
</table>

<table>: Define a tabela.
<tr>: Define uma linha da tabela.
<th>: Define o cabeçalho de uma coluna (por padrão, em negrito).
<td>: Define uma célula com dados.

Com CSS, é possível estilizar as tabelas, tornando-as mais bonitas e fáceis de ler, adicionando bordas, cores alternadas nas linhas, entre outros ajustes.
"""

criar_pdf(titulo, conteudo)
