from intermediario.criandopacotesmodulos88.vendas.formata.preco import real


def aumento(valor, porcentagem, formata = False):
    resultado = valor + (valor * (porcentagem/100))
    if formata:
        return real(resultado)
    else:
        return resultado

def reducao(valor, porcentagem, formata = False):
    resultado = valor - (valor * (porcentagem/100))

    if formata:
        return real(resultado)
    else:
        return resultado

