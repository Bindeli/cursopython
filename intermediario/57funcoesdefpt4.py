"""
Funções Definidas - Aula 57

Não conseguimos alterar o valor de uma variável global através de uma variável local dentro de uma função
"""
# Quando eu defino uma função, posso utilizar em todo o código, até mesmo em uma função

variavel_exemplo = 'valor' # valor escopo global da variavel

def func_exemplo():
    # Estarei chamando ela de dentro de uma função
    print(variavel_exemplo)

def func_exemplo2():
    # se eu chamar a variável e definir um valor para ela, ela só irá mudar seu valor nesta função
    # fora desta função, ela tera seu valor antigo
    # ela só está acessível para essa função aqui
    variavel_exemplo = 'Outro valor'
    print(variavel_exemplo)

func_exemplo()
func_exemplo2()

# quando eu edito uma variavel, dentro da função, o valor dela não altera no escopo global

print(variavel_exemplo)

# Não é correto, mas quando queremos alterar o valor de uma variável de dentro da função, utilizamos o global
# global variável

# def func_defglobal():
#     # chamamos a função global, e depois a variável
#     global variavel_exemplo
#     variavel_exemplo = 'Um novo valor!'
#     print(variavel_exemplo)
#
# func_defglobal()

# Lembrando que isso não é uma boa prática, podendo deixar seu código muito estranho

# O correto é utilizar return ou argumentos

# variavel_exemplo = 'valor' é a principal variavel
print('')
print('Utiliando o replace e mudando o valor da variavel:')
def func_replace(arg=None):
    # replace é utilizado para trocar valores, caracteres.
    # irá trocar V pelo C
    arg = arg.replace('v', 'c')
    return arg

outra_variavel = func_replace(arg=variavel_exemplo)

print(outra_variavel)

"""
# Também não podemos chamar uma variável que está dentro uma função, dentro de uma outra função

Exemplo : 
def func():
    outra_variavel = 'valor'
    
def func2():
    print(outra_variavel)
    
pois a outra-variavel está dentro do escopo local da primeira função e ele só funciona dentro dessa função

Para resolver isso, podemos fazer deste jeito: utilizando return e jogar para uma variável:
"""
print('')

def func_outrav():
    variavel_alter = 'Um valor vindo de uma outra função'
    return variavel_alter

def func_outraalter(arg):
    print(arg)

variavel_alter = func_outrav()
func_outraalter(variavel_alter)
