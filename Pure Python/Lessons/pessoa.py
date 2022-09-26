class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        else:
            print(f'{self.nome} está comendo')
            self.comendo = True

    def pararComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print('Não se pode falar comendo')
            return

        if self.falando:
            print('Já está falando')
            return

        print(assunto)
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print('Não está falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False