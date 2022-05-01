"""
62 - Dicionarios em Python

Em listas, o python cria os índices para ti
No dicionário você que controla o índice ou chave!!!.
O dicionário é uma estrutura de dados que suporta um par de chaves e valor
Sempre que eu for criar um dicionário eu preciso falar uma chave e um valor

"""
# vai o nome da chave e depois o valor ou valores
dicionario = { 'chave1':'primeiro valor'}
print(f'Dicionário : {dicionario}')
# Se eu quiser adicionar uma nova chave no dicionario
dicionario['Nova chave'] = 'Valor da nova chave'
print(f'Novo dicionário : {dicionario}')
# para acessar uma das chaves, utiliza o colchetes
# iremos ver o valor da chave 1
print(f"Valor da chave 1 : {dicionario['chave1']}")
print(' ')

#----------------------------------------------------------------------------------------------------------------
# Um outro jeito de criar dicionários:

dicionario2 = dict(chave_1='Valor da chave', chave_2='Valor da segunda chave')
print('Printando o segundo dicionário:')
print(dicionario2)
print(' ')
# Caso tenha chaves duplicadas, triplicadas, a última vez que ela apareceu no dicionário, será seu valor final
dicionario_dupic = {'chave': 'valor', 'chave': 'valor', 'chave': 'Este será seu valor final'}
print(f'Pegando o valor da chave que foi duplicada: ')
print(dicionario_dupic)
print(' ')
# as chaves no dicionário, precisam ser únicas, se caso eu precise ter mais de uma chave, cada uma tem que ter seu próprio valor
dicionario_exemplo1 = {1:'Valor1', 2: 'Valor2',3:'Valor3'}
print('Dicionário com números como índice: ')
print(dicionario_exemplo1)

# Para criar a chaves eu posso utilizar qualquer tipo de dado imutável.
# Geralmente nós veremos Strings, sendo usados como chaves, mas também pode utilizar números:
# tuplas também são imutáveis, então pode ser utilizadas também
# contando que essas tuplas só tenham valores imutáveis
print(' ')
print('Criando com diferentes tipos de chaves:')
dicionario_ch = {
    'str' : 'valor_str',
    123 : 'valor_num',
    (1,2,3,4) : 'Tupla',
}
print(f'Dicionário: {dicionario_ch}')
print( f'Acessando a chave (1,2,3,4) : {dicionario_ch[(1,2,3,4)]}' )

#----------------------------------------------------------------------------------------------------------------
# Caso eu chame uma chave que não existe, irá dar erro no código e não irá ler o que tem abaixo do código
# Para contornar este problema, há duas maneiras:
# Com if:
print(' ')
print('Verificando se existe uma chave no dicionario criado:')
if 'naoexiste' in dicionario_ch:
    print(dicionario_ch['naoexiste'])
else:
    print(f'Não existe essa chave.!')
# ou posso fazer ao contrário, caso não esteja no dicionario, podemos criar também

#----------------------------------------------------------------------------------------------------------------
print(f' O dicionário não possui a chave : {dicionario_ch}')
print(' ')
print('Agora irá verificar se não está e adicionar se não encontrar:')
if 'naoexiste' not in dicionario_ch:
    dicionario_ch['naoexistia'] = 'valor da chave que não existia'
    print(dicionario_ch)


#----------------------------------------------------------------------------------------------------------------
print('\nUtilizando get:')
# Também podemos utilizar o get para obter o conteúdo da chave.
# Não causa erro caso a chave não exista.
# caso não exista, irá aparecer apenas 'None' e o código não irá parar por causa de erro
print(dicionario_ch.get('chave_inexistente'))
print(dicionario_ch.get(123))
print(' ')
if dicionario_ch.get('nomedachave') is not None: # mas não irá executar pois não tem a chave
    print(dicionario_ch.get('nomedachave'))
if dicionario_ch.get(123) is not None:
    print(dicionario_ch.get(123))

#----------------------------------------------------------------------------------------------------------------
# Caso eu queira atualizar o valor da chave, eu posso utilizar o nome da chave que já existe no dicionario
# e irei atualizar o valor dela
print(' ')
print('Alterando o valor de uma chave: ')
dicionario_ch['str'] = 'Valor Alterado'
print(dicionario_ch)
print(' ')
print('Utilizando Update: ')

#----------------------------------------------------------------------------------------------------------------
# Função Update : esta função recebe um dicionário, utilizado para adicionar elementos para um dicionário também
# também pode ser utilizada para unir dois dicionários fazendo um receber elementos do outro
# Exemplo : dicionário1.update(dicionario2)
# mas abaixo iremos apenas adicionar uma nova chave com um valor
dicionario_ch.update({'nova_chave':'Novo Valor'})

if dicionario_ch.get('nova_chave') is not None:
    print(dicionario_ch.get('nova_chave'))

print(' ')
print('Excluindo itens do dicionário utilizando o del: ')
del  dicionario_ch['str'] # estou apagando a chave str
print(dicionario_ch)
print(' ')

print(f"Verificando se ainda possui str no dicionario: {'str' in dicionario_ch}")

#----------------------------------------------------------------------------------------------------------------
# E também tem uma função para a chaves mas é a mesma coisa do que isso aqui : {'str' in dicionario_ch}
print(f"Verificando str de outra maneira : {'str' in dicionario_ch.keys()}")

#----------------------------------------------------------------------------------------------------------------
# Acessando os valores sem utilizar a chave:
print(f"Verificando se possui o valor 'Novo Valor': {'Novo Valor' in dicionario_ch.values()}")

#----------------------------------------------------------------------------------------------------------------
# Podemos utilizar também len, para dizer quantos pares têm no dicionário
print(' ')
print(f'Utilizando o len no dicionário: {len(dicionario_ch)}')
print(' ')

#----------------------------------------------------------------------------------------------------------------
# Também podemos fazer iteração com dicionários:
novo_dicionario = {
    'chave_1' : 'valor_1',
    'chave_2' : 'valor_2',
    'chave_3' : 'valor_3',
    'chave_4' : 'valor_4',
}

print('Iteração com dicionários : ')
print('Como padrão irá mostrar as chaves: ')
for elemento in novo_dicionario:
    print(elemento)
# porém deste modo, estaremos acessando apenas as chaves

#----------------------------------------------------------------------------------------------------------------
# para mostrar os valores, será necessário utilizar o values()
print('Agora com values, irá mostrar os valores das chaves: ')
for valores in novo_dicionario.values():
    print(valores)
#----------------------------------------------------------------------------------------------------------------
# Para ver as chaves e os itens podemos utilizar a função items
# Função items : para retornar o valor junto com sua chave, fazemos deste jeito :
print(' ')
print('Verificando as chaves e os valores :')
for itens in dicionario_ch.items():
    print(itens)
print(' ')
print(f'Acessando a chave e o valor separadamente:')
for two in dicionario_ch.items():
    print(two[0], two[1])
print(' ')
print('Outro método para acessar chave e o valor, é desempacotar.')
for k, v in dicionario_ch.items():
    print(k, v)
print(' ')

#----------------------------------------------------------------------------------------------------------------
# Criando um dicionário maior :
# adicionando dicionário dentro de dicionário
print('Criando um dicionário grande com outro dicionário dentro dele:')
clientes = {
    # iremos criar um dicionário para a chave, lembrando sempre dos dois pontos
    'cliente1' : {
        'Nome' : 'Lucas',
        'Sobrenome' : 'Bindeli',
    },
    'cliente2' : {
        'Nome' : 'Anildson',
        'Sobrenome' : 'Ribeiro',
    },
    'cliente3' : {
        'Nome' : 'André',
        'Sobrenome': 'Santos',
    },
}

#----------------------------------------------------------------------------------------------------------------
# Para iterar o dicionário :
for clientes_k, clientes_v in clientes.items(): # este for é responsável pelo loop inteiro do dicionário
    print(f'Exibindo {clientes_k}')
    # agora irei criar um outro for para iterar nos itens da chave cliente1, cliente2 e cliente3
    # o segundo for irá pegar agora o valor, no caso o clientes_v
    for dados_k, dados_v in clientes_v.items():
        print(f'\t {dados_k}: {dados_v}') # utilizando o \t para ficar identado, que fica o espaço de 1 Tab


#----------------------------------------------------------------------------------------------------------------
# Outro Exemplo de dicionário mais complicado!
print(' ')
dados_dic = {1: 'a', 2: 'b', 3: 'c'}
# se algum momento eu queira jogar o valor desse dicionario em uma outra variável

dados_alt = dados_dic
print(f'Dados Dic: {dados_dic}')
print(f'Dados Alt: {dados_alt}')
# parecem ser idênticos, mas aqui não estamos criando um novo dicionário como se fosse como variaveis
# Se eu alterar o valor em um , o outro também será alterado como por exemplo:

dados_alt[1] = 'Lucas'
print('Um valor foi alterado no segundo dicionário, mas também será alterado no primeiro:')
print(f'Dados Dic: {dados_dic}')
print(f'Dados Alt: {dados_alt}')


#----------------------------------------------------------------------------------------------------------------
# Quando você utiliza o sinal de igual = , você não está criando um novo objeto
# Esses dois objetos são idênticos
print(f'Verificando se os dois são idênticos: {dados_alt==dados_dic}')
print('Ambos apontam para a mesma localização na memória de seu computador!')
# se você alterar um, o outro será alterado

#----------------------------------------------------------------------------------------------------------------
# Caso eu queria criar uma ""shell"" ou cópia do seu dicionário
# Para contornar isso, utilizamos o """copy"""
print('Utilizando a função copy: ')

dados_sh = dados_dic.copy()
dados_sh[1] = 'Alterado'

print(f'Dicionário Principal : {dados_dic}')
print(f'Dicionário Cópia : {dados_sh}')
# Somente o valor em dados_sh foi alterado, o dicionário principal não sofreu alteração
# Isso é uma cópia rasa, os valores não foram copiados para o dicionário dados_sh
# Os valores de dados_sh são uma referência em dados_sh
print(' ')

#----------------------------------------------------------------------------------------------------------------
d1 = {1: 'a', 2: 'b', 3: 'c', 4 : ['Lucas','Nil','Andre']}
print('Acessando a chave 4 e seu indice 0 dentro de sua lista')
print(d1[4][0]) # Estou querendo ver o valor da chave 4 , e dentro da lista, o indice 0
d1_alt = d1.copy()
d1_alt[1] = 'Luiz'

#----------------------------------------------------------------------------------------------------------------
# Tentando alterar o valor dentro da lista da chave 4
d1_alt[4][0] = 'João'
print('Tentei alterar um elemento dentro da lista da chave 4 : ')
print(f'Dicionário Original: {d1}')
print(f'Dicionário cópia: {d1_alt}')

#----------------------------------------------------------------------------------------------------------------
# Os dois sofrem alterações na lista
# A lista é mutável, pode ser alterada, e por ser uma cópia rasa, sofre alteração em ambas
# poderia contornar isso criando objetos imutáveis, como tuplas

#----------------------------------------------------------------------------------------------------------------
"""
Para criar uma cópia verdadeira do dicionário utilizamos o import copy

import copy

invés de utilizar o .copy

d1_alt = d1.copy()

ficará assim : 

d1_alt = copy.deepcopy(d1) 

E Neste momento ambos os dicionários são independentes, o valor de um não afeta o outro

"""
print(' ')

#----------------------------------------------------------------------------------------------------------------
print('Utilizando o import copy')
import copy

dicionario_P = {1: 'a', 2: 'b', 3: 'c', 4 : ['Lucas','Nil','Andre']}

dicionario_C = copy.deepcopy(dicionario_P)

dicionario_C[1] = 'Bindeli'
dicionario_C[4][0] = 'Motta'

print(f'Dicionário Principal: {dicionario_P}')
print(f'Dicionário Cópia: {dicionario_C}')

"""
Também podemos transformar algo em dicionário utilizando dict
Assim como transformar em lista com list
Ou tupla com tuple

"""
print(' ')

#----------------------------------------------------------------------------------------------------------------
print('Convertendo uma lista em um dicionário:')
# eu posso converter em um dicionário pois eu tenho um par
lista = [
    ['Chave1', 1],
    ['Chave2', 2],
    ['Chave3', 3],
    ['Chave4', 4],
]
dicio_lst = dict(lista)
print(dicio_lst)
# Isso vai funcionar com listas, com tuplas dentro de listas também

#----------------------------------------------------------------------------------------------------------------
print('Agora com lista que contém tuplas : ')
lista2 = [
    ('Chave1', 1),
    ('Chave2', 2),
    ('Chave3', 3),
    ('Chave4', 4),
]
dicio_tpl = dict(lista2)
print(dicio_tpl)
# Também funciona com tuplas que possui tuplas dentro dela, ou tuplas com listas dentro dela

#----------------------------------------------------------------------------------------------------------------
# Aqui no dicionário também temos a função pop e popitem igual de listas
# porém é diferente das listas
print(' ')
print('Utilizando POP e POPITEM')
dicionario_pop = {
    1 : 2,
    4 : 5,
    5 : 6,
    7 : 8,
}
print(dicionario_pop)
# caso eu queira eliminar a última chave, posso utilizar :
dicionario_pop.pop(4)
# irei eliminar a chave 4 do dicionário
print(f'Dicionário sem a chave 4 : {dicionario_pop}')
# com pop eu tenho que falar qual chave eu quero eliminar

#----------------------------------------------------------------------------------------------------------------
# se eu quiser eliminar o último item independente do que seja, eu utiliza o popitem
dicionario_pop.popitem()
print(f'Agora sem o último, utilizando popitem: {dicionario_pop}')
print(' ')

#----------------------------------------------------------------------------------------------------------------
# Também posso concatenar dicionários :

print('Concatenando dicionários:')
# O operador de + não irá funcionar aqui
dicio_1 = {
    1 : 'valor1',
    2 : 'valor2',
    3 : 'valor3',
}
dicio_2 = {
    4 : 'valor4',
    5 : 'valor5',
    6 : 'valor6',
}
print(f'Primeiro dicionário: {dicio_1}')
print(f'Segundo dicionário: {dicio_2}')
# Também podemos utilizar a função update

dicio_1.update(dicio_2)
print(f'Dicionário 1 depois do update: {dicio_1}')