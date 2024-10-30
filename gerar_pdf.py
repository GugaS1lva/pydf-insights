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

titulo = "Tags Semânticas no HTML"
conteudo = """Tags Semânticas no HTML
As tags semânticas são fundamentais para dar significado ao conteúdo da sua página e melhorar a acessibilidade e a otimização para motores de busca (SEO). Elas descrevem o propósito de cada parte do conteúdo, facilitando a leitura por humanos e máquinas.

8. Tags Semânticas Importantes
Header: Representa o cabeçalho da página.
Nav: Define um conjunto de links de navegação.
Main: Representa o conteúdo principal da página.
Section: Representa uma seção de conteúdo.
Footer: Define o rodapé da página.

9. Outras Tags Semânticas
Article: Indica um artigo ou conteúdo independente.
Aside: Representa conteúdo relacionado, como barras laterais ou informações complementares.
Figure e Figcaption: Usadas para agrupar imagens e suas descrições.
Address: Representa informações de contato, como endereços e números de telefone.

Com o uso das tags semânticas, você garante que seu HTML seja mais fácil de ler e compreender, tanto para outros desenvolvedores quanto para os algoritmos de indexação.
"""

criar_pdf(titulo, conteudo)
