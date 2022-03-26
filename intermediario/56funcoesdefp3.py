"""
Funções (def) em Python -
*args - utilizamos quando não sabemos quantos argumentos a função irá receber
**kwargs - argumentos com palavras chaves EX : 'nome'="Lucas"

"""
# Sobre Argumentos nomeados: quando eu seto um valor já para o argumentos
# os próximos argumentos também deverão ter um valor definido
# Exemplo:

def func_arg(a1,a2,a3, nome = None, a6=None):
    print(a1,a2,a3, nome, a6)
    return nome,a6

# e apartir do momento que eu chamo um valor nomeado, eu não posso chamar sem nomear
# errado : func_arg(1,2,3, nome='Lucas', a6)
# Correto : func_arg(1,2,3, nome='Lucas', a6='Algo')

# Para uma variavel receber o valor de uma função, tem que ter return e o valor desejado
# a variável se tornará uma tupla
var = func_arg(1,2,3, nome='Lucas', a6='Algo')
print(f'Váriavel como Tupla : {var} {type(var)}')
print('')
# Pode ter um momento que você não saiba quantos argumentos a função irá receber
# então utilizamos a *args

def func_args(*args):
    # Também podemos verificar quais são os elementos
    # Porém lembrando que tupla não pode ser modificada
    print(args) # Aqui veremos a tupla inteira
    print(args[0]) # o primeiro elemento
    print(args[-1]) # o ultimo elemento
    print(len(args)) # verificar quantos elementos há


func_args(1,2,3,4,5,6)
print(' ')

# Por Tuplas não poderem ser modificadas, podemos transformar-las em listas primeiro para fazer uma modificação pela
# função definitiva
# Exemplo :
print('Modificando um valor:')
def func_mod(*args):
    args = list(args) # transformando em lista
    args[0] = 20 #modificando o primeiro valor no indice 0 para 20
    print(args) # irá printar uma lista, dá para ver pelos "[]"

func_mod(1,2,3,4,5,6)

# Para desempacotar elementos :
print('')
print('Adicionando uma lista junto com outros elementos')
def func_add (*args):
    print(args)

lista1 = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
# se eu não colocar o asterísco *, a lista inteira contará como um elemento só
func_add(lista1,10,20,30,40,50) # a lista contará como um elemento
func_add(*lista1,10,20,30,40,50) # cada elemento da lista agorá irá ficar em um índice separado
func_add(lista1, lista2) # nesse as duas listas ficarão separadas e contará como apenas 2 índices
func_add(*lista1, *lista2) # nesse as duas listas irão se juntar e cada elemento terá um índice próprio

# **kwargs - quando os argumentos tem palavras chaves
print('')
print('Utilizando Kwargs:')

def fun_pc(*args, **kwargs):
    print(args)
    print(kwargs)
    # print(kwargs['nome']) # caso eu queira acessar somente a nomeada com nome
    # Caso eu queira saber se alguém enviou algo, e quero saber se tem nome
    # eu crio uma variavel
    nome = kwargs.get('nome')
    print(nome)
    # também dá para descobrir se não tem
    # é bom utilizar get quando não temos certeza se a chave existe, se não existe, irá voltar como None
    idade = kwargs.get('idade')
    # irá aparecer como None
    print(idade)

fun_pc(1,2,3,4,5,6, nome='Lucas', sobrenome='Bindeli')




