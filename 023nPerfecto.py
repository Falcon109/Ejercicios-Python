X=int(input("ingrese un numero:"))
suma=0
for i in range(1,X,1):
    if ((X%i)==0):
        suma=i+suma
if X==suma:
    print ("es perfecto")
else:
    print ("no es perfecto")


