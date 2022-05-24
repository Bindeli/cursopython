
variavel2 = 'variavel2'

from intermediario.aula90.pacote1.modulo1 import variavel1

print(variavel1)

"""
Já que eu fiz uma especificação bem completa de onde o pacote se encontrava, não deu erro 
de " no module named 'pacote1'

é considerado a raiz ou entrada, onde o primeiro main no arquivo foi criado

não conseguimos fazer importação para trás do arquivo de entrada que estamos utilizando

então o meu arquivo de entrada, de vista do arquivo de programa, vai afetar todas as outras importações
de dentro de meu programa

Então todas as importas precisam levar em consideração o ponto de vista do arquivo de entrada.



"""


