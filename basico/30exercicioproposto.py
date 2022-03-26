"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro
"""
numero1 = input('Digite um número inteiro: ')

if numero1.isdigit():
    numero1 = int(numero1)
    if numero1 % 2 == 0:
        print(f'O número {numero1} é um número par.')
    else:
        print(f'O número {numero1} é um número impar')
else:
    print('O conteúdo digitado não é um numero inteiro. Digite corretamente.')

"""
Faça um programa que pergunte a hora ao usuário, e baseando-se no horário descrito,
exiba a saudação apropriada. EX:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18:23
"""
print('')
numero2 = input('Que horas é agora? (0 - 23) R:')

if numero2.isdigit():
    numero2 = int(numero2)
    if numero2 >= 0 and numero2 <= 11:
        print(f'Bom dia! Digitado : {numero2}')
    elif numero2 >=12 and numero2 <= 17:
        print(f'Boa tarde! Digitado : {numero2}')
    elif numero2 >= 17 and numero2 <= 23:
        print(f'Boa noite! Digitado : {numero2}')
    else:
        print('Digite um número entre 0 a 23')
else:
    print('Por favor, Digite um número inteiro.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "seu nome é curto", se tiver entre 5 e 6 letras, escreva "seu nome é normal!"
maior que 6 escreva "Seu nome é muito grande"
"""
print('')
nome = input('Digite seu primeiro nome: ')

qtd_nome = len(nome)
print(f'A quantidade de letras em seu nome é de {qtd_nome}.')
if qtd_nome <= 4:
    print('Seu nome é curto!')
elif qtd_nome >= 5 and qtd_nome <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande')

