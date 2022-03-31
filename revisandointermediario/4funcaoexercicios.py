"""
1 - Crie uma função1 que receba uma função2 como parâmetro e retorne o valor da função2 executada.
"""
print('Exercício 1:')
def func_arg():
    parametro = 'valor do parametro'
    return parametro

def chamafunc(arg):
    print(arg)

variavel_recebe = func_arg().capitalize()
chamafunc(variavel_recebe)

"""
2 - Crie uma função mestre que receba uma função como parâmetro e retorne o valor da função 2 executada.
Faça uma função  executar duas funções que recebam um número diferente de argumentos.
"""
print('\nExercício 2:')
def funcao_mestre(funcao,*args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return print(f'Olá! {nome}')

def saudacao(nome, saudacao):
    return print(f'{saudacao}, {nome}!')

exercutar_func1 = funcao_mestre(fala_oi,'Lucas')

exercutar_func2 = funcao_mestre(saudacao,'Lucas','Bom dia')



