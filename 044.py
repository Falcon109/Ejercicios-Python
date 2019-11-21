import random
TABLA1 = [[0 for columna in range (0,4)]for filas in range(0,4)]
TABLA2 = [[0 for columna in range (0,4)]for filas in range(0,4)]
TABLA3 = [[0 for columna in range (0,4)]for filas in range(0,4)]
for i in range (0,4):
    for j in range(0,4):
        TABLA1[i][j]=random.randint(0,10) #el random.randint introduce numeros entre los numeros que le das a colocar
        TABLA2[i][j]=random.randint(0,10)
print("TABLA 1:", TABLA1)
print("TABLA 2:", TABLA2)
numer1=0
numero2=0
for i in range (0,4):
    for j in range(0,4):
        numer1=TABLA1[i][j]
        numero2=TABLA2[i][j]
        TABLA3[i][j]=(numer1+numero2)
print("TABLA 3:", TABLA3)