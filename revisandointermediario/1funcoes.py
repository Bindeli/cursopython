"""
Funções em Python

"""

def funcao_oi():
    print('Hello! Executando a primeira função!\n')

funcao_oi()

def alt_mensg(arg):
    print(f'Esta é a mensagem: {arg}')

alt_mensg('Um novo começo surge a cada escolha que iremos fazer\n')


def saudacao_1(msg, nome):
    print(f'{msg}, {nome}!!!')

saudacao_1('Bem vindo!!!','Lucas')

print('\nArgumentos nomeados!')

def arg_nomeado(msg = 'Olá! Tudo Bem?', nome='Lucas'):
    print(f'{msg}! {nome}')

arg_nomeado()
arg_nomeado(msg='Bom dia!', nome='João')
print('')
print('Utilizando função para desenvolver uma calculadora simples:\n')

def soma(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    return x/y

while True:
    print('\nSelecione uma operação ou digite s para sair: \n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n[S]Sair')
    opcao = input('Digite sua escolha! R:')
    num1 = 0
    num2 = 0
    resultado = 0
    if opcao == 's' or opcao == 'S':
        break

    if opcao.isnumeric():
        opcao = int(opcao)
        num1 = input('Digite um valor para o primeiro número:')
        num2 = input('Digite um valor para o segundo número:')
        if num1.isnumeric() and num2.isnumeric():
            num1 = int(num1)
            num2 = int(num2)
            if opcao == 1:
                resultado = soma(num1,num2)
                print(f'Resultado : {resultado}')
            elif opcao == 2:
                resultado = subtracao(num1,num2)
                print(f'Resultado : {resultado}')
            elif opcao == 3:
                resultado = multiplicacao(num1,num2)
                print(f'Resultado : {resultado}')
            elif opcao == 4:
                resultado = divisao(num1,num2)
                print(f'Resultado : {resultado}')
            else:
                print('Digite um opcao de operador entre 1 e 4')
        else:
            print('Digite números inteiros!')
    else:
        print('Digite uma opção válida')










