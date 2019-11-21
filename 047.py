import random
TwT = [[0 for columna in range(0,5)]for fila in range(0,4)]
suma=0
for i in range(0,4):
    suma=0
    for j in range(0,5):
        #TwT[i][j]=int(input("ingrese un numero:"))
        TwT[i][j]=random.randint(0,10)
        suma=TwT[i][j]+suma
    if (i+1)%2!=0:
        print("la suma de los elementos en la comuna N°",i+1,"es:",suma)
print(TwT)
print(TwT[1][2])
print(TwT[2][1])
