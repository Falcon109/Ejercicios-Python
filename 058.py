Archivo=open("C:/Users/User/Desktop/Python/058.txt","w")
Num1=int(input("ingrese un numero:"))
Num2=int(input("ingrese un numero:"))
if Num1<Num2:
    for i in range (Num1+1,Num2,1):
        x=str(i)
        Archivo.write(x+" ")
else:
    for i in range (Num2+1,Num1,1):
        x=str(i)
        Archivo.write(x+" ")
Archivo.close