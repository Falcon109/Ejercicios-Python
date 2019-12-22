import os #esta libreria es para limpiar pantalla, es de windows
import time #esta libreria es para porder pausar el programa en ciertos lugares
os.system("cls")#limpiar pantalla
print("******************************************************")#Aqui se da inicio al programa, de una forma mas profecional
print("")
print("                 Bienvenido Usuario")
print("")
print("******************************************************")
time.sleep(3) #el time.sleep(#) se utiliza para que el programa se pause o duerma por el tiempo en segundos dado en el ()
os.system("cls")
print("******************************************************")
print("")
print("            Gracias por elegirnos")
print("   Para empezar se necesita saber algunos datos")
print("")
print("******************************************************")
print("")
NombreUsuario=str(input("ingrese su nombre:")) #aqui se le solicita al usuario que registre su nombre
ApellidoUsuario=str(input("ingrese su apellido:")) #aqui se le solicita al usuario que registre su apellido
NumeroDeCaracteresEnUsuario=int(len(NombreUsuario)+len(ApellidoUsuario)) #aqui el programa calcula la cantidad de caracteres que tiene en total (la suma de su nombre y apellido)
os.system("cls")
print("******************************************************")
print("")
print("         ",NombreUsuario,ApellidoUsuario) #aqui se imprime lo que el usuario ingreso
print("")
print("******************************************************")
print("¿es correcta esta informacion?") #aqui el programa le pregunta al usuario si lo que el ingreso esta correcto
RespuestaAInformacionUsuario=int(input("Es Correcta(1) / Es Incorrecta(2), Su respuesta es:")) #aqui se guarda la respuesta dada por el usuario
while RespuestaAInformacionUsuario!=1 and RespuestaAInformacionUsuario!=2: #aqui volvera a preguntar si la informacion es incorrecta si el usuario ingresa un valor distinto a 1 y 2
    os.system("cls")
    print("******************************************************")
    print("")
    print("         ",NombreUsuario,ApellidoUsuario)
    print("")
    print("******************************************************")
    print("¿es correcta esta informacion?")
    RespuestaAInformacionUsuario=int(input("Es Correcta(1) / Es Incorrecta(2), Su respuesta es:"))
while RespuestaAInformacionUsuario==2: #aqui se entrara si el usuario dice que es incorrecto, y podra ingresar nuevamente su nombre y apellido
    os.system("cls")
    print("******************************************************")
    print("")
    NombreUsuario=str(input("ingrese su nombre:"))
    ApellidoUsuario=str(input("ingrese su apellido:"))
    NumeroDeCaracteresEnUsuario=int(len(NombreUsuario)+len(ApellidoUsuario))
    os.system("cls")
    print("******************************************************")
    print("")
    print("         ",NombreUsuario,ApellidoUsuario)
    print("")
    print("******************************************************")
    print("¿es correcta esta informacion?")
    RespuestaAInformacionUsuario=int(input("Es Correcta(1) / Es Incorrecta(2), Su respuesta es:"))
    #se volvera apreguntar si esta correcta la informacion
    while RespuestaAInformacionUsuario!=1 and RespuestaAInformacionUsuario!=2:
        os.system("cls")
        print("******************************************************")
        print("")
        print("         ",NombreUsuario,ApellidoUsuario)
        print("")
        print("******************************************************")
        print("¿es correcta esta informacion?")
        RespuestaAInformacionUsuario=int(input("Es Correcta(1) / Es Incorrecta(2), Su respuesta es:"))
os.system("cls")
vocales=["A","E","I","O","U","Á","É","Í","Ó","Ú"] #se crea una lista con las vocales a comparar
contadoramigos=0 #este contador sirve para saber cuantos amigos tiene el usuario y si el archivo tiene nombres ingresados
archivo=open("C:/Users/User/Desktop/Fuentes-Ariel_prueba3/ingresos.txt","r")#ARCHIVO. se hace la lectura del archivo ingreso.txt para saber su largo
for linea in archivo.readlines():#se hace la lectura de las lineas del archivo
    contadoramigos=contadoramigos+1 #cuenta la cantidad de amigos y lineas que tiene el archivo ingresados
archivo.close() #se cierra el archivo
if contadoramigos==0: #si el archivo no tiene nada adentro, imprimira lo siguiente:
    print("*************************************************************************")
    print("")
    print("       No tiene amigos registrados en el archivo 'ingresos.txt'")
    print("   Por favor cierre el programa, ingrese a sus amigos en 'ingresos.txt'")
    print("           El formato es: 'Nombre del amigo' 'Apellido del amigo'")
    print("")
    print("*************************************************************************")
    print("                                                              By Ariel F.")
else: #si el archivo tiene lineas ingresadas pasara lo siguiente:
    Archivo=open("C:/Users/User/Desktop/Fuentes-Ariel_prueba3/Mi_afinidad.txt","w") #Archivo. se crea un archivo donde estara la informacion de la afinidad
    contadoramigos1=str(contadoramigos) #se transforma la variable "contadoramigos" que estava en int a str para poder ser guardada en el archivo
    Archivo.write("Para el Usuario "+NombreUsuario+" "+ApellidoUsuario+" los amigos son "+contadoramigos1+" y su nivel de afinidad es:"+"\n") #se escribe en el archivo creado
    Archivo.close() #se cierra el archivo
    variables=open("C:/Users/User/Desktop/Fuentes-Ariel_prueba3/ingresos.txt","r") #Archivo. se lee nuevamente el archivo ingresos para calcular la afinidad
    for linea in variables.readlines(): #se leen las lineas del archivo
        #esta varibles cumplen la misma funcion, pero cree distintas para poder manejar de manera mas facil 
        contadorafinidad=0
        contadorafinidad2=0
        contadorafinidad3=0
        contadorafinidad4=0
        transformacion_variables=linea.split() #se transforma la linea del archivo a una lista que se guardara en una varible
        NombreAmigo=str(transformacion_variables[0]) #se busca en la lista que se creo la posicion (en este caso la 0), para poder trabajar en ella. tambien se tranforma a str lo que facilita la comparacion
        ApellidoAmigo=str(transformacion_variables[1])
        NombreAmigoComparar=(NombreAmigo.upper()) #aqui se transforma en mayusculas para que todas sean iguales
        ApellidoAmigoComparar=(ApellidoAmigo.upper())
        NombreUsuarioComparar=(NombreUsuario.upper())
        ApellidoUsuarioComparar=(ApellidoUsuario.upper())
        #aqui se hace la compracion del nombre del usuario con el nombre del amigo
        for i in NombreUsuarioComparar: #i tomara el valor de las letras en la variable NombreUsuarioComparar
            for j in vocales: #j tomara el valor de las vocales en la lista vocales
                if j==i: #se compa la vocales con las letras en el Nombre del usuario
                    comparar=j #si se encuentra una igualdad se guarda la vocal en comparar
                    for x in NombreAmigoComparar: #x tomara el valor de las letras del nombre del amigo
                        if comparar==x: #se compara la vocal encontrada en el nombre del usuario con la letras en el nombre del amigo
                            contadorafinidad=contadorafinidad+1 #si encuentra una igualda se suma 1
        #en los siguientes casos se sigue el mismo metodo que en el anterioro pero se comparar distintas varibles
        #aqui se hace la comparcion del apellido del usuario con el apellido del amigo
        for k in ApellidoUsuarioComparar:
            for t in vocales:
                if t==k:
                    comparar2=t
                    for e in ApellidoAmigoComparar:
                        if comparar2==e:
                            contadorafinidad2=contadorafinidad2+1
        #aqui se hace la comparcion entre el nombre del usuario y el apellido del amigo
        for g in NombreUsuarioComparar:
            for l in vocales:
                if l==g:
                    comparar3=l
                    for r in ApellidoAmigoComparar:
                        if comparar3==r:
                            contadorafinidad3=contadorafinidad3+1
        #aqui se hace la comparcion del apellido del usuario con el nombre del amigo
        for w in ApellidoUsuarioComparar:
            for h in vocales:
                if h==w:
                    comparar4=h
                    for z in NombreAmigoComparar:
                        if comparar4==z:
                            contadorafinidad4=contadorafinidad4+1
        caracteresencomun=(contadorafinidad+contadorafinidad2+contadorafinidad3+contadorafinidad4) #aqui se suma las vocales encontradas del usuario en sus amigos
        espacio=" " #se le da este valor para porder despues encadenar
        caracteresencomunstr=str(caracteresencomun) #aqui transformo algunas varibles que estaban en int a str para poder encadenar
        NumeroDeCaracteresEnUsuariostr=str(NumeroDeCaracteresEnUsuario)
        promedioafinidad=((caracteresencomun*100)/NumeroDeCaracteresEnUsuario) #se saca la afinidad con la cantidad de vocales encontradas por 100 divido por el total en usuario
        promedioafinidadstr=str(promedioafinidad)
        ArchivoAfinidad=open("C:/Users/User/Desktop/Fuentes-Ariel_prueba3/Mi_afinidad.txt","a") #se habre el archivo para porder ingresar los nuevos datos, y para eso se utiliza el "a" para que no elimine lo anterior y los escriba despues de lo escrito anterior
        ArchivoAfinidad.write(NombreAmigo+espacio+ApellidoAmigo+espacio+caracteresencomunstr+espacio+"de"+espacio+NumeroDeCaracteresEnUsuariostr+espacio+"similitudes posibles,"+espacio+promedioafinidadstr+"%"+"\n") #aqui se escribe en el archivo la informacion obtenida y de la forma que no se escriba en cima
        ArchivoAfinidad.close() #se cierra el archivo
    variables.close() #se cierra el archivo que le los nombres de los amigos
    print("*****************************************************************************************************************************")
    print("")
    print("          Hola",NombreUsuario,ApellidoUsuario,"Los datos calculados se han guardado correctamente en el archivo 'Mi_afinidad.txt'")
    print("                                                    Gracias por su tiempo")
    print("")
    print("*****************************************************************************************************************************")  
    print("                                                                                                                  By Ariel F.")
