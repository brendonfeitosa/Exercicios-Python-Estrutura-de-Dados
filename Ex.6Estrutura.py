'''6. Elabore uma estrutura para representar um Funcionario (código, nome, endereço, salário). Para o membro endereço deve-se criar outra estrutura Endereço (logradouro, número, bairro, cidade). Utilize aninhamento de estruturas para resolver este desenvolvimento. Construa uma função para cada opçao do menu a seguir:
Menu de opções:

1. Cadastrar funcionários
2. Visualizar todos os dados
3. Sair'''

class Logradouro:
    logradouro = ''
    numero = 0
    bairro = ''
    cidade = ''

class TipoFuncionario:
    codigo = 0
    nome = ''
    endereço = Logradouro()
    salario = 0.00

def menu():
    print('\n {:*^40}'.format(' MENU '))
    print('''\n  [ 1 ] Cadastrar funcionários
  [ 2 ] Visualizar todos os dados
  [ 3 ] Sair''')
    opcao = int(input('\nDigite a sua opção: '))
    return opcao

def cadastrar():
    vet_funciocarios = []
    for i in range(2):
        a = TipoFuncionario()
        a.codigo = int(input('\nDigite o código do funcionário: '))
        a.nome = input('Digite o nome completo do funcionário: ')
        a.endereco = Logradouro() #solução encontrada pela Evilin para que entenda o logradouro
        a.endereco.logradouro = input('Digite o logradouro(rua) do funcionário: ')
        a.endereco.numero = int(input('Digite o número da casa do funcionário: '))
        a.endereco.bairro = input('Digite o bairro: ')
        a.endereco.cidade = input('Digite a cidade: ')
        a.salario = float(input('Digite o salário do funcionário: R$ '))
        vet_funciocarios.append(a)
    return vet_funciocarios

def visualizar(vet_funcionarios):
    for i in range(len(vet_funcionarios)):
        print('\nDados dos Funcionários cadastrados!')
        print(f'\n - Código: {vet_funcionarios[i].codigo} - Nome: {vet_funcionarios[i].nome} - Logradouro: {vet_funcionarios[i].endereco.logradouro}, nº {vet_funcionarios[i].endereco.numero} - Bairro: {vet_funcionarios[i].endereco.bairro} - Cidade: {vet_funcionarios[i].endereco.cidade} - Salário: {vet_funcionarios[i].salario}')

def main():
    op = menu()
    while op >= 1 and op <= 3:
        if op == 1:
            vetor_func = cadastrar()
        elif op == 2:
            visualizar(vetor_func)
        elif op == 3:
            print('\nFIM!')
            break
        op = menu()
main()