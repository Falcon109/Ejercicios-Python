nombre=str(input("ingrese su nombre:"))
edad=int(input("Ingrese su edad:"))
if edad<18 or edad>60:
    print("Lo lamento",nombre+", No se puede calcular")
else:
    peso=float(input("Ingrese su peso EN KG:"))
    altura=float(input("Ingrese su altura EN METROS:"))
    IMC=(peso/(altura)**2)

    if IMC<20:
        print("Usted esta bajo peso")
    elif IMC>25:
        print("usted esta sobre peso")
    else:
        print("Usted tiene el peso ideal")