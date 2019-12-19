import os
archivo=open("C:/Users/User/Desktop/Python/OwO059.txt","w")
for i in range(1,4):
    Nombre=str(input("ingrese el nombre:"))
    Apellido=str(input("ingrese el apellido:"))
    Nota1=float(input("Nota N°1:"))
    Nota2=float(input("Nota N°2:"))
    Nota3=float(input("Nota N°3:"))
    notaa=str(Nota1)
    notab=str(Nota2)
    notac=str(Nota3)
    archivo.write(Nombre+" "+Apellido+" "+notaa+" "+notab+" "+notac+" "+"\n")
    os.system("cls")
archivo.close()
archivo=open("OwO059.txt","r")
Lista=[]
for linea in archivo.readlines():
    print(linea)
    Lista.append(linea)
archivo.close()
archivo=open("OwO059.txt","r")
archivoUwU=open("C:/Users/User/Desktop/Python/UwU059.txt","w")
Lista=[]
for linea in archivo.readlines():
    Lineatrajo=linea.split()
    Nota1a=float(Lineatrajo[2])
    Nota2b=float(Lineatrajo[3])
    Nota3c=float(Lineatrajo[4])
    promedioestudiante=float((Nota1a+Nota2b+Nota3c)/3)
    pronota=str(promedioestudiante)
    archivoUwU.write(Lineatrajo[0]+" "+Lineatrajo[1]+" "+Lineatrajo[2]+" "+Lineatrajo[3]+" "+Lineatrajo[4]+" "+pronota+"\n")
archivoUwU.close()
archivo.close()
archivo=open("C:/Users/User/Desktop/Python/UwU059.txt","r")
Lista=[]
for linea in archivo.readlines():
    print(linea)
    Lista.append(linea)