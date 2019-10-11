datos = [0 for x in range(20)]
for i in range(0,len(datos)):
    datos[i] = int(input("dime el dato numero {}: ".format(i+1) ))
print ("los datos al reves son: ")
for i in range(len(datos),0,-1):
    print(datos[i-1])