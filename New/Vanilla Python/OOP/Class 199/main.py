# string = "Arthur".upper()
# print(isinstance(string, str))


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Arthur', 'Vitor')
print(p1.nome)