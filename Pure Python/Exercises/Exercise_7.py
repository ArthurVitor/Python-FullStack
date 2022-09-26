carrinho = []

carrinho.append(('Produto 1', 23))
carrinho.append(('Produto 2', 33))
carrinho.append(('Produto 3', 44))
carrinho.append(('Produto 4', 31))
carrinho.append(('Produto 5', 26))
carrinho.append(('Produto 6', 38))

def formata(valor):
    return f'R$ {valor}'

total = sum([float(y) for x, y in carrinho]) #Desempacotou o nome e o valor, mas armazenou apenas o valor


print(formata(total))