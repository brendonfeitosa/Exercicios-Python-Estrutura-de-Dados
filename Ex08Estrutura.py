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
A seguir são apresentados os detalhes de implementação de cada opção do menu: ok
1 Cadastrar clientes — não pode existir mais que um cliente com o mesmo código. ok
2 Relatório de clientes - listar todos os clientes cadastrados. ok
3 Cadastrar documentos — ao cadastrar um documento, se o dia de pagamento for maior que o dia de vencimento, calcular o campo ‘juros’ do registro documentos (5% sobre o valor original do documento). ok
4 Relatório de documentos - listar todos os documentos cadastrados. ok
5 Excluir clientes — um cliente só poderá ser excluído se não existir nenhum documento associado a ele. ok-
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

def cad_cliente(): #1
    v_cliente = []
    for i in range(2):
        c = TipoCliente()
        c.cod_cliente = int(input('\nDigite o código do cliente: '))
        c.nome = input('Digite o nome do cliente: ')
        c.telefone = input('Digite o telefone do cliente: ')
        v_cliente.append(c)
    return v_cliente

def visualizar_cliente(v_cliente): #2
    print('\nExistem {} clientes cadastrados, sáo eles: '.format(len(v_cliente)))
    for i in range(len(v_cliente)):
        print('\n| Código: {} | Nome: {} | Telefone {} |'.format(v_cliente[i].cod_cliente, v_cliente[i].nome, v_cliente[i].telefone))

def cad_doc(v_cliente): #3
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

def visualizar_docs(v_doc): #4
    print('\nExistem {} documentos cadastrados.'.format(len(v_doc)))
    for i in range(len(v_doc)):
        print('\n| Número do documento: {} | Código do cliente: {} | Dia de Vencimento: {} | Dia de pagamento: {} | Valor original: R$ {} | Valor de juros: R$ {} | Valor a pagar R$ : {} |'.format(v_doc[i].num_doc, v_doc[i].cod_clien, v_doc[i].dia_venc, v_doc[i].dia_pag, v_doc[i].valor, v_doc[i].juros, v_doc[i].valor + v_doc[i].juros))

def exc_cliente_s_doc(v_doc, v_cliente): #5
    if len(v_cliente) > 0:
        print('\nExclusáo de cliente sem nenhum documento associado...')
        for i in range(len(v_cliente)):
            if i == 0:
                indice_exclusao = i
                excluir_cliente = v_doc[i].cod_clien
            if v_doc[i].cod_clien not in v_cliente[i].cod_cliente:
                excluir_cliente = v_cliente[i]
                indice_exclusao = i
        v_cliente.pop(indice_exclusao)
        print('Exclusão realizada com sucesso...')
    else: 
        print('Não existem clientes para exclusão...')

def exc_doc_num(v_doc): #6
    cont = 0
    if len(v_doc) > 0:
        doc_excluir = int(input('Digite o número do documento que deseja excluir: '))
        for i in range(len(v_doc)):
            if doc_excluir != v_doc[i].num_doc:
                indice = i
                excluir = v_doc[i].num_doc
                print('\nDocumento não encontrado.')
            if doc_excluir == v_doc[i].num_doc:
                indice = i
                excluir = v_doc[i].num_doc
                print('Exclusão Efetuada!')
        v_doc.pop(indice)
    return v_doc

def exc_doc_p_cliente(v_doc, v_cliente): #7
    cont = 0
    if len(v_cliente) > 0:
        cod_cliente = int(input('Digite o código do cliente que deseja excluir os documentos: '))
        for i in range(len(v_cliente)):
            if 


def exc_doc_periodo(v_doc): #8
    if

def alt_inf_cliente(v_cliente): #9
    cont = 0
    if len(v_cliente) > 0:
        cliente_consultar = int(input('\nDigite o código do cliente que deseja alterar: '))
        for i in range(len(v_cliente)):
            if cliente_consultar == v_cliente[i].cod_cliente:
                print('\nCliente localizado, qual alteração deseja fazer: ')
                print('\nO código do cliente não pode ser alterado.')
                print('\n{:<} \n{:<} \n{:<}'.format('1. Nome', '2. Telefone', "3. Voltar ao menu anterior"))
                opcao = int(input('\nDigite a sua opção: '))
                if opcao == 1:
                    alterar_nome = input('\nDigite o novo nome: ')
                    v_cliente[i].nome = alterar_nome
                elif opcao == 2:
                    alterar_telefone = input('\nDigite o novo telefone: ')
                    v_cliente[i].telefone = alterar_telefone
                elif opcao == 3:
                    menu()
            else:
                cont += 1
        if cont > len(v_cliente):
            print('Não há dados para alteração.')
    return v_cliente
    
def visualizar_doc_cliente(v_doc, v_cliente): #10
    total_doc = 0
    cliente_consultar = input('Digite o código do cliente que quer saber a quantidade de documentos: ')
    if len(v_cliente) > 0:
        for i in range(v_doc):
            total_doc += i
        print('A quantidade de documentos cadastrados para o cliente com código {} é de {} documentos.'.format(cliente_consultar, total_doc))
    else:
        print('Não há documentos cadastrados para o cliente informado.')

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