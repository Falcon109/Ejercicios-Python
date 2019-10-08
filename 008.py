entrada=""
suma=0
while suma<3 and entrada!="despedida":
    entrada=input("clave:")
    suma=suma+1
    print("intento %d. \n" % suma)
print("utilizaste %d intentos." % suma)6