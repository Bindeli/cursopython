"""
71 - Comportamento de Geradores e Iteradores

Iterável : listas, tuples, str -> sequências

Utilizando next, estou consumindo os valores dele, quando eu consumir, ele não estará mais disponível


Exemplo abaixo :
"""
nome = 'Lucas_Bindeli'
"""
Se eu der next, e acabar os dados, irá ocorrer um erro
Para que isso não aconteça, utilizamos try e except, quando acabar, se der erro, ele irá rodar o except
"""
iterador = iter(nome)

print(next(iterador)) #1
print(next(iterador)) #2
print(next(iterador)) #3
print(next(iterador)) #4
print(next(iterador)) #5
print(next(iterador)) #6
print(next(iterador)) #7
print(next(iterador)) #8
print(next(iterador)) #9
print(next(iterador)) #10
print(next(iterador)) #11
print(next(iterador)) #12
print(next(iterador)) #13
# print(next(iterador)) Se eu rodar mais um next, irá ocorrer o erro StopIteration
# pois não possui mais elementos
print(f'Fim do iterador n° 1.')
# agora utilizando o try e except
iterador_2 = iter(nome)
print(f'\nUtilizando o try e except no iterador 2:')
try:
    print(next(iterador_2))  # 1 - L
    print(next(iterador_2))  # 2 - u
    print(next(iterador_2))  # 3 - c
    print(next(iterador_2))  # 4 - a
    print(next(iterador_2))  # 5 - s
    print(next(iterador_2))  # 6 - espaço
    print(next(iterador_2))  # 7 - B
    print(next(iterador_2))  # 8 - i
    print(next(iterador_2))  # 9 - n
    print(next(iterador_2))  # 10 - d
    print(next(iterador_2))  # 11 - e
    print(next(iterador_2))  # 12 - L
    print(next(iterador_2))  # 13 - i ,  aqui é onde termina
    print(next(iterador_2))  # 14, seria onde iria dar o erro
    print(next(iterador_2))  # 15, seria onde iria dar o erro
except:
    print(f'Fim')


# Como eu utilizei todos os caracteres da string, não há mais nada para iterar
# se eu passar um for agora, não irá aparecer nada


print(f'Utilizando o for para puxar elementos do iterador 2 :')
for elemento in iterador_2:
    print(elemento)

print(f'Não irá aparecer nada, pois todos os elementos foram utilizados')
print(f'\nAgora chamando apenas alguns elementos com o next')
nome_2 = 'Lucas'
nome_iterador = iter(nome_2)

print(next(nome_iterador))
print(next(nome_iterador))
# Chamei apenas 2 letras
print(f'Agora chamando com o for todo a variavel!')
print(f'Porém irá aparecer apenas alguns não lidos pelo next')

for letra in nome_iterador:
    print(letra)
print(f'Utilizando o for novamente para verificar se aparece mais:')

for letra_2 in nome_iterador:
    print(letra_2)

print(f'Não irá aparecer mais nada, pois já foi iterado')
print('Os dois irão consumir os valores')
print('\nAgora trabalhando com Geradores : ')
iterador_3 = iter(nome)
gerador = (letra for letra in iterador_3)
print('Utilizando next:')
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
# irá aparecer Lucas
print(f'\nAgora utilizando for no restante : ')
for letras in gerador:
    print(letras)
# irá terminar de consumir o restante do gerador
print(f'Um outro for, porém não irá aparecer nada, pois está vazio também:')
for letras in gerador:
    print(letras)
