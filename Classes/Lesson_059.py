# d1 = {'chave1':'Chave1 Valor', 'chave2':'Chave2 Valor'}
# d1['nova_chave'] = 'Lindo'
# print(d1['nova_chave'])

# d1 = {
#     'str':'String',
#     123:'Int',
#     (1,2,3,4):'Tupla'
# }
#
# for k, v in d1.items():
#     print(k, ':', v)

clientes = {
    'cliente1': {
        'nome': 'Arthur',
        'sobrenome': 'Vitor'
    },
    'cliente2': {
        'nome': 'Pedro',
        'sobrenome': 'Moreira'
    },
}

for ck, cv in clientes.items():
    print(f'Cliente: {ck}')
    for dd_k, dd_v in cv.items():
        print(f'\t {dd_k}, {dd_v}')