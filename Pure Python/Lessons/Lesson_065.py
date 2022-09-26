from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']
cidades_estados = zip(
    indice,
    cidades,
    estados)

for valor in cidades_estados:
    print(valor )