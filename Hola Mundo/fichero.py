no=int(input())
f=open("tabla-"+str(no)+".txt","w")
for i in range(10):
    f.write("%dx%d=%d\n"%((i+1),no,(i+1)*no))
no=int(input())
f=open("tabla-"+str(no)+".txt","r")
for i in range(10):
    print(f.readline())
