"""
Operador ternário em Python

"""
# se o usuário estiver logado, a variavel será true, se não estiver logado, será false
logado_user = True

# caso não tenha algo, é por que está conferindo se está true, a mesma coisa que if logado_user == True:
if logado_user:
    mensagem = 'Olá. Usuário logado'
else:
    mensagem = 'Usuário não está logado'

print(mensagem)
print('')
# posso simplificar ainda mais utilizando operador ternário

User_logado = True
# eu coloco depois sem os dois pontos, se tiver mais de uma condição, posso usar o ()
mensagem_2 = 'Usuário logado.' if logado_user else 'Usuário precisa logar.'

print(f'Com operador ternário : {mensagem_2}')

# temos também outros atalhos
# supondo que temos um sistema que seja para maiores de 18 anos
print('')

idade = input('Qual a sua idade ? R: ')

# if idade >= 18:
#     print('Pode Acessar!')
# else:
#     print('Não pode acessar!')
# posso simplicar criando a variavel e colocando a condição

if not idade.isnumeric():
    print('Você precisa digitar apenas números!')
else:
    idade = int(idade) # transforamndo o valor em inteiro
    e_de_maior = (idade >= 18) # verificar se a comparação é True ou False
    mensagem_3 = 'Pode acessar!' if e_de_maior else 'Não pode acessar'
    print(mensagem_3)










