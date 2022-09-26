#Write a function that returns two parameters, "Saudacao, Nome"

def saudation(saudacao, nome):
    return f'{saudacao}, {nome}'

if __name__ == '__main__':
    print(saudation('Olá', 'Arthur'))