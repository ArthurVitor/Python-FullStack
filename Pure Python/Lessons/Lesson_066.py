from itertools import count


cc = count()
nomes = ['Arthur', 'Vitor', 'Silva', 'Alfred']
nomes = zip(nomes, cc)
print(list(nomes))