print('Lucas')
print(123456)
print(10.5)
print('Lucas','Bindeli','da','Motta', sep='-')
print('Lucas','Bindeli', sep='.')
print('Conteúdo no final: ', end='&%&%')
print('') # o end puxa a próxima linha para ficar no final
print('167','213','578', sep='.', end='-')
print('18')
# deste modo o 18 ficará no final do print anterior
print('')
print('Desafio 1:')
"""
Criar variaveis para nome, idade, altura e peso
Apresentar o ano atual 
Obter o ano de nascimento da pessoa
Obter o imc da pessoa com 2 casas decimais
utilizando f-string

"""
nome = 'Lucas'
idade = 25
altura = 1.68
peso = 88.2
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso/ altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')

"""
Operadores Aritmeticos
+ soma
- subtração
* multiplicação
/ divisão
// divisão inteira
** um número elevado ao outro, potencia
% retorna o resto da divisão
() altera a precedencia das contas
"""
print('')
print('Mesmo desafio anterior só que com input')
# utilizamos o input para receber um dado digitado do usuário

nome1 = input('Qual é o seu nome? R:')
idade1 = input('Qual a sua idade? R:')
altura1 = input('Qual a sua altura? (use . para separar) R:')
peso1 = input('Qual o seu peso ? (use . para separar) R:')
ano_atual1 = input('Qual o ano atual ? R:')

idade1 = int(idade1)
altura1 = float(altura1)
peso1 = float(peso1)
ano_atual1 = int(ano_atual1)

nascimento1 = ano_atual1 - idade1
imc1 = peso1 / altura1 ** 2

print(f'{nome1} tem {altura1} de altura e pesa {peso1}KG.')
print(f'O IMC de {nome1} é de {imc1:.2f}')
print(f'{nome1} nasceu em {nascimento1}')

