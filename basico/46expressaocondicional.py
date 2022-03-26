nome = input('Qual o seu nome? R: ')

# checando se a pessoa digitou alguma coisa
# if nome:
#     print(nome)
# else:
#     print('Digite algo! Você não digitou nada!')
# Simplificando o código :

print(nome or 'Você não digitou nada')
# posso fazer vários or na mesma expressão
# print ( nome or expressao1 or expressao2 or 'Você não digitou nada' ) ele irá parar na primeira verdadeira
print('')

a = 0  # retorna falso
b = None # retorna falso
c = False # retorna falso
d = [] # uma lista vazia retorna falso
e = {} # um Dicionario vazio retorna falso
f = 22 # retorna verdadeiro
g = 'Lucas' # retorna verdadeiro
# ele irá pegar o primeiro verdadeiro e gravar o valor dela
variavel = a or b or c or d or e or f or g

print(f'{variavel}')



