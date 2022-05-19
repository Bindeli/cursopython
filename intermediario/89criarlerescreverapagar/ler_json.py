import json

with open('abc.json', 'r') as file:
    # vou criar uma variavel que contenha o json
    d1_json = file.read()
    print(d1_json)
    # agora quero que isso aqui, volte a ser um dicionário, pois assim não consigo acessar nenhuma chave
    d1_json = json.loads(d1_json) # agora eu estou voltando ele para um dicionário como estava antes


print(f'\nAGORA IMPRIMINDO PARA VERIFICAR SE ELE VOLTOU A SER UM DICIONÁRIO:')

for chave, valor in d1_json.items():

    print(chave)
    for key1, var1 in valor.items():
        print(key1,var1)
    print('\n')