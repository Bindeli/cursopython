# 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

print(f'Exercicio 1:')
lista_ex1 = range(1,6)

for elemento in lista_ex1:
    print(elemento)

# Feito
#----------------------------------------------------------------------------------------------------------------------------------------------
# 2 - Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

print(f'\nExercicio 2:')
lista_ex2 = range(1,11)

for elemento in lista_ex2[::-1]:
    print(elemento)

# Feito
#----------------------------------------------------------------------------------------------------------------------------------------------
# 3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

print(f'\nExercicio 3:')

notas_3 = [10, 7 , 6 , 8]
soma = 0
for elementos in notas_3:
    soma += elementos
total = soma/len(notas_3)

print(f'Notas : {notas_3}')
print(f'Média das notas: {total}')
#----------------------------------------------------------------------------------------------------------------------------------------------
# 4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
print(f'\nExercicio 4:')
lista_ex4 = ['a','b','c','d','e','f','g','h','i','j']
consoantes = []
for letras in lista_ex4:
    if letras == 'a' or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u':
        continue
    else:
        consoantes.append(letras)
print(f'Lista completa: {lista_ex4}')

print(f'Consoantes : {consoantes}')

#----------------------------------------------------------------------------------------------------------------------------------------------
"""
5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e
os números IMPARES no vetor impar. Imprima os três vetores.
"""
print(f'\nExercicio 5')
lista_ex5 = range(0,20)
par = []
impar = []
for numero in lista_ex5:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f'Lista inteira : {lista_ex5}')
print(f'Pares : {par}')
print(f'Impares : {impar}')
#----------------------------------------------------------------------------------------------------------------------------------------------
"""
6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
"""


#----------------------------------------------------------------------------------------------------------------------------------------------
# 7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.


#----------------------------------------------------------------------------------------------------------------------------------------------
"""
8 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
"""


#----------------------------------------------------------------------------------------------------------------------------------------------
"""
9 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos 
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""


#----------------------------------------------------------------------------------------------------------------------------------------------
# 10 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.


#----------------------------------------------------------------------------------------------------------------------------------------------
"""
11 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 
13 anos possuem altura inferior à média de altura desses alunos.

"""

#----------------------------------------------------------------------------------------------------------------------------------------------
"""
12 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

"""

#----------------------------------------------------------------------------------------------------------------------------------------------
"""
# 13 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
- "Telefonou para a vítima?"
- "Esteve no local do crime?"
- "Mora perto da vítima?"
- "Devia para a vítima?"
-"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

"""


#----------------------------------------------------------------------------------------------------------------------------------------------
"""
14 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

"""


