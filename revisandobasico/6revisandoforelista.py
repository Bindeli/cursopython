"""
For in Python
While é utilizando quando não sabemos o final
Já o For, é quando temos algo que sabemos que tem final
iteração string com for
Função range(start = 0, stop, step = 1)

"""
nome = 'Lucas'
for letra in nome:
    print(letra)

# range returna uma sequencia de numeros
print('Crescente:')
for numero in range(5):
    print(numero)
print('Decrescente:')
for numero in range(6,1,-1):
    print(numero)

"""
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
print('')
print('Listas:')
lista_1 = [1,2,3,4,5]
print(lista_1)
print(lista_1[2])
lista_1[4] = 'valor5'
print(f'{lista_1}\n')

print('Concatenando listas')
lista1 = [2,37,9]
lista2 = [8,4,6,7]

lista1e2 = lista1 + lista2
print(lista1)
print(lista2)
print(lista1e2)

print(f'\nComando Extend para uma lista receber o valor de outra lista sem alterar a outra lista')
lista3 = [1,3,2,0]
lista3.extend(lista2)
print(f'Lista 3 com extende da lista2 : {lista3}\n')

print('Comando append para adicionar um elemento no final da lista')
lista3.append('append')
print(lista3)

print('\nComando insert utilizado para inserir um elemento onde quisermos na lista')
print('Eu coloco o indice onde sera inserido e também o valor')
lista3.insert(2, 'Lucas')
print(lista3)

print('\nComando pop utilizado para remover o ultimo elemento da lista')
lista3.pop()
print(lista3)

print('\nComando del eu utilizo para excluir elemento de uma determinada posição')
print(f'Elemento no indice 4 que será removido: {lista3[4]}')
del(lista3[4])
print(f'Removi o elemento do índice 4: {lista3}\n')

print('Comando max e min para saber qual é o maior e menor elemento da lista')
lista_int = [6,7,1,9,-1,45,34,20,21]
print(lista_int)
print(f'Maior: {max(lista_int)}')
print(f'Menor: {min(lista_int)}\n')

print('Comando list para transformar um objeto iteravel em uma lista')
lista_ran = list(range(1,7))
print(lista_ran)

