from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import monthrange

setlocale(LC_ALL, '')


def converter_em_dicionario(data) -> dict:
    formatacao = list(data.strftime('%d %m %Y'))
    formatacao = ''.join(formatacao).split()
    dctt = dict(zip(('dia', 'mes', 'ano'), formatacao))
    return dctt


dt = datetime.now()
mes_atual = int(datetime.strftime('%m'))
formatacao1 = dt.strftime('%A, %d, de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y')

print(monthrange(2022, mes_atual))
print(formatacao1)
print(formatacao2)
