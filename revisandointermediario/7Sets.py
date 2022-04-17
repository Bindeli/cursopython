"""
Sets em Python

Os conjustos são bem similares a listas e tuplas em Python

São uma coleção de elementos que você pode adicionar dentro de uma mesma estrutura de dado

Porém a maior diferença entre as listas e as tuplas, os sets só suportam elementos únicos
EX : set1 = {1,2,3,4,5}
Elementos imutáveis

A diferença entre criar set e dicionário em Python é que sets não tem par de chave/valor
Sets só recebem valores
Seria como você estivesse criando uma lista, porém utilizando as chaves {}

Funções :
add - adicionar
update - atualizar
clear
discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
defference - (elementos apanas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

"""

set1 = {1,2,3,4,5}
# não possui um par de chaves/valores, aqui só temos valores.
"""
Aqui também não há índices, então não dá para acessar um determinado valor diretamente do set
Mas podemos iterar
"""
for valores in set1:
    print(f'Valor: {valores}')
"""
Uma outra maneira de criar sets :
Se eu deixar o conteúdo vazio, não estarei criando um set, esterei criando um dicionário
Set = {}, irá virar um dicionário
Se eu quiser criar um set vazio, devo utilizar a função ""set""

"""
set_teste1 = set()
# Caso eu queira adicionar elementos ao set, eu utilizo a função add
set_teste1.add(1)
set_teste1.add(8)
set_teste1.add(5.2)
set_teste1.add(('Tupla',2,'Lucas'))
print(f'\nImprimindo o set que era vazio: {set_teste1}')
# caso eu queira remover um elemento do Set eu utilização a função ""discard"", e informamos o elemento que iremos remover
set_teste1.discard(8)
print(f'Após ter removido o elemento 8 com discard: {set_teste1}')
"""
Outra função é o ''update'', é bem similar ao add, porém aqui, ele recebe um iteravel
e ela itera sobre esse elemento
Por exemplo a string 'python', ela irá iterar cada elemento dessa String
"""
set_teste1.update('a')
set_teste1.update('Python')
print(f'Após utilizar a função update: {set_teste1}')
"""
Os sets não respeitam ordem, e a cada hora, pode ser que seu elemento apareça em uma ordem diferente que você criou
Com a função update, geralmente mandamos uma lista
Criando um outro set abaixo:
"""
set_teste2 = set()
set_teste2.update([1,9,7,5,4,10,11,2,3,4], {6,7,4,5,3})
print('\nUm outro Set, porém foi adicionado com update contendo uma Lista e um Set')
print(set_teste2)
print(f'Os elementos duplicados foram ignorados')
"""
Os sets não aceitam elementos duplicados, como eu mandei dois elementos de 7,5,4,3 não irão aparecer
Podem ser utilizados para remover itens duplicados de uma lista
"""
print(f'\nOs Sets podem ser utilizados para remover elementos duplicados de uma lista, exemplo:')
lista1 = [1,2,3,4,5,6,1,3,4,7,4,'Lucas','Lucas','lucas']
print(f'Lista a ser editada: {lista1}, seu tipo: {type(lista1)}')
#irei fazer um cast da lsita em um set
lista1 = set(lista1)
print(f'Após ser transformada em set : {lista1}, seu tipo: {type(lista1)}')
# agora não possui mais elementos duplicados, e podemos voltar para lista
lista1 = list(lista1)
print(f'Agora voltou a ser uma lista: {lista1}, seu tipo: {type(lista1)}')
# pode acontecer que volte em fora de ordem
"""
Função Union - unir dois sets, utilizando o sinal |
"""
set_1 = {1,3,4,8,2,9}
set_2 = {10,2,3,4,6,4,7}
set_unidos = set_1|set_2
print(f"\nUtilizando a função union para unir dois set's:")
print(f'Set 1 : {set_1}')
print(f'Set 2 : {set_2}')
print(f'União: {set_unidos}')
"""
Intersection - elementos presentes nos dois sets, sinal = &
"""
print(f'Verificando elementos semelhantes intersection &')
set_inter1 = {1,3,4,6,7,2,7,9,11,13,45}
set_inter2 = {0,8,4,6,1,3,5,7,11}
set_interf = set_inter1 & set_inter2
print(f'Set 1 : {set_inter1}')
print(f'Set 2 : {set_inter2}')
print(f'Set unido : {set_interf}')

"""
Difference - elementos únicos apenas no set da esquerda, sinal -
"""
set_dif1 = {1,2,3,4,67,94,31,44,0}
set_dif2 = {0,13,4,1,14,49,7,6,10,7,8}
set_final1 = set_dif1 - set_dif2 # Aqui vero ver elementos unicos do primeiro
set_final2 = set_dif2 - set_dif1 # Aqui vero ver elementos unicos do segundo
print('\nVendo elementos unicos com Difference - ')
print(f'Set 1 : {set_dif1}')
print(f'Set 2 : {set_dif2}')
print(f'Set 1, elementos únicos do 1 : {set_final1}')
print(f'Set 2, elementos únicos do 2 : {set_final2}')

"""
Symmetric_difference - elementos que estão nos dois Sets, mas não em ambos, sinal = ^
irá pegar os valores únicos de ambos os sets, que não são repetidos
"""
set_sym1 = {1,2,3,4,6,8,6,4,9,2,1}
set_sym2 = {0,12,3,4,56,8,42,6,7}
set_symfinal = set_sym1 ^ set_sym2
print(f'\nSymmetric_difference : irá pegar os valores únicos de ambos os sets: ')
print(f'ignorando os repetidos')
print(f'Set 1 : {set_sym1}')
print(f'Set 2 : {set_sym2}')
print(f'Elementos únicos de ambos : {set_symfinal}')
print('\nUtilizando os sets para retirar elementos duplicados de uma lista: ')
lista_final = ['Lucas','Bindeli','Motta']
print(f'Como a lista deve ficar : {lista_final}')
lista_original = ['Lucas','Bindeli','Motta','Motta','Bindeli','Lucas','Lucas']
print(f'Lista com elementos duplicados: {lista_original}')
print(f'Verificando se são iguais : {lista_final == lista_original}')
# vamos remover os elementos duplicados transformando-o em Set
lista_original = list(set(lista_original)) # converti em Set, e depois em lista
lista_final = list(set(lista_final)) # convertendo para ficar igual a ambas
print(f'Estado atual da lista que tinha elementos duplicados : {lista_original}')
print(f'Exemplo de lista como deveria ficar: {lista_final}')
print(f'Verificando se agora estão iguais: {lista_original == lista_final}')

"""
Um exemplo para não modificar a lista é utilizar if e else
Como no exemplo abaixo
"""
print('\nUtilizando If e Else com set para não modificar a lista:')
lista_exemplo1 = ['Lucas','João', 'Maria']
lista_exemplo2 = ['João','Lucas', 'Maria','Maria' ,'Lucas','Lucas','Lucas']

if set(lista_exemplo1) == set(lista_exemplo2):
    print(f'As listas são iguais!')
else:
    print(f'São diferentes')
print(lista_exemplo1)
print(lista_exemplo2)
# como podemos ver, não foi alterado

print(f'\nResumindo tudo: ')

meu_set = {1, 2, 3, 4, 1}
meu_set_2 = set([1, 2, 8, 9, 10])

# União
print("União")
print(meu_set | meu_set_2)
print(meu_set.union(meu_set_2))

# Interseção
print("Interseção")
print(meu_set & meu_set_2)
print(meu_set.intersection(meu_set_2))

# Diferença
print("Diferença")
print(meu_set - meu_set_2)
print(meu_set.difference(meu_set_2))

# Diferença Simétrica
print("Diferença Simétrica")
print(meu_set ^ meu_set_2)
print(meu_set.symmetric_difference(meu_set_2))
