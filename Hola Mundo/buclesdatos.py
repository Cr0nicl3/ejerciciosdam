asignaturas={"Fisica":0,"Quimica":0,"Historia":0}
for i in asignaturas:
   asignaturas[i]=input("Dame la nota de la asignatura "+i+":")
for i in asignaturas:
    print("La nota en la asignatura de "+i+" es "+asignaturas[i])

loteria=[]
for i in range(5):
    loteria.insert(loteria.__len__(),int(input("Dame el numero de loteria: ")))
loteria.sort()
print(loteria)