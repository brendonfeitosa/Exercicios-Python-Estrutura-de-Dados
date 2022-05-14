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
