class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'O {self.nome} está acelerando')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
print('')
celta = Carro('Celta')
print(celta.nome)
celta.acelerar()