X1=int(input("ingrese un numero:"))
X2=int(input("ingrese un numero:"))
if X1>X2:
    Mayor=X1
    Menor=X2
else:
    Mayor=X2
    Menor=X1
divicion=(Mayor%Menor)
if divicion>0:
    Respuesta=Mayor-Menor
    print(Respuesta)
else:
    Respuesta=Mayor+Menor
    print(Respuesta)