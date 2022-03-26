"""
While em Python - Aula 34
Utilizando para realizar ações enquanto
uma condição for verdadeira
Requisitos : Entender condições e operadores
"""

# Enquanto a condição for verdadeira, irá repetir o código
contador = 0
while contador < 2:
    nome = input('Qual o seu nome ? ')
    print(f'Olá {nome}!')
    # contador irá receber ele e irá somar mais um para não travar o contador em somente um número
    # fazendo que o código rode até determinado número da condição do while
    contador += 1
    print(f'Valor do contador: {contador}')
print('')
# Para exibir uma contagem com número até tanto valor
print('Exibindo uma contagem!')
g = 1
while g < 5:
    # caso eu queira pular o numero 3
    if g == 3:
        g = g + 1
        print('Pulei o número 3.')
    print(f'Número {g}!')
    # g recebe ele mesmo e mais um, para avançar até chegar na condição do while
    g = g + 1
# continue e break
# continue é utilizado para pular para o próximo laço
# já o break, irá parar toda repetição
print('UTILIZANDO O CONTINUE')
z = 0
while z <= 5:
    if z == 3:
        z = z + 1
        print('Irá pular.')
        # ele irá pular para o próximo laço, mas antes tenho que adicionar um valor para o contador
        continue
    print(f'Número atual de Z é: {z}')
    z = z + 1
# o break irá forçar a saida do loop
c = 0
print('UTILIZANDO O BREAK')
while c <= 10:
    # caso eu queira parar no 4
    if c == 4:
        print('O break irá finalizar o laço agora.')
        break
    print(f'O número atual de C é {c}')
    c = c + 1
print('')
# uma mini tabela
x = 0 # Coluna
y = 0 # linha

while x < 2:
    y = 0 # para reiniciar as linhas para ir para a próxima coluna
    while y < 2:
        print(f'X={x} e Y={y}')
        y += 1

    x += 1

# Criando uma mini calculadora utilizando o while
print('')
print('Calculadora')
while True:
    sair = input('Deseja sair ? [s]im ou [n]ão: ')

    if sair == 's':
        print('Finalizando')
        break
    num1 = input('Digite um número: ')
    num2 = input('Digite um outro número: ')
    operador = input('Digite um operador (+,-,* ou /): ')


    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        if operador == '+':
            resultado = num1 + num2
            print(f'Resultado da soma é: {resultado}')
        elif operador == '-':
            resultado = num1 - num2
            print(f'Resultado da subtração é: {resultado}')
        elif operador == '*':
            resultado = num1 * num2
            print(f'Resultado da multiplicação é: {resultado}')
        elif operador == '/':
            resultado = num1/num2
            print(f'Resultado da divisão é: {resultado}')
        else:
            print('Digite um operador válido')
    else:
        print('Digite números inteiros!')
    print('')

print('Acabou o código!')


