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

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)