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

#print(string[0:10])
sequencia = 10

string_lista = [ string[i : i+ sequencia] for i in range(0 , len(string), sequencia) ]

print(string_lista)
string_final = '.'.join(string_lista)
print(string_final)