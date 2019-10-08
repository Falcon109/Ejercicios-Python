numer1=int(input("ingrese un numero:"))
divisor=0
for i in range (1,numer1+1,1):
    if ((numer1%i)==0):
        divisor=divisor+1
if divisor>2:
    print("no es primo")
else:
    print("es primo")