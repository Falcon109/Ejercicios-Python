OwO = []
for i in range (0,10):
    numer=int(input("ingrese un numero:"))
    OwO.append(numer)
aviso=0
for i in range(0,10):  
    elemento=OwO[i]
    for j in range(0,10):
        if ((OwO[j])==elemento) and (i)!=(j):
            aviso=1
        else:
            aviso=0
    if aviso==0:
        print(elemento)
    else:
        ()