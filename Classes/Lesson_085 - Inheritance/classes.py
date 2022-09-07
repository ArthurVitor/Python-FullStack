class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter  # O setter somente afeta o nome na classe "Cliente", outros classes permaneceram intocadas
    def nome(self, valor):
        if isinstance(valor, str):
            valor = valor.replace('Ar', 'BA')
        self._nome = valor



class Cliente(Pessoa):  # Herdou os atributos 'NOME' e 'IDADE' da classe pai (Pessoa).
    pass

class Aluno(Pessoa):
    def prainta(self):
        print(self.nome)
