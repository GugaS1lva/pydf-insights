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
    conteudo = re.sub(r'[^\x20-\x7E]+', ' ', conteudo) 

    pdf.multi_cell(0, 10, conteudo)
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    
    nome_arquivo = re.sub(r'[\\/*?:"<>|]', "", titulo_pdf.replace(" ", "_")) + ".pdf"
    pdf.output(nome_arquivo)

titulo = "18 Gerenciando pacotes com NPM"
conteudo = """Nesta aula, vamos aprofundar nosso conhecimento sobre o gerenciamento de pacotes usando o NPM (Node Package Manager) e entender como essa ferramenta é utilizada na prática para criar e manter projetos JavaScript organizados e eficientes.
Inicializando um Projeto com o NPM
Para começar a usar o NPM em um projeto, precisamos inicializar o gerenciador de pacotes dentro da pasta do projeto. Esse processo cria um arquivo package.json, que serve como um ponto central de controle de pacotes e configurações do projeto.
Para isso, vamos usar o comando:


npm init

Esse comando precisa ser executado no terminal dentro da pasta raiz do projeto. Ao rodar npm init, o NPM nos guiará por uma série de perguntas para configurar o projeto. Vamos ver cada uma delas:
Nome do projeto: Define o nome único do projeto. É importante que ele não contenha espaços, por isso geralmente usamos - ou _ para separar palavras. Exemplo: projeto_npm.
Versão do projeto: Geralmente, começamos com 1.0.0, indicando a primeira versão. Futuras atualizações incrementam esses números.
Descrição: Uma breve descrição do que o projeto faz. Exemplo: Projeto de teste para aprender NPM no módulo de JavaScript Avançado.
Entry point (ponto de entrada): Arquivo principal do projeto, como index.js. Esse é o arquivo que o Node.js procurará para iniciar a aplicação.
Test command: Comando usado para rodar testes automatizados. Podemos deixar vazio se não vamos usar testes por enquanto.
Git repository: URL do repositório Git, se o projeto estiver vinculado a um controle de versão.
Keywords: Palavras-chave para identificar o projeto (separadas por vírgulas).
Author: Nome do autor do projeto (você!).
License: Tipo de licença. Podemos usar a licença padrão (ISC).
Após confirmar as informações, o NPM gera um arquivo package.json contendo todas essas configurações.
Instalando Pacotes com NPM
Depois de configurar o package.json, podemos começar a instalar pacotes no projeto usando o comando:


npm install <nome-do-pacote>

Por exemplo, vamos instalar um pacote chamado kind-of, que ajuda a identificar o tipo de variáveis:


npm install kind-of --save

Esse comando faz duas coisas:
Atualiza o package.json: Ele cria uma seção chamada dependencies e adiciona o pacote kind-of como dependência.

"dependencies": {
  "kind-of": "^6.0.3"
}

Cria a pasta node_modules: Dentro dessa pasta, o NPM armazena todos os pacotes e suas dependências. É importante lembrar que essa pasta é apenas para uso local e não deve ser enviada para o controle de versão.
Além disso, o NPM também cria um arquivo package-lock.json, que contém informações detalhadas sobre a árvore de dependências do projeto. Esse arquivo é essencial para garantir que todos os colaboradores do projeto tenham exatamente as mesmas versões de pacotes instaladas.
Utilizando Pacotes no Projeto
Depois de instalar um pacote, podemos utilizá-lo no nosso projeto usando o require. Por exemplo:


var kindOf = require('kind-of');
console.log(kindOf(true)); // Output: 'boolean'

O método require carrega o pacote kind-of e permite usar suas funcionalidades no nosso código. Vale lembrar que esse método é específico para o ambiente Node.js e não funcionará diretamente no navegador.
Gerenciando o node_modules no Controle de Versão
A pasta node_modules geralmente contém centenas ou até milhares de arquivos e não deve ser enviada para o repositório Git. Em vez disso, enviamos apenas o package.json e o package-lock.json. Assim, quem for trabalhar no projeto no futuro só precisa rodar o comando:


npm install

Esse comando verifica o package.json e o package-lock.json e baixa todas as dependências listadas, recriando a pasta node_modules no ambiente local.
O que é o package-lock.json?
O package-lock.json é um arquivo criado automaticamente pelo NPM sempre que instalamos ou removemos um pacote. Ele serve para garantir que o ambiente do projeto seja replicado exatamente igual em outras máquinas, especificando versões exatas das dependências.
Quando compartilhamos um projeto com outras pessoas, o package-lock.json ajuda a garantir que todos usem as mesmas versões dos pacotes, evitando problemas de compatibilidade.
"""

criar_pdf(titulo, conteudo)
