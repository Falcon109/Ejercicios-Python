import random
N=int(input("ingrese el largo de la matriz :"))
OwO = [[0 for columnas in range (0,N)]for filas in range(0,N)] #definicio de la matriz
sumadiagonaltotal=0
sumadiagonal_1=0
sumadiagonal_2=0
numer1=0
numer2=0
suma_2=0
suma_3=0
numer3=0
J=4
for i in range (0,5): #recorre las filas
    for j in range(0,5): #recorre las columnas
        OwO[i][j]=random.randint(1,1000) #numeros a lo loco
        if i==j:
            numer1=OwO[i][j]
            sumadiagonal_1=(numer1+sumadiagonal_1)
        elif ((i+j)==N-1):
            numer2=OwO[i][j]
            sumadiagonal_2=(sumadiagonal_2+numer2)
        else:
            numer3=OwO[i][j]
            suma_3=numer3+suma_3
        if i==0:
            numer2=OwO[0][j]
            suma_2=numer2+suma_2
print(OwO)
sumadiagonaltotal=sumadiagonal_1+sumadiagonal_2
print("la suma de las dianogales es:",sumadiagonaltotal)
print("la suma de la fila 1 es:",suma_2)
print("la suma de los numeros que no estan en la diagonal es:",suma_3)