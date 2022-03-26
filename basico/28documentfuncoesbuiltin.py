"""
Algumas funções built-in
isdigit
isnumeric
isdecimal
elas irão retornar true se todos os caracteres da string forem decimais
Quando pedirmos para o usuário digitar números, caso ele digite uma letra, irá fazer a leitura se
o dado que ele inseriu é número ou letra através destas funções.
Eles irão checar se a string podem ser convertidas em inteiros
"""
numero1 = (input('Digite um número: '))
numero2 = (input('Digite um outro número: '))

#irão retornar um boolean se pode ou não
print(numero1.isnumeric())
print(numero2.isnumeric())
#caso seja um número negativo, ele irá retornar false
# utilizando número negativos e letras, irá direto para o else
if numero1.isdigit() and numero2.isdigit():
    numero1 = int(numero1)
    numero2 = int(numero2)
    print(f'A soma do número 1 e número 2 é: ', numero1 + numero2)
else:
    print('Não pude converter os números para realizar contas.')
