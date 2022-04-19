# tenho uma lista com chave e valor
lista = [
    ('Chave1','Valor1'),
    ('Chave2','Valor2'),
    ('Chave3','Valor3'),
    ('Chave4','Valor4'),
]
print(f'Exemplo 1 : criando um dicionario com comprehension')
dict_ex1 = { x : y for x,y in lista}
print(dict_ex1)
print('\nExemplo 2 : criando um dicionario com dict')
dict_ex2 = dict(lista)
print(dict_ex2)
# ambos terão o mesmo resultado

print(f'\nExemplo 3 : interagindo com as variaveis do dicionário, no caso multiplicar por 2')
# sendo string, ele vai repetir a string 2x
dict_ex3 = { x : y * 2 for x,y in lista}
print(dict_ex3)

print(f'\nExemplo 4 : Deixando elementos em maiusculo com upper')
dict_ex4 = { x.upper() : y.upper() for x,y in lista}
print(dict_ex4)

print(f'\nExemplo 5 : Deixando elementos em minúsculo com lower')
dict_ex5 = {x.lower() : y.lower() for x,y in lista}
print(dict_ex5)

print(f'\nExemplo 6 : Utilizando enumerate com range: ')
dict_ex6 = { x : y for x,y in enumerate(range(5))}
print(dict_ex6)

print(f'\nCriando um dicionário com chave 1 e valor elevado a dois com range:')
dict_ex7 = {f'chave_{x}' : x**2 for x in range(5)}
print(dict_ex7)






