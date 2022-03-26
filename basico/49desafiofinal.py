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

# caracter2 = 0

while True:
    cpf = input('Digite seu cpf: ')
    if not len(cpf) == 11:
        print('CPF DEVE CONTER 11 CARACTERES!!!')
        break

    novocpf = cpf[:-2]  # elimina os dois ultimos digitos
    multi = 10          # Contador reverso 1
    multi2 = 11         # contador reverso 2
    soma1 = 0           # soma para realizar a multiplicação entre o número e o contador
    total1 = 0          # total para fazer a soma para verificar o caracter final do laço
    soma2 = 0           # soma para o segundo laço for
    total2 = 0          # total para o segundo laço for
    caracter = 0        # variavel que vai receber o último digito do laço for , sendo para o primeiro e segundo

    for contador in range(9):
        soma1 = int(novocpf[contador]) * multi # valor recebe resultado entre o dígito e o contador
        multi -= 1
        total1 = soma1 + total1

    caracter = 11- (total1 % 11) # conta que irá criar o digito final do laço for
    # print(caracter)
    if caracter > 9:
        caracter = 0

    novocpf = novocpf + str(caracter) # concatenar o digito gerado no novo cpf como string

    for contador in range(10):
        soma2 = int(novocpf[contador]) * multi2 # valor recebe resultado entre o dígito e o contador
        multi2 -= 1
        total2 = soma2 + total2
    caracter = 11 - ( total2 % 11) # conta que irá criar o digito final do laço for
    # print(caracter)
    if caracter > 9:
        caracter = 0

    novocpf = novocpf + str(caracter) # concatenar o digito gerado no novo cpf como string
    print(novocpf)

    # PARA EVITAR SEQUENCIAS. EX : 11111111111
    sequencia = novocpf == str(novocpf[0]) * len(cpf)
    # peguei da vídeo aula

    if novocpf == cpf and not sequencia:
        print(f'O CPF {novocpf} é válido!')
    else:
        print(f'O CPF {novocpf} é inválido!')
    print('')



















