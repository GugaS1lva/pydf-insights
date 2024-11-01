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

titulo = "Incorporando Vídeos com iframe"
conteudo = """Incorporando Vídeos com iframe
A tag <iframe> é usada para inserir outra página HTML dentro de uma página principal, funcionando como uma "janela" que mostra o conteúdo de um site externo. Um dos usos mais comuns do <iframe> é incorporar vídeos de plataformas como YouTube e Vimeo, tornando o processo de inclusão de mídia mais leve e prático.
Exemplo:
<iframe width="560" height="315" src="https://www.youtube.com/embed/NcGnLdUPnpo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Neste exemplo, o vídeo é carregado diretamente do YouTube e a largura e altura do quadro podem ser ajustadas conforme necessário. O atributo allowfullscreen permite que o usuário expanda o vídeo para tela cheia.
O <iframe> é ideal para vídeos por não exigir o carregamento direto no servidor, economizando espaço e recursos de banda."""

criar_pdf(titulo, conteudo)
