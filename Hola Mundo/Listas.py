asignaturas=["Matemáticas","Física","Química","Historia","Lengua"]
print(asignaturas)
print("Yo estudio %s"%(asignaturas))
asignaturas=asignaturas.__add__(asignaturas+asignaturas)
listaset=set(asignaturas)
aux=input()
print(aux in listaset)

numeros=[1,2,3]
cadena=["hola","mundo"]
numeros.append(4)
print(numeros)
a=["Jake","John","Eric"]
b=["John","Jill"]
c=a.intersection(b)
print(c)