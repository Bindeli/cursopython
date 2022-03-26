idade = int(input('Digite sua idade: '))

if idade <= 11:
    print('Criança')
elif idade >= 18:
    print('Adulto')
else:
    print('Adolescente')

print('')

"""
Operadores relacionais

== igualdade, verifique se é igual
>  maior que
>= maior que ou igual
<  menor que
<= menor que ou igual
!= diferente

Voltando um valor booleano
"""

"""
Operadores lógicos
and
or
not
in
not in

Comparações
"""

"""
len - utilizado para contar os caracteres

"""
print('Exemplo de len:')
string = 'Lucas'
qtd_string = len(string)
print(f'A string {string} possui {qtd_string} caracteres.')

print('')
print('Verificando se é um digito inteiro com isnumeric, isdigit ou isdecimal:')

while True:
    opcao = input('Deseja continuar? [S]im ou [N]ão: ').lower()
    if opcao == 'n':
        break
    else:
        variavel = input('Digite algo para ver se é número inteiro: ')

        if variavel.isdigit():
            print('É um número inteiro.')
            print('')
        else:
            print('Não é um número inteiro.')
            print('')

