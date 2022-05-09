"""
AULA 84 - LEVANTANDO EXCEÇÕES EM PYTHON (raise)

Como lançar suas própris exceções

Para lançar uma exceção de dentro de uma função ou método, usa-se o comando raise

# Link que contém todas as exceções que podemos utilizar no Python :

https://docs.python.org/3/library/exceptions.html

"""

# def dividir(num1, num2):
#     return num1/num2
#
# print(dividir(2,0))

# Suponha que um outro desenvolvedor olhe para o código e chame valores inválidos igual o exemplo acima
# Para contornar, posso mostrar ou criar um log do erro que está aparecendo
# Como no exemplo abaixo

def dividir(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError as error1:
        print(error1)
        return False
print(dividir(2,0))

# se eu lançar um try agora, não irá ler a exceções, pois o que vai dominar será o try e except da função

try:
    print(dividir(10,0))
except:
    print(f'Error, não irá aparecer')
#_______________________________________________________________________________________________________

# Agora utilizando o ""raise""
print('\nAgora utilizando o Raise!!!')

# Com isso posso logar um erro e depois capturar ela posteriormente, o segundo except não será ignorado
# Eu quero logar o erro que ocorreu na função, e reelançar depois para o dev
print(f'Primeiro na função:')
def dividindo(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError as erro_3:
        print('Log : ',erro_3)
        raise


# Com o raise, agora o try e except irá capturar a exceção
try:
    print(dividindo(3,0))
except ZeroDivisionError as erro_4:
    print(f'Agora fora da função:')
    print(erro_4)
#_______________________________________________________________________________________________________
# Uma outra coisa que podemos fazer é lançar sua própria mensagem de erro, sua própria exceção

# Supondo que eu queira levantar minha própria exceção caso alguém utilize essa função de forma incorreta

print(f'\nCriando nossa própria mensagem de erro: ')
def dividindo3(num1,num2):
    if num2 == 0:
        raise ValueError('Número 2 não pode ser 0.')
    # No pycharm, podemos ver todas as exceções só digitando Error
    return num1/num2

print(dividindo3(10,5)) # Não vai dar erro
print(dividindo3(6,2)) # Não vai dar erro
# print(dividindo3(10,0)) # Vai chamar o erro que criei com a mensagem que coloquei para aparecer
# ValueError: Número 2 não pode ser 0. , isso irá aparecer no console

# Se eu quiser capturar a minha exceção, eu posso criar um try e except

try:
    print(dividindo3(2,0))
except ValueError as erro_5:
    print(f'Log: {erro_5}, esse error aqui, eu jogaria em um arquivo de texto')
    # Para o usuário final, abaixo
    print(f'Você está tentando dividir por 0.')

# Para o usuário final, não deverá aparecer o erro para ele
# Para o usuário final, deverá aparecer alguma coisa mais significativa
#_______________________________________________________________________________________________________
