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

def cadastrar():
    




def main():
    v_prod = []
    op = menu()
    while True:
        if op == 1:
            v_prod = cadastrar()
        elif op == 2:
            visualizar(v_prod)
        elif op == 3:
            print('{:-^*40}'.format('FIM!'))
            break
        elif op != 1 or op !=2 or op != 3:
            print('Opção Inválida, tente novamente!')
main()
    
