# string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
#
# def stringSplitting(string):
#     lista = []
#     stt, sep = 0, 10
#     for c in range(0, int(string.count('9'))):
#         lista.append(string[stt:sep])
#         stt, sep + 10, 10
#     return lista
#
#
# if __name__ == '__main__':
#     print(stringSplitting(string))
# Minha solução

# Solução do video
string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
lista = [(string[i: i + n]) for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(retorno)