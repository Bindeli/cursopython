"""
Zip - Unindo iteráveis
Zip_longest - itertools

Esta função retornar uma lista de tuplas!!!!!!!!!!!!!!!!!!
Porém ao utilizarmos um print, irá mostrar que ela aponta para um objeto instanciado
Exemplo :
zip(x, y)
<zip object at 0x7faded7b3608>

Para visualizarmos podemos transformar em uma lista com list
ou utilizar um for

"""

cidades = ['Cariacica','Belo Horizonte','Salvador','São Paulo','Viana']
estados = ['Espirito Santo', 'Minas Gerais','Bahia']

# eu quero que cada cidade esteja associado com seu estado

cidades_estados = zip(cidades, estados)
# isso irá criar um gerador, se eu der print agora, irá aparecer o tipo dele
print(cidades_estados)
# para visualizar, irei utilizar o next, para ver o próximo passo
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))

# mas o correto é trabalhar com for
for valor in cidades_estados:
    print(valor)

"""
Poderia juntar mais de uma lista,

cidades_estados = zip(estados, cidades, outro)

"""

# -----------------------------------------------------------------------------------------------------------
"""
A função zip junto a primeira lista com a segunda lista 
Os elementos da primeira lista ficarão na frente dos elementos da segunda lista
Para inverter o exemplo, só colocar zip(estados, cidades)
"""

# Exemplo de uso utilizando um dicionário, invertendo os valores e as chaves
print('\nInvertendo valores e chaves de um dicionário utilizando zip')
produtos = {
    'Refrigerante' : 10.00,
    'Salgado' : 6.50,
    'Doce' : 2.00,
    'Cerveja': 8.50
}

produtos_lista = list(zip(produtos.values(), produtos.keys()))
# vai retornar uma lista
for item in produtos_lista:
    print(item)

print(f'\nLista inteira : {produtos_lista}')

#------------------------------------------------------------------------------------------------

"""
Listas de tamanhos diferentes serão equiparadas e a diferença entre elas será desconsiderado.
Ele irá unir até a quantidade que tem a menor lista, no exemplo, a menor possui 4 elementos
Então ele irá juntar 4 vezes

Como no exemplo abaixo:
"""
print('\nQuando temos duas listas de tamanhos diferentes:')
print('Serão equiparadas e a diferença desconsiderada:')
lista_1a = [1,2,3,4,5]
lista_1b = [6,7,8,9]

print(f'Primeira lista : {lista_1a}')
print(f'Segunda lista : {lista_1b}')
for x in zip(lista_1a, lista_1b):
    print(x)

#------------------------------------------------------------------------------------------------

"""
Para corrigir isso, e adicionar todos os elementos, utilizamos o zip_longest.
Ele vai pegar a quantidade da maior lista, e os que não possui elemento, terá valor None.
"""
from itertools import zip_longest
# fiz um import, estou importando a função zip_longest da biblioteca itertools
print(f'\nUtilizando o zip_longest')
lista_2a = [1,2,3,4,5,6]
lista_2b = ['Primeiro','Segundo','Terceiro','Quarto']

print(f'Primeira lista : {lista_2a}')
print(f'Segunda lista : {lista_2b}\n')

for itens in zip_longest(lista_2a,lista_2b):
    print(itens)

#------------------------------------------------------------------------------------------------
"""
Para que Não fique com None, podemos utilizar o fillvalue='Qualquervalor'
E preencher com o valor que desejamos que apareça invés de None
"""
print(f'\nUtilizando o fillvalue para preencher o espaço do None')
lista_3a = [1,2,3,4,5,6]
lista_3b = ['Primeiro','Segundo','Terceiro','Quarto']

for itens in zip_longest(lista_3a,lista_3b,fillvalue='Atualizando...'):
    print(f'{itens}')

#------------------------------------------------------------------------------------------------
"""
Importando também o módulo count, um contador
Ele também é um gerador e consome pouco recurso de memória
"""
print('\nAgora importando e utilizando o módulo count')
from itertools import count

indice = count()
cidades_ex = ['São Paulo','Belo Horizonte','Salvador','Monte Belo','Outra']
estados_ex = ['SP','MG','BA']

cidades_estados_ex2 = zip(indice,cidades_ex,estados_ex)

"""
Devo utilizar a função Zip, pois se eu utilizar o zip_longest, irá gerar valores infinitos
Pois o gerador não tem fim, ele vai contando infinitamente
"""

for indice, estado, cidade in cidades_estados_ex2:
    print(indice, estado, cidade)# desempacotando uma tupla tripla


