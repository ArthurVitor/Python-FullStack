# lista_A = [1,2,3,4,5,6,7,8]
# lista_B = [1,2,3,4]
# lista_C = zip(lista_A, lista_B)
# tot = []
# for c in lista_C:
#     tot.append(sum(c))
#
# print(tot) Minha solução

lista_A = [1,2,3,4,5,6,7,8]
lista_B = [1,2,3,4]
tot = [x + y for x, y in zip(lista_A, lista_B)]
print(tot)