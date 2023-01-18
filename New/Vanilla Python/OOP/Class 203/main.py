class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando


    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando')
            return

        print(f'{self.nome} Está filmando')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está filmando')