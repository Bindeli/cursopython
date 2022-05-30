lista_regressiva = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
# ctrl + alt + L para corrigir os espaços

def valida(cnpj):


    novo_cnpj = tiracaracter(cnpj[:-2])
    cnpj = tiracaracter(cnpj)

    verifica = verfsequencia(novo_cnpj)

    novo_cnpj = transforma_lista(novo_cnpj)

    soma = calculardigito(novo_cnpj)
    formula_1 = 11 - (soma % 11)
    if formula_1 > 9:
        formula_1 = 0
    novo_cnpj.append(formula_1)

    soma_2 = calculardigito(novo_cnpj)
    formula_2 = 11 - (soma_2 % 11)
    if formula_2 >9:
        formula_2 = 0
    novo_cnpj.append(formula_2)
    novo_cnpj = transformar_string(novo_cnpj)
    print(f'Final : {novo_cnpj}')

    if novo_cnpj == cnpj:
        return print(f'CNPJ Válido! {novo_cnpj} e {cnpj}')
    else:
        return print(f'CNPJ Inválido! {novo_cnpj} e {cnpj}')


def transformar_string(cnpj):
    novo_cnpj = []
    for elemento in cnpj:
        novo_cnpj.append(str(elemento))
    novo = ''.join(novo_cnpj)
    return novo

def calculardigito(cnpj):
    soma = 0
    contador = 0
    if len(cnpj) == 12:
        contador = 1
    elif len(cnpj) == 13:
        contador = 0
    for elemento in cnpj:
        soma += elemento * lista_regressiva[contador]
        contador += 1
    return soma

def tiracaracter(cnpj):
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    return cnpj

def transforma_lista(cnpj):
    lista = []
    for elemento in cnpj:
        lista.append(int(elemento))
    return lista

def verfsequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        print('Há uma sequência, o cnpj não é válido')


