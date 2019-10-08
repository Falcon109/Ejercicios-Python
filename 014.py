x=int(input("ingrese un numero:"))
while x<0:
    x=int(input("ingrese un numero POSITIVO:"))
for contador in range(0,x+1,2):
    if contador%2==0:
        print(contador)
print()