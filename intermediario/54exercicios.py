"""
1 - Crie uma função que exite uma saudação com os parâmetros saudaçãoo e nome.
"""
print('Exercício Saudações:')
def saudacao(saudacao, var1):
    print(f'{saudacao}! {var1}')

nome = input('Digite seu nome: ')
saudacao('Olá',nome)
saudacao('Oi','Nil')
saudacao('Olá','André')

print('')

"""
2 - Crie uma função que recebe 3 números com parâmetros e exiba a soma entre eles
"""
print('Exercicio recebe 3 números e somar eles:')
def soma(var1,var2,var3):
    return print(var1+var2+var3)

soma(10,10,10)
soma(30,100,20)
print('')

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (EX: 10%) e Retorne (return)
o valor o primeiro número somado do aumento do percentual do mesmo. Exibir o valor!!
Exemplo : 100 + 10% = 110
"""
print('Exercício soma e percentual:')
def porcent(var1, percentual):
    return print(f'Soma de {var1} e seu {percentual}% é {var1 + ((var1*percentual)/100)}')

porcent(100,10)
porcent(50,10)
porcent(100,50)

print('')

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divisível por
5, retorn buzz. Se o parâmetro da função divisível por 5 e por 3, retorne FizzBuzz, caso contrário, nem por 5 ou 3, 
retorne o número enviado.
"""
print('Exercício FizzBuzz:')
def fizzbuzz (var1):
    if var1 % 3 == 0 and not var1 % 5 == 0:
        return print(f'Fizz ! Valor: {var1}')
    elif var1 % 5 == 0 and not var1 % 3 == 0:
        return print(f'Buzz! Valor: {var1}')
    elif var1 % 5 == 0 and var1 % 3 == 0:
        return print(f'FizzBuzz!! Valor: {var1}')
    return print(f'Valor: {var1}')

"""
Também podemos fazer deste jeito, fica um código muito mais limpo!
Indo por eliminatória!

def fizzbuzz (var1):
    if var1 % 3 == 0 and var1 % 5 == 0:
        return f'FizzBuzz!! Valor: {var1}'
    if var1 % 5 == 0:
        return f'Buzz, {var1} é divisível por 5'
    if var1 % 3 == 0:
        return f'Fizz, {var1} é divisível por 3'
    return var1

"""

fizzbuzz(9)
fizzbuzz(25)
fizzbuzz(30)
fizzbuzz(22)




