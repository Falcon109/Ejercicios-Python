def perimetro(R):
    perim=(2*3.14*R)
    print("El perimetro es:",perim)

def area(R):
    are=(3.14*(R**2))
    print ("El area es:",are)

radio=int(input("Ingrese el radio:"))
perimetro(radio)
area(radio)