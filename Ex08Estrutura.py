'''8. Elabore duas estruturas, como é apresentado a seguir:
|CLIENTE |DOCUMENTOS
|cod_cli |num_doc
|nome    |cod_cli
|fone    |dia_venc
|        |dia_pag
|        |valor
|        |juros
Sabe-se que um documento só pode ser cadastrado para um cliente que já exista.
Considere que podem existir, no máximo, 15 clientes e 30 documentos. Crie um vetor para clientes e outro para documentos.
Crie um menu para a realização de cada uma das operações especificadas a seguir:
** SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS **
1 Cadastrar clientes
2 Relatório de clientes
3 Cadastrar documentos
4 Relatório de documentos
5 Excluir clientes sem documentos
6 Excluir documentos individuais pelo número
7 Excluir documentos por cliente
8 Excluir documentos por período
9 Alterar as informações dos clientes
10 Mostrar o total de documentos de determinado cliente
11 Sair
Qual opção deseja?
.................................................................................................
Para cada item do menu, desenvolva uma função.
A seguir são apresentados os detalhes de implementação de cada opção do menu:
1 Cadastrar clientes — não pode existir mais que um cliente com o mesmo código.
2 Relatório de clientes - listar todos os clientes cadastrados.
3 Cadastrar documentos — ao cadastrar um documento, se o dia de pagamento for maior que o dia de vencimento, calcular o campo ‘juros’ do registro documentos (5% sobre o valor original do documento).
4 Relatório de documentos - listar todos os documentos cadastrados.
5 Excluir clientes — um cliente só poderá ser excluído se não existir nenhum documento associado a ele.
6 Excluir documentos individuais — por meio de seu número. Caso o documento não exista, o programa deverá mostrar a mensagem "Documento não encontrado".
7 Excluir documentos por cliente — o programa deverá informar o código do cliente e excluir todos os seus documentos. Caso o cliente não exista, deverá mostrar a mensagem "Cliente não encontrado".
8 Excluir documentos por período — o programa deverá informar o dia inicial e o dia final e excluir todos os documentos que possuam data de vencimento nesse período.
9 Alterar as informações sobre os clientes — só NÃO altere o código do cliente.
10 Mostrar o total de documentos de determinado cliente.'''
class TipoCliente:
    cod_cliente = 0
    nome = ''
    telefone = ''

class TipoDocumentos:
    num_doc = 0
    cod_clien = TipoCliente()
    dia_venc = 0
    dia_pag = 0
    valor = 0
    juros = 0

def menu():
    print('\n{:*^100}'.format(' SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS '))
    print('\n1. Cadastrar clientes')
    print('2. Relatório de clientes')
    print('3. Cadastrar documentos')
    print('4. Relatório de documentos')
    print('5. Excluir clientes sem documentos')
    print('6. Excluir documentos individuais pelo número')
    print('7. Excluir documentos por cliente')
    print('8. Excluir documentos por período')
    print('9. Alterar as informações dos clientes')
    print('10. Mostrar o total de documentos de determinado cliente')
    print('11. Sair')
    opcao = int(input('\nQual opção deseja? '))
    return opcao

def cad_cliente():
    v_cliente = []
    for i in range(2):
        c = TipoCliente()
        c.cod_cliente = int(input('\nDigite o código do cliente: '))
        c.nome = input('Digite o nome do cliente: ')
        c.telefone = input('Digite o telefone do cliente: ')
        v_cliente.append(c)
    return v_cliente

def visualizar_cliente(v_cliente):
    print('\nExistem {} clientes cadastrados, sáo eles: '.format(len(v_cliente)))
    for i in range(len(v_cliente)):
        print('\n| Código: {} | Nome: {} | Telefone {} |'.format(v_cliente[i].cod_cliente, v_cliente[i].nome, v_cliente[i].telefone))

def cad_doc(v_cliente):
    v_doc = []
    for i in range(2):
        d = TipoDocumentos()
        d.num_doc = int(input('\nDigite o número do documento (apenas números): '))
        d.cod_clien = v_cliente[i].cod_cliente
        d.dia_venc = int(input('Digite o dia do vencimento: '))
        d.dia_pag = int(input('Digite o dia do pagamento: '))
        d.valor = float(input('Digite o valor do documento: R$ '))
        qtd_dias = d.dia_pag - d.dia_venc
        d.juros = qtd_dias * (5 / 100)
        v_doc.append(d)
    return v_doc

def visualizar_docs(v_doc):
    print('\nExistem {} documentos cadastrados.'.format(len(v_doc)))
    for i in range(len(v_doc)):
        print('\n| Número do documento: {} | Código do cliente: {} | Dia de Vencimento: {} | Dia de pagamento: {} | Valor original: R$ {} | Valor de juros: R$ {} | Valor a pagar R$ : {} |'.format(v_doc[i].num_doc, v_doc[i].cod_clien, v_doc[i].dia_venc, v_doc[i].dia_pag, v_doc[i].valor, v_doc[i].juros, v_doc[i].valor + v_doc[i].juros))

def main():
    vet_doc = []
    vet_cliente = []
    op = menu()
    while op >= 1 and op <= 11:
        if op == 1:
            vet_cliente = cad_cliente()
        elif op == 2:
            visualizar_cliente(vet_cliente)
        elif op == 3:
            vet_doc = cad_doc(vet_cliente)
        elif op == 4:
            visualizar_docs(vet_doc)
        elif op == 5:
            exc_cliente_s_doc(vet_doc, vet_cliente)
        elif op == 6:
            exc_doc_num(vet_doc)
        elif op == 7:
            exc_doc_p_cliente(vet_doc,vet_cliente)
        elif op == 8:
            exc_doc_periodo(vet_doc)
        elif op == 9:
            alt_inf_cliente(vet_cliente)
        elif op == 10:
            visualizar_doc_cliente(vet_doc, vet_cliente)
        elif op == 11:
            print('FIM!')
            break
        op = menu()
main()