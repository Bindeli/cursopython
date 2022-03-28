# print('Hello World!')
# print('Este é novo um começo')
# comando print para aparecer na tela, o que está dentro do '' que irá aparecer
# pode utilizar tanto "" aspas duplas ou aspas simples
# Comando para comentário

"""
Também pode ser usado como comentário as 3 aspas duplas para abrir e fechar o comando
"""

print('Linha 1') # vai mostrar uma linha
print('Linha 2') # logo abaixo irá aparecer este comando
print('Linha 3')

while True:
    altura = 1.68
    peso = input('Digite o peso ou s para sair: ')
    peso = float(peso)
    if peso == 's' or peso == 'S':
        break
    else:
        imc = peso / altura ** 2
        print(f'Seu imc é de : {imc}')


"""
mexer com banco de dados (armazenamento de dados)
modelagem de dados
pipe lines
tratar dados
"""
