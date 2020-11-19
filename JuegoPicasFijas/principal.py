from random import randint

#Funcion para validar el numero a encontrar   
def validar_numero(numero):
    if len(numero) == 1:
        return True
    else:
        if numero[0] in numero[1:]:
            return False
        else: 
            return validar_numero(numero[1:])

#Inicializando variables
intentos=0
s=True
picas=0
fijas=0
numint=0

#Menu del juego 
print("\nPicas y fijas\n")
print("Ingrese su nombre:")
name = input()
print("\nCon cuantas cifras quiere jugar:  \n")
print("3 cifras \n")
print("4 cifras \n")
print("5 cifras \n")

#Mensaje para cuando se ingresa un valor invalido
def default ():
    print ("\nIngrese una opcion valida\n")

#Opciones de juego
while True:
    a=int(input("Cifras: "))
    if a==3:
        intentos=10
        break
    elif a==4:
        intentos=12
        break
    elif a==5:
        intentos=15   
        break
    default()

#Genera el numero aleatorio a encontrar
while s:   
    numero=[]      
    for i in range(0,a):
        numero.append(randint(0,9))
    if validar_numero(numero):
        s=False

#Logica de juego
while intentos>0:
    ganador=False
    numint=intentos
    #print(numero)
    print("\nIntentos: "+str(intentos))
    intentos-=1
    
    #Ingresa numero
    while True:
        intento=[int(x) for x in input("Ingrese un número de "+ str(a) + " digitos: ")]
        if len(intento) == a:
            break
        else:
            default()
    #Valida las picas y fijas
    for i,valor in enumerate(numero):
        for j,valor2 in enumerate(intento):
            if i==j and valor==valor2:
                fijas+=1 
            if i != j and valor==valor2:
                picas+=1
    print("fijas: "+ str(fijas))
    print("picas: "+ str(picas)+"\n")

    #Escribe los datos de cada intento en el archivo
    archivo = open("puntaje.txt", "a" )
    if fijas==len(numero):
        ganador=True
    archivo.write(name+","+ str(a)+","+ str(fijas)+","+str(picas)+","+str(numint)+","+str(intento)+","+str(ganador)+"\n")
    archivo.close()
    numint=numint-1

    #Condicional cuando gana
    if fijas==len(numero):
        ganador=True
        print("Enhorabuena")
        break

    #Conidicional cuando pierde
    if intentos == 0:
        print("Enhoramala")
        
    picas=0
    fijas=0


#Guarda los mejores partidas
archivo = open("puntaje.txt", "r")
ganador= []
for linea in archivo.readlines():
    elementos =[str(x) for x in linea.split(",")]
    if (elementos[1] == elementos[2]):
        ganador.append(int(elementos[4])) 
        #print(ganador)
archivo.close()

#Muestra el mejor jugador
archivo = open("puntaje.txt", "r")
for line in archivo.readlines():
    elemento =[str(y) for y in line.split(",")]
    if (((elemento[1]== elemento[2]) & (elemento[4]== str(max(ganador))))):
        print("\n\t .: Ganador :.\n")     
        print("El mejor jugador es "+elemento[0]+" en "+elemento[1]+" cifras, con "+elemento[4]+" intentos restantes.")     
archivo.close()





