"""
AULA 92 - PROBLEMAS DOS PARÂMETROS MUTÁVEIS EM FUNÇÕES

"""

# problema com argumentos padrões mutáveis em funções

# iterável, qualquer coisa que você pode percorrer por ela

# Se eu tiver uma lista pronta, ela irá para o argumento secundário lista=[]

# Eu mando uma lista, se ela lista já existir, elas serão unidas dentro da função

def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista

clientes_1 = lista_de_clientes(['Lucas','Anildson','André','Marcelo'])
# suponha que em outra parte do meu código, eu queira criar uma outra lista de clientes
clientes_2 = lista_de_clientes(['João','Gabrieal','Rafaela','Leticia'])

print(f'Lista 1: {clientes_1}')
print(f'Lista 2: {clientes_2}')

"""
Deste modo, as duas listas de clientes, que devia ser separada, foram unidas

Lista 1: ['Lucas', 'Anildson', 'André', 'Marcelo', 'João', 'Gabrieal', 'Rafaela', 'Leticia']
Lista 2: ['Lucas', 'Anildson', 'André', 'Marcelo', 'João', 'Gabrieal', 'Rafaela', 'Leticia']

Este é o problema de você ter algum argumento de algo mutável

# Alguns exemplos :
# Objetos mutáveis : como Listas, dicionários
# Objetos imutáveis : tuplas, string, números (int, float), boolean, None
"""

"""
Quando o interpretador do Python detecta uma função, ele avalia os argumentos padrões uma vez só.
Ele setou essa lista uma vez e a cada vez que eu chamar essa função, se eu não passar uma lista aqui (lista=[])
Ele vai usar uma lista padrão da função


Eu posso criar várias e várias listas/variáveis, que eu não vou alterar em nada, eu to apenas me referindo a 
lista da função padrão que vai manter, se eu mandar 10x, ela só irá alongar a mesma lista, ela não está mudando
a lista.

clientes_1 = lista_de_clientes(['Lucas','Anildson','André','Marcelo'])
clientes_2 = lista_de_clientes(['João','Gabrieal','Rafaela','Leticia'])
clientes_3 = lista_de_clientes(['José']) 

se eu adicionasse no clientes_3, um valor, ele já vai estar no clientes_1

Eu criei 3 variáveis e todas elas possuem o mesmo valor
"""
#____________________________________________________________________________________________________________________

# Para corrigir este problema podemos fazer desta maneira:
# Eu posso enviar um atributo imutável, que no caso é None, para a lista como argumento da função
# Exemplo : lista = None

print(f'\nCorrigindo o problema da repetição com argumento mutável:')

def nova_lista_clientes(clientes_iteravel, lista=None):
    if lista is None: # para arrumar o erro pois não podemos utilizar extend em um valor None
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_de_clientes_1 = ['Bindeli']
# Criei uma lista aqui com apenas um valor para passar para a próxima variável, isso já irá resolver

clientes_new1 = nova_lista_clientes(['Junior','Ribeiro','Angeli'], lista_de_clientes_1)
clientes_new2 = nova_lista_clientes(['Silva','Pereira','Di Caprio'])
clientes_new3 = nova_lista_clientes(['Camara','Souza','Rodrigues'])

print(f'Agora todas as listas terão seus valores independentes : ')
print(f'Nova Lista 1 : {clientes_new1}')
print(f'Nova Lista 2 : {clientes_new2}')
print(f'Nova Lista 3 : {clientes_new3}')
#____________________________________________________________________________________________________________________

# Então não podemos utilizar objetos mutáveis como parâmetros de uma função
# E caso precise, podemos fazer igual o segundo Exemplo


