class Animal:
    def __init__(self, nome):
        self.nome = nome

    def acao(self, fala):
        print(f'{self.nome} falou, {fala}')

leao = Animal(nome='Leão')
leao.acao('vai cachorro vai')