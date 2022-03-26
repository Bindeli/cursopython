"""
Operadores Lógicos
and
or
not
in
not in
São utilizados para realizar duas ou mais comparações
"""
num1 = 2
num2 = 6
num3 = 42
num4 = 6
print(f'Numéro 1 = {num1} ,Número 2 = {num2}, Número 3 = {num3} e Número 4 = {num4}')

#Para and, as duas expressões devem estar corretas, se não irá ignorar o laço
# Verdadeiro e verdadeiro = verdadeiro
# Verdadeiro e Falso = Falso
print('')
print('Utilizando and, as duas expressões devem ser verdadeiras')
if num1 < num2 and num4 == num2:
    print('Número 1 é menor que número 2 e número 4 é menor ou igual a numero 2')
else:
    print('Número 1 não é menor que o número 2 e número 4 não é igual ou menor que número 2.')
print('')
print('Utilizando OR, uma das expressões deve ser verdadeiras')
#Para or , uma das duas expressões deve ser verdadeiras
# Verdadeira ou Falsa = verdadeiro
# Falsa ou Falsa = Falsa
# Verdadeiro ou Verdadeiro = verdadeiro
if num1 > num3 or num3 > 4:
    print('Uma das expressões utilizando OR é verdadeira')
else:
    print('As duas expressões utilizando OR são falsas')
print('')
# Também temos o operador NOT, conhecido como inversor ou inversão, ele inverte o valor
a = 2
b = 3
print('Preparando o código para NOT')
if b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')
print('Utilizando agora o NOT:')
if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')
print('NOT inverte os valores.')

# Utilizamos o NOT também para variações vazias ou variavel com zero, podemos checar que a varivem tem valor
vazia = ''
zero = 0
print('Utilizando o not para verificar se a variavel está vazia')
if not vazia:
    print('Por favor, preencher o valor de vazia.')
else:
    print('A variavel tem valor.')
print('Verificando se zero tem valor:')
if not zero:
    print('Não há valor no zero, pois zero é considerado um boolean falso')
# se tiver o valor 1, é verdadeiro
print('')
# Utilizando IN, para verificar se um valor está presente em algo
nome = 'Lucas'
#verificar se a letra U está presente em nome
# se o valor estiver na varivel, faça este laço.
if 'u' in nome:
    print('A letra u está presente no seu nome.')
else:
    print('A letra u não está presente no seu nome.')
# Verificar se existe Luc no nome
if 'Luc' in nome:
    print('Luc pertence ao nome')
else:
    print('Luc não pertence ao nome')
# Verificando se existe Let no nome
if 'Let' in nome:
    print('Let pertence ao nome')
else:
    print('Let não pertence ao nome')

# Criando um código para verificar se a letra pertence ao nome inserido
print('')
usuario = input('Digite o seu nome para verificar se possui letra A: ')
if 'a' in usuario:
    print(f'Seu nome {usuario} possui a letra a.')
else:
    print(f'Seu nome {usuario} não possui letra a')
print('')
print('Exemplo para verificar se usuário e a senha inseridas são iguais aos que estão cadastrados')

usuario_inserido = input('Nome do usuário: ')
senha_inserida = input('Senha do usuário: ')

usuario_cadastrado = 'lucas'
senha_cadastrada = '22041997'

if usuario_cadastrado == usuario_inserido and senha_cadastrada == senha_inserida:
    print('Você está logado no sistema.')
else:
    print('Usuário ou Senha estão incorretos.')

