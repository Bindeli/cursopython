"""
Criando um Sistema de perguntas e respostas com Dicionário
"""

perguntas = {
    'Pergunta 1' : {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : {
            'a' : 4,
            'b' : 5,
            'c' : 8,
            'd' : 10,
            'e' : 9,
        },
        'Resposta' : 'a'
    },
    'Pergunta 2' : {
        'Pergunta' : 'Quanto é 4*4?',
        'Opções' : {
            'a' : 8,
            'b' : 3,
            'c' : 4,
            'd' : 100,
            'e' : 16,
        },
        'Resposta' : 'e'
    },
}

for chave_princ, chave_filha in perguntas.items():
    print(f"[{chave_princ}] : {chave_filha['Pergunta']}")

    print(f'Escolha uma das opções abaixo: ')
    print('')
    for opcoes, escolhas in chave_filha['Opções'].items():
        print(f"[{opcoes}] : {escolhas}")
    escolha_usuario = input('Digite sua escolha : ').lower()
    if escolha_usuario == chave_filha['Resposta']:
        print(f"Parabéns! Você acertou a resposta era realmente : {escolha_usuario.upper()} !!")
    else:
        print(f'Parabéns! Você errou, a resposta era a opção : {chave_filha["Resposta"].upper()}')
    print('')













