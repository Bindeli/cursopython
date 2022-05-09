"""
AULA 85 - Uso de Try e Except como condicional


"""

#______________________________________________________________________________________________________________
# Criando uma função que converter em inteiro ou float

# A função isinstance () retorna True se o objeto especificado for do tipo especificado, caso contrário, False .
def converte_numero(valor):
    # Vamos tentar fazer a função converter
    try:
        # vai tentar converter o número para inteiro primeiro
        valor = int(valor)
        return valor
    # se ela não conseguir, vai entrar neste except
    except ValueError:
        try:
            # primeiro vai entrar neste try, e tentar converter para um float
            valor = float(valor)
            return valor
        # e se ela não conseguir, vai retornar o que ela retorna como padrão, None
        except ValueError:
            pass

rodar = True
while rodar:
    numero = converte_numero(input('Digite um número: '))
    rodar = input('Digite continuar? ').lower()

    if rodar == 'n' or rodar == 'N':
        rodar = False


    if numero is not None:
        print(f'{numero} * 5 : {numero * 5}')
    else:
        print(f'O dígito inserido não é um número')







#______________________________________________________________________________________________________________








#______________________________________________________________________________________________________________







#______________________________________________________________________________________________________________








#______________________________________________________________________________________________________________






