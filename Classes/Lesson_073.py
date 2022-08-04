file = open('abc.txt', 'w+')
file.write('Linha 1 \n')
file.write('Linha 2 \n')
file.write('Linha 3 \n')
file.seek(0, 0)
print(file.read())
print('###')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

print('###')
file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')
file.close()
