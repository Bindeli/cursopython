"""
For in Python
While é utilizando quando não sabemos o final
Já o For, é quando temos algo que sabemos que tem final
iteração string com for
Função range(start = 0, stop, step = 1)

"""
texto = 'Python'
#Aqui não temos contador, mas podemos utilizar enumarate, que numera cada laço do for
# letra vai ser uma variavel
for letra in texto:
    print(f'Letra : {letra}')
"""
for n, letra in enumerate(texto):
    print(n,letra) 
    # irá aparecer os indices e a letra ao lado
"""
# range returna uma sequencia de numeros
for numero in range(5):
    print(numero) # Vai mostrar de 0 a 4
# range recebe 3 argumentos, o start que eu decido onde vai começar, o stop, onde eu decido que vai parar
# e também o step, de quantas em quantas casas ele irá andar
novotexto = ''
for c in range(0, 6, 1):
    print(f'Vez do número {c}')
# para apresentar valores decrecente
for n in range(10,5,-1):
    print(f'Decrecente: {n}')

# para modificar uma informação, como colocar letra minuscula para maiuscula
print('')
texto_min = 'python'
texto_mai = ''

for let in texto_min:
    if let == 't':
        texto_mai = texto_mai + let.upper()
    elif let == 'h':
        texto_mai += let.upper()
    elif let == 'o':
        continue
    else:
        texto_mai += let
print(f'Agora com algumas letras maiusculas sem a letra "o": {texto_mai}')
# caso eu quisesse que uma letra não fosse aparacer na minha nova string, inves de adicionar, era só colocar um continue



