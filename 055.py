archivo=open("UwU.txt","w")
archivo.write("hola usuario\nhoy es un buen dia\nbueno\nadios")
archivo.close()
archivo=open("UwU.txt","r")
print(archivo.readline())
archivo.seek(0)
print("ahora leeremos todas las lineas")
lista=[]
for linea in archivo.readlines():
    print(linea)
    lista.append(linea)
archivo.close()
print("*****aqui esta cerrando el archivo*****")
print(lista)