"""
87 - criando módulos em Python

"""

#____________________________________________________________________________________________________________________
# Simulando um aplicativo que faça alguns calculos

# Saber o valor de pi
# Importo math
import math

# No Python não temos o conceito de constante, então se quiser criar uma constante (uma variável que não muda o valor)
# Você deve utilizar ela com todas as letras maiúsculas
PI = math.pi


# No exemplo dobra lista
def dobra_lista(lista):
    return [ x * 2 for x in lista]



# Suponha agora que eu queira fazer uma função que multiplica todos os valores de uma lista em um valor único
def multiplica_tudo(lista):
    r = 1
    for i in lista:
        r *= i
    return r


# Agora eu decido utilizar essas funções em outras partes do meu programa

"""
Para impedir que o código seja executado no outro arquivo
"""

if __name__ == '__main__':
    lista = [1,2,3,4,5]
    print(f'Dobra Lista:')
    print(dobra_lista(lista))
    print('Multiplica tudo:')
    print(multiplica_tudo(lista))
    print(f'Valor de Pi : {PI}')

# print(__name__)
#======================================================================================================================