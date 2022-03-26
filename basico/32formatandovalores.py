"""
Formatando valores com modificadores - aula 32
:s - Texto (strings)
:d - Inteiros (int)
:f - números de ponto flutuante (float)
:.(número)f - Quantidade de casas decimais (float)
:(caractere) (> ou < ou ^)(Quantidade)(tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num1 = 10
num2 = 3
# divisao irá retornar um valor float
divisao = num1/num2
#print('Resultado: {:.2f}'.format(divisao))
#ou
print(f'Resultado: {divisao:.2f}')

num3 = 3
num4 = 1256
# Ele vai preencher de 0, até ter 10 casas, o número da variavel estará entre essas 10 também
# O numero da variavel será adicionado no ultimo lugar onde a seta aponta
print(f'{num3:0>10}')
print(f'{num4:0<10}')
print(f'{num4:0^10}')
#transformando um número inteiro em float
print(f'{num4:.2f}')
#podemos fazer isso também com strings, não só números
nome = 'Lucas Bindeli'
# O espaço também conta como um caracter
print(f'{nome} tem {len(nome)} caracteres')
print(f'{nome:#^30}')
# ou utilizar o ljust ou rjust
nome_ljust = nome.ljust(20, '#') # o nome vai para o lado left e vai preencher o resto com #
nome_rjust = nome.rjust(20, '#') # o nome vai para o lado right e vai preencher o resto com #
print(f'O nome utilizando ljust : {nome_ljust}')
print(f'O nome utilizando rjust : {nome_rjust}')
print(f'')
# Também podemos transformar todas as letras em letras minusculas com o lower
nome1 = 'Lucas Bindeli'
nome1 = nome1.lower()
print(nome1)
# Também podemos transformar todas as letras em letras maiusculas com o upper
nome2 = 'lucas bindeli'
nome2 = nome2.upper()
print(nome2)
# Também podemos transformar as primeiras letras em maiusculas utilizando o title
# as outras letras ficarão minúsculas
nome3 = 'lucAs binDeli'
nome3 = nome3.title()
print(nome3)


