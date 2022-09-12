from eletronico import Eletronico


class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            print(f'{self._nome} não está ligado')
            return

        if self._conectado:
            print(f'{self._nome} já está conectado')
            return

        self._conectado = True
        print(f'{self._nome} está conectado')

    def desconectar(self):
        if not self._conectado:
            print(f'{self._nome} não está conectado')
            return
        self._conectado = False
