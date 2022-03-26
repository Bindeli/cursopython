"""
63 - Sistema de perguntas e respostas com dicionário em Python
"""
# variavel onde terá todo o sistema de perguntas e respostas
perguntas = {
    'Pergunta 1' : {
        'Pergunta' : 'Quanto é 2 + 2?',
        # como eu quero um sistema de multipla escolha, vou poder adicionar quantas respostas eu quiser
        # terá apenas uma verdadeira
        'Resposta' : {
            'a' : 4,
            'b' : 3,
            'c' : 9,
            'd' : 2,
            'e' : 22,
        },
        'Resposta_certa' : 'a',
    },
    'Pergunta 2' : {
        'Pergunta' : 'Quanto é 4 * 2?',
        'Resposta' : {
            'a' : 9,
            'b' : 3,
            'c' : 8,
            'd' : 42,
            'e' : 22,
        },
        'Resposta_certa' : 'c',
    },
    'Pergunta 3' : {
        'Pergunta' : 'Quanto é 30 / 3?',
        'Resposta' : {
            'a' : 9,
            'b' : 30,
            'c' : 3,
            'd' : 11,
            'e' : 10,
        },
        'Resposta_certa' : 'e',
    },
    'Pergunta 4' : {
        'Pergunta' : 'Quanto é 40 - 16?',
        'Resposta' : {
            'a' : 21,
            'b' : 26,
            'c' : 4,
            'd' : 24,
            'e' : 36,
        },
        'Resposta_certa' : 'd',
    },
    'Pergunta 5' : {
            'Pergunta' : 'Quanto é 20 + 60?',
            'Resposta' : {
                'a' : 10,
                'b' : 80,
                'c' : 60,
                'd' : 65,
                'e' : 260,
            },
            'Resposta_certa' : 'b',
        },

}
# variavel para contar quantas respostas o usuário acertou
respostas_certas = 0

print()
# iterando com a primeira chave, pergunta 1,2,3,4,5
for chave_perg, chave_resp in perguntas.items():
    print(f"{chave_perg}: {chave_resp['Pergunta']}")
    # agora vou acessar as respostas:
    # a primeira é para as chaves de opções
    # a segunda é para as respostas
    # na chave_resp tem os valores : Pergunta, Resposta, Resposta_certa

    print('Escolha as opções abaixo:')
    for resposta_mult, resposta_op in chave_resp['Resposta'].items():
        print(f'[{resposta_mult}]: {resposta_op}')
    resposta_usuario = input('Sua resposta: ').lower()
    if resposta_usuario == chave_resp['Resposta_certa']:
        print('Resultado : Acertou!')
        respostas_certas += 1
    else:
        print('Resultado : Errou')


    print('')

print(f'Respostas certas: {respostas_certas}')

# Criando a porcentagem de acertos:
qtd_perguntas = len(perguntas) # vai retornar a quantidade de perguntas, é considerado o valor da chave
porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(f'Porcentagem de Acertos : {porcentagem_acerto}%')


















