"""
AULA 77 - COUNT ( Itertools )

Esta função vai gerar um contador que posso iterar nele
Vai retornar um iterador.
Posso utilizar a função Next neste contador

diferente da função range, que é um iterável, mas não é um iterador
"""

#-------------------------------------------------------------------------------------------------
"""
suponha que você quer gerar um contador para algo
mas primeiro, tenho que importar a função count
"""

from itertools import count

# agora criando uma variavel que vai receber o contador, e printando os 3 primeiros valores
contador = count() # esse count, deste modo, é infinito
print(next(contador))
print(next(contador))
print(next(contador))

# tomar cuidado, ao utilizar o for, pois posso gerar um loop infinito

#-------------------------------------------------------------------------------------------------
print('\nAgora utilizando parâmetros para o count, tendo 5 como inicio')
# o contador também tem um start, por exemplo, quero iniciar do 5
# e quero que ele pule de 0.5 em 0.5
# em Contadores, não teremos stop!!!!!!!!!!!!!!!!!!!!!!!!!

contador_2 = count(start=5, step=0.5)

# Também podemos utilizar float em step, como por exemplo step = 0.5
# Função '''round''' = para arredondar em quantas casas decimais eu quero

for num in contador_2:
    print(round(num, 2))

    if num >= 7:
        break

print('')

#-------------------------------------------------------------------------------------------------
# suponha que eu tenha uma lista de nomes, e quero colocar um indice para cada nome
# utilizo o zip e o count
print('Utilizando Contador com Zip para criar uma lista com indices e nomes')
contador_nomes = count()

lista_nomes = ['Lucas','Bindeli','Motta']

conjunto = zip(contador_nomes, lista_nomes)

print(list(conjunto))

#-------------------------------------------------------------------------------------------------








