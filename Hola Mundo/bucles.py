count=int(input("Dame un numero desde el que contar: "))
string=""
for i in range(count+1):
    string=string+str(i)+", "
print(string)

count=int(input("Dame un numero desde el que contar: "))
string=""
for i in range(count+1):
    if i%2==1:
        string=string+str(i)+", "
print(string)

for i in range(10):
    print("%dx10=%d"%((i+1),(i+1)*10))

while string!="salir":
    string=input()
    if string=="salir":
        break
    print(string)
