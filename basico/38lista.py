"""
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# a diferença de lista para variavel, é que a variavel só tem um valor, já a lista tem vários
texto_exemplo = 'Valor'
lista_exemplo = [1,2,3,4] # contem 4 valores
# ela suporta vários tipos
lista_dem = [1,2,3,4, 'string', 10.1, True]
# tem que abrir e fechar o []
# na lista, temos indices
# indices       0   1         2   3   4  5  6   7
lista_teste = ['A','Bindeli','C','D','E',1 ,3, 10.5]
# indices   -   8   7         6   5   4  3  2   1
print(lista_teste)
print('')

# -----------------------------------------------------------------------------------------------
# caso eu queira acessar o valor a, posso utilizar os índices para pegar tal valor

print(f'Acessando o item 1 da lista: {lista_teste[1]}')
# Caso eu queira modificar algum valor, como por exemplo, no indice 6
lista_teste[6] = 'NovoValor'
print(lista_teste)

# -----------------------------------------------------------------------------------------------
lista_1 = [1,2,3]
lista_2 = [4,5,6]
print(f'Lista 1: {lista_1}')
print(f'Lista 2: {lista_2}')
#concatenando lista
lista_3 = lista_1+lista_2 # junção da lista 1 com a lista 2
print(f'Lista 3: {lista_3}')

# -----------------------------------------------------------------------------------------------
# para uma lista receber valores de uma outra lista sem alterar a outra lista, utilizamos """extend"""
# a primeira lista irá receber elementos da segunda

lista_4 = [7,8,9]
lista_4.extend(lista_2)
print(f'Lista 4 com extend (com a lista 2): {lista_4}')
# -----------------------------------------------------------------------------------------------
# dá para inserir também só um valor para a lista
# exemplo, lista.extend('a'), será adicionado o valor "a" no final da lista
lista_4.extend('a')
print(f'Lista 4 adicionando somente 1 elemento com extende: {lista_4}')
# -----------------------------------------------------------------------------------------------
# porém normalmente quando queremos adicionar um elemento a uma lista, utilizando o """append"""
# será adicionado um valor no final da lista
# caso eu queira adicionar na lista 2, o valor b
lista_2.append('b')
print(f'Lista 2, adicionando b com append : {lista_2}')
# -----------------------------------------------------------------------------------------------
# Para inserirmos onde nós quisermos um valor na lista, podemos utilizar o """insert"""
# eu coloco o indice que irá ser inserido o valor e também o valor
lista_2.insert(0, 'Lucas')
print(f'Lista 2 alterado com insert: {lista_2}')

# -----------------------------------------------------------------------------------------------
# quando eu quero remover o último valor da lista, eu utilizo o """pop"""
lista_2.pop()
print(f'Lista 2 com o último elemento removido com pop: {lista_2}')
#
lista_5 = [1,2,3,4,5,6,7,8,9]
print(f'Nova lista criada: Lista 5 {lista_5}')

# -----------------------------------------------------------------------------------------------
# caso eu queira excluir elementos em uma determinado posição, utilizamos o """del"""
del(lista_5[3:5]) # vou excluir os valores do indice 3 até o 5
#lembrando que o limite não será excluir, no caso o indice 5
print(f'Lista 5 após excluir os elementos do indice 3 e 4: {lista_5}')
print('')

# -----------------------------------------------------------------------------------------------
# para sabermos qual é o maior e o menos valor da lista:
# utilizamos o min() e o max()
print(f'Maior valor da lista 5: {max(lista_5)}')
print(f'Menor valor da lista 5: {min(lista_5)}')
print('')
# para adicionar elementos sem ser manualmente, podemos utilizar o range
# porém o range não me retorna uma lista, retorna um objeto range
lista_6 = range(1, 5) # vai printar range(1, 5)
print(f'Lista 6 utilizando range : {lista_6}')

# -----------------------------------------------------------------------------------------------
# porém o Python tem uma função """list"""
# uma função built-in que converte um objeto iteravel em uma lista
lista_7 = list(range(1,5))
# com isso a função list junto com o range me retornou uma lista com todos os números possiveis
# dentro do alcance do range, de 1 a 4, pois termina em 5 e o 5 não irá entrar.
print(f'Lista 7 com range porém com a função list : {lista_7}')
# lista também é um objeto iteravel, podendo utilizar também um for
# a variavel soma vai ser para somar todos os elementos que passarem pelo laço for
soma_lista7 = 0
for valor in lista_7:
    print(f'Valor : {valor}')
    soma_lista7 += valor
print(f'A soma de todos os elementos da Lista 7 é : {soma_lista7}')
print(f'lista FINAL : {lista_2}')
del lista_2[0:2]
print(f'Depois do del : {lista_2}')
