import os #esta libreria la importe para poder utilizar una funcion de windows la cual es limpiar pantalla
import time #esta libreria la utilize para que el programa se durmiera o pausara por unos segundos, para darle un toque mas estetico
def informacion_personal(Primernombre,Segundonombre,Primerapellido,Segundoapellido,Edad,Rut,Telefono,Saldo):#esta funcion se utiliza para ver la informacion del usuario
    print("*******************************************************")
    punto="."#esto sirve a la hora de escribir el rut tenga los puntos de separacion
    print()
    print("Nombre completo:",Primernombre.upper(),Segundonombre.upper(),Primerapellido.upper(),Segundoapellido.upper())#aqui utilize la caracteristica .upper() para que todas las letras se vieran de igual manera
    print("Edad:",Edad)
    print("Rut:",Rut[0:2]+punto+Rut[2:5]+punto+Rut[5:len(Rut)])#aqui utilize la caracteristica de inprimir una parte de la variable y concetarla con otra varible en teste caso un punto "."
    print("Telefono: +"+Telefono)
    print("Sueldo:",Saldo)
    print()
    print("*******************************************************")
def carga():#esta funcion sirve mas de forma estetica, fu funcion es simular una pantalla de carga
    punto="."
    carga=1
    os.system("cls")
    for i in range(0,2):#este for es para que se repita dos veces
        while carga!=4:
            os.system("cls")#limpiar pantalla
            print("*******************************************************")
            print()
            print("                    cargando"+(punto*carga))
            print()
            print("*******************************************************")
            time.sleep(1)#espera 1 segundo o la cantidad de segundos que este dentro del parentesis
            carga=carga+1#suma 1 asta que sea 4
        carga=1#carga vuelve a tomar el valor de 1 en ves de 4
    os.system("cls")#limpiar pantalla
def correcion():#esta funcio espara preguntarle al usuario si tiene algun error la informacion ingresada
    print("*******************************************************")
    print()
    print("             ¿Es Correcta la informacion?")
    print()
    print("*******************************************************")
def credito(Primernombre,Segundonombre,Primerapellido,Segundoapellido,Edad,Rut,Telefono,Saldo,Monto,Meses,MontoTotal,MontoMensual):#esta funcion es para informar al usuario los datos ingresados y calculados para el credito, tambien utilizo caracteristica que utilize en "informacion_personal"
    os.system("cls")
    punto="."
    print("**********************************************************************")
    print()#estos print son para dejar un espacio entre la decoracion y la informacion
    print("Nombre completo:",Primernombre.upper(),Segundonombre.upper(),Primerapellido.upper(),Segundoapellido.upper())
    print("Edad:",Edad)
    print("Rut:",Rut[0:2]+punto+Rut[2:5]+punto+Rut[5:len(Rut)])
    print("Telefono: +"+Telefono)
    print("Sueldo:",Saldo)
    print("Monto solicitado:",Monto)
    print("Meses en que pagara el credito:",Meses)
    print("La taza de interes (mensual) es de 1,89% y al año es de 22,68%")#aqui lo coloque como texto ya que esos valores no cambiarian
    print("El Monto Total es de:",MontoTotal)
    print("El Monto mesual es de:",MontoMensual)
    print()
    print("**********************************************************************")
def credito2(Primernombre,Segundonombre,Primerapellido,Segundoapellido,Edad,Rut,Telefono,Saldo,Montototalantiguo,Mesessinpagar,Montoantiguo,Monto,Meses,MontoTotal,MontoMensual):#es pacerido al anterio pero esta funcion es utilizada para unado tiene un credito activo
    os.system("cls")
    punto="."
    print("**********************************************************************")
    print()  
    print("Nombre completo:",Primernombre.upper(),Segundonombre.upper(),Primerapellido.upper(),Segundoapellido.upper())
    print("Edad:",Edad)
    print("Rut:",Rut[0:2]+punto+Rut[2:5]+punto+Rut[5:len(Rut)])
    print("Telefono: +"+Telefono)
    print("Sueldo:",Saldo)
    print()
    print("**********************************************************************")
    print()
    print("Monto del credito aun activo:",Montototalantiguo)
    print("Meses sin pagar:",Mesessinpagar)
    print("Monto mensual del credito antiguo:",Montoantiguo)
    print()
    print("**********************************************************************")
    print()        
    print("Monto solicitado:",Monto)
    print("Meses en que pagara el credito:",Meses)
    print("La taza de interes (mensual) es de 1,89% y al año es de 22,68%")
    print("El Monto Total es de:",MontoTotal)
    print("El Monto mesual es de:",MontoMensual)
    print()
    print("**********************************************************************")
def informacio_credito(Monto,Meses):
    print("*****************************************************")
    print()
    print("El monto del credito es:",Monto)
    print("Los meses en que desea pagar el credito son:",Meses)
    print()
    print("*****************************************************")
os.system("cls")
print("*******************************************************")
print()
print("Bienvenido al servicio de contratacion de creditos ICI")
print()
print("*******************************************************")
time.sleep(8)
print()
print("POR FAVOR NO COLOCAR ESPACIOS AL MOMENTO DE INGRESAR DATOS")
time.sleep(5)
os.system("cls")
print("**********************************************************************")
print()
print("Para poder contratar un credito, es necesario algunos datos personales")
print()
print("**********************************************************************")
time.sleep(8)
print()
primernombre=str(input("Ingrese su primer nombre:"))#aqui se guardara su primero nombre
segundonombre=str(input("ingrese su segundo nombre:"))#segundo nombre
primerapellido=str(input("Ingrese su primer apellido:"))#apellido paterno
segundoapellido=str(input("ingrese su segundo apellido:"))#apellido materno
edad=int(input("ingrese su edad:"))#la edad
rut=input("ingrese su rut (como aparece en el ejemplo: 123456789-0):")#el rut no lo defini como un entero o un flotante para hasi poder trabajar mejor con el
telefono=input("ingress su numero telefonico (como en este ejemplo: ***123456789):+")#el medio de contacto es algo muy importante en tramites como es este, lo defini como entero porque no hay puntos y el "+" lo deje como parte de la pregunta y a la ves parte de la respuesta
saldo=int(input("ingrese su salario mensual (solo numeros, sin puntos):"))#aqui es neserario ingresarlo sin puntos porque se puede tomar como un decimal
carga()
informacion_personal(primernombre,segundonombre,primerapellido,segundoapellido,edad,rut,telefono,saldo)
correcion()
#llamo a 3 funciones, una para algo mas estetico y las otras 2 son para que el usuario revici si la informacion que ingreso es correcta y poder cambiarla
respuestacorrecion=int(input("Es correcto = 1 / Es Incorrecto = 2. Su respuesta es:"))#aqui pregunto si la informacion ingresada es conreta
while respuestacorrecion!=1 and respuestacorrecion!=2:#este while repetira la pregunta asta que colouqe las opciones dadas
    respuestacorrecion=int(input("Es correcto = 1 / Es Incorrecto = 2. Su respuesta es:"))
while respuestacorrecion==2:#aqui se vuelven a pedir los datos para que el usuario pueda corregir los errores que ingreso hasta que el usuario diga (escriba) que esta bien los datos ingresados
    os.system("cls")
    print("**********************************************************************")
    print()
    primernombre=str(input("Ingrese su primer nombre:"))
    segundonombre=str(input("ingrese su segundo nombre:"))
    primerapellido=str(input("Ingrese su primer apellido:"))
    segundoapellido=str(input("ingrese su segundo apellido:"))
    edad=int(input("ingrese su edad:"))
    rut=input("ingrese su rut (como aparece en el ejemplo: 123456789-0):")
    telefono=input("ingress su numero telefonico (como en este ejemplo: ***123456789):+")
    saldo=int(input("ingrese su salario mensual (solo numeros, sin puntos):"))
    carga()
    informacion_personal(primernombre,segundonombre,primerapellido,segundoapellido,edad,rut,telefono,saldo)
    correcion()
    respuestacorrecion=int(input("Es correcto = 1 / Es Incorrecto = 2. Su respuesta es:"))
    while respuestacorrecion!=1 and respuestacorrecion!=2:
        respuestacorrecion=int(input("Es correcto = 1 / Es Incorrecto = 2. Su respuesta es:"))
os.system("cls")
print("************************************************************************************")
print()
print("        Ahora necesitamos saber si Usted tiene algun otro credito activo")
print()
print("************************************************************************************")
print()
print("                         ¿Tiene algun Credito activo?")
print()
print("************************************************************************************")
#una de la condiciones que teniamos que tener era que si tenia un credito anteriormente
#aqui es una del las diviciones que tiene el programa
respuestacreditoactivo=int(input("Si tengo un credito activo (1) / No tengo un credito activo (2). Su resuesta es:"))#aqui el usuario tiene que responder si tiene un credrito activo
while respuestacreditoactivo!=1 and respuestacreditoactivo!=2:#aqui se repetira hasta que el usuario responda con las opciones que se le dan
    os.system("cls")
    print("************************************************************************************")
    print()
    print("        Ahora necesitamos saber si Usted tiene algun otro credito activo")
    print()
    print("************************************************************************************")
    print()
    print("                         ¿Tiene algun Credito activo?")
    print()
    print("************************************************************************************")
    respuestacreditoactivo=int(input("Si tengo un credito activo (1) / No tengo un credito activo (2). Su resuesta es:"))
if respuestacreditoactivo==1:#aqui sigue la ruta de que el usuario tiene una credito activo
    os.system("cls")
    print("***********************************************")
    print()
    print("  Muy bien, ahora necesitamos algunos datos")
    print()
    print("***********************************************")
    time.sleep(4)
    os.system("cls")
    print("***********************************************************")
    montototalantiguo=int(input("cuanto es el Monto que pidió:"))
    mesesdecreditoantiguo=int(input("De cuantos meses es el credito:"))
    mesespagados=int(input("Cuantos meses estan pagados:"))
    montoantiguo=int(input("Cuanto paga:"))
    while mesespagados>mesesdecreditoantiguo:#aqui esto se repetira si es que la cantidad de meses pagados es mayor a la del credito
        os.system("cls")
        print("***********************************************************")
        print("    ¡INGRESO DE VALOR INCORRECTO, INGRESE NUEVAMENTE!")
        montototalantiguo=int(input("cuanto es el Monto que pidió:"))
        mesesdecreditoantiguo=int(input("De cuantos meses es el credito:"))
        mesespagados=int(input("Cuantos meses estan pagados:"))
    mesessinpagar=mesesdecreditoantiguo-mesespagados#aqui se calculas los meses sin pagar
    os.system("cls")
    #aqui se continua con la contratacion del nuevo credito
    print("*****************************************************************")
    print()
    print("Muy bien, ahora podemos empezar con la contratacion del creditos")
    print()
    print("*****************************************************************")
    time.sleep(5)
    os.system("cls")
    print("*****************************************************************")
    print()
    print("        Ahora se necesita que complete otros datos")
    print()
    print("*****************************************************************")
    time.sleep(4)
    os.system("cls")
    print("*****************************************************************")
    monto=int(input("Ingrese el Monoto que desea solicitar (sin puntos o comas):"))
    if monto<=0:#si el monto es menor que 0 volvera a preguntar
        while monto<=0:
            monto=int(input("Ingrese el Monoto que desea solicitar (sin puntos o comas):"))
    meses=int(input("En cuantos Meses desea que sea el plaso (12-60):"))#aqui el usuario tendra que escoger en cuantos meses decea que sea el credito
    while meses<12 or meses>60:#aqui se repetira hasta que el usuario coloque un numero entre 12 a 60
        meses=int(input("En cuantos Meses desea que sea el plaso (12-60):"))
    os.system("cls")
    informacio_credito(monto,meses)
    correcion()
    respuestacorrecioncredito=int(input("Es corecto (1) / es incorrecto (2). su respuesta es:"))
    while respuestacorrecioncredito!=1 and respuestacorrecioncredito!=2:
        respuestacorrecioncredito=int(input("Es corecto (1) / es incorrecto (2). su respuesta es:"))
    while respuestacorrecioncredito==2:#aqui se confiarma si la informacion para el credito es correcta
        os.system("cls")
        print("*****************************************************************")
        monto=int(input("Ingrese el Monoto que desea solicitar (sin puntos o comas):"))
        if monto<=0:
            while monto<=0:
                monto=int(input("Ingrese el Monoto que desea solicitar (sin puntos o comas):"))
        meses=int(input("En cuantos Meses desea que sea el plaso (12-60):"))
        while meses<12 or meses>60:
            meses=int(input("En cuantos Meses desea que sea el plaso (12-60):"))
        os.system("cls")
        informacio_credito(monto,meses)
        correcion()
        respuestacorrecioncredito=int(input("Es corecto (1) / es incorrecto (2). su respuesta es:"))
        while respuestacorrecioncredito!=1 and respuestacorrecioncredito!=2:
            respuestacorrecioncredito=int(input("Es corecto (1) / es incorrecto (2). su respuesta es:"))
    os.system("cls")
    carga()
    #aqui se ven las variables para calcular el nuevo credito
    montoTotal=((monto*(100+(1.89*meses)))/100)#aqui se calcula la cantidad del monto que pidio mas la tasa de interes
    montoMensual=(montoTotal/meses)#aqui se calcula lo que tendra que pagar el usuario por cada mes
    montodeambaspartes=montoMensual+montoantiguo#aqui se suman el nuevo monto mesual mas el anterio para saber si el usuario esta pagando mas de lo que gana
    if montodeambaspartes<saldo:#si la suma de los montos(antiguo y nuevo) es menor que el saldo inprimira la informacion
        os.system("cls")
        credito2(primernombre,segundonombre,primerapellido,segundoapellido,edad,rut,telefono,saldo,montototalantiguo,mesessinpagar,montoantiguo,monto,meses,montoTotal,montoMensual)
    else:
        #si la suma de montos es mayor que el saldo se le pregunta al usuario si quiere continuar con el tramite a responsabilidad del usuario
        os.system("cls")
        print("**************************************************************")
        print()
        print("    Su saldo es menor que la cuota mensual del credito")
        print()
        print("**************************************************************")
        respuestaasaldomenor=int(input("¿desea continuar de todas formas? (si = 1 / no = 2). su respuesta es:"))
        while respuestaasaldomenor!=1 and respuestaasaldomenor!=2:#seguira preguntando hasta que responda con las opciones dadas
            os.system("cls")
            print("**************************************************************")
            print()
            print("    Su saldo es menor que la cuota mensual del credito")
            print()
            print("**************************************************************")
            respuestaasaldomenor=int(input("¿desea continuar de todas formas? (si = 1 / no = 2). su respuesta es:"))
        if respuestaasaldomenor==1:#aqui el usuario decidio continuar con el credito
            credito2(primernombre,segundonombre,primerapellido,segundoapellido,edad,rut,telefono,saldo,montototalantiguo,mesessinpagar,montoantiguo,monto,meses,montoTotal,montoMensual)    
            print()
            print("Gracias por elegir servicio de contratacion de creditos ICI")
            print()
            print("************************************************************")
            print("                                            by Ariel Fuentes")
        else:#si decide no continuar se ternima
            os.system("cls")
            print("************************************************************")
            print()
            print("Gracias por elegir servicio de contratacion de creditos ICI")
            print()
            print("************************************************************")
            print("                                            by Ariel Fuentes")
else:#esta es la ruta cuando no tiene un credito ya activo
    os.system("cls")
    print("*****************************************************************")
    print()
    print("Muy bien, ahora podemos empezar con la contratacion del creditos")
    print()
    print("*****************************************************************")
    time.sleep(5)
    os.system("cls")
    print("*****************************************************************")
    print()
    print("        Ahora se necesita que complete otros datos")
    print()
    print("*****************************************************************")
    time.sleep(4)
    os.system("cls")
    print("*****************************************************************")
    monto=int(input("Ingrese el Monoto que desea solicitar (sin puntos o comas):"))
    while monto<=-1:
            monto=int(input("Ingrese el Monoto que desea solicitar (sin puntos o comas):"))
    meses=int(input("En cuantos Meses desea que sea el plaso (12-60):"))
    while meses<12 or meses>60:
        meses=int(input("En cuantos Meses desea que sea el plaso (12-60):"))
    os.system("cls")
    informacio_credito(monto,meses)
    correcion()
    respuestacorrecioncredito=int(input("Es corecto (1) / es incorrecto (2). su respuesta es:"))
    while respuestacorrecioncredito!=1 and respuestacorrecioncredito!=2:
        respuestacorrecioncredito=int(input("Es corecto (1) / es incorrecto (2). su respuesta es:"))
    while respuestacorrecioncredito==2:#aqui se confiarma si la informacion para el credito es correcta
        os.system("cls")
        print("*****************************************************************")
        monto=int(input("Ingrese el Monoto que desea solicitar (sin puntos o comas):"))
        if monto<=0:
            while monto<=0:
             monto=int(input("Ingrese el Monoto que desea solicitar (sin puntos o comas):"))
        meses=int(input("En cuantos Meses desea que sea el plaso (12-60):"))
        while meses<12 or meses>60:
            meses=int(input("En cuantos Meses desea que sea el plaso (12-60):"))
        os.system("cls")
        informacio_credito(monto,meses)
        correcion
        respuestacorrecioncredito=int(input("Es corecto (1) / es incorrecto (2). su respuesta es:"))
        while respuestacorrecioncredito!=1 and respuestacorrecioncredito!=2:
            respuestacorrecioncredito=int(input("Es corecto (1) / es incorrecto (2). su respuesta es:"))
    os.system("cls")
    carga()
    tasainteres=1.89
    montoTotal=((monto*(100+(tasainteres*meses)))/100)
    montoMensual=(montoTotal/meses)
    if montoMensual<saldo:#aqui se revisa si su saldo es suficiente para poder pagar el monto mensual
        #esta ruta es la de que puede pagar el credito mensual sin problemas
        os.system("cls")
        credito(primernombre,segundonombre,primerapellido,segundoapellido,edad,rut,telefono,saldo,monto,meses,montoTotal,montoMensual)
    else:
        #aqui se ve nuevamente la situacion de que su saldo no puede pagar el credito
        os.system("cls")
        print("**************************************************************")
        print()
        print("    Su saldo es menor que la cuota mensual del credito")
        print()
        print("**************************************************************")
        respuestaasaldomenor=int(input("¿desea continuar de todas formas? (si = 1 / no = 2). su respuesta es:"))
        while respuestaasaldomenor!=1 and respuestaasaldomenor!=2:#se repetira hasta que ingrese la opciones dadas
            os.system("cls")
            print("**************************************************************")
            print()
            print("    Su saldo es menor que la cuota mensual del credito")
            print()
            print("**************************************************************")
            respuestaasaldomenor=int(input("¿desea continuar de todas formas? (si = 1 / no = 2). su respuesta es:"))
        if respuestaasaldomenor==1:
            #en el caso continuar
            credito(primernombre,segundonombre,primerapellido,segundoapellido,edad,rut,telefono,saldo,monto,meses,montoTotal,montoMensual)
            print()
            print("Gracias por elegir servicio de contratacion de creditos ICI")
            print()
            print("************************************************************")
            print("                                            by Ariel Fuentes")
        else:
            #en el caso de no querer continuar
            os.system("cls")
            print("************************************************************")
            print()
            print("Gracias por elegir servicio de contratacion de creditos ICI")
            print()
            print("************************************************************")
            print("                                            by Ariel Fuentes")