from Dados import produtos, pessoas, lista


nova_lista = filter(lambda p: p['preco'] > 10, produtos)
for c in nova_lista:
    print(c)