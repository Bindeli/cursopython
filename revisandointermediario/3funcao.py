"""
Funções (def) em Python -
*args - utilizamos quando não sabemos quantos argumentos a função irá receber
**kwargs - argumentos com palavras chaves EX : 'nome'="Lucas"

"""

"""
Sobre argumentos nomeados: Quando eu seto um valor já para o argumento nomeados
os proximos argumentos depois dele , deverão também ser nomeados, ter um valor definitivo

"""

def func_exn(a1,a2,a3, nome='Lucas', a5=None):
    print(a1,a2,a3,nome,a5)
    return nome,a5

var_exn = func_exn(1,3,7,nome='Bindeli',a5='Algo para não dar erro')
# irá virar uma tupla
print(f'Variavel : {var_exn}')
# por causa do return, a variável só recebeu nome e a5

"""
Função de *arg : Quando não sabemos quantos argumentos iremos receber na função

"""

def fun_arg (*args):
    print('Mexendo com *args')
    print(args)
    print(args[0]) # primeiro elemento
    print(args[2]) # terceiro elemento
    print(args[-1]) #ultimo
    print(len(args))

fun_arg(1,2,4,6,7,8,12)

"""
Função de **kwargs - Quando os argumentos tem palavras chaves

"""
print('\nMexendo com Kwargs:')
def fun_kw(*args,**kwargs):
    print(f'Args : {args}')
    print(f'Kwargs : {kwargs}')
    # quando eu quero saber se tem a chave que o usuário enviou, eu utilizo get
    # eu crio uma variavel para receber o resultado
    nome = kwargs.get('nome')
    print(nome)
    # quando não tiver, o valor irá retornar como None, que não existe
    idade = kwargs.get('idade')
    print(idade) # irá aparecer None

fun_kw(1,2,9,7,5,8, nome='Lucas',sobrenome='Bindeli')

"""
Não conseguimos alterar valores de uma variável global através de uma variável local em uma função
"""
print('\nNão conseguimos alterar o vlaor de uma variavel global dentro de uma função')
variavel_global = 'valor'

def fun_naltera():
    # chamando a função global pela função, posso pegar o valor dela
    print(variavel_global)
fun_naltera()
print('\nPorém podemos induzir um valor que será recebido somente na função')
def fun_alt():
    variavel_global = 'valor somente na função'
    print(variavel_global)

fun_alt()

print('O valor alterado na função, não irá seu escopo global\n')
print('Não é uma boa prática, mas podemos alterar utilizando a função global')
print('Desta maneira:\n')
def func_altglobal():
    #chamamos a função global, e depois a variável
    global variavel_global
    variavel_global = 'Um novo valor!'
    print(variavel_global)

func_altglobal()
print(f'A variável agora tem um novo valor: {variavel_global}\n')
print('Não é uma boa prática, o correto seria utilizar o return ou argumentos')
print('\nUtilizando o replace e mudando o valor da variavel')

def fun_replace(var):
    # replace é utilizado para trocar caracteres
    # primeiro a letra que será alterada e depois pelo que será trocado
    var = var.replace('v','@')
    return var

outra_variavel = fun_replace('variavel exemplo')

print(outra_variavel)
print('')

"""
Também não podemos chamar uma variável que está dentro de uma função para dentro de uma outra função

pois a outra variável está dentro do escopo local da primeira função e ele só funciona dentro dessa função

Para resolver isso, poemos fazer deste jeito : utilizando return, e jogar para uma variável

"""

def primeirafunc():
    variavel_func = 'valor da variavel da primeira função'
    return variavel_func

def segunda_func(arg):
    print(arg)

variavel_p = primeirafunc()
segunda_func(variavel_p)


