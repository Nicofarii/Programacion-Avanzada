from random import randint


        
def validar_numero(numero):
    if len(numero) == 1:
        return True
    else:
        if numero[0] in numero[1:]:
            return False
        else: 
            return validar_numero(numero[1:])

intentos=10
print("\n\tPicas y fijas\n")
print("\nCuántas cifras quieres descubrir: \n\n")
print("3 cifras, " +str(intentos) +" intentos para ganar \n")
print("4 cifras, " + str(intentos+2)+" intentos para ganar \n")
print("5 cifras, " + str(intentos+5)+ " intentos para ganar \n")
a=int(input("Cifras: "))

s=True
picas=0
fijas=0

if a==3:
    intentos=10
elif a==4:
    intentos=12
elif a==5:
    intentos=15   
while s:   
    numero=[]      
    for i in range(0,a):
        numero.append(randint(0,9))
    if validar_numero(numero):
        s=False


#print(numero)
while intentos>0:
    print("\nIntentos: "+str(intentos))
    intentos-=1
    intento=[int(x) for x in input("Ingrese un número de "+ str(a) + " digitos: ")]

    for i,valor in enumerate(numero):
        for j,valor2 in enumerate(intento):
            if i==j and valor==valor2:
                fijas+=1 
            if i != j and valor==valor2:
                picas+=1
    print("fijas: "+ str(fijas))
    print("picas: "+ str(picas)+"\n")
    if fijas==len(numero):
        break
    picas=0
    fijas=0



#f=open("rankings.txt","w")
