mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista+mi_lista2
resuelto = mi_lista[0:]
mi_lista3.append("g")
deleted = mi_lista3.pop(0)
# elimina elementos y sin parametro el último,
# y el parametro el el indice sin corchete
print(mi_lista3)
print(deleted)

lista = ['q', 'd', 'f', 'r', 'b']
lista.sort()
lista.reverse()
print(lista)
