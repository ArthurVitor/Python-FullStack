#Python functions


def saudacao(msg='Olá', nome='usuário'): #Receives two parameters and print it
    return f'{msg}, {nome}'

variavel = saudacao()

if __name__ == '__main__':
    print(variavel)