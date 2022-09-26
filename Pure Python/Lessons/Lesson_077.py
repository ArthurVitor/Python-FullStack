from random import randint


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome='Arthur', idade=15):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_de_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Arthur', 15)
print(p1.nome, p1.idade)