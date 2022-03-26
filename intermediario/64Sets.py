"""
Sets em Python (Conjuntos) - Aula 64

Os conjuntos são bem similares a listas e tuplas em Python
São uma coleção de elementos que você pode adicionar dentro de uma mesma estrutura de dado

Porém a maior diferença entre as listas e as tuplas, os sets só suportam elementos únicos.
EX : set1 = {1,2,3,4,5}
Elementos imutáveis

A diferença entre criar set e dicionário em python é que sets não têm par de chave/valor
Sets só recebem valores
Seria como você estivesse criando uma lista, porém utilizando as chaves

Funções :
add - adicionar
update - atualizar
clear -
discard -
union | (Une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^  (elementos que estão nos dois sets, mas não em ambos)

"""

set1 = {1,2,3,4,5}
# Não possui par de chaves/valores, aqui só temos valores.
print(f'Set : {set1}, Tipo: {type(set1)}')
# Aqui também não temos índices, então não dá para acessar um valor específico diretamente do set
# Mas tem como iterar
print(f'Iterando o Set1: ')
for valor1 in set1:
    print(f'Valor : {valor1}')
print(' ')

# Uma outra maneira de criar Sets :
# Se eu deixar o conteúdo vazio, não estarei criando um Sets, estarei criando um dicionário
# Ex : Set = {}, isso irá virar um dicionário vazio
# Se eu quiser criar um Set vazio, eu devo utilizar a função """set"""

set_n = set()
# caso eu queira adicionar elementos ao Set, eu utilizo a função """add"""

set_n.add(1) # um valor inteiro
set_n.add(3) # um outro valor inteiro
set_n.add(('Uma','tupla',7,8)) # uma tupla
set_n.add(8.5) # um valor inteiro

print(f'Imprimindo o set_n : {set_n}')
# Caso eu queira remover um elemento do Set:
# Utilizando a """função""" discard e colocamos qual elemento queremos remover
set_n.discard(3) # Aqui irei remover o elemento 3 do Set
print('')
print('Após ter removido o elemento 3 utilizando discard: ')
print(set_n)
print('')
# Uma outra função é o """update""", é bem similar ao add, porém aqui, ela recebe um iteravel
# e ela itera sobre esse elemento
# Por exemplo se eu adicionar 'Python', ela irá iterar sobre cada elemento dessa String
set_n.update('a')
set_n.update('Python')
print('Após ter utilizado a função update no set: ')
print(set_n)
print('')
# os Sets não respeitam ordem, e cada hora, pode ser que seu elemento apareça em uma ordem diferente que você criou
# Com a função update, geralmente mandamos uma lista
# Criando um outro Set
set_2 = set()
set_2.update([1,2,3,4,5], {5,6,7,8})
print('Um outro Set, porém foi adicionado com update contendo uma Lista e um Set:')
print(set_2)
print('')
# Os Sets não aceitam elementos duplicados, como eu mandei dois "5", ele irá aparecer somente uma vez
# Os Sets podem ser utilizados para remover elementos duplicados de uma lista
print('Os Sets podem ser utilizados para remover elementos duplicados de uma lista, exemplo:')
lista1 = [1,2,1,3,4,5,7,6,8,4,5,9,'Lucas','Lucas']
print(f'Lista a ser editada: {lista1}, seu tipo: {type(lista1)}')
# fazendo um cast da lista em um set
lista1 = set(lista1)
print(f'Após transformar em set: {lista1}, seu tipo: {type(lista1)}')
# agora ela não tem mais elementos duplicados
# Agora caso eu queira que ela volte a ser uma
lista1 = list(lista1)
print(f'Agora voltando para lista: {lista1}, seu tipo: {type(lista1)}')
# pode ser que volte em fora de ordem
print('')
# Union - une dois sets, sinal = |
set_union1 = {1,2,3,4,5,8}
set_union2 = {1,3,4,5,6,7}
set_unionfinal = set_union1|set_union2
print(f'União de Set : {set_unionfinal}')
print(' ')

# Intersection - elementos presentes nos dois sets, sinal = &
set_inter1 = {1,2,3,4,5,6,8,9,10}
set_inter2 = {0,2,4,6,8,10,11}
set_interfinal = set_inter1 & set_inter2
print(f'Elementos semelhantes entre os sets: {set_interfinal}')
print(' ')

# Difference - elementos apenas no set da esquerda, sinal = -
set_dif1 = {1,2,3,4,5,6,8,9,10}
set_dif2 = {0,2,4,6,8,10,11}
set_dif_do_1 = set_dif1 - set_dif2 # Aqui quero ver apenas elemetnos unicos do primeiro
set_dif_do_2 = set_dif2 - set_dif1 # Aqui quero ver apenas elementos unicos do segundo
print(f'Utilizando difference para o primeiro : {set_dif_do_1}')
print(f'Utilizando difference para o segundo : {set_dif_do_2}')
# Tipo uma eliminatória, irá aparecer elementos que está apenas no Set da Esquerda, e não no da direita
print(' ')

# Symmetric_difference - elementos que estão nos dois sets, mas não em ambos, sinal = ^
# irá pegar os valores únicos, não repetidos, de ambos os sets
set_sym1 = {1,2,3,4,5,6,8,9,10}
set_sym2 = {0,2,4,6,8,10,11}
set_symfinal = set_sym1 ^ set_sym2
print(f'Elementos únicos de ambos : {set_symfinal}')
print(' ')
# um Exemplo utilizando Set :
print('Duas listas:')
lista_1 = ['Lucas','João', 'Maria']
print(lista_1)
lista_2 = ['João','Lucas', 'Maria','Maria' ,'Lucas','Lucas','Lucas']
print(lista_2)
print(f'Verificando se as duas listas são iguais : {lista_1==lista_2}')
# são diferentes
# retirando os elementos duplicados
print('Utilizando Set para retirar os duplicados')
lista_1 = list(set(lista_1)) # convertendo em Set, e depois em lista
lista_2 = list(set(lista_2)) # convertendo em Set, e depois em lista
print(f'Verificando se as duas listas são iguais : {lista_1==lista_2}')
print(lista_1)
print(lista_2)
print(' ')

# Uma forma de verificar se é igual sem comprometer as listas:
print('Utilizando If e Else com set para não modificar a lista:')
lista_if1 = ['Lucas','João', 'Maria']
lista_if2 = ['João','Lucas', 'Maria','Maria' ,'Lucas','Lucas','Lucas']

if set(lista_if1) == set(lista_if2):
    print(f'Lista1 é igual a Lista2')
else:
    print(f'Lista1 é diferente de Lista2')

print(lista_if1)
print(lista_if2)