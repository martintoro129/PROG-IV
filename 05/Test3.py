def todos_positivos(lista_numeros):
    lista_numeros = []

    for n in lista_numeros:
        if n in range(1, 100):
            return True
        else:
            return False


lista_numeros = [10, 20, -20, -10]