"""
For / Else
"""
print('Checar se há um elemento que começa com A:')
lista_1 = ['Lucas','André','Anildson','Marcelo']
print(lista_1)
print('Função startwith checa se o valor do item começa com determinado dado')
for valor in lista_1:
    if valor.lower().startswith('a'):
        print(f'{valor} começa com a.')
    else:
        print(f'{valor} não começa com a.')

print('')

print('Utilizando For com Else para checar se há elementos que começa com L:')
contagem = 0
for elemento in lista_1:
    if elemento.lower().startswith('l'):
        print('Há elemento que começa com L')
        break
else:
    print('Não existe elementos que começa com L.')
print('')
"""
Split, Join, Enumerate em Python
* Split - dividir uma string #str
* Join - juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis

"""
frase_aleatoria = "Nunca aceite o mundo como ele parece ser"
print(f'Frase = {frase_aleatoria}')
print('Utilizando a função split:')
print('Com essa função posso dividir uma string e criar uma lista com ela')

lista_1 = frase_aleatoria.split(' ')
print(f'Lista feita pela frase: {lista_1}\n')

print('Para contar quantos vezes um item apareceu na lista, utilizamos o count: ')
lista_contagem = [2,3,7,6,4,8,2,1,3,4]

for valor in lista_contagem:
    print(f'O elemento {valor} apareceu {lista_contagem.count(valor)}')

print('')
print('Exemplo de como pegar o elemento que mais apareceu: ')
lista_maiorx = [2,3,4,6,1,7,6,7,4,1,4,7,1,2]
valor = ''
contagem = 0

for elemento in lista_maiorx:
    qtd_vezes = lista_maiorx.count(elemento)

    if qtd_vezes > contagem:
        valor = elemento
        contagem = qtd_vezes

print(f'O elemento que apareceu mais vezes é : {valor} aparecendo {contagem}x')
print('Utilizamos a função "strip" para remover o espaço no inicio e no fim da string:')
print('E utilizamos a função "capitalize" para deixar em maiusculo a primeira letra')
lista_strip = frase_aleatoria.split(' ')

for elementos in lista_strip:
    print(elementos.strip().capitalize())

print(lista_strip)
print('Utilizo a função join para transformar uma string em uma lista')
print("O que for dentro das aspas, será o separador de cada elemento da lista na string")
string_da_lista = ' '.join(lista_strip)
print(string_da_lista)
print('')
print('A função enumerate serve para enumerar os elementos')
lista_enu = ['O','Brasil','é','um','país','enorme']

for indice_v1, valorreal in enumerate(lista_enu):
    print(f'indice: {indice_v1} e valor:  {valorreal}')
    print(f'{lista_enu[indice_v1]}')
print(lista_enu)
print('')
"""
Enumerate - enumerar elementos da lista # list
Não é um indice
Enumera cada elemento que você tem na repetição
"""

lista = [
    ['Lucas','Bindeli'],
    ['Maria','João'],
    ['Matheus','Jorge'],
]

for valor_1, valor_2 in enumerate(lista,3):
    print(f'{valor_1} e {valor_2}')
print('')

# enumerando agora a lista

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
print('')
# Desempacotamento :
print('Desempacotamente')
lista_nomes = ['Lucas','Anildson','André','Marcelo']
print(f'Lista : {lista_nomes}')
nome1, nome2, nome3, *nome = lista_nomes

print(f'Nome 1: {nome1}')
print(f'Nome 2: {nome2}')
print(f'Nome 3: {nome3}')
print(f'Nome 4: {nome}')
print('')
print('Trocando valores:')

nome1, nome2 = nome2, nome1

print(f'Agora o nome 1 é {nome1}')
print(f'Agora o nome 2 é {nome2}\n')
print('Utilizando operação ternária')
print('Criando um sistema que veja se a pessoa é maior de idade:\n')
idade = input('Digite sua idade: ')

if not idade.isnumeric():
    print('Você precisa digitar um número ')
else:
    idade = int(idade)
    e_maior = (idade >= 18)
    mensagem = "Pode acessar, você é de maior" if e_maior else 'Você é de menor'
    print(mensagem)



