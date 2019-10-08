a=int(input("ingrese a:"))
b=int(input("ingrese b:"))
c=int(input("ingrese c:"))
raiz=(((b)**2-(4*a*c)))**0.5
if raiz>=0:
    xp=((-b+raiz)/(2*a))
    xn=((-b-raiz)/(2*a))
    print("los resultados son:", xp,xn)
else:
    print ("No se puede determinar")