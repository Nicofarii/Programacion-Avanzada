from random import randint

nivel = int(input("Ingrese la cantidad de cifras con las que quiere jugar (3,4 o 5 cifras): "))
k1 = randint(0,9)
k2 = randint(0,9)
k3 = randint(0,9)
k4 = randint(0,9)
if nivel == 3:
    while (k1 == k2) or (k1 == k3) or (k2 == k3):
        k1 = randint(0,9)
        k2 = randint(0,9)
        k3 = randint(0,9)

    print(k1,k2,k3)
    for i in range(15):
        lista = [int(x) for x in input("Ingrese el numero de 3 cifras: ")]

        if (lista[0] == k1) and (lista[1] == k2) and (lista[2] == k3):
            print(" Picas || fijas " + "\n" + "   3   ||" + "   3   " + "\n" + "Ganaste el juego")
            break        
        elif (((lista[0] == k1) and (lista[1] == k2)) or ((lista[0] == k1) and (lista[2] == k3)) or ((lista[1] == k2) and (lista[2] == k3))):
            print(" Picas || fijas " + "\n" + "   2   ||" + "   2   ")
        elif (lista[0] == k1):
            if (lista[1] == k3 and lista[2] == k2):
                print(" Picas || fijas " + "\n" + "   3   ||" + "   1   ")
            elif (lista[1] == k3 or lista[2] == k2):
                print(" Picas || fijas " + "\n" + "   2   ||" + "   1   ")
            else:
                print(" Picas || fijas " + "\n" + "   1   ||" + "   1   ")
        elif (lista[1] == k2):
            if (lista[0] == k3 and lista[2] == k1):
                print(" Picas || fijas " + "\n" + "   3   ||" + "   1   ")
            elif (lista[0] == k3 or lista[2] == k1):
                print(" Picas || fijas " + "\n" + "   2   ||" + "   1   ")
            else:
                print(" Picas || fijas " + "\n" + "   1   ||" + "   1   ")
        elif (lista[2] == k3):
            if (lista[0] == k2 and lista[1] == k1):
                print(" Picas || fijas " + "\n" + "   3   ||" + "   1   ")
            elif (lista[0] == k2 or lista[1] == k1):
                print(" Picas || fijas " + "\n" + "   2   ||" + "   1   ")
            else:
                print(" Picas || fijas " + "\n" + "   1   ||" + "   1   ")
        elif (lista[0] == k2 or lista[0] == k3):
            if (lista[1] == k1 or lista[1] == k3):
                if (lista[2] == k1 or lista[2] == k2):
                    print(" Picas || fijas " + "\n" + "   3   ||" + "   0   ")
                else:
                    print(" Picas || fijas " + "\n" + "   2   ||" + "   0   ")
            elif (lista[2] == k1 or lista[2] == k2):
                 print(" Picas || fijas " + "\n" + "   2   ||" + "   0   ")
            else:
                print(" Picas || fijas " + "\n" + "   1   ||" + "   0   ")
        elif (lista[1] == k1 or lista[1] == k3):
            if (lista[0] == k2 or lista[0] == k3):
                if (lista[2] == k1 or lista[2] == k2):
                    print(" Picas || fijas " + "\n" + "   3   ||" + "   0   ")
                else:
                    print(" Picas || fijas " + "\n" + "   2   ||" + "   0   ")
            elif (lista[2] == k1 or lista[2] == k2):
                 print(" Picas || fijas " + "\n" + "   2   ||" + "   0   ")
            else:
                print(" Picas || fijas " + "\n" + "   1   ||" + "   0   ")
        elif (lista[2] == k1 or lista[2] == k2):
            if (lista[1] == k1 or lista[1] == k3):
                if (lista[0] == k2 or lista[0] == k3):
                    print(" Picas || fijas " + "\n" + "   3   ||" + "   0   ")
                else:
                    print(" Picas || fijas " + "\n" + "   2   ||" + "   0   ")
            elif (lista[0] == k2 or lista[0] == k3):
                 print(" Picas || fijas " + "\n" + "   2   ||" + "   0   ")
            else:
                print(" Picas || fijas " + "\n" + "   1   ||" + "   0   ")
        else:
            print(" Picas || fijas " + "\n" + "   0   ||" + "   0   ")
else:
    print("Ingrese un numero entre 3 y 5")       

    
