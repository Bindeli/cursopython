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

num1 = 13
num2 = 3
divisao1 = num1/num2

print(f'Resultado1: {divisao1:.2f}')

print(f'{num1:0>10}')
print(f'{num2:0<10}')
print(f'{num1:0^10}')

nome = 'Lucas Bindeli'
print(f'{nome:#^20}')

nome_ljust = nome.ljust(20, '@')
nome_rjust = nome.rjust(20, '@')
print(f'O nome utilizando ljust : {nome_ljust}')
print(f'O nome utilizando rjust : {nome_rjust}\n')

print('Deixando tudo minusculo')
nome1 = 'LuCaS BiNdELi'
nome1 = nome1.lower()
print(f'{nome1}\n')

print('Deixando tudo maiúsculo')
nome2 = 'LuCaS BiNdELi'
nome2 = nome2.lower()
print(f'{nome2}\n')

print('Deixando somente as primeiras letras')
nome3 = 'lucas bindeli'
nome3 = nome3.title()
print(f'{nome3}\n')

"""
Manipulando strings - Aula 33
* String indices
* Fatiamento de Strings [inicio: parar : passo]
* Funções Built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

"""

texto = 'Python_s2'
print(f'Texto : {texto}')
print(texto[2])
print(texto[3])
print(texto[6])
print(texto[-4])
print(texto[-5])
print(texto[:-1])
print(texto[2:6])
print(texto[0::2])
