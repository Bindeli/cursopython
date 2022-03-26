"""
+ : soma
- : subtração
* : multiplicação
/ : divisão
// : divisão inteira
** : um número elevado a outro
% : retorna o resto da divisao entre um numero e outro
() : altera a precedencia das contas
"""
print('Multiplicação *:',10 * 10) # vai ser 100, multiplicação
print('Adicao +:', 10 + 10) # 20, adição
print('Subtração -: ',10 - 5) #5, subtração
print('Divisão / :', 10/2) #5, divisão
print('Multiplicando String:', 3 * 'Lucas')
print("Adicionando String com String: '10+A': ", '10'+'A')
# vai retornar um valor inteiro por ter dois inteiros, caso tivesse float, retornaria com uma casa
print('Divisão inteira : ',10 // 3)
# caso tivesse feito com a divisão normal, teria várias casas
print('Divisão normal: ', 10/3)
#potencialização
print('Potência **: ', 2**2)
# porcetagem retorna o resto da divisão
print('Porcentagem: ', 10 % 3)
# () são utilizados para alterar as precendias dos operadores, o que está em parenteses será prioridade
print('Não utilizando Parenteses "5+2*10" : ', 5+2*10) # vai dar 25
print('Utilizando Parenteses: "(5+2)*10" :', (5+2)*10) # vai dar 70
