x=int(input("ingrese un numero:"))
while x<0:
    x=int(input("ingrese un numero POSITIVO:"))
for contador in range(1,x+1,2):
    print(contador)
print()