"""
04.252.011/0001-10 (esse tem uma regrinha) (A validação é feito por esses números iniciais 04.252.011/0001 )
antes do ' - '
40.688.134/0001-61
71.506.168/0001-11
12.544.992/0001-05

pode escolher qualquer um dos 4 cnpj's
tirar os pontos e as barras
e abrir desse jeito :

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2 (essa é uma sequencia que vai de 5 a 2 e 9 a 6 e 5 a 2 dnv)
x ---------------------------------------------
0   16  6   10  18  0   7   6   0   0   0   2 = 65 (vai somar o resultado da multiplicação e somar )
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2 (uma outra sequencia)
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito

Vou criar um módulo chamado de cnpj, onde vou criar o código. seria bom em funções
Como remover ponto, /,

import re    = expressão regular

def removercaractere(cnpj):
    return re.sub(r'[^0-9]','',cnpj)  , o que não for entre 0 a 9, será substituido por nada ''

removercaracteres('04.252.011/0001-10')

ou

cnpj = cnpj.replace('/','')
cnpj = cnpj.replace('.','')
cnpj = cnpj.replace('-','')
return cnpj

uma outra coisa, é fazer uma função desencadear outras funções




"""


def valida():
    fala_oi()
    falaoutracoisa()


def fala_oi():
    print('Oi')


def falaoutracoisa():
    print('Fala outra coisa')
