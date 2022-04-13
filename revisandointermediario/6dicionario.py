"""
Aula Dicionário

Diferente de listas, no dicionário você que controla os indices e as chaves!
O dicionário é uma estrutura de dados que suporta um par de chaves e valor
Sempre eu for criar um dicionário, eu preciso falar uma chave e um valor

"""
import copy

dicionario_exemplo = {'chave1':'valor da chave1'} # desta maneira
print(f'Primeiro dicionário : {dicionario_exemplo}')

# caso eu queira adicionar mais uma chave para o dicionário:
dicionario_exemplo['chave2'] = 'valor da chave2'
print(f'Atualizando o dicionário : {dicionario_exemplo}')
print(f"Para acessar o valor da chave 1: {dicionario_exemplo['chave1']}\n")
print('Outro jeito de criar um dicionário é utilizando o dict:')
dicionario_dict = dict(chave_1 = 'Valor chave1', chave_2='valor chave 2')
print(f'{dicionario_dict}')
# Caso tenhamos chaves duplicadas, triplicadas ou mais, a última vez que ele aparecer, será seu valor final.
dicionario_duplic = {'chave1': 'primeiro valor 1', 'chave2': 'valor chave2','chave1' : 'segundo valor da chave1'}
print(f'Dicionario com chave duplicada: {dicionario_duplic}')
print('O valor final da chave, será o valor que aparecer pela última vez.')
print('As chaves do dicionário precisam ser únicas, cada uma tendo seu valor.\n')
"""
Para criar as chaves, eu posso utilizar qualquer tipo de dado imutável.
Geralmente é uma string como chave, mas também podemos encontrar números
tuplas também são imutáveis, então pode ser utilizadas também
contando que essas tuplas só tenham valores imutáveis.
"""

dicionario_multkey = {
    'str' : 'valor do str',
    123 : 'valor do 123',
    (1,2,3,4) : 'valor da tupla',
}
print(f'Dicionário com multiplos tipos de chaves: {dicionario_multkey}')
"""
Caso eu chame uma chave que não exista no dicionário, irá dar erro no código.
para contornar este problema, podemos utilizar duas maneiras, com if e else ou também o get.
"""
print('\nUtilizando if e else para ver se há a chave no dicionario:')
if 'naoexiste' in dicionario_multkey:
    print(dicionario_multkey['naoexiste'])
else:
    print('Não existe essa chave!')
print('Não vai encontrar pois não existe.\n')
print('Agora utilizando o get:')
"""
O get não causa erro, caso não exista a chave
Caso não existe, apenas irá aparecer None e o código não irá parar de rodar
"""
print(f"Imprimindo uma chave que não existe com get : {dicionario_multkey.get('chave_naoexiste')}")
print(f'Criando chave caso não exista: ')

if 'naoexiste' not in dicionario_multkey:
    dicionario_multkey['nao_existe'] = 'valor da chave nova'
    print(dicionario_multkey)

print(dicionario_multkey.get('chave_inexistente')) #irá aparecer None pois não existe

if dicionario_multkey.get('nomedachave') is not None: # mas não irá executar pois não tem a chave
    print(dicionario_multkey.get('nomedachave'))
if dicionario_multkey.get(123) is not None: # vai executar pois tem a chave que não é Nulo
    print(dicionario_multkey.get(123))

print('\nCaso eu queira atualizar um valor de um chave:')
dicionario_multkey['nao_existe'] = 'valor novo'
print(dicionario_multkey)
print('\nUtilizando a função update:')
"""
Função update : esta função recebe um dicionário, utilizado para adicionar elementos para um dicionário também
Também pode ser utilizada para unir dois dicionários, para um receber elementos do outro
Exemplo : dicionario1.update(dicionario2)
mas abaixo iremos apenas adicionar uma nova chave com um valor
"""
dicionario_multkey.update({'nova_chave':'valor da nova chave'})

if dicionario_multkey.get('nova_chave') is not None:
     print(dicionario_multkey.get('nova_chave'))
print('\bExcluindo elementos do dicionario utilizando del: ')
"""
Função del - deletar elementos do dicionário
del dicionario['item']
"""

del dicionario_multkey['str']
print(dicionario_multkey)
print('Duas maneiras para verificar se ainda possui a chave str:')
print(f"Verificando se ainda possui com True ou False : {'str' in dicionario_multkey}")
print(f"Verificando str com keys: {'str' in dicionario_multkey.keys()}")
print(f"Verificando se possui o valor em uma das chaves: {'valor novo' in dicionario_multkey.values()}")

print('\nPodemos utilizar len par saber quantos pares há no dicionário:')
print(f'Utilizando len: {len(dicionario_multkey)}')
print(dicionario_multkey)

"""
Também podemos fazer iteração com dicionários:
"""
novo_dicionario = {
    'chave_1': 'valor_1',
    'chave_2': 'valor_2',
    'chave_3': 'valor_3',
    'chave_4': 'valor_4',
}
print('\nFazendo iteração com dicionário, como padrão irá mostrar as chaves:')
for elemento in novo_dicionario:
    print(elemento)
print('\nAgora utilizando a função values, que irá mostrar os valores')
for valores in novo_dicionario.values():
    print(valores)
print('\nAgora utilizando a função items para retornar o valor junto com a chave:')
for itens in novo_dicionario.items():
    print(itens)

print('\nCriando um dicionario grande com outro dicionario dentro dele:')
clientes = {
    'cliente_1' : {
        'Nome' : 'Lucas',
        'Sobrenome' : 'Bindeli'
    },
    'cliente_2' : {
        'Nome' : 'Anildson',
        'Sobrenome' : 'Ribeiro',
    },
    'cliente_3' : {
        'Nome' : 'André',
        'Sobrenome' : 'Santos',
    },

}

for clientes_keys, clientes_values in clientes.items():
    print(f'Exibindo {clientes_keys}')
    # agora vou criar um outro foto para iterar nos items de cada chave cliente
    for dados_keys, dados_values in clientes_values.items():
        print(f'\t {dados_keys} : {dados_values}')# \t para ficar identado

print('\nNovo exemplo de dicionário: ')
dicionado_novo1 = {1 : 'a', 2 : 'b', 3 : 'c'}
# Se algum momento eu queira jogar o valor desse dicionario em outra variavel

dicionado_novoalt = dicionado_novo1
print(f'Novo dicionario : {dicionado_novo1}')
print(f'Novo dicionario alternativo : {dicionado_novoalt}')
"""
Quando utilizado o receber " = ", não estamos criando um novo usuário, ele está recebendo dados do primeiro dicionário
Caso altere o valor de um, o outro também será alterado.
Parecem ser idênticos, mas aqui não estaremos criando um outro dicionário, assim como se fosse variaveis
"""
print(f'Verificando se ambos os dicionarios são idênticos: {dicionado_novo1 == dicionado_novoalt}')
print(f'Ambos apontam para o mesmo local de memória')

"""
Se você alterar um, o outro será alterado.
Para Contornar isso, devemos criar um shell ou cópia do seu dicionário
Utilizando a função "copy"
"""
print('\nCriando um dicionario cópia')
dicionario_copia = dicionado_novo1.copy()
print(dicionario_copia)

dicionario_copia[1] = 'valor alterado'
print(f'Dicionario original : {dicionado_novo1}')
print(f'Dicionario copia : {dicionario_copia}')

"""
Somente o valor em dicionario_copia foi alterado, o dicionario principal não sofreu alteração
isso é uma copia rasa, os valores não foram copiados para o dicionário_copia
os valores de dicionario_copia é uma referencia
"""

# caso for alterar um valor de um indice dentro de um valor, não iria funcionar o exemplo de cima
# ambas iriam sofrer alteração , como o exemplo abaixo

dic1 = { 1:'a',2 : 'b', 3 : 'c', 4 : ['Lucas','João','Maria'] }
print(f'\nAcessando a chave 4 e pegando seu valor no indice 0 de sua lista: {dic1[4][0]} ')
dic_copy = dic1.copy()
dic_copy[1] = 'Bindeli'
# alterando um valor dentro da lista da chave 4
dic_copy[4][0] = 'Matheus'
print(f'Lista original : {dic1}')
print(f'Lista rasa ou lista cópia : {dic_copy}')
"""
A chave foi modificada apenas na cópia porém o elemento dentro da lista foi alterada nas duas
"""

"""
para criar uma copia verdadeira do dicionario utilizamos o import copy 

invés de utilizar o .copy

d2 = d1.copy()

ficará assim:

d2 = copy.deepcopy(d1)

E neste momento, ambos os dicionários serão independentes, o valor de um não afeta o outro
 
"""
print('\nUtilizando deepcopy para criar uma copia verdadeira, em que ambas serão independentes')

dic_real = {1: 'a', 2: 'b', 3: 'c', 4 : ['Lucas','Nil','Andre']}

dic_copia = copy.deepcopy(dic_real)

dic_real[1] = 'Lucas'
dic_copia[1] = 'Bindeli'
dic_copia[4][0] = 'Bindeli'

print(f'Dicionario original: {dic_real}')
print(f'Dicionario cópia : {dic_copia}')

"""
Também podemos transformar algo em dicionário utilizando dict
Transformando lista ou tupla em dicionario

"""

print('\nConvertendo uma lista em dicionario:')
lista_ori = [
    ['chave1', 1],
    ['chave2', 2],
    ['chave3', 3],
    ['chave4', 4],
]
dicio_lista = dict(lista_ori)
print(f'{dicio_lista}')
"""
Issso vai funcionar com lista, com tuplas dentro de listas também.
Também funciona com tuplas que possui tuplas dentro dela, ou tuplas com listas dentro dela
Aqui no dicionario também temos a função pop e popitem igual de listas
porém sua função é diferente das listas
"""
print('\nUtilizando Pop e Pop item')
dicionario_for_pop = {
    1 : 'a',
    2 : 'b',
    3 : 'c',
    4 : 'd',
}
print(dicionario_for_pop)

# caso eu queira eliminar a última chave, posso utilizar o pop

dicionario_for_pop.pop(4)
print('Utilizando pop')
print(dicionario_for_pop)
#irei eliminar a chave 4 do dicionario
"""
Com o Pop, eu tenho que falar qual chave eu quero eliminar.
Se eu quiser eliminar o último item independente do que seja, eu vou utilizar o popitem()
"""
dicionario_for_pop.popitem()
print('Utilizando o popitem')
dicionario_for_pop.popitem()
print(f'Agora sem o ultimo elemento do dicionário: {dicionario_for_pop}\n')

"""
Também podemos concatenar dicionários 
"""
print('Concatenando dicionários:')
dicionario_1 = {
    'chave1' : 'valor1',
    'chave2' : 'valor2',
    'chave3' : 'valor3',
    'chave4' : 'valor4',

}

dicionario_2 = {
    'chave8' : 'valor5',
    'chave2' : 'valor6',
    'chave23' : 'valor7',
}
print(f'Dicionário 1 : {dicionario_1}')
print(f'Dicionário 2 : {dicionario_2}')

# podemos utilizar a função update para concatenar:

dicionario_1.update(dicionario_2)
print(f'Dicionário concatenado : {dicionario_1}')
# um deles não apareceu pois tinha a mesma chave, e o último valor que apareceu foi o definitivo