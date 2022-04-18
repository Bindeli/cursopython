"""
Aula 66 - List Comprehension (Compreensão de listas)
São utilizadas para :
Otimização - em termos de performance
Escrever menos linha de código.
"""

lista_l1 = [1,2,3,4,5,6,7,8,9]
# e agora eu vou iterar sobre cada elemento da lista l1 com uma linha de código só
lista_l2 = [valor for valor in lista_l1]
# quero jogar cada elemento dessa lista l1 para a lista l2
# Estou enviando cada elemento para a variável valor e criando uma nova lista
print(f'Lista 1 : {lista_l1}')
print(f'Lista 2 : {lista_l2}')

# podemos fazer várias coisas com a variavel
# supondo que eu queira multiplicar a variável por 2

lista_m1 = [variavel * 2 for variavel in lista_l1]
# cada valor da lista, foi multiplicado por 2
print(f'Lista multiplicada : {lista_m1}')

# supor que eu queira criar uma tupla para cada elemento da lista criando algo tipo uma coordernada
# Ex : (0,1) (1,1) (1,2) (2,0) (2,1) (2,2)

lista_coor1 = [(valor1, valor2) for valor1 in lista_l1 for valor2 in range(3)]
# o primeiro for vai iterar sobre a lista
# e o segundo for vai iterar com cada elemento desta lista
print(f'Lista Coordernada : {lista_coor1}')
# Resultado : Lista Coordernada : [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2)]
print('')
# Trocando caracteres, utilizando o replace

lista_nome = ['Lucas', 'André','Anildson','Marcelo']
# replace para modificar o caracter 'a' pelo @
# upper para deixar tudo maiúsculo
lista_replace = [valor.upper().replace('A','@') for valor in lista_nome]
print(f'Lista com nomes modificados a por @: {lista_replace}')

# Próximo exemplo
# Suponha que há uma tupla
print('')
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),

)

# suponha que eu queira acessar a chave e o valor, e ao mesmo tempo, eu queira inverter
# invés de ser assim : [(x, y) for x,y in tupla]
# para inverter ficará trocado o x pelo y no primeiro espaço:
tupla_ex1 = [(y, x) for x,y in tupla]
print(f'Tupla invertida: {tupla_ex1}')
# poderia até transformar em um dicionário :
tupla_ex1 = dict(tupla_ex1)
print(f'Tupla agora em dicionário : {tupla_ex1}')

# podemos também utilizar mais de um if na list comprehension
# suponha que eu queira filtrar uma lista

lista_nova = list(range(20))
# supondo que eu queira mostrar todos os números que sejam divisíveis por 2
print('')
# pegando todos os números que são divisiveis por 2
exemplo_div = [valor for valor in lista_nova if valor % 2 == 0]
print(f'Lista : {lista_nova}')
print(f'Divisiveis por 2 : {exemplo_div}')

# agora pegando dois
lista_grande = list(range(100)) # tem de 0 a 99

exemplo_div2 = [ valor for valor in lista_grande if valor % 3 == 0 if valor % 8 == 0]
print(f'Divisiveis por 3 e 8 : {exemplo_div2}')

# como utilizariamos o ""else"" neste modo ?
lista_div3 = list(range(16)) # até o 16 para pegar o número 15
# invés do não é, poderia colocar para receber o valor que eu quiser
exemplo_el = [valor if valor % 3 == 0 else 'Não é' for valor in lista_div3]
# se não for divisivel por 3, irá receber o não é
print(f'Somente por 3: {exemplo_el}')

# também podemos utilizar and, or, in, not in, not também

exemplo_and = [valor if valor % 3 == 0 and valor % 8 == 0 else 0 for valor in lista_grande]
print(f'Utilizando and : {exemplo_and}')
# saída : Utilizando and : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 96, 0, 0, 0]






