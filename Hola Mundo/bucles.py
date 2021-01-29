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

string="ana"
palin=True
for i in range(string.__len__()):
    if(i==0):
        i=1
    palin=(string[i]==string[-i-1])
    if(not palin):
        print("No es un palindromo")
        break

if (palin):
    print("Es un palindromo")

import re
string=input()
for i in range(string.__len__()):
    if(i==0):i=1
        
    r1=re.findall(string[i],string)
    print(r1.__len__())