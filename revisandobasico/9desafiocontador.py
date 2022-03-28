"""
Utilizando o FOR ou o While
0   10
1   9
2   8
3   7
4   6
5   5
6   4
7   3
8   2
9   1
10  0
for - é quando sabemos quantas repetições teremos
while - é quando não sabemos o quanto de repetições teremos
iremos criar dois contadores, os dois dentro do mesmo laço
a cada volta do laço, um contador irá contar de forma progressiva e o outro contador conte de forma regressiva
"""

for valor1, valor2 in enumerate(range(10,-1,-1)):
    print(valor1, valor2)



