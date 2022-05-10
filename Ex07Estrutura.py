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
    print('\n{:*^40}'.format( 'MENU '))
    print('''\n  [ 1 ] Cadastrar produtos
  [ 2 ] Visualizar todos os dados
  [ 3 ] Sair''')
    opcao = int(input('\nDigite a sua opção: '))
    return opcao




def main():
    op = menu()
    
