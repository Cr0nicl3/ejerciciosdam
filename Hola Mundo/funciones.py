def ultimo_elemento(lista):
    print(lista[-1])
def sumar_elemento(lista):
    suma=0
    for i in range(lista.__len__()):
        suma=suma+lista[i]
    return suma
lista=[1,2,3,4]
ultimo_elemento(lista)
print(sumar_elemento(lista))