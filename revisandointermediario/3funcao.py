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






