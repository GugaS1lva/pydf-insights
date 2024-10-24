from fpdf import FPDF

# Função para criar um PDF com formatações
def criar_pdf(titulo_pdf, conteudo):
    # Criando um objeto PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Adicionando uma página
    pdf.add_page()
    
    # Título principal
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 10, "RESUMO DO MÓDULO\n" + titulo_pdf, align='C')
    pdf.ln(2)  # Adiciona um pequeno espaçamento
    
    # Linha horizontal após o título
    pdf.set_line_width(0.5)
    pdf.line(10, 33, 200, 33)
    pdf.ln(10)

    # Conteúdo do PDF
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, conteudo)
    
    # Linha horizontal no final
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    # Salvando o PDF com o nome escolhido
    nome_arquivo = titulo_pdf.replace(" ", "_") + ".pdf"
    pdf.output(nome_arquivo)

# Textos para o conteúdo do PDF
titulo = "Backend com JavaScript"
conteudo = """1 - O que é Backend?
Seja bem-vindo ao módulo de backend! Aqui, vamos aprender de forma completa o que é backend e como ele se relaciona com o frontend. Além disso, vamos entender como essas duas áreas se comunicam.

Revisão: O que é Frontend?
Antes de falarmos sobre o backend, vamos revisar rapidamente o que é o frontend. Quando você acessa um site, o navegador recebe arquivos HTML, CSS e JavaScript e os interpreta para montar a interface do site. Esses são os elementos visíveis e interativos com os quais você interage. 

Outro exemplo muito comum de frontend são os aplicativos para dispositivos móveis. Ao abrir um aplicativo de banco, pedir comida, chamar um carro ou acessar redes sociais, tudo o que você vê é o frontend. No nosso curso, focamos no desenvolvimento web, mas o frontend está presente em diversas áreas além do navegador.

O que é o Backend na prática?
Agora, vamos falar sobre o backend. O frontend é apenas uma camada que permite ao usuário acessar os serviços de forma amigável. Vamos supor que você está no Facebook atualizando a foto do perfil. Ao clicar no botão para alterar a foto, uma janela se abre para você escolher o arquivo e, ao clicar em salvar, o que acontece?

O backend entra em ação a partir do momento em que a foto é carregada. O navegador envia uma mensagem ao servidor do Facebook com as informações da foto. Essa mensagem é chamada de requisição. O computador que envia a mensagem é o cliente, e o computador que recebe é o servidor.

No servidor, há toda uma estrutura que recebe a requisição, armazena a imagem em um banco de dados ou de arquivos, e deixa a imagem disponível sempre que você acessar o perfil novamente.

Comunicação via API REST e protocolo HTTP
Na prática, o backend é um serviço que, através da internet, recebe requisições e acessa recursos como bancos de dados. A forma mais comum de criar um serviço backend é utilizando uma API REST através do protocolo HTTP, trocando informações no formato JSON.

Essas tecnologias são fundamentais para a comunicação entre o frontend e o backend. Mesmo que pareçam complexas agora, mais adiante vamos entender melhor cada uma delas.
"""

# Criando o PDF com base no conteúdo fornecido
criar_pdf(titulo, conteudo)
