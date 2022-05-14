"""
AULA 87 - criando módulos em Python

Arquivo principal
"""

"""
Caso eu queira utilizar os calculos que eu criei no outro file, posso importar ele como um módulo padrão
"""
import calculos87

# supondo que eu queira imprimir o Pi
# print(calculos87.PI)

"""
Porém se eu já realizar o print, irá aparecer também os print's que eu deixei no outro arquivo que eu importei
A partir do momento que eu importei o módulo, tudo que está dentro dele, será executado.
"""

#____________________________________________________________________________________________________________________

# Printando o nome do arquivo

print(__name__)

# irá aparecer como Main, apesar de seu nome estar "aplicativo87"
# essa função name irá importar o nome do módulo, apenas se o módulo estiver sendo importado por outro módulo
# se eu importar o aplicativo87 para um outro, invés de aparecer __main__, irá aparecer aplicativo87

"""
Para resolver este problema de executar os comandos de teste, como por exemplo, os prints que eu utilizei
no outro arquivo, caso eu queira impedir de vir para cá, posso utilizar um if __name__ == '__main__':

Como foi escrito no código do calculos87

"""
# Agora se eu for executar, não irá aparecer aqueles print's

#======================================================================================================================

# Agora vou utilizar as funções que eu criei no outro arquivo

print('Pi:')
print(calculos87.PI)

print('Agora criando uma lista:')
lista_new = [40,2,3,4,7,6,1]
print(f'Lista: {lista_new}')
print(f'Função multiplica: {calculos87.dobra_lista(lista_new)}')

print(f'Agora multiplicando tudo : {calculos87.multiplica_tudo(lista_new)}')

#======================================================================================================================

# Uma outra maneira para importar os módulos, é utilizar o from

from calculos87 import multiplica_tudo, dobra_lista, PI

"""
Quando fica escuro, é por que não estou utilizando o módulo que eu importei
"""

# invés de ter que digitar calculos87.multiplica_tudo, eu já posso utilizar ela direto

lista_multi = [1,2,3,4,5]
print('\nPuxando apenas a função multiplica tudo :')
print(multiplica_tudo(lista_multi))

print(PI)

#======================================================================================================================
print(f'\nImportando um outro arquivo .py')
from outro87 import fala_oi

fala_oi()