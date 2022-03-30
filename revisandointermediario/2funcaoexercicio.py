"""
Podemos criar uma função que retorne outra funcao
"""

print('Função que chame outra função:')

def fun(var):
    print(var)

def dumb():
    return fun

variavel_alt = dumb()('Valor para a função que foi chamada por outra!\n')

"""
1 - Crie uma função que exige uma saudação com os parâmetros saudação e nome.
"""

def saudacao(msg, nome):
    print(f'{msg}! {nome}')

saudacao('Boas vindas!','Lucas')

"""
2 - Crie uma função que recebe 3 números com parâmetros e exiba a soma entre eles
"""

def soma_1(var1,var2,var3):
    return var1 + var2 + var3
print('Exercicio 3: ', end='')
print(soma_1(3,6,9))


"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (EX: 10%) e Retorne (return)
o valor o primeiro número somado do aumento do percentual do mesmo. Exibir o valor!!
Exemplo : 100 + 10% = 110
"""

def porcent(var1, var2):
    return print(f'Soma de {var1} e seu {var2}% é de {var1 + ((var1*var2)/100)}')

porcent(100,25)
porcent(200,50)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por
5, retorn buzz. Se o parâmetro da função divisível por 5 e por 3, retorne FizzBuzz, caso contrário, nem por 5 ou 3, 
retorne o número enviado.
"""

def fizzbuzz(var):
    if var % 3 == 0 and var % 5 == 0:
        return print(f'FizzBuzz! {var}')
    elif var % 5 == 0:
        return print(f'Buzz! {var}')
    elif var % 3 == 0:
        return print(f'Fizz! {var}')
    else:
        return print(f'{var}, não é divisível por 5 e nem por 3')

fizzbuzz(30)
fizzbuzz(20)
fizzbuzz(9)
fizzbuzz(7)

