"""
AULA 79 - Group by

Agrupando elementos em um dicionário
"""
# importando a ferramenta groupby de itertools
from itertools import groupby

alunos = [
    {'nome' : 'Lucas', 'nota' : 'A'},
    {'nome' : 'Letícia', 'nota' : 'B'},
    {'nome' : 'João', 'nota' : 'C'},
    {'nome' : 'Eduardo', 'nota' : 'D'},
    {'nome' : 'Thayna', 'nota' : 'E'},
    {'nome' : 'Paola', 'nota' : 'A'},
    {'nome' : 'Paulo', 'nota' : 'C'},
    {'nome' : 'Ana', 'nota' : 'A'},
    {'nome' : 'Otavio', 'nota' : 'B'},
    {'nome' : 'Evandro', 'nota' : 'D'},
]

#--------------------------------------------------------------------------------------------

"""
A função ''group by'' precisa que o dicionario esteja ordernado
Se eu quisesse agrupar por nota, eu iria precisar que todos eles estivessem em ordem
"""
# criei um lambda para sortear pela nota
ordernada = lambda item: item['nota']
alunos.sort(key=ordernada)

# for aluno in alunos:
#     print(aluno)

#--------------------------------------------------------------------------------------------

"""
Agora queremos agrupar em um dicionário, todo mundo que possui notas semelhantes
"""
# eu crio uma variavel para receber o group by, passo o iteravel que desejo
# e depois da virgula, coloco por qual chave eu quero agrupar.
alunos_agrupados = groupby(alunos,ordernada)


#--------------------------------------------------------------------------------------------

"""
for agrupados in alunos_agrupados:
    print(agrupados)
    
Se eu fazer deste modelo, irá aparecer o valor agrupado e um endereço
Não irá aparecer os elementos
Exemplo : ('A', <itertools._grouper object at 0x000001722EAE7F40>)
"""
# extrai a chave para agrupamento, que será as notas
# e os valores_agrupados, irá receber os alunos

#--------------------------------------------------------------------------------------------

from itertools import tee

"""
Vou importar a ferramenta tee para poder iterar sobre a mesma lista
"""
# --------------------------------------------------------------------------------------------
for agrupamento, valores_agrupados in alunos_agrupados:

    lista_1, lista_2 = tee(valores_agrupados)

    print(f'Agrupamento : {agrupamento}')
    for aluno in lista_1:
        print(f'\t{aluno}')

    # eu transformei os valores_agrupados em uma lista, pois o groupby não possui len
    # irá dar esse erro : TypeError: object of type 'itertools._grouper' has no len()
    quantidade_total = len(list(lista_2))

    print(f'\t{quantidade_total} alunos tiraram a nota {agrupamento}\n')
    """
    {len(list(valores_agrupados))} - Como isso aqui é um iterador, eu esgotei os dados
    onde está cada nome de aluno.
    se eu utilizar um novo for para imprimir cada aluno, ou utilizar o len com list depois de
    ter utilizado o for com alunos, eles não terão valores.
    """
#--------------------------------------------------------------------------------------------

"""
Como os valores_agrupados retornou um iterador, a partir do momento que eu esgotei os valores
desse iterador, no momento que eu fiz um for
for aluno in valores_agrupados:
    print(aluno)
    
eu cheguei no final do iterador, e esgotei os valores
no momento que eu chamei ele novamente, não tinha mais valores para puxar

E com o itertool, ''tee'', eu fiz duas copias do iterador, e invés de ter utilizado o iterador
eu utilizei as duas copias do iterador , lista_1 e lista_2


"""

# print('\nAgora sem utilizar tee: ')


# Sem tee (com list)
# for agrupamento, valores_agrupados in alunos_agrupados:
#   valores = list(valores_agrupados)
#   print(f'Agrupamento: {agrupamento}')
#   for aluno in valores:
#     print(f'\t{aluno}')
#   quantidade = len(valores)
#   print(f'\t{quantidade} alunos tiraram nota {agrupamento}')

# --------------------------------------------------------------------------------------------------




