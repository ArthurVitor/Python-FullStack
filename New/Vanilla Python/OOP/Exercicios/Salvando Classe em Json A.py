import json
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Vai', 15)
dados = json.dumps(vars(p1), indent=2)
print(dados)
dados = json.loads(dados)
p2 = Pessoa(**dados)
print(p2.idade)