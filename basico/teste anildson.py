"""
Características (regras) de uma variável:

* Deve iniciar com uma letra;
* Pode conter números (mas obrigatoriamente deve iniciar com letra);
* Utiliza o sinal de igual como operador de atribuição, ou seja,: nome= 'Anildson' O sinal de igual, atribui a str
   'Anildson' à variável 'nome'
* Usa o sinal de 'underline' para fazer a separação dos caracteres. Ex: 'dataatual =', pode ser separado em 'data_atual =',
   utilizando o "_"
* Utilizar sempre letras minúsculas para criar uma variável.
"""
print('==============')
nome = 'Anildson'
idade = 37  # int
altura = 1.75  # float
peso = 90.0  # float
e_maior = idade > 18  # bool
data_atual = 2019  # int
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade, 'Anos')
print('Altura:', altura, 'M')
print('Peso:', peso, 'Kg')
print('É maior de idade?', e_maior)
print('==============')

# print(nome, 'tem', idade, 'anos de idade, e o  seu imc é de:', int(imc))
print(f'{nome} tem {idade} anos de idade, e seu imc é de {imc:.2f}')
print('==============')

# Crie um código onde exiba uma pergunta sobre a idade do usuário.
# Ao fornecer os dados, o código irá classificar o usuário como 'criança', 'adolescente' ou 'adulto'.

nome = input('Qual o seu nome, seu infeliz!!! ')
idade = int(input('...e qual é a sua idade, seu desajustado! '))
criança = 11
adoles = 12
adulto = 18

if idade <= 11:
    print(f'{nome}, você é uma criança.')
elif idade < 18 and idade > 11:
    print(f'{nome}, você é um adolescente.')
else:
    print(f'{nome}, você é um adulto.')