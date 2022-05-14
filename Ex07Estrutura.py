'''7. Elabore uma estrutura para representar um Produto (código, nome, data_fabricacao, data_validade, preço). Para o membro data_fabricacao e data_validade, deve-se criar outra estrutura Data (dia, mês, ano). Utilize aninhamento de estruturas para resolver este desenvolvimento. Construa uma função para cada opçao do menu a seguir:
Menu de opções:
1. Cadastrar produtos
2. Visualizar todos os dados
3. Sair'''

class DataFabricacao:
    dia = 0
    mes = 0
    ano = 0

class DataValidade:
    dia = 0
    mes = 0
    ano = 0

class Produto:
    codigo = 0
    nome = ''
    data_fabricacao = DataFabricacao()
    data_validade = DataValidade()
    preco = 0.00

def menu():
    print('\n{:*^40}'.format( ' MENU '))
    print('''\n  [ 1 ] Cadastrar produtos
  [ 2 ] Visualizar todos os dados
  [ 3 ] Sair''')
    opcao = int(input('\nDigite a sua opção: '))
    return opcao

def cadastrar():
    vet_prod = []
    for i in range(2):
        a = Produto()
        print('\n{:-^40}'.format(' Cadastre um Produto '))
        a.codigo = int(input('\nDigite o código do produto: '))
        a.nome = input('Digite o nome do produto: ')
        a.data_fabricacao = DataFabricacao()
        print('\n{:-^40}'.format(' Data de Fabricação '))
        a.data_fabricacao.dia = int(input('\nDigite o dia da fabicação: '))
        a.data_fabricacao.mes = int(input('Digite o mês de fabricação: '))
        a.data_fabricacao.ano = int(input('Digite o ano de fabricação: '))
        a.data_validade = DataValidade()
        print('\n{:-^40}'.format(' Data de Validade '))
        a.data_validade.dia = int(input('\nDigite o dia da validade: '))
        a.data_validade.mes = int(input('Digite o mês da validade: '))
        a.data_validade.ano = int(input('Digite o ano da validade: '))
        a.preco = float(input('Digite o preço do produto: R$ '))
        vet_prod.append(a)
    return vet_prod

def visualizar(vet_prod):
    cont = 0
    for i in range(len(vet_prod)):
        print('\n| Código do produto: {} | Nome: {} | Data de fabricação: {}/{}/{} | Data de validade: {}/{}/{} | Preço: R$ {:.2f}'.format(vet_prod[i].codigo, vet_prod[i].nome, vet_prod[i].data_fabricacao.dia, vet_prod[i].data_fabricacao.mes, vet_prod[i].data_fabricacao.ano, vet_prod[i].data_validade.dia, vet_prod[i].data_validade.mes, vet_prod[i].data_validade.ano, vet_prod[i].preco))
        cont = i + 1
    if cont > 1:
        print('\nFim dos resultados!')

def main():
    v_prod = []
    op = menu()
    while True:
        if op == 1:
            v_prod = cadastrar()
        elif op == 2:
            visualizar(v_prod)
        elif op == 3:
            break
        elif op != 1 or op !=2 or op != 3:
            print('\nOpção Inválida, tente novamente!')
        op = menu()
main()