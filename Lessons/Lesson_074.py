from time import time, sleep


def velocity(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resul = funcao(*args, **kwargs)
        end_time = time()
        temp = (end_time - start_time) * 1000
        print(f'Levou {temp}')
        return resul
    return interna


@velocity
def demora():
    for i in range(5):
        sleep(1)


demora()
