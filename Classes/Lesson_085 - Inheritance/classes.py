class Pessoa: # Super classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    @property  # Getter
    def nome(self):
        return self._nome

    @nome.setter  # O setter afeta o nome em todas as classes
    def nome(self, valor):
        if isinstance(valor, str):
            valor = valor.title()
        self._nome = valor


class Cliente(Pessoa):  # Sub-classe. 0Herdou os atributos 'NOME' e 'IDADE' da super classe (Pessoa), além de seus metodos.
    def comprar(self):
        print(f'{self.nome_classe} está comprando')


class Aluno(Pessoa): # Sub-classe. Herdou os atributos 'NOME' e 'IDADE' da da super-classe (Pessoa), além de seus metodos.
    def estudar(self):
        print(f'{self.nome_classe} está estudando')
