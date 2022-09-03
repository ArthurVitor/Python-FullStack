class Pessoa:
    def __init__(self):
        self.atributo = 'Teste'

    @property
    def nome(self):
        return 'Arthur'

    @nome.setter
    def nome(self, valor):
        self.atributo = valor


p1 = Pessoa()
p1.nome = 'João'
print(p1.atributo)
print(p1.nome)
