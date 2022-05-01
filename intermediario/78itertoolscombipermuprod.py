"""
AULA 78 - COMBINATIONS, PERMUTATIONS E PRODUCT - Itertools
Combinations
Combinação
Permutação
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

# ---------------------------------------------------------------------------------
# imagine que eu tenha uma lista de pessoas
pessoas = ['Andre','Lucas','Marcelo','Nildson']
print(f'Lista de pessoas : {pessoas}')
# suponha que eu queira saber todas as combinações possíveis desta lista
# a ordem não me importa neste momento, pois só quero saber as combinações possíveis
# posso fazer da seguinte maneira

# ---------------------------------------------------------------------------------

# importando combinations
from itertools import combinations

# eu chamo a função combinations, indico a variavel e em quantas combinações eu quero, no caso 2
print(f'\nUtilizando o combinations : ')
for grupos in combinations(pessoas, 2):
    print(grupos)

# A ordem não importa, pois no primeiro, 'Lucas' e 'André, já temos uma combinação
# Então não teremos a combinação na ordem 'André' e 'Lucas', pois os elementos já foram combinados



# ---------------------------------------------------------------------------------

# Se a ordem para você, for importante, onde todas as palavras aparecem em primeiro, seguido pelas combinações
# EX : 'Lucas' e 'André'  /  'André' e 'Lucas'
# Podemos utilizar Permutations :
print(f'\nUtilizando o permutation :')

from itertools import permutations

for grupo in permutations(pessoas, 2):
    print(grupo)

# Agora todos os nomes irão aparecer primeiro, juntos de suas duplas
# Mas combination e permutation não gera combinações como 'Lucas' e 'Lucas'

# ---------------------------------------------------------------------------------
# Se eu quiser ter valores repetidos e com a ordem importando
# Vou precisar utilizar o Product !!!!!!!!!!!!!!!

from itertools import product
print('\nUtilizando o product :')

# Agora eu irei colocar o repeat
for duplas in product(pessoas, repeat=2 ):
    print(duplas)


# ---------------------------------------------------------------------------------




