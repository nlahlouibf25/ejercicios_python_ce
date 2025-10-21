import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_tablero(tablero):
    print("\n")
    for i in range(3):
        print(" " + tablero[i*3] + " | " + tablero[i*3+1] + " | " + tablero[i*3+2])
        if i < 2:
            print("-----------")
    print("\n")

def verificar_ganador(tablero, simbolo):
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in combinaciones:
        if tablero[combo[0]] == simbolo and tablero[combo[1]] == simbolo and tablero[combo[2]] == simbolo:
            return True
    return False

def hay_empate(tablero):
    for casilla in tablero:
        if casilla != "X" and casilla != "O":
            return False
    return True

def movimiento_jugador(tablero, jugador):
    while True:
        try:
            posicion = int(input(f"Jugador {jugador}, donde pones tu ficha? (1-9): "))
            if posicion < 1 or posicion > 9:
                print("Tiene que ser entre 1 y 9 tio!")
                continue
            if tablero[posicion-1] == "X" or tablero[posicion-1] == "O":
                print("Ahi ya hay una ficha, elige otra")
                continue
            return posicion - 1
        except:
            print("Pon un numero porfa")

def jugar():
    tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    print("Vamos a jugar al tres en raya!")
    print("Jugador 1 eres las X")
    print("Jugador 2 eres las O")
    input("\nPulsa ENTER para empezar...")
    
    turno = 1
    
    while True:
        limpiar_pantalla()
        mostrar_tablero(tablero)
        
        if turno == 1:
            simbolo = "X"
            jugador = "1 (X)"
        else:
            simbolo = "O"
            jugador = "2 (O)"
        
        pos = movimiento_jugador(tablero, jugador)
        tablero[pos] = simbolo
        
        limpiar_pantalla()
        mostrar_tablero(tablero)
        
        if verificar_ganador(tablero, simbolo):
            print(f"Ha ganado el Jugador {turno}!!")
            break
        
        if hay_empate(tablero):
            print("Vaya ha quedado en empate")
            break
        
        if turno == 1:
            turno = 2
        else:
            turno = 1

jugar()