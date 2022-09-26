from random import randint
from faker import Faker

fake = Faker()
id = randint(1, 100)


class BaseDeDados:
    def __init__(self):
        self.__dados = [{'id': 0, 'nome': 'Arthur'}]

    def inserir_cliente(self, id, nome):
        self.__dados.append({'id': id, 'nome': nome})

    def lista_clientes(self, sor=False, rev=False):
        if sor == True:
            self.__dados.sort(key=lambda item: item['id'], reverse=rev)
            for c in self.__dados:
                print(c)
        else:
            for c in self.__dados:
                print(c)

    def remove(self, id):
        for c in self.__dados:
            if c['id'] == id:
                self.__dados.pop(self.__dados.index(c))
                return


vc = BaseDeDados()
for c in range(100):
    vc.inserir_cliente(randint(1, 100), fake.name())

vc.lista_clientes(True, True)
