"""
Aula 82 - Reduce

Essa função não vem como padrão junto com Python como uma função built-in
Então temos que importar ela

Ela irá fazer uma acumulação de valores!

from functools import reduce

"""

from dados import produtos, pessoas, lista

#_________________________________________________________________________________________________________
print(f'\nUm acumulador padrão criado por variável que vai somar os itens da lista')
acumula = 0

print(f'Lista: {lista}')
for item in lista:
    acumula += item

print(f'Valor do acumulador : {acumula}')

#_________________________________________________________________________________________________________
from functools import reduce
# chamei a função reduce pelo import de functools

print(f'\nAgora utilizando a função reduce para acumular os valores da lista: ')

# também recebe uma função como parâmetro
# o elemento que vou trabalhar que é a lista
# e o valor inicial zero

soma_lista = reduce(lambda acumula, elemento: elemento + acumula, lista, 0)
"""
Ela vai começar com o primeiro valor que é 0 e somar com o elemento, que é 1 e vai gravar no acumula.
E depois ela vai pegar o próximo valor do item e somar com o valor gravado no acumula
1° [ 0 + 1 ] / 2° [ 1 + 2 ] / 3° [3 + 3] ...
"""
print(f'Valor do acumulador com reduce : {soma_lista}')
#_________________________________________________________________________________________________________

# Agora utilizando o dicionário que criamos :
print(f'\nAgora somando os valores do dicionário produtos com reduce: ')
# função = lambda acu, produto: produto['preco'] + acu
# objeto = produtos (dicionário do arquivo dados.py)
# valor inicial = 0
soma_precos = reduce(lambda acu, produto: produto['preco'] + acu, produtos, 0)

print(f'Valor reduzido com a soma de todos os preços : {soma_precos}')

media = soma_precos/len(produtos) # media dos preços dos produtos
print(f'\nAgora pegando a media de preços por produtos : {media:.2f}')

#_________________________________________________________________________________________________________
# Agora vou pegar a média de idades das pessoas do dicionário pessoas
print(f'\nAgora vou pegar a media da idade das pessoas no dicionario (pessoas): ')

soma_idade = reduce(lambda acumule, idade: idade['idade']+acumule, pessoas, 0)

print(f'A soma das idades ficou : {soma_idade}')
print(f'Há exatamente {len(pessoas)} pessoas no dicionário!')
print(f'A média das idades é de {soma_idade/len(pessoas)}')
#_________________________________________________________________________________________________________




