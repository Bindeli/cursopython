"""
Aula 14 no curso - Python Básico
Strings = textos que estão dentro de aspas, tipo de dado primitivo em Python.
Tudo em Python, é um objeto.
Até mesmo com uma String, você tem várias funções para utilizar.
str = string
"""

# print(algumacoisa)
#Como o interpretador procura por comandos, vai tentar exercutar este comando, dando erro Syntax
#alguamcoisa não está definido.

print('Alguma coisa')
print("Aspas duplas")

print(123456) # o python sabe que é um número inteiro, e não precisa de aspas.
#O interpretador considera este número como inteiro, se colocar aspas, será considerado String.
print('123456')

print('Essa é uma String (str)')
#o inicio de uma string está de uma aspa para a outra '', para colocar uma aspas dentro de aspas, só alterar entre aspas simples e duplas
print('Essa é uma "String" (str)') # ou print("Essa é uma 'string' (str)")

# print('Este é um \'texto\'') Também pode utilizar o \ para impedir de executar o comando aspas
#porém é melhor aspas dentro de aspas de forma estética.

# comando r para dizer ao código que tudo que estiver estre as aspas será um texto.
print(r'Este é meu \n texto') # o \n utilizado de forma normal, salta uma linha
#porém não é legal de forma estética também. o ideal é começar com aspas simples e colocar no meio aspas duplas




