"""
Condições IF, ELIF e ELSE

"""
# SE isso aqui for verdadeiro, execute o bloco abaixo
# em python,a hierarquia dos códigos é feito de espaço, para dar um espaço, aperte TAB
print()
if True:
    print("Verdadeiro.")
    num_1 = 2
    num_2 = 4
    print(num_2 + num_1)

#quando ocorrer da expressão ser falsa, ele irá ignorar a condição if
print("Testando IF com informação falsa, não irá aparecer na tela")
if False:
    print("A informação falsa não deve aparecer")
print("Não apareceu, pois é uma expressão falsa.")

if 2 > 4:
    print("Também não irá aparecer")

# Caso a expressão for falsa, podemos utilizar uma outra condição que é o ELSE
# Caso o código não execute o if, irá exercutar o que estiver no ELSE.
if False:
    print("Não irá aparecer, somente a informação do ELSE")
else:
    print("Leitura do código que está dentro da condição ELSE")
# o ELSE só é utilizando com uma condição IF.

# Podemos utilizar ELIF para criar uma outra expressão além de IF e Else,

if False:
    print("Expressão Falsa")
elif True:
    print("Rodando a informação que está dentro do ELIF")
elif False:
    print("Outra expressão")
else:
    print("Não chegará a esta condição pois elif está com a expressão verdadeira")
# O else só será executado quando nenhuma das expressões forem verdadeiras
# pode tirar o else, não é necessário, caso tudo for falso, nada será executado
print()
#exemplo
print("Exemplo de condição.")
if False:
    print("Expressão Falsa.")
elif False:
    print("Outra Expressão Falsa.")
elif True:
    print("Agora é verdadeiro")
    nome = input("Qual o seu nome? ")
    print(f'Seu nome é {nome}')
else:
    print("Expressão ignorada.")

