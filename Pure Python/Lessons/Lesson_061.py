lista = [c * 3 for c in range(0, 10)]
print(f'Lista 1 {lista}')

ex2 = [v * 2 for v in lista]
print(f'Lista 2 {ex2}')

ex3 = [(v, v2) for v in lista for v2 in range(3)]
print(f'Lista 3 {ex3}')

l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@') for v in l2]
print(f'Lista 4 {ex4}')

tupla = (
    ('chave1', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(y, x) for x, y in tupla]
print(ex5)