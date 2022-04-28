"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
==================================================================== resultado
lista_soma  = [2, 4, 6, 8]
"""

import itertools

lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4,5]

lista_somaAB = []

for num1, num2 in zip(lista_a,lista_b):
  # print(f'Primeiro : {num1}')
  # print(f'Segundo : {num2}')
  lista_somaAB.append(num1+num2)

print(f'Primeira lista : {lista_a}')
print(f'Segunda lista : {lista_b}')
print(f'\nSoma das duas listas: {lista_somaAB}')




