from Dados import produto, pessoas, lista

def aumentaIdade(p):
    p['novaIdade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumentaIdade, pessoas)

for pessoa in nomes:
    print(pessoa)