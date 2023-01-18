lista = [
    ['P1', 13],
    ['P2', 4],
    ['P3', 34],
    ['P4', 51],
    ['P5', 3],
]

lista = sorted(lista, key=lambda i: i[1])
for nm, vl in lista:
    print(f'Name: {nm}, value: {vl}')