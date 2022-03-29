"""
Validar um CPF
CPF = 168.995.350.09

vamos pegar os primeiros 9 dígitos e vou fazer desta maneira abaixo
e vou multiplicar os 9 primeiros, fazendo essa contagem regressiva de 10 a 2
devemos salvar o resultado em algum lugar e somar todos os valores
o resultado da soma será colocado nesta formula: 11 - ( "soma" % 11 ) = x

se o resultado for maior que 9, o resultado vai ser 0
se o resultado for igual ou menor que 9, o resultado é o desta conta mesmo

no cpf, por exemplo, o resultado vai dar 11 , sendo maior que 9, será colocado 0 ( zero )
e no outro, o resultado será 9, como 9 é igual ou menor que 9 = true, então o ultimo digito será 9

será incluido como décimo, o resultado da primeira conta

porém agora, invés de começar a contagem regressiva de 10, vai começar de 11

com o resultado, fazer a mesma formula, e se der menor ou igual a nove, fica o valor do resultado

1 * 10 = 10                 #   1 * 11 = 11
6 * 9 = 54                  #   6 * 10 = 60
8 * 8 = 64                  #   8 * 9  = 72
9 * 7 = 63                  #   9 * 8  = 72
9 * 6 = 54                  #   9 * 7  = 63
5 * 5 = 25                  #   5 * 6  = 30
3 * 4 = 12                  #   3 * 5  = 15
5 * 3 = 15                  #   5 * 4  = 20
0 * 2 = 0                   #   0 * 3  = 0
                            #>> 0 * 2  = 0
                            #   " o zero da última conta será adicionado aqui "
soma =  297                 #   soma = 343
11 - (297 % 11) = 11        #   11 - ( 343 % 11 ) = 9
11 > 9 = 0                  #
Digito 1 = 0                #    Digito 2 = 9

para validar o cpf, pegar os 9 primeiros digitos
criar uma nova variavel como string, adicionado com os 2 ultimos elementos

para checar :

if cpf == novocpf
    print ( valido )
else:
    print ( invalido )

se o novo cpf, for diferente do original, ele é inválido
"""
while True:
    cpf = input('Digite seu cpf: ')
    if not len(cpf) == 11:
        print('Digite um cpf válido com 11 caracteres')
        print('')
        continue

    novo_cpf = cpf[:-2]

    print(novo_cpf)

    contador_1 = 10
    contador_2 = 11
    soma_1 = 0
    total_1 = 0
    soma_2 = 0
    total_2 = 0
    digitofinal = 0

    for elemento in range(9):
        soma_1 = int(novo_cpf[elemento]) * contador_1
        contador_1 -= 1
        total_1 = soma_1 + total_1

    digitofinal = 11 - (total_1 % 11)

    if digitofinal > 9:
        digitofinal = 0

    print(f'Total 1 : {total_1}')
    print(f'Digito final 1 : {digitofinal}')

    novo_cpf = novo_cpf + str(digitofinal)
    print(f'Novo cpf por enquanto : {novo_cpf}')

    for elemento in range(10):
        soma_2 = int(novo_cpf[elemento]) * contador_2
        contador_2 -= 1
        total_2 = soma_2 + total_2

    print(f'Total 2 : {total_2}')
    digitofinal = 11 - (total_2 % 11)

    if digitofinal > 9:
        digitofinal = 0

    print(f'Segundo Digito: {digitofinal}')
    novo_cpf = novo_cpf + str(digitofinal)
    print(f'Novo cpf : {novo_cpf}')

    #evitar sequencias:
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if novo_cpf == cpf and not sequencia:
        print(f'O cpf {novo_cpf} é válido')
    else:
        print(f'O cpf {novo_cpf} é inválido')
    print('')
