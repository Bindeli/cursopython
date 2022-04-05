"""
Aula Dicionário

Diferente de listas, no dicionário você que controla os indices e as chaves!
O dicionário é uma estrutura de dados que suporta um par de chaves e valor
Sempre eu for criar um dicionário, eu preciso falar uma chave e um valor

"""

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










