funcao = lambda y: y
h = funcao(4)
print(h)
#------------------------------------------------------------------------------------------------------------------
"""
Faça um programa que escreva “Minha primeira função”, esta escrita deve ser realizada a partir da chamada de uma 
função que foi declarada como uma expressão lambda.
"""
texto_1 = lambda texto: texto
variavel_recebe = texto_1('Minha primeira função')
print(f'Recebido : {variavel_recebe}')
#------------------------------------------------------------------------------------------------------------------
"""
Faça um programa que solicite o nome do usuário e a idade do usuário, depois disso exiba a mensagem: 
“{nome} possui {idade} anos.”. Esta mensagem deve ser escrita em uma função lambda.
"""
mostra_texto = lambda nome, idade : (f'{nome} tem {idade} de idade')
exemplo_2 = mostra_texto('Lucas', 25)
print(f'Texto : {exemplo_2}')

#------------------------------------------------------------------------------------------------------------------
"""
Faça um programa que solicite dois números ao usuário e exiba a multiplicação deles. 
A multiplicação deve ser calculada em uma função lambda.
"""
print('\nMultiplicação com lambda:')
func_mult = lambda x, y : x * y
num_1 = int(input('Digite o numero 1 : '))
num_2 = int(input('Digite o numero 2 : '))
result_mult = func_mult(num_1, num_2)
print(f'Resultado entre {num_1} e {num_2} foi : {result_mult}\n')
#------------------------------------------------------------------------------------------------------------------
"""
Faça um programa que solicite cinco números ao usuário, depois disso, exiba apenas os números maiores do que 10. 
Utilize a função filter para fazer isso.
"""
count = 0
lista_5 = []
while count <= 4:
    add_num = input(f'Digite o numero {count+1} : ')
    if add_num.isdigit():
        add_num = int(add_num)
        lista_5.append(add_num)
        count += 1
    else:
        print(f'Digite um número inteiro')
print(f'Lista com números : {lista_5}')
see_five = filter(lambda numero: numero > 10, lista_5)
print(f'Lista com números maiores que 10 : {list(see_five)}\n')
#------------------------------------------------------------------------------------------------------------------
"""
Faça um programa que solicite dez números ao usuário, depois disso, exiba todos números pares e só então exiba 
todos os números ímpares. Utilize a função filter para fazer isso.
"""
print(f'Lista Ímpares e Pares')
contador = 0
lista_full = []
while contador <= 9:
    verf_num = input(f'[{contador+1}] Digite um número: ')
    if verf_num.isdigit():
        verf_num = int(verf_num)
        lista_full.append(verf_num)
        contador += 1
    else:
        print(f'Digite um número inteiro!')
print(f'Lista do impar e par: {lista_full}')
separa_par = filter(lambda item: item % 2 == 0, lista_full)
separa_impar = filter(lambda item: item % 2 != 0, lista_full)
print(f'\nPares : {list(separa_par)} | ímpares : {list(separa_impar)}')
#------------------------------------------------------------------------------------------------------------------








