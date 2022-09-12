class Pessoa:  # Super classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_classe} falando | Falar de pessoa')

    def teste(self):
        print('Teste | Classe Pessoa')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_classe} está comprando')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} está estudando')


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome}, {self.sobrenome}')
