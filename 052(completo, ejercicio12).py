Matriz = [[0 for columna in range (0,4)]for filas in range (0,5)]

for i in range (0,5):
    for j in range (0,4):
            if i==0:
                if j==0:
                    Matriz[i][j]=(i*(j+1))+((i+1)*(j+1))+((i+1)*j)
                elif j==3:
                    Matriz[i][j]=(i*(j-1))+((i+1)*(j-1))+((i+1)*j)
                else:
                    Matriz[i][j]=(i*(j-1))+((i+1)*(j-1))+((i+1)*j)+((i+1)*(j+1))+(i*(j+1))
            if i==1 or i==2 or i==3:
                if j==0:
                    Matriz[i][j]=((i-1)*j)+((i-1)*(j+1))+(i*(j+1))+((i+1)*(j+1))+((i+1)*j)
                elif j==3:
                    Matriz[i][j]=((i-1)*j)+((i-1)*(j-1))+(i*(j-1))+((i+1)*(j-1))+((i+1)*j)
                else:
                    Matriz[i][j]=((i-1)*j)+((i-1)*(j+1))+(i*(j+1))+((i+1)*(j+1))+((i+1)*j)+((i-1)*(j-1))+(i*(j-1))+((i+1)*(j-1))
            if i==4:
                if j==0:
                    Matriz[i][j]=(i*(j+1))+((i-1)*(j+1))+((i-1)*j)
                elif j==3:
                    Matriz[i][j]=(i*(j-1))+((i-1)*(j-1))+((i-1)*j)
                else:
                    Matriz[i][j]=(i*(j-1))+((i-1)*(j-1))+((i-1)*j)+((i-1)*(j+1))+(i*(j+1))
print(Matriz)