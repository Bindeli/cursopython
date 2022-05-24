"""
AULA 91 - FUNÇÕES DECORADORAS E DECORADORES

Uma função decoradora é uma função que aceita outra função como argumento (a função decorada), realiza algum
processamento com a função decorada e a devolve ou a substitui por outra função que poderá ser invocada
posteriormente. S
ó nesse trecho já da pra perceber que você pode interceptar a chamada de uma função, fazer alguma coisa
no meio do caminho e depois devolver uma nova função (mudando o comportamento da função real).


Um uso comum para um decorador é o de medir o tempo de execução de um bloco de código qualquer.
Isso pode ser útil na otimização de um programa. Para isso usamos o módulo time, e suas funções time.time(),
que lê a hora em segundos †, e time.sleep(n), que suspende a execução do código por n segundos.

Um decorador é uma entidade que pode ser chamada, e que aceita outra dessa entidade (como alvo) e retorna,
mais uma vez, uma dessas entidades (o decorador) que aceita os mesmos argumentos do alvo original.
O que é uma entidade que pode ser chamada? Isso, em Python, é um objecto que tem o método __call__().

"""

"""
Funções decoradoras recebem uma função como parâmetro e decoram/modificam
ela retornando uma nova a ser usada no lugar.
"""


def fala_oi():
    print('Oi')

fala_oi()

# um exemplo bem básico
#____________________________________________________________________________________________________________________
print('')
# também posso jogar uma função em uma variável

variavel_oi = fala_oi
variavel_oi()

print(type(variavel_oi)) # vai aparecer que ela é uma função
# Agora estou executando a variável como uma função
#____________________________________________________________________________________________________________________

# Outra coisa que posso realizar em Python é criar uma função dentro de uma outra função
# Porém para funcionar, devo executar a função que foi criada dentro


"""
def mestre(): # criei uma função mestre
    def slave(): # e dentro do corpo da função mastrei criei uma outra função para fazer qualquer coisa
        print('Olá!')
"""
# Para executar a função mestre, terei que executar a função slave
# master() # Não irá executar pois a função só criar uma outra função
# então o que eu quero é criar a função e executar a função
print(f'\nAgora vou executar uma função que tem uma outra função dentro dela:')
def mestre(): # criei uma função mestre
    def slave(): # e dentro do corpo da função mastrei criei uma outra função para fazer qualquer coisa
        print('Olá! Estou sendo printando de dentro de uma função!')
    return slave # então vou chamar a slave para ser executada
    # slave()
mestre()

# também posso passar ela para uma variavel

variavel_func_master = mestre
print(f'Agora vou printar a variavel que recebeu a função mestre:')
variavel_func_master()
#____________________________________________________________________________________________________________________
"""
Agora vamos criar uma função que irá receber uma função como parâmetro, e dentro do função de há nela
que no caso é slave_2, irá receber a função que irei colocar como parâmetro


"""
print(f'\nAgora vou trabalhar com uma função que receber como parâmetro, uma outra função!')
print(f'Lembrando que a função que irá receber também possui uma função!!!!!!\n')

def falar_ola():
    print('Olá!!! Função_Olá')

# invés de executar o print na função mestre, eu irei executar a minha função falar_ola

def mestre_2(funcao):
    def slave_2(): # essa função escrava 2 vai fazer o trabalho que executar a função que a mestre está recebendo
        print('Agora estou decorada!')
        funcao()
    return slave_2 # e aqui vou retornar a função slave_2 sem executar ela

variavel_func_mestre2 = mestre_2(falar_ola)
print(f'\nAgora vou executar uma variável que recebeu a função:')
variavel_func_mestre2()

#____________________________________________________________________________________________________________________
"""
Também posso fazer com que a função falar_ola() receba a mestre_2 como parâmetro a própria falar_ola()
"""
print(f'Agora vou fazer com que a função falar_ola receba a função mestre_2:')
falar_ola = mestre_2(falar_ola)
falar_ola()

"""
A função falar_ola já está decorada,
A função falar_ola foi decorada com a função mestre_2
"""
#____________________________________________________________________________________________________________________
print('')
# Agora quero decorar algo com essa função master, como parâmetro, eu faço deste modo:

def master(funcao):
    def escrava():
        print(f'Agora estou decorada!')
        funcao()
    return escrava

@master # isso é uma função decoradora
def falando_algo():
    print('Um print mostrando algo, utilizando a função mestre_2 como decoradora')

#@master porém se eu tentar colocar um decorador nela vai dar erro!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# esse erro : master.<locals>.escrava() takes 0 positional arguments but 1 was given
def outra_funcao(mensagem):
    print(mensagem)

print(f'Primeira função falando algo: ')
falando_algo()
print(f'\nSegunda função de mensagem: ')
outra_funcao('Olá estou printando a minha mensagem pela função')

#____________________________________________________________________________________________________________________

"""
Para resolver este erro, podemos utilizar o *args e **kwargs!
"""
print(f'\nAgora vou utilizar args e kwargs para resolver um erro')
def novo_master(funcao):
    def novo_escravo(*args, **kwargs):
        print('Utilizando args e kwargs, estou decorada: ')
        funcao(*args, **kwargs) # a função que veio como parâmetro
    return novo_escravo

@novo_master
def falando_outracoisa():
    print(f'A primeira mensagem da primeira função!')

@novo_master
def funcao_secundaria():
    print(f'Isso pertence a uma outra função!')

print(f'\nPrimeira função:')
falando_outracoisa()

print(f'\nSegunda função')
funcao_secundaria()
#____________________________________________________________________________________________________________________

"""
Geralmente a função decoradora é utilizada, normalmente, para adicionar algum recurso na função
Ou por exemplo:
"""
print(f'\nTestando quanto tempo demora para uma função ser executada!')
# para vermos o tempo
from time import time
# para fazer a função dormir por alguns segundos
from time import sleep

# Testando o tempo que uma função leva para executar!!

def velocidade(funcao): #função decoradora
    def interna(*args, **kwargs):
        tempo_inicio = time() # to pegando o tempo atual
        resultado = funcao(*args, **kwargs) # a variavel vai receber a função! , vai começar a executar
        end_time = time() # e depois que executou, vou pegar o tempo
        tempo = (end_time - tempo_inicio) * 1000
        # por que 1000 ? vai gerar um número bem grande, e vou transformar para milisegundos
        print(f'A função {funcao.__name__}levou {tempo:.2f}ms para executar!')
        return resultado
    return interna # vai retornar a função interna sem executar

# agora vou criar uma função que demora a ser executada
@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1) # a cada volta do laço, vai dormir 1 seg

demora()


#____________________________________________________________________________________________________________________
