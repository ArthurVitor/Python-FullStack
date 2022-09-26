def soma(*args):
    args = sorted(args)
    print(args)


lista1 = [45,7,5,3,2,1,4,8,6,5,9,5,7]
lista2 = [-9,74,5,56,4,48,3,416,6]
soma(*lista1, *lista2)