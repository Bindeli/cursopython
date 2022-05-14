"""
86 - Módulos padrão do Python

Módulos são arquivos .py (que contém código python) que você pode importar para dentro do seu código
para extender a funcionalidade da linguagem, expandir as funcionalidades padrão da linguagem.

Link para ver todos os módulos "padrão" do Python em:
https://docs.python.org/3/py-modindex.html

"""
# A utilidade do Python por si só é bem diversificada sem instalar algo

# por exemplo, quero ver em qual plataforma o python está sendo executado no momento.
# eu utilizo o platform
import sys
print(f'Verificando em qual plataforma o Python está sendo executado :')
"""
Estou importando o módulo sys.
para ver quais os módulos disponíveis, só colocar sys.  , que irá aparecer
Exemplo : print(sys.)
"""
print(sys.platform) # estou pedindo o interpretador acessar o módulo sys e acessar o módulo para verificar
# a plataforma

"""
Uma outra forma seria assim, renomeando  :
from sys import platform as so

print(so)
"""
#__________________________________________________________________________________________________________

#Gerar números aleatórios utilizando o módulo random
import random
print(f'\nQuero gerar números aleatórios utilizando o random, 3x: ')
for i in range(3):
    print(random.randint(0, 10))

"""
Um outra forma é importando somente o randint

from random import randint

porém eu não poderia colocar random.randint , pois estou puxando apenas o randint

"""
#__________________________________________________________________________________________________________
"""
Uma outra coisa é puxar apenas o método

from random import randint

e nomear uma função igual ao método

def randint(*arg):
    return algo
    
print(randint(0,10))

quem iria dominar seria o nome que você renomeou
"""

"""
Para resolver isso :

import random

def randint(*arg):
    return algo
     
print(random.randint(0,10))

Chamar o random antes do randint

"""
#__________________________________________________________________________________________________________

# Caso eu queira importar mais de dois métodos, eu utilizo a vírgula :

from random import randint, randrange

#__________________________________________________________________________________________________________

# Caso eu queira instalar um método direto do terminal, posso ir no canto inferior e ir em Terminal

"""
supondo que eu queira instalar o pymysql:

eu digito isso no terminal
pip install pymysql

"""
print(f'Importando o PyMySQL, que instalei no terminal: (se não der erro, vai ter instalado)')
#import pymysql

print(f'Tentar corrigir depois!!!!!!!!!!!')


"""
Para desinstalar é só digitar pip uninstall pymysql
"""
#__________________________________________________________________________________________________________