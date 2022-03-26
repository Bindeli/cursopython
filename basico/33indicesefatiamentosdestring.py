"""
Manipulando strings - Aula 33
* String indices
* Fatiamento de Strings [inicio: parar : passo]
* Funções Built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

"""

# indices positivos     [012345678] começa com 0
texto =                 "Python s2"
# indices negativos    -[987654321] como os positivos já possuem o 0, começa do 1, porém de trás para frente

# indice=contéudo do indice : 0=P , 1=Y , 2=T , 3=H, 4=O, 5=N,6=espaço,7=s e 8=2
# printar na tela o conteúdo do indice 2 da variavel texto
print(f'Texto gravado : {texto}')
print(f'No índice 2 teremos : {texto[2]}')
print(f'No índice 3 teremos : {texto[3]}')
print(f'No índice 6 teremos : {texto[6]}') #terá um espaço, não terá nada
print(f'No índice 8 teremos : {texto[8]}')
print(f'No índice -4 teremos : {texto[-4]}')
print(f'No índice -5 teremos : {texto[-5]}')

print('Utilizando fatiamento')
url = 'www.google.com.br/'
# caso eu não queria que printe com a barra, puxo todos de antes antes indice -1
# os dois pontos para sinalizar o conteúdo que eu quero
print(url[:-1])

# Fatiamento de Strings [inicio: parar : passo]
# vou começar no índice 2 e o fim será um indice não incluindo
# quero pegar do t até o n, então vou começar no indice 2 e finalizar no 6
# ele não irá incluir o conteúdo do indice selecionado para finalizar.
nova_string = texto[2:6]
print(f'utilizando fatiamento : {nova_string}') # irá imprimir somente thon
# caso eu queira que ele comece deste o inicio, só não colocar nada ou 0 antes dos dois pontos:
nova_string2 = texto[:6] # vai até o indice 6 e não inclui o indice 6
print(f'utilizando fatiamento : {nova_string2}') # irá imprimir somente Python
# caso eu queira pegar o final, eu coloco o indice 7 e depois dos dois pontos deixo sem nada
nova_string3 = texto[7:]
print(f'utilizando fatiamento : {nova_string3}')
#Caso eu queria que ele pule alguns indice, por exemplo, pegue o indice 1 e depois o 3
#[inicio: parar : passo]
nova_string4 = texto[0::2] # vai começar no indice 0, vai pular o 1 e vai imprimir o 2
print(f'Pulando indice: {nova_string4}')
# lembrando que no indice 6 tem apenas espaço e não irá aparecer

