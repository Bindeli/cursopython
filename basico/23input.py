"""
Entrada de dados
input("recebe uma string")
esse texto será apresentado para o usuário na tela, importante deixar um espaço no final do texto
se não o texto que digitar fica colado ao texto do input, questão de estética
"""
nome = input('Qual o seu nome ? R: ')
# o que o usuário digitar na tela, será atribuido como uma string
print(f'O usuário se chama: {nome} e o tipo da variavel é {type(nome)}')
print() # print vazio para quebrar linha

idade = input("Qual a sua idade ? R: ")

# a função input sempre retorna uma string
# podemos converter uma variavel para um outro tipo, como string para int

ano_nascimento = 2022 - int(idade)
print(f'O {nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}')
print()
#Calculadora de soma
print("Somando com input")
numero_1 = int(input('Digite um número. R: '))
numero_2 = int(input('Digite um outro número. R: '))
# utilizando o int para converter o dado em um número inteiro
print(f'Resultado:', numero_1 + numero_2)
