"""
1 - Crie uma função1 que receba uma função2 como parâmetro e retorne o valor da função2 executada.
"""
def principal(arg):
    return arg()

def func_2():
    return 'Bem-Vindo ao nosso mundo'

variavel1 = principal(func_2) # sem ser func_2()
print(variavel1)
print('')
"""
2 - Crie uma função1 que receba uma função2 como parâmetro e retorne o valor da função2 executada.
Faça uma função  executar duas funções que recebam um número diferente de argumentos.
"""

# A função mestre está repassando args e kwargs, repassando eles para a função
#
def funcao_mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'OLÁ! {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao}! {nome}!'

# estou passando para a função mestre, minha função fala_oi.
# a função mestre vai repassar somente o nome para a função
executar = funcao_mestre(fala_oi, 'Lucas')
print(executar)

executar2 = funcao_mestre(saudacao, 'Lucas', 'Bom dia!')
print(executar2)




