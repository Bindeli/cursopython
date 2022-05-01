"""
Exercício :

imagine que eu tenha um grupo de pessoas com idades variadas, porém, algumas delas tem exatamente a mesma idade.
Suponha que eu queira escrever um programa para separar as pessoas de mesma idade em seus próprios grupos...
Pessoas de 20 anos, pessoas de 30 anos, todos com a mesma idade em agrupados em grupos menores...
Esse é o cenário exato para usar groupby (vamos agrupar por idade).
"""
from itertools import groupby,tee
idade = [
    {'nome' : 'Lucas','idade' : 25},
    {'nome' : 'Andre','idade' : 23},
    {'nome' : 'Anildson','idade' : 37},
    {'nome' : 'Marcelo','idade' : 35},
    {'nome' : 'Julia','idade' : 20},
    {'nome' : 'Evandro','idade' : 37},
    {'nome' : 'Ana','idade' : 15},
    {'nome' : 'Carol','idade' : 25},
    {'nome' : 'Jane','idade' : 28},
    {'nome' : 'Arildo','idade' : 31},
    {'nome' : 'Otavio','idade' : 25},
    {'nome' : 'Julia','idade' : 20},
    {'nome' : 'Gustavo','idade' : 30},
]

idade_key = lambda item : item['idade']
idade.sort(key=idade_key)

idade_agrupada = groupby(idade, idade_key)

for agrupamento, valores_agrupados in idade_agrupada:

    print(f'\nIdade : {agrupamento}')
    # lista_1, lista_2 = tee(valores_agrupados)
    for pessoa in valores_agrupados:
        print(f'{pessoa}')







