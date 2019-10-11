def suma(N1,N2,N3):
    sumade3=N1+N2+N3
    print("la suma de los numeros son:",sumade3)
def mult(N1,N2,N3):
    sumamax=N1*N2*N3
    print("la multiplicacion es:",sumamax)
print("¿que es lo que decea hacer?")
print("Opcion 1:suma o Opcion2:multiplicacion")
res1=int(input("la Opcion es:"))
while res1!=1 and res1!=2:
    print("¿que es lo que decea hacer?")
    print("Opcion 1:suma o Opcion2:multiplicacion")
    res1=int(input("la Opcion es:"))
if res1==1:
    n1=int(input("Ingrese un nunmero:"))
    n2=int(input("Ingrese un nunmero:"))
    n3=int(input("Ingrese un nunmero:"))
    suma(n1,n2,n3)
else:
    n1=int(input("Ingrese un nunmero:"))
    n2=int(input("Ingrese un nunmero:"))
    n3=int(input("Ingrese un nunmero:"))
    mult(n1,n2,n3)