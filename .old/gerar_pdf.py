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

titulo = "10 Promises"
conteudo = """Promises são uma maneira moderna de lidar com operações assíncronas no JavaScript. Elas permitem representar fluxos assíncronos de maneira mais sequencial e legível, além de facilitarem o tratamento de exceções caso algo dê errado nesse processo.

O que é uma Promise?
Uma Promise representa um valor que pode estar disponível agora, no futuro ou nunca. Basicamente, ela é uma promessa de que algo será concluído (com sucesso ou falha) no futuro. Uma Promise pode estar em um dos seguintes estados:
- Pendente (pending): Estado inicial, ainda não resolvida.
- Realizada (fulfilled): A operação foi concluída com sucesso.
- Recusada (rejected): A operação falhou.
- Estabelecida (settled): Foi realizada ou recusada, indicando que a operação foi concluída de alguma forma.

Criando uma Promise
Para criar uma Promise, usamos a sintaxe new Promise(), onde passamos uma função callback que possui dois parâmetros principais: resolve e reject. Esses parâmetros são funções que indicam se a operação foi concluída com sucesso (resolve) ou com falha (reject).

let ferverAgua = () => {
    return new Promise((resolve, reject) => {
        let chaleiraEstaNoFogao = true;
        let fogaoEstaLigado = true;

        if (chaleiraEstaNoFogao && fogaoEstaLigado) {
            console.log('Começando a ferver a água...');
            resolve("Água pronta para o café!"); // Sucesso
        } else {
            reject("Erro: É necessário colocar a chaleira no fogão e ligar o fogão."); // Falha
        }
    });
};

No exemplo acima, criamos uma função ferverAgua que retorna uma Promise. A Promise verifica se a chaleira está no fogão e se o fogão está ligado. Se ambos forem true, a promessa é cumprida (resolve). Caso contrário, ela é rejeitada (reject).

Usando a Promise com then e catch
Para capturar o resultado de uma Promise, usamos os métodos then e catch. O then é executado quando a promessa é cumprida, e o catch é executado quando a promessa é rejeitada.

ferverAgua()
    .then((resultado) => {
        console.log(resultado); // "Água pronta para o café!"
        console.log("Continuando a fazer o café...");
    })
    .catch((erro) => {
        console.error(erro); // "Erro: É necessário colocar a chaleira no fogão e ligar o fogão."
    });

Evitando o Callback Hell
Antes das Promises, o JavaScript usava funções de callback para lidar com código assíncrono, o que levava ao problema conhecido como callback hell — um encadeamento de funções aninhadas que tornava o código difícil de ler e manter.

Exemplo de Callback Hell:
colocarAguaPraFerver(function () {
    prepararFiltroECafe(function () {
        passarOCafe(function () {
            console.log("Café pronto!");
        });
    });
});

Usando Promises, o mesmo código pode ser reescrito de forma mais legível:
colocarAguaPraFerver()
    .then(() => prepararFiltroECafe())
    .then(() => passarOCafe())
    .then(() => console.log("Café pronto!"))
    .catch((erro) => console.error("Erro ao fazer o café: " + erro));

Como as Promises ajudam?
- Facilitam o fluxo assíncrono: As Promises ajudam a escrever código assíncrono de forma mais organizada e fácil de entender.
- Tratamento de Erros: Com as Promises, o tratamento de erros se torna mais eficiente e padronizado usando o .catch.
- Encadeamento de Promises: Permite que as operações assíncronas sejam encadeadas, tornando a leitura do código mais fluida e sem a necessidade de funções aninhadas.

Exemplo Prático
Vamos construir um exemplo prático utilizando Promises para simular o processo de fazer café:

function colocarAguaPraFerver() {
    return new Promise((resolve, reject) => {
        console.log('Colocando água para ferver...');
        setTimeout(() => {
            console.log('Água ferveu!');
            resolve();
        }, 2000);
    });
}

function prepararTudoParaOCafe() {
    return new Promise((resolve) => {
        console.log('Pegando o pó de café...');
        console.log('Pegando o filtro...');
        console.log('Colocando o café no filtro...');
        resolve();
    });
}

function passarOCafe() {
    return new Promise((resolve) => {
        console.log('Passando o café...');
        setTimeout(() => {
            console.log('Café pronto!');
            resolve();
        }, 1000);
    });
}

colocarAguaPraFerver()
    .then(() => prepararTudoParaOCafe())
    .then(() => passarOCafe())
    .then(() => console.log("O café está servido!"))
    .catch((erro) => console.error("Erro ao preparar o café: " + erro));

Como o exemplo funciona:
A função colocarAguaPraFerver é executada e leva 2 segundos para "ferver" a água.
Após a conclusão dessa etapa, prepararTudoParaOCafe é chamada para preparar os filtros e o pó de café.
Em seguida, passarOCafe é executada, o que leva mais 1 segundo.
Quando todas as etapas são concluídas, a mensagem final "O café está servido!" é exibida.
Caso qualquer uma das Promises falhe, o catch será acionado e exibirá a mensagem de erro.

Conclusão
As Promises tornaram a execução assíncrona muito mais organizada e eficiente no JavaScript. Elas permitem que a gente fuja do callback hell e crie fluxos assíncronos que sejam fáceis de ler e manter. Além disso, elas oferecem uma maneira simples e padronizada de lidar com erros e controlar o fluxo de execução.
"""

criar_pdf(titulo, conteudo)
