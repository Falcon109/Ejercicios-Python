archivo=open("claseOwO.txt","w")
archivo.write("hola mundo")
archivo.close
archivo=open("claseOwO.txt","r")
print(archivo.read())
archivo.close
archivo.seek(0)
print(archivo.read(6))
archivo.seek(3)
print(archivo.read(5))
archivo.close()