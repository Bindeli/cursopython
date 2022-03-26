def reaispdolar():
    while True:
        print('Selecionado Real (R$) para Dolar (US$)')
        reais = (input("Quantos reais? R$: "))

        if reais.isnumeric():
            reais = float(reais)
        else:
            print('Valor inválido.')
            print()
            break  # Termina o loop caso nao se digite um número.

        cotacao = (input("Cotação de hoje é? "))

        if cotacao.isnumeric():
            cotacao = float(cotacao)
        elif not cotacao.isnumeric():
            print('Valor inválido')
            break  # Termina o loop caso nao se digite um número.
        else:
            break  # Fim do loop. Pode-se coverter novamente caso queira.

        conversao = reais / cotacao
        print("Você possui US$", ("%.2f" % conversao))
        break


def dolarpreais():
    while True:
        print('Selecionado Dolar par Real')
        dolar = input("Quantos Dolares? US$: ")

        if dolar.isnumeric():
            dolar = float(dolar)
        else:
            print('Valor inválido.')
            print()
            break  # Termina o loop caso nao se digite um número.

        cotacao = input("Cotação de hoje é? ")

        if cotacao.isnumeric():
            cotacao = float(cotacao)
        elif not cotacao.isnumeric():
            print('Valor inválido.')
            print()
            break  # Termina o loop caso nao se digite um número.
        else:
            print('Valor inválido.')
            print()
            break  # Fim do loop. Pode-se coverter novamente caso queira.

        conversao = cotacao * dolar
        print("Você possui: R$", ("%.2f" % conversao))
        break


while True:
    print("O que deseja fazer? ")
    print()
    print("1 - Converter reais (R$) em dolares ($)")
    print("2 - Converter dolares ($) em reais (R$)")
    print()

    menu = input("Deseje a opção desejada: \n")
    print()
    if menu == "1":
        reaispdolar()
    elif menu == "2":
        dolarpreais()
    else:
        print("Valor inválido", )
        print()
    while True:
        opcao = input('Deseja reiniciar (S/N)? ').lower()  # converter para minúsculo
        print()
        if opcao not in ('s', 'n'):
            print('Opcao inválida. Deve ser S ou N')
            print()
        else:
            break  # sai do while interno, pois a opção é S ou N
    if opcao == 'n':
        break  #