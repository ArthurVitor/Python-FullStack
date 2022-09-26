from dados import *
import json


with open('clients.json', 'r') as arquivo:
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave, end=' ')
    print(valor['nome'])