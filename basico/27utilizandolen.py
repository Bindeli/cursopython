"""
len - utilizado para contar os caracteres

"""
# inserir usuario para verificar a quantidade de caracteres
print('Digite um usuário com 6 caracteres ou mais:')
usuario = input('Digite seu usuario: ')
qtd_caracteres = len(usuario)

print(f'Usuário: {usuario}, Quantidade de caracteres: {qtd_caracteres}, tipo do len é {type(qtd_caracteres)}')
# len retorna um valor inteiro
print('Verificar se o usuário possui 6 ou mais caracteres:')
if qtd_caracteres < 6:
    print('Usuário deve ter 6 ou mais caracteres.')
else:
    print('Usuário cadastrado no sistema.')
print('')
# utilizando o len para somar a quantidade de caracteres de 2 strings
print('Digite algo abaixo.')
string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi de {len(string1) + len(string2)} caracteres')

