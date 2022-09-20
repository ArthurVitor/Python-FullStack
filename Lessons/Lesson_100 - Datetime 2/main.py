from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, '')

def converter_em_dicionario(data) -> dict:
    formatacao = list(data.strftime('%d %m %Y'))
    formatacao = ''.join(formatacao).split()
    dctt = dict(zip(('dia', 'mes', 'ano'), formatacao))
    return dctt

dt = datetime.now()
dctt = converter_em_dicionario(dt)
print(dctt['mes'])