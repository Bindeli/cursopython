"""
Jogo da forca em python

"""

palavra_secreta = 'perfume'
digitados = []
letras_erradas = []
chances = 5

while True:
    print(f'Você ainda possui: {chances} chances.')
    letra = input('Digite uma letra: ')

    if chances == 0:
        print('Você perdeu!!')
        break

    if len(letra) > 1:
        print('Você deve digitar apenas uma letra')
        print('-'*50)
        continue

    digitados.append(letra)

    if letra in palavra_secreta:
        print('Essa letra possui na palavra secreta!!!!!!!!!!!!!')
    else:
        letras_erradas.append(letra)
        digitados.pop()
        print('Essa letra não pertence a palavra secreta')
    print(f'Digitados Corretamente : {digitados}')
    print(f'Letras erradas: {letras_erradas}')
    print('')

    secreto_temp = ''
    for letra_digitado in palavra_secreta:
        if letra_digitado in digitados:
            secreto_temp += letra_digitado
        else:
            secreto_temp += '*'

    if letra not in palavra_secreta:
        chances -= 1

    if secreto_temp == palavra_secreta:
        print(f'Parabéns você acertou!! Palavra : {secreto_temp}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}')
        print('='*50)
        continue


    print('')

