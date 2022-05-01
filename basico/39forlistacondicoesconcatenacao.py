"""
iteração = for, cada volta que o for dá

"""

palavra_secreta = 'python'
digitados = ['p','n','d','t','s']
secreto_temporario = ''

for letra in palavra_secreta:
    if letra in digitados:
        secreto_temporario += letra
    else:
        secreto_temporario += '*'


print(f'Secreto : {secreto_temporario}')






