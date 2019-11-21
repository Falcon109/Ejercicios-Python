OwO = [[0 for columna in range (0,4)]for filas in range(0,4)]
cam=0
for i in range(0,4):
    for j in range(0,4):
        OwO[i][j]=0
        OwO[cam][cam]=1 #Tambien siviria si i y j son iguales para darles el valor
    cam=cam+1
print(OwO)
