"""
While / Else - Aula 35
Contadores
Acumuladores
"""
contador = 1

# um valor que você vai adicionar a cada laço
acumulador = 1

# o while será executado até a expressão se tornar falsa
while contador <= 10:
    print(f'Contador atual é {contador} e acumulador será de {acumulador}')
    # a cada laço, vai receber ele e o contador, só de exemplo, pode ser qualquer valor
    acumulador = acumulador + contador
    contador += 1
else:
    print('Agora é a vez do else logo após o while')

# caso eu crie uma condição e utilize o break neste laço, irá também rejeitar o else que está no laço while
# if algo, break, vai ignorar o else também
contadorbreak = 1
print('')
while contadorbreak < 5:

    if contadorbreak == 4:
        break

    print(f'Contador : {contadorbreak}')
    contadorbreak += 1
else:
    print('No break, o else, não será executado')
print('No contador 4 irá dar um break no código e irá pular o else')


