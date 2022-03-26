"""
For / Else em Python

"""
lista_1 = ['Lucas','3468','Bindeli', '25', '1997']
# irei criar a variavel checagem para ver se há o item que eu quero na lista
checagem = False
for valor in lista_1:
    # a função startswith checa se o valor do item começa com um determinado dado
    # utilizo o lower para deixar o caracter em minusculo para não ter problema entre maisculo e minusculo
    if valor.lower().startswith('l'):
        print(f'Começa com L: {valor}')
        #se ele encontrar uma palavra que começa com L, irá mudar o valor da variavel para True
        checagem = True
    else:
        print(f'Não começa com L: {valor}')
print('')
#irei utilizar o valor da variavel checagem para mostrar se tem ou não o item que eu queria
if checagem:
    print('Existe uma palavra que começa com L.')
else:
    print('Não existe uma palavra que começa com L.')
print('')

# ou podemos fazer tudo isso resumidamente assim :

print('Utilizando For e Else juntos:')
checagem_2 = False
for valor2 in lista_1:
    if valor2.lower().startswith('3'):
        print('Há dado que começa com 3.')
        break
else:
    print('Não existe um dado que começa com 3.')
# Mas geralmente não utilizamos while com else ou for com else.