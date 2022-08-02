"""
Escreva uma função, chamada contaVogais, que conta todas as vogais presentes no texto recebido como parâmetro e
retorna um dicionário contendo a quantidade de cada vogal.
Escreva um programa a fim de testar sua função, e exiba, no fim, os dados do dicionário retornado.
"""

# def contaVogais(texto):
#     dicionario = {}
#     for letra in texto:
#         if letra in 'aeiou':
#             if letra in dicionario:
#                 dicionario[letra] += 1
#             else:
#                 dicionario[letra] = 1
#     return dicionario
#
# texto = input('Digite uma frase ou texto : ')
#
# print(contaVogais(texto))

"""
Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones 
e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções:

incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. 
Ela deve receber como argumentos o nome e os telefones. 

incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, 
você deve perguntar se a pessoa deseja incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir 
o novo nome. 

excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. 
Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda. 

excluirNome – essa função exclui uma pessoa da agenda. 

consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.
"""
lista_telefonica = {}

def incluir_novo_nome(nome, telefones):
    lista_telefonica[nome] = telefones

def incluir_telefone(nome, *telefone):
    if nome not in lista_telefonica:
        print('O nome não se encontra na lista!')
        opcao = input('Deseja adicionar o novo nome? S ou N').lower()
        if opcao == 's':
            incluir_novo_nome(nome, *telefone)
        else:
            print('Escolha uma nova opção!\n')
    else:
        lista_telefonica[nome].append(*telefone)

def excluir_telefone(nome, telefone):
    if nome not in lista_telefonica.keys():
        print('Nome não está na lista telefônica')
    elif len(lista_telefonica[nome]) == 1:
        excluir_nome(nome)
    elif nome in lista_telefonica.keys():
        lista_telefonica[nome].remove(telefone)
    else:
        print('Escolha outra opção.\n')

def excluir_nome(nome):
    if nome in lista_telefonica.keys():
        del lista_telefonica[nome]
    else:
        print('Usuário não encontrado!')

def consultar_telefone(nome):
    print('')
    try:
        print(lista_telefonica[nome])
    except:
        print('Nome não encontrado na lista telefônica. Consulte um suporte!')

print('\nDicionário:')
opcao = ''

while opcao != '0':
    print('\n[1]=Incluir Novo Nome [2]=Incluir Telefone [3]=Excluir Telefone [4]=Excluir nome [5]=Consultar Telefone')
    opcao = input('Escolha sua opção ou digite 0 para sair: ')

    if opcao == '1':
        nome = input('\nDigite o nome a ser incluido : ')
        telefone = [input('Digite o numero de telefone: ')]
        while True:
            if nome in lista_telefonica.keys():
                print('Usuário já registrado.')
                break
            opcao = input('Deseja adicionar mais um telefone? [s] para adicionar R:').lower()
            if opcao == 's':
                telefone.append(input('Digite outro telefone: '))
            else:
                break
        incluir_novo_nome(nome, telefone)

    elif opcao == '2':
        nome_2 = input('\nA quem você deseja adicionar um novo número? R: ')
        telefone_2 = input('Digite o numero de telefone : ')
        if nome_2 in lista_telefonica.keys():
            incluir_telefone(nome_2, telefone_2)
        else:
            print('Nome não encontrado! Deseja adicionar esse nome a lista? [s] se sim R:').lower()
            escolha_2 = input('Digite: ')
            if escolha_2 == 's':
                incluir_novo_nome(nome_2, telefone_2)
            else:
                print('Escolha outra opção!\n')

    elif opcao == '3':
        nome_3 = input('\nDe quem você deseja excluir o nome? R: ')
        telefone_3 = input('Qual número ? R: ')
        excluir_telefone(nome_3, telefone_3)

    elif opcao == '4':
        nome_4 = input('\nQuem você deseja excluir? R:')
        excluir_nome(nome_4)

    elif opcao == '5':
        nome = input('\nDe quem você deseja consultar o número ? R:')
        consultar_telefone(nome)
    else:
        print('Escolha uma opção correta!')




