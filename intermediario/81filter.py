"""
AULA 81 - FILTER

Filter - serve para filtrar coisas

variavel = filter(função, objeto)

Vamos utilizar a lista e os dicionarios do arquivo dados.py
"""

#___________________________________________________________________________________________________________
# Utilizando a lista criada na aula anterior, vamos filtrar os valores maiores que 5

from dados import produtos,pessoas,lista

# A função filter, é bem similar a função map, ela recebe uma função
# porém a diferença é que a função filter vai retornar se é verdadeiro ou falso para a expressão

nova_lista = filter( lambda item: item > 5, lista)
# vai retornar um iterador igual o map, então vamos ter que iterar sobre ele
print(f'Printando a nova lista com números maiores que 5:')
print(list(nova_lista))

"""
Então todo elemento que for maior que 5, vai retornar como True e vai continuar na minha lista
E os que voltarem como false, serão removidos na minha nova_lista
"""

#___________________________________________________________________________________________________________
# Agora utilizando list comprehension :
print(f'\nAgora utilizando list comprehension, sem utilizar filter: ')

lista_novacomp = [x for x in lista if x > 5]
print(f'A nova lista: {list(lista_novacomp)}')

#___________________________________________________________________________________________________________
# Agora vamos utilizar um dado um pouco mais complexo, tipo um dicionário :
print(f'\nAgora utilizando um dicionário: ')
print(f'\nQuero pegar os produtos que sejam maiores que 20 reais :')

precos_20mais = filter(lambda pro: pro['preco'] > 20, produtos)
# agora vou iterar sobre ele para ficar mais fácil de ver os dados :
for product in precos_20mais:
    print(product)

#___________________________________________________________________________________________________________
# Se fosse algo mais complexo, podemos criar uma função, assim como map
print(f'\nAgora printando somente os produtos com valor maior que 30:')
def filtre(product):
    if product['preco'] > 30:
        return True
    else:
        return False
    # Se eu não fosse utilizar o else com false, iria voltar como None, que também funcionaria

precos_30mais = filter(filtre, produtos)

for prod in precos_30mais:
    print(prod)
"""
A vantagem de trabalhar com função, invés de lambda, é por que posso reutilizar a função que eu
acabei de criar.
"""
#___________________________________________________________________________________________________________
# podemos utilizar também, algo parecido como no map
# irei criar uma chave chamada caro ou barata
print('\nAgora criei uma nova chave falando se é barato [<= 30] ou caro [>30]:')
def carobarato(produto):
    if produto['preco'] > 30:
        produto['caro'] = True
    else:
        produto['barato'] = True
    return True

caro_barato = filter(carobarato, produtos)

for item in caro_barato:
    print(item)
#___________________________________________________________________________________________________________
# Agora utilizando o dicionário pessoas :
# Verifique quem é maior de idade [ >=18 ]
print(f'\nAgora utilizando o dicionario pessoas')
print(f'Vou pegar as pessoas com idade maior que 18')
def maior_idade(pessoa):
    if pessoa['idade'] >= 18:
        return True


maiores_idade = filter(maior_idade,pessoas)

for pessoa in maiores_idade:
    print(pessoa)
#___________________________________________________________________________________________________________
#




#___________________________________________________________________________________________________________



