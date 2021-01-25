print("Cuantos años tienes?")
edad=int(input())
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("Dame tu contraseña")
contr=input()
print("Pon de nuevo tu contraseña")
contr2=input()
if contr.upper() == contr2.upper():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
año=int(input("Dime un numero: "))
if año%2==0:
    print("Es par")
else:
    print("Es impar")
x=int(input("Dame el primer numero: "))
y=int(input("Dame el segundo numero: "))
if y==0:
    print("ERROR")
else:
    print(x/y)