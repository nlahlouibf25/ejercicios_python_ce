import random

def cargarPalabras():
    with open('palabras.txt', 'r') as f:
        palabras = f.read().splitlines()
    return palabras

def getPalabra(lista):
    return random.choice(lista)

def transformaPalabra(palabra):
    return ['_' for _ in palabra]

def reemplazarLetra(palabraSecreta, estado, letra):
    for n in range(len(palabraSecreta)):
        if letra == palabraSecreta[n]:
            estado[n] = letra
    return estado

def compruebaEstado(estado):
    return '_' not in estado

def compruebaLetra(letra, palabraSecreta, estado, numIntentos):
    if letra in palabraSecreta:
        print('¡Has elegido una letra correcta!')
        estado = reemplazarLetra(palabraSecreta, estado, letra)
    else:
        print('La letra no está en la palabra')
        numIntentos -= 1
    return estado, numIntentos

def compruebaIntentos(numIntentos):
    if numIntentos > 0:
        print(f'Te quedan {numIntentos} intentos')
    else:
        print('¡Game Over! No te quedan intentos')

listaPalabras = cargarPalabras()
aciertoFinal = False
numIntentos = 6

palabraSecreta = getPalabra(listaPalabras)
estado = transformaPalabra(palabraSecreta)

while not aciertoFinal and numIntentos > 0:
    print(" ".join(estado))
    
    letra = input('Introduzca una letra: ')
    estado, numIntentos = compruebaLetra(letra, palabraSecreta, estado, numIntentos)

    if compruebaEstado(estado):
        print('¡Has adivinado la palabra!')
        aciertoFinal = True
    else:
        compruebaIntentos(numIntentos)
