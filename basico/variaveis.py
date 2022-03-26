"""
Variaveis
iniciar com letras, pode conter numeros, separar com _, letras minúsculas
se começar com números, dá erro
"""
# estou atribuindo este valor a uma variavel, e toda vez que eu chamar a variavel, irá mostrar seu valor
nome = 'Lucas'
print(nome, type(nome))
idade = 25 #inteiro
altura = 1.68 #float
idademaior = idade > 18 #bool(essa variavel está sustentando o resultado desta expressao idade maior que 18)
data_atual = 2022
peso = 86
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Se é de maior de idade:', idademaior)
print('Multiplicando idade com altura:', idade*altura)
imc = peso/altura ** 2
print(nome,'tem', idade, 'de idade e seu IMC é:', imc)