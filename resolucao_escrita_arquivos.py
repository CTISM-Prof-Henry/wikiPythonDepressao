import json

with open('arquivo.json', 'r') as json_file:

    arquivo = json.load(json_file)

print(arquivo)

print(type(arquivo))
