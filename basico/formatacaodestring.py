"""
Formatação com Python de String
"""
nome = 'Lucas'
idade = 25 #inteiro
altura = 1.68 #float
idademaior = idade > 18
data_atual = 2022
peso = 86
imc = peso/altura ** 2

# print(nome,'tem', idade, 'de idade e seu IMC é:', imc)
# a variavel vai dentro de {}
print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc}')
#caso eu queira arredondar um valor para aparecer somentes duas casas decimais
print(f'IMC: {imc:.2f}')
# ou pode fazer assim, utilizando o format:
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))
#outro método para repetir o valor
print('nome:{0}, idade:{1}, nome:{0}, idade:{1}, altura:{2}'.format(nome,idade,altura))
#outro método
print('{n} tem {i} anos e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))