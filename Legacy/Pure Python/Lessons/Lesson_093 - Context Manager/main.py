class Arquivo:
    def __init__(self, arquivo, modo):
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Entrou no arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechou')
        self.arquivo.close()


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')