"""
Enumerate - enumerar elementos da lista # list
Não é um indice
Enumera cada elemento que você tem na repetição
"""

lista = [
    #0        #1     #2
    ['João','Lucas','David'], #0
    ['Fátima','Nathy','Eloa'], #1
    ['Antonio','Bento','Rony'], #2
    ['Arilda','Carol','Mary'], #3
]

# indice 2 da lista mãe, e indice 1 da lista filha
print(f'Imprimindo o primeiro elemento da 2 lista filha: {lista[2][1]}')
print('')
# enumerando uma lista
# enumerada é uma variavel que vai receber a lista enumerada
enumerada = list(enumerate(lista))
# mudando o enumerada para uma lista
print(enumerada)
print(f'Imprimindo o primeiro elemento da lista filha [2][0] : {enumerada[1][1][2]}')
# enumerada [1][1][2] = será no indice 1 da lista mãe, o 1 se refere a lista que foi enumerada
# e o 2 foi para o nome que está dentro da lista de nomes
# quando eu enumero, o indice 0 vira o enumerate e o 1 vira a lista
"""
[    0    1        
    (0, ['João', 'Lucas', 'David']), 
    (1, ['Fátima', 'Nathy', 'Eloa']), 
    (2, ['Antonio', 'Bento', 'Rony']), 
    (3, ['Arilda', 'Carol', 'Mary'])
]
"""
# enumerate não começa só com 0
for v1,v2 in enumerate(lista, 50):
    # vai começar com 50
    print(f'v1:{v1} e v2:{v2}')
    # v1 é do enumarate, e v2 é a lista que foi enumerada
print('')

