datos = [[0 for columna in range(0,5)]for fila in range(0,4)] #las filas y columna se cuentan desde el 0
for i in range(0,4):
    for j in range(0,5):
        print("datos[%d][%d]:%d" %(i,j,datos[i][j]))
#print(datos)