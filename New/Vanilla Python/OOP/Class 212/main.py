class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    @property
    def cor_tampa(self):
        return 123456


c1 = Caneta('Azul')
print(c1.cor)
print(c1.cor_tampa)
