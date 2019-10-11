def perimetro(R):
    perim=(2*3.14*R)
    return(perim)

def area(R):
    are=(3.14*(R**2))
    return(are)

radio=int(input("Ingrese el radio:"))

res1=perimetro(radio)
res2=area(radio)
print("El perimetro es:",res1)
print("El area es:",res2)