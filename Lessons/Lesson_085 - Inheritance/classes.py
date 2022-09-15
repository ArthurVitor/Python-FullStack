class Pessoa:  # Super classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_classe} está falando')


class Cliente(Pessoa):  # Sub-classe. 0Herdou os atributos 'NOME' e 'IDADE' da super classe (Pessoa), além de seus metodos.
    def comprar(self):
        print(f'{self.nome_classe} está comprando')


class Aluno(Pessoa):  # Sub-classe. Herdou os atributos 'NOME' e 'IDADE' da da super-classe (Pessoa), além de seus metodos.
    def estudar(self):
        print(f'{self.nome_classe} está estudando')
