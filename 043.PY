TABLA = [[0 for columna in range (0,4)]for filas in range(0,4)]
for i in range (0,4):
    for j in range(0,4):
            if (i+1)%2==0:
                TABLA[i][j]=1
            else:
                TABLA[i][j]=0
print(TABLA)
