"""
Operadores relacionais
== > >= < <= !=
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente

O resultado deles será um valor booleano
"""
variavel = 'Valor' # variavel recebe valor, só tem um sinal de igual

# Para comparar se uma coisa é igual a outra, utiliza dois iguais ==
print(f'Irá aparecer True 2 == 2:', 2 == 2) # vai aparecer True na tela
print(f'Irá aparecer False 2 == 1:', 2 == 1) # vai aparecer False na tela

# Posso criar uma expressão que recebe o resultado da comparação também
num1 = 2
num2 = '2'
# Uma é string e a outra é inteiro, então vai dar False
expressao = num1 == num2
print(f'Valor da Expressao : {expressao}')
print('')
print('Utilizando o sinal > maior que e também o >= maior que ou igual a :')
print(f'Resultado de 2 > 1: ', 2 > 1) # Vai dar True
print(f'Resultado de 2 >= 2 ', 2 >= 2) # vai dar true
print(f'Resultado, verificando se 2 >= 3: ', 2 >= 3) # vai dar False
print('Utilizando o sinal < menor que e também o <= menor que ou igual a')
print(f'Resultado de 4 < 5: ', 4 > 5) # Vai dar True
print(f'Resultado de 5 <= 5 ', 5 <= 5) # vai dar true
print(f'Resultado, verificando se 5 <= 3: ', 5 <= 3) # vai dar False
print('')
print('Verificar se duas expressões são diferentes')
print(f'Verificando se 2 é diferente de 2: 2!=2 é ', 2!=2)
print(f'Verificando se 2 é diferente de 4: 2!=4 é ', 2!=4)
print('')
print('Verificando se uma pessoa possui idade maior que 18 anos para pegar empréstimo:')
nome = input('Qual o seu nome? R:')
idade = int (input('Qual a sua idade? R:')) # utilizei o int para transformar a string em inteiro

idade_limite = 18 # limite para pegar empréstimo

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')
print('')
print('Checagem para verificar se tem entre 20 a 30 anos.')
idade_menor = 20
idade_limite = 30

# and é utilizado para fazer duas comparações
if idade >=idade_menor and idade <= idade_limite:
    print(f'{nome} possui uma idade entre 20 a 30 anos.')
else:
    print(f'{nome} não possui uma idade entre 20 a 30 anos.')
