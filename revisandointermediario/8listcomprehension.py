"""
List Comprehension (Compreensão de listas)
Utilizadas para otimizar em termos de performance e escrever menos linha de código
"""
print('List Comprehension ou Compreensão de listas')
lista_exemplo1 = [1,2,3,4,5,6,7,8,9]
# vou iterar sobre cada elemento da lista com uma linha de código só

lista_recebe1 = [valor for valor in lista_exemplo1]
# vou jogar cada elemento dessa lista_exemplo 1 para lista_recebe1
print(f'Lista inicial : {lista_exemplo1}')
print(f'Lista que recebeu : {lista_recebe1}')
# podemos realizar várias coisas com a variável, como, supondo que eu queria multiplicar por 2

lista_mult1 = [valor * 2 for valor in lista_exemplo1]
# primeiro eu coloco o que eu quero fazer com cada elemento e depois itero
print(f'Lista multiplicada: {lista_mult1}')

"""
Exemplo utilizando range(inicio, fim, step)
Supondo que eu queira criar uma tupla para cada elemetno da lista criando algo como uma coordernada
Exemplo : (0,1) (1,1) (1,2) (2,0) (2,1) (2,2)
"""
lista_coord = [(valor1 , valor2) for valor1 in lista_exemplo1 for valor2 in range(3)]
# o valor1 será os valores da lista_exemplos1
# já o valor 2 irá receber os valores do range(3)
# o primeiro for vai iterar sobre a lista
# o segundo for vai iterar com cada elemento dessa lista
print(f'Lista coordernada: {lista_coord}')

print(f'\nTrocando os caracteres, utilizando o replace')
lista_nomes = ['Lucas','Anildson','André','Marcelo']
# replace para modificar o caracter 'a' pelo @
# upper para deixar tudo maiúsculo

lista_replace = [valor.upper().replace('A','@') for valor in lista_nomes]
print(f'Lista original : {lista_nomes}')
print(f'Lista com os nomes modificados : {lista_replace}\n')

# próximo exemplo, suponha que há uma tupla
tupla_ex1 = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
"""
suponha que eu queira acessar a chave e o valor, e ao mesmo tempo, eu queira inverter eles
invés de ser assim : [(x, y) for x,y in tupla_ex1]
será [(y, x) for x,y in tupla_ex1]
"""
tupla_final1 = [(y,x) for x,y in tupla_ex1]
print(f'Tupla original : {tupla_ex1}')
print(f'Invertendo os valores: {tupla_final1}')
# poderiamos até transformar em um dicionário
tupla_final1 = dict(tupla_final1)
print(f'Tupla agora sendo um dicionário : {tupla_final1}, seu tipo : {type(tupla_final1)}\n')
"""
podemos também utilizar mais de um if na lista comprehension
Supondo que eu queira filtrar uma lista:
"""
lista_numerica = list(range(21))
print('Supondo que eu queira mostrar todos os numeros que sejam divisiveis por 2')
lista_div2 = [valor for valor in lista_numerica if valor % 2 == 0]
print(f'Lista : {lista_numerica}')
print(f'Divisiveis por 2 : {lista_div2}')

# agora pegando dois
lista_grande = list(range(100))
print(f'Criando uma lista com 100 números e pegando os divisiveis de 3 e 8')
exemplo_div3e8 = [valor for valor in lista_grande if valor % 3 == 0 if valor % 8 == 0]
print(f'Divisiveis por 3 e 8 : {exemplo_div3e8}')

print(f'\nUtilizando else:')

lista_enorme = list(range(50))

lista_mul3ornot = [ valor if valor % 3 == 0  else 'Não é divisivel' for valor in lista_enorme ]
print(f'Somente divisível por 3: {lista_mul3ornot}')

# Também podemos utilizar and, or, in, not in, not também

exemplo_and = [valor if valor % 3 == 0 and valor % 8 == 0 else 0 for valor in lista_enorme]

print(f'Utilizando and para divisivel por 3 e 8 : {exemplo_and}')




