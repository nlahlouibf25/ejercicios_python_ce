import random

numero = random.randint(1, 10)
intentos = 0

print("Adivina el numero del 1 al 10")

while intentos < 3:
    intento = int(input("Intento: "))
    intentos += 1
    
    if intento == numero:
        print("Lo has acertado")
        break
    elif intento < numero:
        print("Mas alto")
    else:
        print("Mas bajo")
    
    if intentos < 3:
        print(f"Te quedan {3 - intentos} intentos")

if intento != numero:
    print(f"Has perdido, era el {numero}")