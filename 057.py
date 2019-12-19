archivo=open("C:/Users/User/Desktop/Python/057.txt","a")#recordar que w es para escribir y sobre escribir. a es para continuar con un archivo ya creado
for i in range(0,4):
    Nombre=str(input("Ingrese el nombre:"))
    Apellido=str(input("ingrese el apellido:"))
    archivo.write(Nombre+" "+Apellido+"\n")
archivo.close()
Archivo2=open("C:/Users/User/Desktop/Python/057.txt","r")
Lista=[]
for linea in Archivo2.readlines():
    print(linea)
    Lista.append(linea)
Archivo2.close()