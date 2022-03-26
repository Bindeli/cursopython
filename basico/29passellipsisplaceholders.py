"""
PLACEHOLDERS
PASS e ELLIPSIS
"""
# Quando eu quero deixar um espaço para posteriormente escrever algum código,
# para não dar erro e impedir toda a estrutura do código, posso utilizar pass e ellipsis ...

# deixando em False para mostrar o código else
valor = False
valor2 = False

if valor:
    #geralmente possui um comentário explicando o que irá ser feito aqui
    pass
else:
    print('Irá aparecer este print, foi utilizado o pass.')

if valor2:
    ...
    #o ellipsis são 3 pontos que também possui o mesmo objetivo do pass
    # de segurar um espaço para escrever um código posteriormente
else:
    print('print que irá aparecer, foi utilizado ... "ellipsis')

