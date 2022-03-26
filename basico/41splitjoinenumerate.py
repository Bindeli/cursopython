"""
Split, Join, Enumerate em Python
* Split - dividir uma string #str
* Join - juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis

"""
print('')
frase_aleatoria = "Nunca aceite o mundo como ele parece ser,ouse vê-lo como ele poderia ser"
# com essa função posso dividir uma string e criar uma lista com ela
# no caso eu coloquei o espaço para dividir a string
# a cada espaço entre uma palavra e outra, será feito um novo valor para a lista
lista_1 = frase_aleatoria.split(' ')
lista_2 = frase_aleatoria.split(',')
print('')
print(f'Lista 1 : {lista_1}')
print('')
print(f'Lista 2 : {lista_2}')
print('')
for valor in lista_2:
    print(valor)

# para contar quantas vezes um item apareceu, utilizamos o count
palavra = ''
# vou criar uma variavel para receber a palavra da lista
# para ser salvo a palavra que mais apareceu na frase
print('')
for valor in lista_1:
    print(f' A palavra "{valor}" apareceu {lista_1.count(valor)}x na frase.')
print('')
print('Checagem para verificar qual item apareceu mais vezes: ')
lista_3 = ['2','5','6','8','4','7','5','8','3','6','5']
# vou criar uma variavel para receber o número da lista
# vai simbolizar o valor que mais apareceu na lista.
valor = ''
contagem = 0
for valor2 in lista_3:
    qtd_vezes = lista_3.count(valor2)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        valor = valor2
print(f'O número que apareceu mais vezes é {valor} (Contagem : {contagem}x)')
print('')
print('Removendo espaço das frases:')
frase_3 = 'Dê mais valor a coisas simples, por mais simples que ela seja, ainda tem o seu valor'
# utilizamos o """strip""" para remover o espaço do inicio e ao fim da string
# e o """capitalize""" que deixa em maiusculo a primeira letra
lista_4 = frase_3.split(' ')
lista_5 = frase_3.split(',')

for valor3 in lista_5:
    print(valor3.strip().capitalize())
print('')
print('Transformando uma lista em uma string.')
lista_string = ['O','espaço','é','gigante']
# se eu quiser formar uma string dessa lista, posso utilizar a função """join"""
# todos os elementos da lista serão juntados e separados pelo elemento que está entre aspas simples
# que no caso do exemplo é a vírgula, ou pode ser também um espaço
string_de_lista = ','.join(lista_string)
print(f'A String criada de uma lista : {string_de_lista}')
# v1, v2 estão para desempacotando
# v1 terá o valor do indice servindo como contador também
# """enumarate""" serve como estivesse criando indices para os itens da lista porém aparecendo para nós
lista_6 = ['O','Brasil','é','um', 'país','gigante']
for indice_v1, valorreal_v2 in enumerate(lista_6):
    print(f'indice: {indice_v1} valor: {valorreal_v2}')
    print(f'{lista_6[indice_v1]}')

# Uma lista pode conter uma outra lista dentro dela
print('')
lista_list = [
    [1,2],
    [3,4],
    [5,6]
]
# essa lista tem 3 elementos
# o v recebe cada valor de cada indice
for v in lista_list:
    print(f'Imprimindo os valores da lista_list: {v}')
    # e também posso puxar um elemento pelo indice dentro da lista que está dentro da outra lista
    print(f'Imprimindo itens da lista que está dentro: {v[0]}')

lista_alet = [
    [0,'Lucas'],
    [1, 'Bindeli'],
    [2,'Maria'],
]
print('')
print('Imprimindo indice e nome')

# for indice, nome in lista_alet:
#     print(f'indice: {indice}, nome : {nome}')

for indice, nome in enumerate(lista_alet):
    print(f'indice: {indice}, nome : {nome}')
