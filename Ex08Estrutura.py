class TipoCliente:
    cli_cod = 0
    nome = ''
    fone = ''

class TipoDocumento:
    num_doc = 0
    cli_cod = 0
    dia_venc = 0
    dia_pag = 0
    valor = 0.0
    juros = 0.0

def Menu(vet_cliente, vet_doc):
    while True: 
        print('\n{:*^100}'.format(' MENU SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS '))
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
        op = int(input('\nDigite a opção desejada: '))
        if op == 1: #1
            if len(vet_cliente) >= 15:
                print('\n O limite de clientes foi atingido.')
            else:
                cad_cliente(vet_cliente)
        elif op == 2: #2
            relatorio_clientes(vet_cliente)
        elif op == 3: #3
            if len(vet_doc) >= 30:
                print('\n O limite de documentos foi atingido.')
            else:
                cad_documentos(vet_doc, vet_cliente)
        elif op == 4: #4
            relatorio_docs(vet_doc)
        elif op == 5: #5
            excluir_cliente_s_doc(vet_cliente, vet_doc)
        elif op == 6: #6
            numero = int(input('\nDigite o número do documento para excluir: '))
            excluir_doc_num(vet_doc, numero)
        elif op == 7: #7
            cli_codigo = int(input('\nDigite o codigo do cliente: '))
            excluir_doc_cliente(vet_doc, cli_codigo)
        elif op == 8: #8
            data_inicial = int(input('\nDigita a data incial: '))
            data_final = int(input('Digita a data final: '))
            Excluir_DocData(data_inicial, data_final, vet_doc)
        elif op == 9: #9
            cli_codigo = int(input('\nDigite o código do cliente que deseja alterar: '))
            alterar_cliente(vet_cliente, cli_codigo)
        elif op == 10: #10
            cli_codigo = int(input('\nDigite o código do cliente: '))
            print(f'\nEste cliente possui um total de {visualizar_doc_cliente(vet_doc, cli_codigo)} documentos.')
        elif op == 11: #11
            print('FIM!')
            break

def cad_cliente(vet_cliente): #1
    codigos = []
    c = TipoCliente() #iniciar a class no começo da função, para poder ultiliza-la em todo lugar
    for i in vet_cliente:
        codigos.append(i.cli_cod)
    while True:
        c.cli_cod = int(input('\nDigite o código do cliente: '))
        if c.cli_cod not in codigos:
            break #break para sair da estrutura de repetição
        else:
            print('\n Código de cliente já existente.')
    c.nome = input('Digite o nome do cliente: ')
    c.fone = input('Digite o telefone do cliente: ')
    print('\n Cliente cadastrado com sucesso.')
    vet_cliente.append(c)
    return vet_cliente

def relatorio_clientes(vet_cliente): #sem return #2
    print('\nExistem {} clientes cadastrados, sáo eles: '.format(len(vet_cliente)))
    for i in vet_cliente:
        if len(vet_cliente) > 0:
            print(f'\nCódigo: {i.cli_cod} | Nome: {i.nome} | Telefone: {i.fone}')
        else:
            print('\n Não existem clientes cadastrados.')

def cad_documentos(vet_doc, vet_cliente): #3
    d = TipoDocumento()
    numeros_doc = []
    for i in vet_doc:
        numeros_doc.append(i.num_doc) #guarda os num_doc do vetor de documentos em um outro vetor
    while True:
        d.num_doc = int(input('\nDigite o número do documento: ')) #pedir o num_doc que deseja cadastrar
        if d.num_doc in numeros_doc: #verificar se o num_doc do input é igual a algum num_doc que ja existe no vetor
            print('\n Código de documento já existente.')
        else:
            break #se não existir, sai da repetição e continua o código
    cod_clientes = []
    for i in vet_cliente:
        cod_clientes.append(i.cli_cod) #guarda os cli_cod do vetor de clientes em um outro vetor
    while True:
        d.cli_cod = int(input('Digite o código do cliente: ')) #pedir o cli_cod que deseja vincular o documento
        if d.cli_cod in cod_clientes: #verificar se aquele cli_cod do input existe no vetor 
            break #se existir, sai da repetição e continua o codigo
        else:
            print('\nCódigo de cliente não cadastrado, tente novamente.')
    d.dia_pag = int(input('Digite o dia de pagamento: '))
    d.dia_venc = int(input('Digite o dia de vencimento: '))
    d.valor = float(input('Digite o valor: R$ '))
    if d.dia_pag > d.dia_venc:
        d.juros = d.valor * 0.05
    vet_doc.append(d)
    print('\nDocumento cadastrado com sucesso.')
    return vet_doc

def relatorio_docs(vet_doc): #sem return #4
    if len(vet_doc) > 0:
        print('\nDocumentos cadastrados: ')
        for i in vet_doc:
            print(f'\nNúmero: {i.num_doc} | Código cliente: {i.cli_cod} | Dia pagamento: {i.dia_pag} | Dia vencimento: {i.dia_venc} | Valor: {i.valor} | Juros: {i.juros}')
    else:
        print('\nNão existem documentos cadastrados.')

def excluir_cliente_s_doc(vet_cliente, vet_doc): #5
    CliComDoc_codigos = []
    for i in vet_doc:
        CliComDoc_codigos.append(i.cli_cod)
    for j in vet_cliente:
        if j.cli_cod not in CliComDoc_codigos:
            print('\nCliente excluido com sucesso.')
            vet_cliente.remove(j)
    return vet_cliente

def excluir_doc_num(vet_doc, num): #6
    numeros_doc = []
    for i in vet_doc:
        numeros_doc.append(i.num_doc)
    if num not in numeros_doc:
        print('\nCódigo de documento não existente.')
    else:
        for j in vet_doc:
            if j.num_doc == num:
                print('\nDocumento excluido com sucesso.')
                vet_doc.remove(j)
    return vet_doc

def excluir_doc_cliente(vet_doc, cli_codigo): #7
    clientecod_vet_codigo = []
    indices = []
    for i in vet_doc: #salvar o codigo dos clientes que possuem documentos
        clientecod_vet_codigo.append(i.cli_cod)
    if cli_codigo in clientecod_vet_codigo: #ver se o 'codigo inserido' possui documentos
        ind = 0 #armazenar o indice
        for documento in vet_doc:
            if documento.cli_cod == cli_codigo: #ver se o 'codigo inserido' é igual a o cli_cod do vetor documentos
                indices.append(ind) #guardar indice dos documentos que tem o mesmo cli_cod que foi inserido
            ind += 1 #aumentar em 1 o indice toda vez que repete
        for j in indices:
            print('\nDocumentos excluidos com sucesso.')
        vet_doc.pop(j) #excluir todos os 'indices' do vetor 'vet_doc'
    else:
        print('\nNenhum documento encontrado.')
    return vet_doc

def Excluir_DocData(data_i, data_f, vet_doc):
    for i in vet_doc:
        if data_i < i.dia_venc and data_f > i.dia_venc: #excluir com DATA DE VENCIMENTO dentro do periodo
            print('\nExclusão bem sucedida.')
            print(f'Foi excluido o documento de número: {i.doc_num}')
            vet_doc.remove(i)
    return vet_doc

def alterar_cliente(vet_cliente, cliente_cod):
    for i in vet_cliente:
        if i.cli_cod == cliente_cod:
            i.nome = input('Digite o novo nome do cliente: ')
            i.fone = int(input('Digite o novo telefone do cliente: '))
    print('\nAlteração realizada com sucesso.')
    return vet_cliente

def visualizar_doc_cliente(vet_doc, cli_codigo):
    qtde_doc = 0
    for i in vet_doc:
        if i.cli_cod == cli_codigo:
            qtde_doc += 1
    return qtde_doc

def main():
    clientes = []
    documentos = []
    op = Menu(clientes, documentos)
main()