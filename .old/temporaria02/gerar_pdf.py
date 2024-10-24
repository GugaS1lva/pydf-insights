from fpdf import FPDF

class CustomPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'DevQuest - Guia de Planejamento', ln=True, align='C')  # Cabeçalho centralizado
        self.ln(20)  # Espaçamento após o cabeçalho

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

# Função para criar um PDF com formatações e rodapé/cabeçalho
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

# Texto para o conteúdo do PDF
titulo = "Introdução ao Treinamento e Pontos Importantes"
conteudo = """1.1 - Introdução ao treinamento e pontos importantes

1. Leia o Módulo de Suporte e o Contrato
O primeiro passo é garantir que você leia o Módulo de Suporte e o contrato do curso dentro da plataforma das aulas. Por quê? Porque é nele que você vai encontrar informações importantes sobre onde tirar suas dúvidas e quais canais utilizar. Se você não prestar atenção a esses detalhes, pode acabar se perdendo e atrasando o seu progresso.
"""

# Criando o PDF com base no conteúdo fornecido
criar_pdf(titulo, conteudo)
