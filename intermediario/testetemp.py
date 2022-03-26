"""
2 - Crie uma função1 que receba uma função2 como parâmetro e retorne o valor da função2 executada.
Faça uma função  executar duas funções que recebam um número diferente de argumentos.
"""

# A função mestre está repassando args e kwargs, repassando eles para a função
#
def funcaoo_mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'OLÁ! {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao}! {nome}!'

# estou passando para a função mestre, minha função fala_oi.
# a função mestre vai repassar somente o nome para a função
executar = funcaoo_mestre(fala_oi, 'Lucas')
print(executar)

executar2 = funcaoo_mestre(saudacao, 'Lucas', 'Bom dia!')
print(executar2)

