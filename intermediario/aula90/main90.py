"""
Como corrigir alguns erros

"""

# supondo que no modulo 1 e modulo 2, eu tenha uma variavel que eu quero importar

# from pacote1.modulo1 import variavel1
# Não preciso desse importo pois já estou fazendo este import no módulo 2

from pacote2.modulo2 import variavel2

# print(f'Variavel do modulo 1 : {variavel1}') # já tenho um print no módulo 2 para variável 1
print(f'Variavel do modulo 2 : {variavel2}')

"""
Só que um programa não funciona dessa maneira, de um main você não irá importar todos os arquivos de seu programa

Geralmente de dentro de um pacote ou de um módulo, você importa outro módulo

Então indo para o módulo 2, vamos tentar importar a variavel do modulo 1, eles estão longe um do outro

Sempre que eu for fazer uma importação, tenho que analisar qual é o ponto de vista, da entrada de meu programa

no momento, o main90.py
"""

#_________________________________________________________________________________________________________________
# Como o Python sabe quais os módulos que ele pode importar e de onde que ele pode importar esses módulos?
# isso está presente dentro de sys

import sys

# e se eu utilizar o sys.path com print irei ver todos os caminhos que o Python vai buscar os módulos

print(sys.path)
#_________________________________________________________________________________________________________________




#_________________________________________________________________________________________________________________




#_________________________________________________________________________________________________________________

# print(f'')












