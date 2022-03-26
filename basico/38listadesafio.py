"""
Jogo da força com palavra secreta

"""

palavra_secreta = 'perfume'
digitado = []
letras_erradas = []
chances = 5
while True:
    print(f'Você ainda possui: {chances} chances.')
    letra = input('Digite uma letra: ')

    if chances == 0:
        print('')
        print(f'Você perdeu!')
        break
    if len(letra) > 1:
        print('Deve digitar somente uma letra.')
        print('=============================================')
        continue

    digitado.append(letra)

    if letra in palavra_secreta:
        print(f'Acertou uma letra! A letra {letra} existe na palavra secreta!')
        print('')
    else:
        print(f'A letra {letra} não existe na palavra secreta!.')
        print('')
        # chances -= 1
        digitado.pop()
        letras_erradas.append(letra)
    print(f'Letras digitadas : {digitado}')
    print(f'Letras errada : {letras_erradas}')
    print('')
    print(f'Formando a palavra secreta:')
    secretotemp = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in digitado:
            secretotemp += letra_secreta
        else:
            secretotemp += '*'

    print('')

    if letra not in palavra_secreta:
        chances -= 1

    if secretotemp == palavra_secreta:
        print(f'Parabéns, você adivinhou a palavra secreta!! A palavra era: {secretotemp}')
        print('')
        break
    else:
        print(f'A palavra secreta está assim: {secretotemp}')
        print('=============================================')
        continue



