from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Arthur', 'Vitor')
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)