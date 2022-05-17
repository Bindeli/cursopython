# Caso eu queira importar algo que está dentro do pacote vendas
# Posso fazer de várias maneiras diferentes.

# from vendas.calc_preco88 import aumento,reducao
# import vendas.calc_preco88

from vendas.calc_preco88 import aumento,reducao

from vendas.formata import preco

valor = 49.90
print(f'Valor do produto : {valor}')
preco_com_aumento = aumento(valor, 15, formata=True)
print(f'Com aumento : {preco_com_aumento}')

preco_com_reducao = reducao(valor, 20, formata=True)
print(f'Com redução : {preco_com_reducao}')

"""
Supondo que em um momento você queira criar formatação dos textos que aparecem 

Por exemplo : Resultado = 57.897 ou 49.9 ou 39.922

Então dentro do módulo de vendas, vou criar um sub pacote chamado formata para formatar os preços

"""

print(f'\nImportando agora a função real do modulo preco e utilizando-a')
print(preco.real(50))

"""
Também teria como nomear uma função de um módulo

import vendas.formata.preco as formata

Caso tenha um nome parecido com alguma variável de um elemento de minha main.py
"""