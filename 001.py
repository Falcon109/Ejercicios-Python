t=int(input("ingrese una variable entre 0 al 60:"))
while t>60 or t<0:
    t=int(input("ingrese una variable ENTRE 0 AL 60:"))
y=2**(2.71828**(-0.1*t))
print("el valor de y es:",y)