"""
Aula 80 - MAP

"""

from dados import pessoas,produtos, lista

# --------------------------------------------------------------------------------------------
# suponha que eu queira pegar cada elemento dar lista e multiplicar por um número

# utilizando a função ""map"", essa função recebe uma função como primeiro argumento
# vamos utilizar a expressão lambda como primeiro argumento
# e como ultimo argumento, vou passar minha lista

lista_double = map(lambda item: item * 2, lista)

# print(f'Lista com os valores multiplicados : {lista_double}')

# se eu colocar para imprimir agora, vai aparecer um iterador <map object at 0x000001D40B2660B0>
# A função map retorna um iterador para você iterar sobre o elemento
# teriamos que iterar sobre cada elemento para poder ver ela
# ou podemos fazer um typecast como list

print(f'Lista com os valores multiplicados :')
print(list(lista_double))

# Agora temos os resultados

# --------------------------------------------------------------------------------------------
# Agora com lista comprehension

lista_compr = [x * 2 for x in lista]
print(f'Agora com list comprehension : {list(lista_compr)}')


# --------------------------------------------------------------------------------------------
# Agora utilizando a função map com dicionario
print(f'\nPrintando o dicionario produtos utilizando um for:')
for produto in produtos:
    print(produto)

# Agora vamos a um exemplo
# Caso eu queira acrescentar 5% em cada valor desses produtos

# Supondo que eu quero agora, uma lista com o valor desses produtos

precos = map(lambda prod: prod['preco'], produtos) # neste momento estou acessando produtos
# e pegando os dados da chave que tenha preco

print(f'\nAgora mexendo com o dicionario produtos: ')
print(f'Uma lista contendo somente os preços : {list(precos)}')

# Agora quero acrescentar os 5% em cada valor
# lembrando que podemos fazer uma "copia" para não alterar o valor do dicionario original
# na expressão lambda, não irei conseguir fazer isso

# --------------------------------------------------------------------------------------------
# o que eu posso fazer é definir uma função

def acrescente(produto):
    produto['preco'] = round(produto['preco'] * 1.05, 2)
    return produto

# agora vou voltar no lambda e vou colocar a função acrescente

print(f'\nAgora vou criar uma função para aumentar o preço dos produtos : ')
preco_novo = map(acrescente, produtos)
# a função map está mapeando uma função que passa em cada elemento do meu iteravel


for produto in preco_novo:
    print(produto)

# porém ficou cheio de casas decimais, então vou colocar um round(...,2) para pegar duas casas decimais
# --------------------------------------------------------------------------------------------
print('')
# Agora vamos fazer com o dicionario pessoas

print(f'Printando o dicionário pessoas :')
for pessoa in pessoas:
    print(pessoa)

# suponha que eu queira criar uma lista só com esses nomes
# utilizando map

# vou utilizar lambda, pois só estou pegando um campo e é mais fácil mexer com lambda
nomes = map(lambda p: p['nome'], pessoas)
print(f'\nAgora pegando somentes os nomes:')
for pers in nomes:
    print(pers)

print(f'\nAgora pegando somente as idades:')
idades = map(lambda idade: idade['idade'], pessoas)
for idade in idades:
    print(idade)
# --------------------------------------------------------------------------------------------
# criando uma nova chave no dicionario pessoas :
print('\nCriei uma nova chave chamado de nova_idade, somando a atual + 1')
def aumenta_idade(pessoa):
    pessoa['nova_idade'] = pessoa['idade'] + 1
    return pessoa

# agora nós temos uma nova chave

novo_pessoas = map(aumenta_idade, pessoas)

for person in novo_pessoas:
    print(person)




