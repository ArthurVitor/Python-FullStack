alunos = list([
    {'id': 15, 'nome': 'Arthur'},
    {'id': 51, 'nome': 'Cleber'},
    {'id': 412, 'nome': 'Pedro'},
    {'id': -15, 'nome': 'Tutu'}
])

alunos.append({'id': 84, 'nome': 'Astolfo'})
alunos.sort(key=lambda item: item['id'])
for c in alunos:
    print(c)