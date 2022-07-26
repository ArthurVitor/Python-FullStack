string = '01234567890123456789012345678901234567890123456789'
lista = []
min, sep = 0, 10
for c in range(0, int(string.count('9'))):
    lista.append(string[min:sep])
    min, sep + 10, 10

print(lista, sep='_')