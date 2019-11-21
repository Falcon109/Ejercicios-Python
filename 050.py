nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
print("En mayúsculas sería {}".format( nombre.upper() ) )
print("En Minúsculas sería {}".format( nombre.lower() ) )


#otra manera seria
# print(nombre.upper())
# print(nombre.lower())

print(nombre[2: ])#esto sirve para escribir sierta parte de la varible, el primer numero es de donde Empieza y el numero que esta despues de los : es el HASTA
print(nombre[-2: ])
print(nombre[2:len(nombre)])#al parecer si coloco len tanto me manga hasta el final de la variable

#esto sirve para poder juntar varibles
espacio=" "
saludos="hola"
frase= saludos + espacio + nombre + espacio + apellido
print(frase)

print("hola",nombre,apellido)

for i in range ((len(nombre)-1),-1,-1):
    print(nombre[i])

print ("al revés seria: ", end="" )
print (nombre[::-1] )