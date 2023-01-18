class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def sobrenome(self):
        return 'Vitor'


p1 = Pessoa('Arthur')
print(p1.nome)
print(p1.sobrenome)