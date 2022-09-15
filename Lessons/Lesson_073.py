import json

d1 = {
    'P1': {
        'nome': 'Arthur',
        'idade': 15
    },
    'P2': {
        'nome': 'Cleber',
        'idade': 16
    }
}

for k, v in d1.items():
    print(k.upper())
    for k1, v1 in v.items():
        print(f' \t {k1.capitalize()}, {v1}')