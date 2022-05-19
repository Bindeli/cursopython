"""
AULA 89 - Criando, lendo, escrevendo e apagando arquivos

https://docs.python.org/3/library/functions.html#open

'r' = open for reading (default)
'w' = open for writing, truncating the file first
'x' = open for exclusive creation, failing if the file already exists
'a' = open for writing, appending to the end of file if it exists
'b' = binary mode
't' = text mode (default)
'+' = open for updating (reading and writing)


"""

# falei para a função open que eu quero o nome do meu arquivo
# e qual o modo que eu quero trabalhar com ele
# coloquei um w para falar que quero para escrita e também o + para leitura e escrita
# Quando não tiver, eu crio, e se tiver, eu vou abrir o arquivo
primeiro_file = open('abc.txt', 'w+')

#----------------------------------------------------------------------------------------------------------------
"""
Com o arquivo aberto, posso escrever coisas nesse meu arquivo
E para isso, eu utilizo a função write
"""

primeiro_file.write('Linha 1\n')
primeiro_file.write('Linha 2\n')
primeiro_file.write('Linha 3\n')
#----------------------------------------------------------------------------------------------------------------
"""
Eu quero ler coisas desse arquivo, uma maneira para realizar isso, seria :
Ele vai ler o arquivo inteiro e vai me retornar como uma string
"""

# utilizo a função seek
# os parâmetros são offset que é a posição, e o renzi que é a relatividade que você está procurando.
# geralmente é com 0 mesmo pois queremos buscar a posição absoluta no arquivo
# 0 inicio
# 1 é relativo ao momento que o cursor está
# 2 é relativo ao final do documento
primeiro_file.seek(0, 0)

print('Lendo linhas: ')
print(primeiro_file.read())

print('#'*20)
#----------------------------------------------------------------------------------------------------------------
primeiro_file.seek(0, 0) # colocando o cursor novamente no inicio do arquivo

"""
Outro modo é ler linha por ler no arquivo, readline é para ler uma linha somente
"""

# Lembrando que coloquei uma quebra de linha \n no final da linha e irá ler isso
# para eu solucionar isso, coloco um end='' no final do print

print(primeiro_file.readline(), end='') # printamos para ler a primeira linha do arquivo
# neste momento o curso está no final da linha
# R : Linha 1|
# e se eu pedir para ler a readline, o curso vai ficar Linha 2|
print(primeiro_file.readline(), end='') # esse end no final vai impedir a quebra de linha
print(primeiro_file.readline(), end='')
print('#'*20)
#----------------------------------------------------------------------------------------------------------------
# Uma outra coisa que podemos fazer é jogar linha por linha em uma única lista

primeiro_file.seek(0,0)

# para ler várias linhas, utilizamos readlines
print(primeiro_file.readlines())

primeiro_file.seek(0,0)
print(f'\nAgora utilizando um for:')
# E também posso chamar o método for
for linha in primeiro_file.readlines():
    print(linha, end='')

print('#'*50)
#----------------------------------------------------------------------------------------------------------------
primeiro_file.seek(0,0)
"""
Além de utilizar o readlines, posso mandar o arquivo direto
"""
print(f'Agora sem utilizar o readlines:')
for linha in primeiro_file:
    print(linha, end='')

print('#'*50)
#----------------------------------------------------------------------------------------------------------------
"""
Muitas pessoas utilizam o bloco try para abrir arquivos

E Utilizam o finally para fechar o arquivo
"""

try:
    file = open('def.txt', 'w+')
    file.write('Linha do novo arquivo 1\n')
    file.write('Linha do novo arquivo 2\n')
    file.write('Linha do novo arquivo 3\n')
    file.seek(0,0)
    print(file.read())
finally: # esse bloco sempre é executado
    file.close()
    print(f'Arquivo fechado')
print('#'*50)
# não é uma maneira muito ideal do python para se trabalhar
#----------------------------------------------------------------------------------------------------------------
"""
Então já que não é uma maneira muito ideal, vamos utilizar o gerenciador de contexto
"""
print('\nAgora utilizando um gerenciado de contexto para abrir o arquivo :')

# mando a função open e coloco como o nome que eu quero trabalhar na função
with open('abc.txt', 'w+') as filealterado:
    # agora posso fazer o que eu quero com o arquivo
    filealterado.write('Nova linha 1\n')
    filealterado.write('Nova linha 2\n')
    filealterado.write('Nova linha 3\n')
    filealterado.seek(0,0)
    print(filealterado.read())
print('#'*50)
"""
A diferença desse método para o método que utiliza o try e o except e finally , foi que eu não preciso fechar 
o arquivo, o gerenciado, vai abrir o arquivo e assim que ele acaba de executar, ele vai fechar o arquivo
"""
#----------------------------------------------------------------------------------------------------------------
"""
Outro módulo é o r
ao ivés de escrever linhas nesse arquivo, eu vou simplesmente ler o que têm no arquivo
"""
print('\nUtilizando o módulo r para ler o arquivo')
with open('def.txt','r') as lendoarquivo:
    print(lendoarquivo.read())
print('#'*50)
#----------------------------------------------------------------------------------------------------------------
"""
E o método do a+ ele o append mode, ele adiciona coisas no arquivos sem apagar o conteúdo dele
o 'a' , já coloca o cursos no final do arquivo
"""
print('\nUtilizando o método a+ para adicionar conteúdo sem apagar o conteúdo existente:')
with open('abc.txt','a+') as fileappend:
    fileappend.write('Outra linha adicionada depois\n')
    # Cada vez que eu executar, ele vai adicionar a frase novamente
    fileappend.seek(0,0)
    print(fileappend.read())
print('#'*50)
#----------------------------------------------------------------------------------------------------------------
""""
E quando eu termino de mexer com o arquivo, eu devo fechar o arquivo para não gerar problema
"""
primeiro_file.close()
#----------------------------------------------------------------------------------------------------------------

"""
Caso eu queira remover esse arquivo, primeiro eu importo o 'os'

import os
os.remove('abc.txt')

E eu deletaria o arquivo
"""
#----------------------------------------------------------------------------------------------------------------
import json

d1 = {
    'Pessoa_1' : {
        'nome' : 'Lucas',
        'idade' : 25
    },
    'Pessoa_2' : {
        'nome' : 'Anildson',
        'idade': 37
    },
}

# aqui eu tenho um dicionário normal
print(d1)
# caso eu queira converter em json, eu iria fazer deste modo
print(f'Agora a versão em JSON: ')
d1_json = json.dumps(d1, indent=True)
print(d1_json)
# Não parece que está muito diferente, mas já foi convertido para json
# Agora vou jogar o dicionário dentro de um arquivo
print(f'Agora vou jogar para um file chamado abc.json:')
with open('abc.json', 'w+') as filejson:
    filejson.write(d1_json)
    filejson.seek(0,0)
    print(filejson.read())

# filejson.close()

# Agora vou criar um arquivo .py chamado ler_json para importar o abc.json

