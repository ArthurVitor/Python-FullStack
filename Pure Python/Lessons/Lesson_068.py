from itertools import groupby

alunos = [
    {'nome': 'Arthur', 'nota': 'A'},
    {'nome': 'Clebar', 'nota': 'C'},
    {'nome': 'Tut', 'nota': 'D'},
    {'nome': 'Miguel', 'nota': 'F'},
    {'nome': 'Alfred', 'nota': 'T'},
    {'nome': 'Dudu', 'nota': 'B'},
    {'nome': 'Leticia', 'nota': 'E'},
    {'nome': 'Rose', 'nota': 'D'},
    {'nome': 'Joana', 'nota': 'F'},
    {'nome': 'João', 'nota': 'Z'},
]
ordena = key=lambda item: item['nota']
alunos.sort(key=ordena)
alunosAgrupados = groupby(alunos, ordena)

for secao, valor in alunosAgrupados:
    print(f'Seção: {secao}')
    print(f'{len(list(valor))} alunos tiraram {secao}')
    print('')

    # for aluno in valor:
    #     print(f' \t Aluno: {aluno}')
    # print('')