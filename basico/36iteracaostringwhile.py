"""
Aula 36
Iteração String com While em Python
Um valor que tem indices, é um valor iterável - ato de percorrer cada um dos elementos

"""
#        Indices
#        0123456789                      33
frase = 'o rato roeu a roupa do rei de roma'

tamanho_frase = len(frase)
print(tamanho_frase)

# para eu acessar a informação no indice 5, eu chamo a variavel e coloco o indice dentro do []
print(f'A letra no indice 5 é : {frase[5]}') # a letra que está no indice 5 será a letra o

# este conteúdo irá mostrar a letra e seu indice, basta tirar os "#"
# contador = 0
# while contador < tamanho_frase:
#     print(f'Letra: {frase[contador]}, Indice: {contador}')
#     contador += 1

# concatenar strings
nova_frase = ''
contador_new = 0
# isso que estamos fazendo com while é iteração
while contador_new < tamanho_frase:
    # tem que ser mais com recebe, pois se repetir sem o mais, irá excluir o dado que possui
    # então ele tem que receber o conteúdo que ele já possui e adicionar o novo elemento
    nova_frase += frase[contador_new]
    contador_new += 1

print(f'Frase nova : {nova_frase}')

# caso eu queira deixar algumas letras em maiusculo como por exemplo o R, eu devo utilizar um if e
# colocar para receber uma versão da palavra desejavel em maiúsculo
#exemplo
nova_string = ''
contador_new2 = 0
while contador_new2 < tamanho_frase:
    # criar uma variavel para receber a letra
    letra = frase[contador_new2]
    # eu escolhi a letra r para virar maiúscula
    if letra == 'r':
        # coloco para receber um R maiúsculo invés do r minúsulo que está no indice
        nova_string += 'R'
    else:
        nova_string += frase[contador_new2]
    contador_new2 += 1

print(f'A nova frase com letras maiúsculas: {nova_string}')

# caso eu fosse pedir para o usuário escolher a letra que deseja deixar maiusculo
# eu iria criar uma variavel para receber um input com a letra
# e no if == 'letrainserida':
# e na hora de colocar a novastring para receber a letra, iria digitar letrainserida.upper()



