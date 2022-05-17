"""
Criado para formatar os valores dos precos

Aqui dentro vou criar uma função que formata para real (moeda brasileira)
"""

def real(valor):
    return f'R$ {valor:.2f}'.replace('.',',')

# E quero utilizar essa função dentro do módulo calcula preço e também do módulo main

