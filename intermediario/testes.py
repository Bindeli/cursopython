operador = ''

while operador != 's':

    num1 = input('Digite um número: ')
    num2 = input('Digite um segundo número: ')
    operador = input('Digite um operador (+ - * /) : ')

    if not num1.isdigit() or not num2.isdigit():
        print('Digite um número!')
    else:
        num1 = int(num1)
        num2 = int(num2)
        if operador == '+':
            print(f'Soma: {num1+num2}')
        elif operador == '-':
            print(f'Subtração: {num1-num2}')
        elif operador == '*':
            print(f'Multiplicação: {num1*num2}')
        elif operador == '/':
            print(f'Divisão: {num1/num2}')
        elif operador == 's':
            print('Saindo...')
        else:
            print('Escolha um operador!')
