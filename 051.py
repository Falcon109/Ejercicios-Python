import random
Matriz = [[0 for columna in range (0,5)]for filas in range (0,4)]

for i in range (0,4): #recorre las filas
    for j in range(0,5): #recorre las columnas
        Matriz[i][j]=random.randint(1,10) #numeros a lo loco
        #Matriz[i][j]=int(input("introdusca un numero:"))
print (Matriz)

suma=0
for i in range (0,4): #recorre las filas
    for j in range(0,5): #recorre las columnas
        if (j%2!=0):
            suma=Matriz[i][j]+suma

print("la suma de las columanas impares es:", suma)
print("el numero en la posicion (2,3) es:",Matriz[1][2])
print("el numero en la posicion (3,2) es:",Matriz[2][1])