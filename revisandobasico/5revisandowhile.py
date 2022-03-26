"""
While em Python - Aula 34
Utilizando para realizar ações enquanto
uma condição for verdadeira
Requisitos : Entender condições e operadores
"""
contador = 0

while contador < 2:
    nome = input('Qual é o seu nome? R:')
    print(f'Olá {nome}')
    contador += 1
    print(f'Contador: {contador}\n')


contador_2 = 0
while contador_2 <= 3:
    # Caso eu queira pular o numero 3
    if contador_2 == 3:
        contador_2 += 1
        print('Pulou')
    print(f'Numero {contador_2}')
    contador_2 += 1
print('')

"""
Continue - utilizado para pular para o próximo laço em uma repetição
"""
print('Utilizando continue')
cont_3 = 0
while cont_3 <= 5:
    if cont_3 == 3:
        cont_3 += 1
        print('Pulou')
        continue
    print(cont_3)
    cont_3 += 1
print('')
"""
Break - irá parar o laço
"""
print('Utilizando break')
# Desejo parar quando o contador chegar a 4
cont_4 = 0
while True:
    if cont_4 == 4:
        print('Irá parar')
        break
    print(cont_4)
    cont_4 += 1
print('')

# uma mini matriz
x = 0
y = 0

while x < 3:
    y = 0 # para reiniciar as linhas
    while y < 3:
        print(f'X = {x} e Y = {y}')
        y += 1
    x += 1
print('')
# concatenar strings

frase = 'o rato roeu a roupa do rei de roma'
nova_frase = ''
contador_new = 0

while contador_new < len(frase):
    nova_frase += frase[contador_new]
    contador_new += 1

print(f'Frase nova : {nova_frase}')
print('')


frase_velha = 'o rato roeu a roupa do rei de roma'
qtd_caracteres = len(frase_velha)
print(f'Frase velha : {frase_velha}')

frase_nova = ''
contador_t = 0
print('Digite a letra que você deseja que fique maiúscula')
letra_escolhida = input('Digite aqui:').lower()
while contador_t < qtd_caracteres:
    # aqui irá receber a letra
    letra = frase_velha[contador_t]
    if letra == letra_escolhida:
        frase_nova += letra_escolhida.upper()
    else:
        frase_nova += letra
    contador_t += 1

print(f'A frase nova ficou assim: {frase_nova}')



