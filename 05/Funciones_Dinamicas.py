

def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

cifra=(555,99,100*1)
resultado = chequear_3_cifras(cifra)
print(resultado)