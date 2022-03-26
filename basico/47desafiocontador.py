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
contador_1 = 0
contador_2 = 10

# utilizei o ranger para criar a sequencia de números
# e o enumerate para enumerar sendo o progressivo
for progressivo, regressivo in enumerate(range(10,-1,-1)):
    print(progressivo, regressivo)







