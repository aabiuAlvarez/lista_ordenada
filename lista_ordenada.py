
lista1 = [8, 3, 7]
lista2 = [2, 5, 9]
lista3 = [4, 6, 1]


lista_combinada = [*lista1, *lista2, *lista3]
lista_ordenada = sorted(lista_combinada)
print(lista_ordenada)