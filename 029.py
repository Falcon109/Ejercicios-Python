datos = []
for i in range (0,10):
    numer1 = int(input("ingrese un numero:"))
    datos.append(numer1)
for i in range (0,10,1):
    if ((datos [i])%2)==0:
        print("los numeros pares son:",(datos [i]))