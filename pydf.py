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

titulo = "TDD e o conceito de Vermelho, Verde e Refatoração"
conteudo = """Nesta aula, vamos falar sobre um conceito fundamental no desenvolvimento de testes automatizados chamado TDD (Test-Driven Development) e entender o processo de Vermelho, Verde e Refatoração.
O que é o TDD?
O TDD, ou desenvolvimento orientado a testes, é uma abordagem em que escrevemos os testes antes de desenvolvermos a funcionalidade. Assim, o código é desenvolvido pensando primeiro no teste e, posteriormente, na implementação. Essa metodologia é ideal para garantir que o código atende aos requisitos definidos desde o início.
O Ciclo Vermelho, Verde e Refatoração
O processo de TDD é guiado por três etapas principais:
Vermelho: Escrevemos um teste que inicialmente falha (pois a funcionalidade ainda não foi implementada).
Verde: Escrevemos o código mínimo necessário para passar no teste.
Refatoração: Melhoramos o código mantendo todos os testes passando.
Aplicando o ciclo de Vermelho, Verde e Refatoração
Vamos aplicar esse conceito no nosso exemplo. Imagine que agora recebemos um novo requisito: precisamos adicionar um valor extra de 20% no frete para entregas destinadas a estados específicos, como RS e SC. Vamos seguir o ciclo:
1. Escrevendo o teste (Vermelho)
Começamos criando um teste para garantir que, ao calcular o valor do pedido com um estado específico (RS), o valor do frete seja acrescido de 20%.


it('deve adicionar 20% no valor da entrega caso o estado do pedido seja RS e valor de produtos menor que 500', () => {
    const pedidoComEstadoRS = {
        estado: 'RS',
        itens: [
            { nome: 'Sanduíche', valor: 10 },
            { nome: 'Bota nova', valor: 400 },
            { nome: 'Entrega', valor: 100, entrega: true }
        ]
    };

    const resultado = calcularValorPedido(pedidoComEstadoRS);
    expect(resultado).toBe(530); // 20% de 100 é 20, logo 100 + 20 = 120, e 10 + 400 + 120 = 530
});

Rodamos o teste e verificamos que ele falha. Estamos no ponto Vermelho: o código atual ainda não tem a funcionalidade implementada.
2. Escrevendo o código para passar no teste (Verde)
Agora, adicionamos a lógica mínima para que o teste passe:


if (pedido.estado === 'RS') {
    const acrescimoEntrega = entrega.valor * 0.2; // 20% de acréscimo
    entrega.valor += acrescimoEntrega;
}

Salvamos e verificamos que o teste passa. Isso nos coloca no ponto Verde: o código está funcionando, mas ainda pode não estar otimizado.
3. Refatoração
Com o teste passando, agora podemos pensar em melhorar o código. Por exemplo, podemos criar uma variável constante para a taxa de acréscimo:


const taxaAcrescimo = 0.2;
if (pedido.estado === 'RS') {
    entrega.valor += entrega.valor * taxaAcrescimo;
}

Após a refatoração, verificamos novamente se os testes continuam passando. Se tudo estiver correto, seguimos para adicionar mais testes.
Adicionando mais cenários de teste
Agora, queremos cobrir mais cenários, como o caso em que o estado é SC e o valor do pedido é menor que 500 reais.


it('deve adicionar 20% no valor da entrega caso o estado do pedido seja SC e valor de produtos menor que 500', () => {
    const pedidoComEstadoSC = {
        estado: 'SC',
        itens: [
            { nome: 'Sanduíche', valor: 10 },
            { nome: 'Bota nova', valor: 400 },
            { nome: 'Entrega', valor: 100, entrega: true }
        ]
    };

    const resultado = calcularValorPedido(pedidoComEstadoSC);
    expect(resultado).toBe(530);
});

Rodamos e, novamente, o teste falha (ponto Vermelho). Adicionamos a correção para passar no teste:


if (pedido.estado === 'RS' || pedido.estado === 'SC') {
    entrega.valor += entrega.valor * taxaAcrescimo;
}

Refatoração Final
Podemos fazer algumas melhorias no nosso código para mantê-lo legível e eficiente. Por exemplo:
Criar uma lista de estados que devem ter o acréscimo de 20%.
Verificar se o estado do pedido está presente nessa lista:


const taxaAcrescimo = 0.2;
const estadosComAcrescimo = ['RS', 'SC'];

if (estadosComAcrescimo.includes(pedido.estado)) {
    entrega.valor += entrega.valor * taxaAcrescimo;
}

Com essa mudança, mantemos o código limpo e flexível para futuros ajustes.
Verificando a ausência de acréscimo para outros estados
Por fim, vamos adicionar um teste para garantir que, caso o estado não seja RS ou SC, o valor do frete permaneça inalterado:


it('não deve adicionar 20% no valor da entrega caso estado do pedido seja diferente de SC ou RS e valor de produtos menor que 500', () => {
    const pedidoComEstadoSP = {
        estado: 'SP',
        itens: [
            { nome: 'Sanduíche', valor: 10 },
            { nome: 'Bota nova', valor: 400 },
            { nome: 'Entrega', valor: 100, entrega: true }
        ]
    };

    const resultado = calcularValorPedido(pedidoComEstadoSP);
    expect(resultado).toBe(510); // Não deve adicionar o valor extra
});

Resumo
Nesta aula, aplicamos o ciclo de Vermelho, Verde e Refatoração usando o TDD para implementar uma nova funcionalidade com segurança e confiança. Cada etapa foi validada por testes automatizados, garantindo que nosso código não quebrasse em nenhum ponto.
Esse é o poder do TDD: nos permite desenvolver de forma iterativa, corrigindo falhas rapidamente e deixando nosso código mais robusto e fácil de manter.
Espero que este módulo tenha te mostrado como testes automatizados podem transformar a maneira como você desenvolve suas funcionalidades, trazendo mais qualidade e tranquilidade para o seu código.
"""

criar_pdf(titulo, conteudo)
