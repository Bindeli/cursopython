"""
Desempacotamento de listas em Python
"""

lista_nomes = ['Lucas','Nil','André']

# irá receber os elementos na ordem que eu coloquei na lista
nome1, nome2, nome3 = lista_nomes

print(f'Nome 1: {nome1}')
print(f'Nome 2: {nome2}')
print(f'Nome 3: {nome3}')
print('')
# caso eu crie menos variaveis do que a lista possui de elementos, irá dar erro
# pois tem muitos valores para desempacotar

lista_nomes2 = ['Bindeli','Ribeiro','Junior','e outros sobrenomes',2,4, 5,7 ,9,10]

nome4, nome5, *outralista , penultimo ,ultimo_da_lista= lista_nomes2
# foi gerado uma nova lista para receber os valores que sobraram
# na ordem foi gerado uma variavel para receber o primeiro elemento
# foi gerado uma segunda variavel para receber o segundo elemento
# foi gerado uma lista para receber o resto
# foi gerado uma variavel antes do último para receber o penultimo valor da lista
# e foi gerado uma variavel depois da lista para indicar que eu quero o último elemento
print(f'Sobrenome 1 : {nome4}')
print(f'Sobrenome 2 : {nome5}')
print(f'Valores que ficaram em uma outra lista: {outralista}')
print(f'Penultimo valor da lista: {penultimo}')
print(f'Ultimo da lista: {ultimo_da_lista}')

# posso utilizar o *_, que é uma variavel como se fosse a outralista
# porém é para outros desenvolvedores saberem que o resto que eu coloquei na variavel *_ não serão utilizados
# nome1, nome2, *_ = lista_de_nomes
