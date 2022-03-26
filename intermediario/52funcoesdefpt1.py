"""
Funções - def em Python (Parte 1)
"""
#Estou definindo uma função com o def
def funcao():
    print('Hello! Essa é uma função')
#Chamando a função, tudo que está definido na função será executado,
funcao()
# caso eu preciso alterar o que tiver nesse código, só eu ir na função definida, e mudar por lá invés de ir no próprio código e mudar.
# as função definidas permitem que você não precise repetir um tipo de código várias vezes.
# se você precisar repetir o código mais de uma vez, é interessante colocar em uma estrutura de repetição,
# ou em uma função,

# o parênteses recebe um parâmetro, ou mais parâmetros, depende do que eu quero
# os parâmetros são basicamente variaveis que nós criamos e que nós passamos para nossa função.
# essa variavel que eu criei chamada de mensagem, pode ser colocar em qualquer lugar da função
print('')
def funcao1(mensagem):
    print(mensagem)

funcao1('Mensagem Enviada!')
print('')
# Vou criar uma função que pegue uma string, e no lugar de uma letra, receba um caracter
# eu crio uma variavel que irá representar a variavel do código
# e depois chamo a função definida pelo nome, com a variavel de string dentro do parênteses
# aqui começa a função

def maiusc(var1):
    string_mod = ''
    for letra in var1:
        if letra == 'e':
            string_mod += '@'
        else:
            string_mod += letra
    print(string_mod)
#aqui terminar a função

string1 = 'Mensagem alterada!'
maiusc(string1)


print('') # Para saltar uma linha
# Criando uma função definida como saudação
# ela irá receber dois parâmetros
def saudacao(msg, nome):
    print(f'{msg}, {nome}!!!')
# dentro está o primeiro parâmetro que é a msg, e separado por vírgula está o outro parâmetro sendo nome
saudacao('Seja Bem-Vindo', 'Lucas')
# posso chamar ela mais de uma vez
saudacao('Tudo bem com você?', 'Lucas')
# caso eu não envie parâmetros, tenho que definir na própria função
print('')

# Argumentos nomeados
def semvalor(msg1 = 'Olá! Tudo bem?', nome= 'Lucas'):
    print(f'{msg1}!!, {nome}!')

semvalor()
# caso eu queira que apenas um argumento tenha um valor definido no código e o outro receba o padrão
# eu tenho que identificar no parênteses e chamar um dos parâmetros
semvalor(nome='Bindeli')

# Utilizando o replace, para alterar um caracteres e ser alterado por outro
print(' ')
def replace(nome):
    # primeiro digito qual caracteres vai ser alterado, e no segundo irei inserir por qual será alterado
    # no exemplo, toda a letra i, irá virar *
    nome = nome.replace('i', '*')
    print(nome)

replace('Lucas Bindeli')



