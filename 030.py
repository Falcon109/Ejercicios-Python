#aca declaro el arreglo
datos = []
#esta linea me crea un bandera que me avisara si es que encuentra o no el numero (ver linea 13)
aviso=0
for i in range (0,10,1):
        numer=int(input("ingrese un numero:"))
        datos.append(numer)
Res=int(input("¿que numero quiere buscar?:"))
while Res!=0:
    for i in range (0,10,1):
        if datos [i] == Res:
            print("el numero esta en el arreglo")
            aviso=1

    if aviso==0:
        print("el numero no esta en el arreglo")
    
    aviso=0
    Res=int(input("¿que numero quiere buscar?:"))
