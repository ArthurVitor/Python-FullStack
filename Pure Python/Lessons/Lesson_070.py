from Dados import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i,: i + ac, lista, 0)
print(soma_lista)