"""
AULA 83 - TRY e EXCEPT

Tratar excessões!

Excessões são erros que ocorrem em seu programa.

Para tratar de excessões, eu envolvo meu bloco é um try (tente isso)
Similar ao if e else
Caso ocorra algum erro do código no Try.
Irá ativar o Except

Tudo que eu executar dentro do bloco try, ele irá tentar executar, se ocorrer algum erro
Ele vai cair no Except e irá rodar o que estiver no except

try:
    print(a)
except:
    print('erro')

Como a variável a não foi definida, irá ocorrer um erro e executará o except, aparecendo o print 'erro' na tela

Digamos que isso não é uma boa prática de programação.

"""
#_________________________________________________________________________________________________________________
# podemos falar também o tipo de exceção que eu quero tratar, posso jogar isso em uma variável

try:
    print(naoexiste)
except NameError as erro:
    print('Erro:', erro)

# e meu código não vai parar por causa deste erro
print(f'Continuando o código....\n')

#_________________________________________________________________________________________________________________

# Também podemos utilizar um outro except, caso possa ocorrer mais um erro de exceção aqui neste local
# utilizando outra exceção com ""expection""

# Exemplo, criando uma lista fazia e tentar imprimir um valor dela
print(f'Utilizando dois except, e Exception que vai pegar qualquer erro que não foi especificado:')
try:
    a = []
    print(a[1])
except NameError as erro2: # criei esse except só para mostrar que podemos trabalhar com mais de um except
    print(f'Erro do tipo NameError : {erro2}')
except Exception as erro2: # ela vai pegar qualquer erro que tiver no bloco try
    # eu não estou expecificando o erro que eu quero
    print(f'Ocorre um outro tipo de erro : {erro2}')

#_________________________________________________________________________________________________________________

# Posso utilizar mais de 2 except
print('')
print(f'Agora utilizando 3 except, incluindo um novo except, o IndexErro')
try:
    a = []
    print(a[2]) # forçando erro de indice
except NameError as erro3:
    print(f'Name error : {erro3}')
except IndexError as erro3:
    print(f'Erro de index: {erro3}')
except Exception as erro3:
    print(f'Ocorreu um erro não especificado : {erro3}')

#_________________________________________________________________________________________________________________

# Agora vamos exemplificar quando queremos tratar duas exceções na mesma exceção

print(f'\nTratando duas exceções em uma mesma exceções:')
try:
    a = {}
    print(a[2]) # forçando erro de indice
except NameError as erro3:
    print(f'Name error : {erro3}')
except (IndexError, KeyError) as erro3:
    print(f'Erro de index ou chave: {erro3}')
except Exception as erro3:
    print(f'Ocorreu um erro não especificado : {erro3}')
print('')

#_________________________________________________________________________________________________________________

# Uma outra coisa que podemos colocar é um else
"""
O else só será executando quando o código não passar por nenhuma exceção
porém quando ocorrer um erro, o bloco else não será executado!!!!!!!!!!!!!!!!!!!!!!
"""
print(f'Utilizando o else com try e except:')
try:
    a = []
    print(a)
except NameError as erro3:
    print(f'Name error : {erro3}')
except:
    print('Ocorreu um erro')
else:
    print('Seu código foi executado sem erros!')

#_________________________________________________________________________________________________________________

# finally sempre será executado, não importa se ocorreu ou não um erro
"""
Pode ser muito util para fechar algum arquivo que tenha sido aberto dentro de qualquer cláusula!!!!!!!!!
ou conexão com bases de dados
"""

print(f'\nAgora utilizando o finally, que será executado sempre:')

try:
    a = []
    print(f'Estou printando a lista vazia no try : {a}')
except:
    print(f'Deu um erro!')
else:
    print(f'Passando pelo else.')
finally:
    print(f'Passando pelo finally neste momento.')

#_________________________________________________________________________________________________________________

print('\nPosso utilizar o finally para finalizar o valor de uma variável, exemplo : ')
"""
No exemplo, se eu não utilizasse um finally, iria dar erro pois não existe divisão por zero!!!!
"""
try:
    a = 1/0
except Exception as erro4:
    print(f'Deu erro : {erro4}')
finally:
    a = None
print(f'Valor de a : {a}\n')

#_________________________________________________________________________________________________________________

"""
Podemos utilizar try e except até dentro de try
"""
print(f'Utilizando um Try e Except dentro de um try:')
try:
    a = 0
    try:
        a = 1/0
    except:
        print(f'Deu Erro! Estamos no momento, dentro do except, que está dentro do primeiro try!')
        print(f'Valor de a no momento : {a}')
except:
    print('Erro do Except')

#_________________________________________________________________________________________________________________