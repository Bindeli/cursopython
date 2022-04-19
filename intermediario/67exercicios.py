"""
Utilizando list comprehension

Separar todos os grupos de 0 a 9

Deste modo:
lista = ['0123456789','0123456789','0123456789','0123456789','0123456789','0123456789','0123456789']

feito isso, deverá retornar

retorno final = 0123456789.0123456789.0123456789.0123456789.0123456789.0123456789
"""

string = '012345678901234567890123456789012345678901234567890123456789'
print(f'String inicial : {string}')

# string_lista = [ letra for letra in string ]
# print(string_lista)
# print(string[0:10])
n = 10
string_list = [string[i:i + n] for i in range(0, len(string), n) ]
print(string_list)

string_final = '.'.join(string_list)

print(f'{string_final}')




