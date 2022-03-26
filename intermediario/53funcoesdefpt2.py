"""
Funções (def) em Python - Return

def função(var):
    print(var)

"""

# função em python sempre que elas chegam no final delas sem contrar a palavra return
# ela retorna um tipo de dado específico

def funcao(var):
    print(var)

variavel = funcao('Valor que eu quero!')
# ela irá me retornar None
print(variavel)
# none representar um não-valor, nada, utilizado para falar que uma vaiavel não tem um valor.
# retornar um valor boolean False
print('')
print('Utilizando a função com return')
# o return irá receber o valor e repassar o valor

def funcao1(var1):
    return var1
# no momento que ele chega no return, ele para a função, não irá rodar o código abaixo do return

variavel1 = funcao1('Valor que o return irá receber')
print(variavel1)
print('')
print('Utilizando função para fazer divisão: ')

def divisao(n1, n2):
    # Para não receber none ou dar erro de o divisor for zero
    if n2 > 0:
        return n1/n2
    # um outro jeito de resolver este problema
    #if n2 == 0:
    #   return
    #return n1/n2

dividido = divisao(10, 2)
if dividido: # se o dividido for true, irá executar o código do resultado
    print(f'Resultado da divisão: {dividido}')
else:
    print('Conta inválida.')
print(' ')
# Podemos criar uma função que chame outra função
print('Função que chama outra função :')

def fun(var2):
    print(var2)

def dumb():
    return fun

variavel2 = dumb()('Valor para função que foi chamada por outra função')

variavel3 = dumb()
# Função ID checa o id da função na memória do computador
print(id(variavel3), id(fun))
# A Função pode retornar qualquer coisa em python
print(' ')
# Como por exemplo, uma tupla:
def dumb():
    return ('Lucas', 'Bindeli')
    # ou return 'Lucas','Bindeli'

variavel4 = dumb()

print(f'Variável : {variavel4}, Tipo: {type(variavel4)}')
# uma tupla é uma lista que não pode ser alterada!!!!!!!!!!!!!!!!!!!
print(f'Verificando o item com índice 0 da tupla: {variavel4[0]}')
