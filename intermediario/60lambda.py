"""
AULA 60 - Expressões com lambda - Funções anônimas em python

a = lambda x, y: x * y

lista.sort(key=lambda item: item[1])
( o sort é para ordernar, só servindo de exemplo )

Posso passar quantos parâmetros eu quiser separados por vírgula
Não preciso dos parênteses para passar os argumentos
e também não preciso da palavra return, sempre que coloco o valor, já irá returnar o valor

"""
def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)
print(f'Resultado : {var}')

# As funções lambda são funções anônimas
# A função abaixo é anônima, pois não possui nome

a = lambda x, y: x * y # Essa expressão é a mesma coisa que a função acima
print(f'Resultado : {a(2,2)}')
# ambos terão o mesmo resultado
print(' ')
# a utilidade é quando você precisa passar uma função por parâmetro para outra função ou para algum método de outra classe
# Exemplo
# suponha que temos uma lista, e dentro desta lista, temos outras listas.
# temos produtos e seus valores
lista = [
    ['Produto1', 11],
    ['Produto2', 8],
    ['Produto3', 18],
    ['Produto4', 4],
    ['Produto5', 30],
]

# suponhamos que eu queria ordenar a lista pelo preços
# a função de lista tem dois modos de você ordenar uma lista em Python
# Como esta aqui: lista.sort()
# Que vai alterar a ordem da lista
# porém vai acontecer nada, pois há lista dentro de lista, e o interpretador não sabe o que fazer

# então irei criar uma função que irá receber o item e sua chave
def func_s(item): # função que recebe um item
    return item[1] # e retorna um item com a chave que eu quero que ordene

# irá pegar o índice 1 como exemplo para ser ordenardo
# Utilizamos a função """sort""" para organizar ordenadamente
# sendo key a chave de qual modo será organizado, no exemplo, será pelo função
# parâmetro key que especifica uma função a ser chamada para cada elemento da lista antes de ser realizada a comparação
lista.sort(key=func_s)
# por isso criamos a função que irá receber um item e retornando um item com a chave escolhida
# caso eu queira inverter, ficaria deste jeito :
# lista.sort(key=func_s, reverse=True)
print(f'Lista ordenada: {lista}')
print(' ')
# Tive que criar uma função só para ordenar, porém as expressões lambda podem ajudar de maneira mais simples
print('Utilizando lambda:')
lista_copia = [
    ['Produto1', 11],
    ['Produto2', 8],
    ['Produto3', 18],
    ['Produto4', 4],
    ['Produto5', 30],
]
# Com a função lambda podemos fazer deste jeito :

lista_copia.sort(key=lambda item: item[1])
print(f'Lista Ordenada com Lambda: {lista_copia}')
print(' ')
print('utilizando sorted() ')
# Uma outra forma é chamar o sorted() que cria uma nova lista para não alterar a lista principal
lista1 = [
    ['Produto1', 11],
    ['Produto2', 8],
    ['Produto3', 18],
    ['Produto4', 4],
    ['Produto5', 30],
]
print(f'Lista ordernada : {sorted(lista1, key=lambda i: i[1])}') # crio uma lambda e seleciono o índice que eu desejo utilizar para ordenar
print(f'Lista invertida : {sorted(lista1, key=lambda i: i[1],reverse=True)}') # invertido


# Então sempre que quiser passar uma função para outra função ou algum método que você queira utilizar
# se a função não tiver muito código dentro dela, pode utilizar a lambda

