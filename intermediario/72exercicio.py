# carrinho = []
#
# o carrinho adiciona o produto, se o produto tiver variação, também adiciona a variação
#
# carrinho.append(('Produto_1', 30))
# carrinho.append(('Produto_2', 20))
# carrinho.append(('Produto_3', 60))
#
# quando terminar e fechar o carrinho, verá algo semelhante a isto aqui
#
# print(carrinho)

"""
O desafio é somar o preço total da 'compra' 
Utilizando list compreehsion

total = 0
preços = []
Exemplo de como pode ser feito a lógica
for produto in carrinho:
    preços.append(produto[1]) ,  seria uma lista só com os preços
    total += produto[1]
print(total)

pegando a lista de preço, no final seria só um print com a soma do total
print(sum(total))
mas em Python temos o compreehsion para realizar em uma linha de código

"""
print(f" {'*' * 30 } Exercicio Proposto [Aula 72] {'*' * 30 }")

carrinho = []
soma = 0

carrinho.append(('Produto_1', 71))
carrinho.append(('Produto_2', 22))
carrinho.append(('Produto_3', 37))
carrinho.append(('Produto_4', 53))
carrinho.append(('Produto_5', 14))

print(f'\nCarrinho : {carrinho}')

total = [ float(valor[1]) for valor in carrinho ]
# total = sum([float(y) for x,y in carrinho])

print(f'\nOs preços adicionados foram : {total}')
print(f'O total da compra deu : {sum(total)}')
print(f'Soma: {soma}')

print(f'\nOutro método, Obrigado André')
total2 = 0
[total2 := total2 + valor[1] for valor in carrinho]
print(f'Total 2 : {total2}')