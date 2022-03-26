"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro
"""

num_1 = input('Digite um número inteiro: ')

if num_1.isdigit():
    num_1 = int(num_1)
    if num_1 % 2 == 0:
        print('Este é um número inteiro e é par.')
    else:
        print('Este é um número inteiro e é ímpar')
else:
    print('Digite um número inteiro válido.')
print('')

"""
Faça um programa que pergunte a hora ao usuário, e baseando-se no horário descrito,
exiba a saudação apropriada. EX:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
horario = input('Qual é a hora agora? (sem os minutos) : ')

if horario.isdigit():
    horario = int(horario)
    if horario <= 11 and horario >= 0:
        print('Bom dia!!!')
    elif horario <= 17:
        print('Boa tarde!!!')
    elif horario <=23:
        print('Boa noite!!!')
    else:
        print('Digite um horário válido')
else:
    print('Digite um numero válido')
print('')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "seu nome é curto", se tiver entre 5 e 6 letras, escreva "seu nome é normal!"
maior que 6 escreva "Seu nome é muito grande"
"""

nome = input('Digite seu nome: ')

qtd_nome = len(nome)

if qtd_nome <= 4:
    print('Seu nome é curto.')
elif qtd_nome <= 6:
    print('Seu nome tem tamanho normal')
else:
    print('Seu nome é grande')


