# PARA GERAR UM NÚMERO ALEATÓRIO PARA SERVIR DE EXEMPLO PARA CPF


from random import  randint
# são 9 digitos
numero = str(randint(100000000, 999999999))

novo_cpf = numero   # 9 número aleatórios
multi = 10          # Contador reverso 1
multi2 = 11         # Contador reverso 1
total1 = 0
total2 = 0

#Loop do CPF:
for contador in range(9):
    soma1 = int(novo_cpf[contador]) * multi  # valor recebe resultado entre o dígito e o contador
    multi -= 1
    total1 = soma1 + total1

caracter = 11 - (total1 % 11)  # conta que irá criar o digito final do laço for
# print(caracter)
if caracter > 9:
    caracter = 0

novo_cpf = novo_cpf + str(caracter)  # concatenar o digito gerado no novo cpf como string

for contador in range(10):
    soma2 = int(novo_cpf[contador]) * multi2  # valor recebe resultado entre o dígito e o contador
    multi2 -= 1
    total2 = soma2 + total2
caracter = 11 - (total2 % 11)  # conta que irá criar o digito final do laço for
# print(caracter)
if caracter > 9:
    caracter = 0

novo_cpf = novo_cpf + str(caracter)  # concatenar o digito gerado no novo cpf como string

print(novo_cpf)

# depois só pesquisar e copiar e colar em um validador de cpf para verificar se é válido