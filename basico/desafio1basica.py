"""
Criar variaveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
Criar variavel com o ano atual (int)
Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
Exibit um texto com todos os valores na tela usando F-String (com as chaves)
"""

nome = 'Lucas'
idade = 25
altura = 1.68
peso = 88.2
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso/ altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}KG.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')
