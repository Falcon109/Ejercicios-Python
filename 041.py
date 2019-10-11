datos = [[0 for columna in range (0,3)]for fila in range (0,4)]
for i in range (0,4):
    suma=0
    for j in range (0,3):
        datos[i][j]=int(input("ingrese un numero:")) # i es filas y j son columnas
        suma=suma+datos[i][j]
    promedio=suma/3
    print("el promedio de la fila es:",promedio)
print(datos)