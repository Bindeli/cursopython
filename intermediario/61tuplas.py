"""
AULA 61 - Tuplas em Python

Tuplas é bem parecido com listas
porém tuplas não podem ser alteradas
Não pode adicionar, remover elementos
Não pode mudar o valor do índice da tupla
Caso queira modificar o valor, é melhor utilizar listas

tuplas = ()  para tuplas, utilizamos parênteses
"""

tupla_1 = (1,2,'Lucas', 10.5, True) # depois que eu criei ela, não posso mais modificar
print(f'Criando a primeira tupla : {tupla_1}, seu tipo é {type(tupla_1)}')
# Também podemos chamar pelo índice
print(f'Indice 2 da tupla: {tupla_1[2]}')
# Também podemos iterar sobre essa tupla
for valor in tupla_1:
    print(valor)
# caso eu queira pegar do indice 2 para frente, faço igual na lista
print(f'Valores do indice 2 para frente: {tupla_1[2:]}')
# outra coisa é que podemos criar ela sem os parênteses também
tupla_2 = 1,2,'a','b'
print(f'Um nova tupla: {tupla_2}, seu tipo é {type(tupla_2)}')
tupla_3 = () # uma tupla vazia
tupla_4 = 1, # Caso eu queira criar sem utilizar os parênteses e tenha apenas um valor, tenho que botar a vírgula

# Também podemos concatenar tuplas :
tupla_conc1 = 1,2,3,4,5
tupla_conc2 = 6,7,8,9,10
tupla_conc3 = tupla_conc1 + tupla_conc2
print(f'Tupla concatenada : {tupla_conc3}')
print(' ')
# Também podemos desempacotar tuplas em variaveis
print('Desempacotando tuplas : ')
tupla_d1 = 1,2, 'Lucas', 10.5
tupla_d2 = 'Jose', 'Valentine',7,8
tupla_d3 = tupla_d1 + tupla_d2
n1,n2,n3,n4,n5, *resto = tupla_d3
print(f'n1={n1}, n2={n2}, n3={n3}, n4={n4}, n5={n5}')
print(f'Resto: {resto}')
print(' ')

# também podemos repetir o valor da tupla utilizando o multiplicador
# para aparecer, por exemplo, 10 vezes, 5, 2
print(f'Multiplicando Tuplas 3 vezes:')
tupla_mult = (1,2,'Lucas',10.5) * 3
print(tupla_mult)
print(' ')
# Também podemos converter tuplas em lista, caso desejarmos alterar algum valor
print('Modificando valors de tuplas (transformando em lista para modificar):')
tupla_mod = (1,4,2,5,3)
print(f'Tupla inicial : {tupla_mod}, seu tipo: {type(tupla_mod)}')
# transformando a tupla em uma lista
tupla_mod = list(tupla_mod)
tupla_mod[1] = 2
tupla_mod[2] = 3
tupla_mod[3] = 4
tupla_mod[4] = 5
print(f'Tupla modificada: {tupla_mod}, seu tipo: {type(tupla_mod)}')
# neste momento ela é uma lista
# para voltar para ser tupla
tupla_mod = tuple(tupla_mod)
print(f'Tupla modificada : {tupla_mod}, seu tipo: {type(tupla_mod)}')

