class TaErradoError(Exception):
    ...



def test():
    raise TaErradoError('Errado')

try:
    test()
except TaErradoError as e:
    print(f'Erro: {e}')