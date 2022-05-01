lista_new = [ item*2 for item in range(1,21)]
print(lista_new)

# ---------------------------------------------------------------------------
lista_letras = ['a','b','c','d','e','f']

lista_maius = [str(item.upper()) for item in lista_letras]
print(f'\nLista original : {lista_letras} ')
print(f'Letras maiúsculas: {lista_maius}')

# ---------------------------------------------------------------------------
# Retirar somente os números impares e multiplicar por 2:
"""
List comprehension com if :
""" 

lista_new2 = list(range(1,21))

lista_dobro = [ item*2 for item in lista_new2 if item % 2 == 0 ]

print(f'\nMultiplicando por 2, todos os itens pares da lista original')
print(f'Lista original : {lista_new2}')
print(f'\nLista modificada : {lista_dobro}')

# ---------------------------------------------------------------------------
# Retirar os números multiplos de 2 e também, ao mesmo tempo, de 3:
"""
List Comprehension com mais de um if: 

Podemos verificar condições em duas listas diferentes dentro da mesma list comprehension.
"""
lista_2e3 = [ numeros for numeros in range(100) if numeros % 2 == 0 if numeros % 3 == 0 ]

print(f'\nLista com multiplos de 2 e também 3:')
print(f'Lista: {lista_2e3}\n')

# ---------------------------------------------------------------------------
"""
Outra forma de se utilizar expressões condicionais e list comprehension é usar o conjunto if + else.

Por exemplo, queremos criar uma lista que contenha “Sim” quando determinado número for múltiplo de 5 e “Não” caso contrário.

"""
print('Lista que 1 a 20, quando for multiplo de 5, aparece Sim, se não, Não')
lista_result = ['Sim' if item % 5 == 0 else 'Não' for item in range(20)]
print(f'Lista: {lista_result}')
















