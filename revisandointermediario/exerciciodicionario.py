"""
Sistema de perguntas e respostas com dicionário em Python

"""

perguntas = {
    'Pergunta_1' : {
        'Pergunta' : 'Quanto é 4 * 2?',
        'Alternativas' : {
            'a' : 4,
            'b' : 8,
            'c' : 5,
            'd' : 2,
            'e' : 9,
        },
        'Resposta' : 'b',
    },
    'Pergunta_2' : {
        'Pergunta' : 'Quanto é 4 + 2?',
        'Alternativas' : {
            'a' : 7,
            'b' : 35,
            'c' : 42,
            'd' : 6,
            'e' : 11,
        },
        'Resposta' : 'd',
    },
    'Pergunta_3' : {
        'Pergunta' : 'Quanto é 8 * 2:',
        'Alternativas' : {
            'a' : 46,
            'b' : 10,
            'c' : 20,
            'd' : 18,
            'e' : 16,
        },
        'Resposta' : 'e',
    },
    'Pergunta_4' : {
        'Pergunta': "Quanto é 10 / 2 : ",
        'Alternativas' : {
            'a' : 10,
            'b' : 5,
            'c' : 7,
            'd' : 4,
            'e' : 17,
        },
        'Resposta' : 'b',
    },
    'Pergunta_5' : {
        'Pergunta' : 'Quanto é 100 - 50?',
        'Alternativas' : {
            'a' : 50,
            'b' : 45,
            'c' : 60,
            'd' : 56,
            'e' : 100,
        },
        'Resposta' : 'a',
    }

}
respostas_corretas = 0

for chave_perg, chave_itens in perguntas.items():
    print(f"\n{chave_perg} : {chave_itens['Pergunta']}")
    print('Escolha uma das opções abaixo:')
    for alternativas, opcoes in chave_itens['Alternativas'].items():
        print(f"{alternativas} : {opcoes}")
    escolhida = input('Qual é a sua resposta ? R:').lower()
    if len(escolhida) > 1 or len(escolhida) == 0:
        print('Escreva uma opção válida')
        continue
    if escolhida == chave_itens['Resposta']:
        print('Você acertou a questão!!! Parabéns!')
        respostas_corretas += 1
    else:
        print('Você errou a questão!')

print(f'\nVocê acertou {respostas_corretas} questões!!')
