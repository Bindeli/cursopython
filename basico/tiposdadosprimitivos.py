"""
Tipos de dados
str - string: textos 'Assim' ou "Assim"
int - inteiro : 123456, 20, 0, -20, -1500,20
float - real/ponto flutuante - 10.50 ou 1.5 ou 10.10, números quebrados
bool - booleano / lógico - ele checa a lógica das coisas, True/False, visto em comparações 10==10
"""
# função type, para mostrar o tipo
print('Lucas: ', type('Lucas')) # string
print('10: ', type(10)) # int
print('10.50: ', type(10.50)) #float
print('True: ', type(True)) #bool

#concatenação, juntar.
print(10 + 10)  # vai somar os dois valores
print('10' + '10') # vai juntar as duas informações.

# Exercicio de tipos primitivos, checar cada tipo de dado, nome, idade, altura, checar se é maior de idade
#string : nome
print('Lucas Bindeli', type('Lucas Bindeli'))
#Int : idade
print(25, type(25))
#Float : Altura
print(1.68, type(1.68))
#Checar se é maior de idade, 25 > 18
print(25>18, type(25>18))


