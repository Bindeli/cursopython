"""
Expressões com lambda - Funções anônimas (é anônima pois não possui nome, diferente das funções)

a = lambda x,y: x * y

Posso passar quantos parâmetros eu quiser separados por vírgula
Não preciso dos parênteses para passar argumentos
e também não preciso de return, sempre que coloco o valor, já irá dar return no valor

a utilidade é quando você precisa passar uma função por parâmetro para outra função ou para algum método de outra classe
"""
print(f'{"#"*10}LAMBDA{"#"*10}')
# Função para multiplicar x lambda de multiplicação

def func_mult(arg1, arg2):
    return arg1 * arg2

var_ex1 = func_mult(4,4)
print(f'Resultado da função multiplica : {var_ex1}')

# Agora a função lambda

var_ex1lamb = lambda x,y: x*y
print(f'Resultado da lambda multiplica: {var_ex1lamb(4,4)}')

# Ambos tem o mesmo resultado.

"""
A utilidade é quando você precisa passar uma função por parâmetro para outra função ou para algum método de outra classe

Exemplo: Suponha que temos uma lista, e dentro desta lista, teremos outras listas
Exemplo : Produto e seu valor

Suponha que eu queira ordenar a lista pelo preço
Teremos que criar uma função que irá receber o item e sua chave
"""
# iremos criar a função para receber os items com o indice que desejamos utilizar para ordernar
def func_pvalor(item):
    return item[1] # Eu quero ordernar pelo valor no primeiro indice

lista_preços = [
    ['Produto1',14],
    ['Produto2',35],
    ['Produto3',5],
    ['Produto4',11],
    ['Produto5',56],
]

# a lista será ordenada pelo preço
# e iremos utilizar a função """sort""" para organizar ordenadamente
# o parametro para key que especifica uma função a ser chamada para cada elemento da lista antes de ser realizada
# a comparação
lista_preços.sort(key=func_pvalor)

# caso eu queira deixar do maior para o menor, ficaria assim:
# lista_preços.sort(key=func_pvalor, reverse=True)
print(f'Lista ordernada pelo preço: {lista_preços}')

# tive que criar uma função só para ordernar, porém com lambda é mais simples
print('\nUtilizando lambda:')
outra_lista = [
['Produto1',14],
    ['Produto2',35],
    ['Produto3',5],
    ['Produto4',11],
    ['Produto5',56],
]

# utilizando a função lambda:

outra_lista.sort(key= lambda item: item[1])
# primeiro colocamos como parametro lambda, depois a variavel, e colocamos depois a variavel com o indice
print(f'Agora com lambda: {outra_lista}\n')
print('Agora criando uma nova lista com sorted() para não alterar a lista principal:')
lista_nova = [
['Produto1', 11],
    ['Produto2', 8],
    ['Produto3', 18],
    ['Produto4', 4],
    ['Produto5', 30],
]

nova_listaf = sorted(lista_nova, key=lambda item: item[1])
print(f'Lista ordernada : {nova_listaf}')

# Então sempre que quiser passar uma função para outra função ou algum método que você queira utilizar
# se a função não tiver muito código dentro dela, pode utilizar a lambda

print(f'\n{"#"*10}TUPLAS{"#"*10}')
"""
Tuplas, são parecidas com listas, porém tuplas não podem ser alteradas, são imutáveis
Não pode adicionar elementos ou remover
Não pode alterar o valor do indice da tupla
Caso queira modificar o valor, deverá utilizar lista

tuplas = ()   , para tuplas, utilizamos parênteses
"""

tupla_inic = (1,2.5,'Lucas',True) # criada, não pode ser modificada

print(f'Tupla: {tupla_inic}, seu tipo {type(tupla_inic)}')
print(f'Chamando pelo indice[0] : {tupla_inic[0]}')
print(f'Chamando pelo indice[1] : {tupla_inic[1]}')
print(f'Chamando pelo indice[2] : {tupla_inic[2]}')
print(f'Chamando pelo indice[3] : {tupla_inic[3]}\n')
print('Também podemos iterar sobre os valores dela:')
for valor in tupla_inic:
    print(valor)
"""
Também podemos criar as tuplas sem parênteses também, porém quando tiver apenas um elemento, deve ter uma vírgula depois
Exemplo:
tupla = 1, 2.5 ,'Lucas', True
tupla = (),     tupla vazia
tupla = 1,      tupla com somente 1 elemento
"""
print('\nTambém podemos concatenar tuplas')
tupla_conc1 = 1,2,3,4,5
tupla_conc2 = 6,7,8,9
tupla_concf = tupla_conc1 + tupla_conc2
print(f'Tupla para concatenar 1 : {tupla_conc1}')
print(f'Tupla para concatenar 2 : {tupla_conc2}')
print(f'Tupla concatenada: {tupla_concf}')

print(f'\nTambém podemos desempacotar tuplas:')
tupla_desem = 1,2.5,'Lucas','João',10,'Maria',True

n1,n2,n3,n4, *resto = tupla_desem

print(f'N1={n1}, N2={n2}, N3={n3}, N4={n4}')
print(f'Resto : {resto}')

print('\nCaso eu queira mudar algo na tupla, posso converter-la em lista, e depois alterar ela novamente para tupla')
print('Para transformar em lista, eu utilizo a função list(variavel)')
print('Para transformar em tupla, eu utilizo a função tuple(variavel)')
print('Exemplo:')

tupla_mod = (10,9,5,45,30)
print(f'Tupla inicial : {tupla_mod}')
tupla_mod = list(tupla_mod) # transformando em lista
# modificando os valores da tupla:
tupla_mod[0] = 'Nomes:'
tupla_mod[1] = 'Lucas'
tupla_mod[2] = 'André'
tupla_mod[3] = 'Anildson'
tupla_mod[4] = 'Marcelo'
print(f'Tupla modificada para lista: {tupla_mod}, seu tipo atual é: {type(tupla_mod)}')
# neste momento é uma lista
# para voltar para tupla, utilizamos o tuple
tupla_mod = tuple(tupla_mod)
print(f'Tupla modificada para tupla: {tupla_mod}, seu tipo atual é {type(tupla_mod)}')





