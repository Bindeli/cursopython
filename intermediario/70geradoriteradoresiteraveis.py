"""
AULA 70 - Geradores, Iteradores e Iteráveis

Iteravel é um elemento que você pode iterar sobre ele, mas não necessariamente é um iterador
(ele não necessariamente vai te dar um valor de cada vez)

Iterador ele vai te dar um valor de cada vez sempre que eu precisar desse valor
Iterador tem o método Next, que irá passar a cada comando

Gerador é utilizado quando precisamos utilizar valores que ocupam muita memória
ou vai gastar muito tempo para ser feito
é um iterável, onde podemos utilizar o for, estrutura de repetição

"""
import sys
"""
fornece funções e variáveis usadas para manipular diferentes partes do ambiente de tempo de execução do Python.
Com o módulo sys você pode ,por exemplo, saber qual a plataforma do dispositivo que está rodando o seu código, 
obter os caminhos de sistema que o interpretador Python utiliza, módulos importados, versão do Python, entre outros.
"""


lista = list(range(10))
print(f'Lista inicial : {lista}')
print(f'Tamanho da primeira lista: {sys.getsizeof(lista)}') # quanto de memoria essa lista está consumindo aqui, em bytes

print(f"Verificando se a lista é um iterador: {hasattr(lista, '__next__')}")
# passando para ver se a lista é um iterador

"""
se tiver next, é um iterador

é false, ele é um objeto iterável

utilizando o iter para transformar em um iterador
print(f'Elemento da lista: {next(lista)}'), se eu colocar agora, vai dar erro
tenho que transformar ele em um iterador
"""

lista = iter(lista) # utilizando a função iter

print(f"Agora depois de utilizar o iter : {hasattr(lista, '__next__')}")
# Agora se eu executar o next, irá passar para o próximo elemento
print(f'Elemento da lista: {next(lista)}')
print(f'Elemento da lista: {next(lista)}')
print(f'Elemento da lista: {next(lista)}')

"""
Podemos utilizar os geradores para evitar problema com memória
Quando não precisamos de todos os valores ao mesmo tempo
Quando precisarmos do valor, nós requisitamos o valor e os geradores retornam o próximo valor daquela lista
"""

import time

def gera():
    r = [] # cria uma lista vazia
    for n in range(100): # faz uma iteração com a função range de 0 a 99
        # r.append(n) # e coloca cada valor na lista
        yield n
        # invés de esperar por todos os valores para completar o ciclo, ele irá gerar os valores
        # ele vai puxar um valor de cada vez
        time.sleep(0.1) # dormir 0.1 segundo
        # para simular que está puxando um comando pesado que vai demorar um pouco para executar
    return r

g = gera()

# for v in g:
#     print(v)
# se eu rodar, vai aparecer cada elemento de cada vez sendo chamado
# chamamos de lazy avaliation, ou avaliação preguiçosa

print(f'\nIterador tem o método Next, que irá passar a cada comando')
print(hasattr(g, '__next__'))
print(next(g)) # cada vez que eu utilizar, vou ver o próximo valor
print(next(g))
print(next(g))

def gera2():
    # igual o for mas estou fazendo manualmente
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

variavel = gera2()
print(next(variavel))
print(next(variavel))
print(next(variavel))

lista = list(range(1000))

print(f'\nTamanho da lista : {sys.getsizeof(lista)}') # bytes

lista2 = [x for x in range(1000)]

print(f'Tamanho da lista 2 : {sys.getsizeof(lista2)}') # tamanho dela vai ser de 8856 bytes
print(f'Tipo da Lista2: {type(lista2)}')

# quero transformar em um gerador.
# invés de utilizar os colchetes [], vou utilizar parênteses ()

lista3 = (x for x in range(1000))
print(f'Tipo da lista 3 : {lista3}')
print(f'Tamanho da lista 3 : {sys.getsizeof(lista3)}')
# Gerador gasta pouca memória no computador

"""
As listas vão reter todos os valores que você mandar nela e salvar na memória

Já os geradores vão reter todos os valores, porém ele não irá todos na memória
Só vai te entregar o valor, caso se você pedir
pedimos este valor, pedindo a função Next
ou podemos também o for para iteração
"""

"""
Se eu quero saber se algo é um gerador 

Suponha que eu queira criar uma variavel que contenha a função zip com dois iteradores

"""
# from types import GeneratorType
#
# # variavel = zip('alo','Alou')
#
# #print(list(variavel))
# # Saida = [('a', 'A'), ('l', 'l'), ('o', 'o')]
# # print(next(variavel))
# # print(next(variavel))
#
# # print(isinstance(variavel, GeneratorType))
# # aqui estou perguntando, se "a variavel é um instancia de um gerador ?"
# # vai dar False, pois ele é um iteravel
#
# # Para criar um gerador, podemos utilizar comprehension
# variavel  = ((x,y) for x,y in zip('alo','alo'))
#
# # print(variavel)
# # saida = <generator object <genexpr> at 0x000001D533569B60>
# # devo transformar em lista antes
#
# print(list(variavel))
