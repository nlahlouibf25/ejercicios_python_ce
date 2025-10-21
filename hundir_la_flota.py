import random
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_tablero():
    tablero = []
    for i in range(7):
        fila = []
        for j in range(7):
            fila.append("~")
        tablero.append(fila)
    return tablero

def mostrar_tablero(tablero, ocultar_barcos=False):
    print("\n    1   2   3   4   5   6   7")
    print("  +---+---+---+---+---+---+---+")
    letras = "ABCDEFG"
    for i in range(7):
        print(letras[i] + " |", end="")
        for j in range(7):
            if ocultar_barcos and tablero[i][j] == "B":
                print(" ~ |", end="")
            else:
                print(" " + tablero[i][j] + " |", end="")
        print("\n  +---+---+---+---+---+---+---+")
    print()

def colocar_barco(tablero, tamaño):
    while True:
        orientacion = random.choice(["H", "V"])
        if orientacion == "H":
            fila = random.randint(0, 6)
            col = random.randint(0, 7 - tamaño)
            valido = True
            for i in range(tamaño):
                if tablero[fila][col + i] != "~":
                    valido = False
                    break
            if valido:
                for i in range(tamaño):
                    tablero[fila][col + i] = "B"
                return
        else:
            fila = random.randint(0, 7 - tamaño)
            col = random.randint(0, 6)
            valido = True
            for i in range(tamaño):
                if tablero[fila + i][col] != "~":
                    valido = False
                    break
            if valido:
                for i in range(tamaño):
                    tablero[fila + i][col] = "B"
                return

def colocar_barcos(tablero):
    barcos = [4, 3, 3, 2]
    for tamaño in barcos:
        colocar_barco(tablero, tamaño)

def obtener_coordenadas(jugador):
    while True:
        try:
            entrada = input(f"Jugador {jugador}, donde disparas (ej: A3): ").upper().strip()
            if len(entrada) < 2:
                print("Formato incorrecto")
                continue
            fila = ord(entrada[0]) - ord('A')
            col = int(entrada[1:]) - 1
            if fila < 0 or fila > 6 or col < 0 or col > 6:
                print("Fuera del tablero")
                continue
            return fila, col
        except:
            print("Pon algo como A3 o B5")

def disparar(tablero, fila, col):
    if tablero[fila][col] == "B":
        tablero[fila][col] = "X"
        return "tocado"
    elif tablero[fila][col] == "~":
        tablero[fila][col] = "O"
        return "agua"
    else:
        return "repetido"

def contar_barcos(tablero):
    contador = 0
    for fila in tablero:
        for casilla in fila:
            if casilla == "B":
                contador += 1
    return contador

def jugar():
    print("HUNDIR LA FLOTA")
    print("-" * 40)
    print("\nInstrucciones:")
    print("- Tablero 7x7 (filas A-G, columnas 1-7)")
    print("- Cada jugador tiene 4 barcos:")
    print("  * 1 portaaviones (4 casillas)")
    print("  * 2 destructores (3 casillas cada uno)")
    print("  * 1 lancha (2 casillas)")
    print("- Dispara con formato letra+numero: A3, B5...")
    print("- Simbolos: ~ agua | X tocado | O fallo | B barco")
    print("- Gana quien hunda todos los barcos primero")
    
    input("\nEnter para empezar...")
    
    tablero_j1 = crear_tablero()
    tablero_j2 = crear_tablero()
    
    colocar_barcos(tablero_j1)
    colocar_barcos(tablero_j2)
    
    print("\nBarcos colocados aleatoriamente")
    
    input("\nJugador 1 mira tu tablero (Jugador 2 no mires)...")
    print("\nTu tablero:")
    mostrar_tablero(tablero_j1)
    input("Enter cuando estes listo...")
    
    limpiar_pantalla()
    
    input("\nJugador 2 mira tu tablero (Jugador 1 no mires)...")
    print("\nTu tablero:")
    mostrar_tablero(tablero_j2)
    input("Enter cuando estes listo...")
    
    turno = 1
    
    while True:
        limpiar_pantalla()
        
        if turno == 1:
            print("\nTURNO JUGADOR 1")
            print("-" * 40)
            print("Tablero enemigo:")
            mostrar_tablero(tablero_j2, ocultar_barcos=True)
            
            fila, col = obtener_coordenadas(1)
            resultado = disparar(tablero_j2, fila, col)
            
            if resultado == "tocado":
                print("\nTocado")
            elif resultado == "agua":
                print("\nAgua")
            else:
                print("\nYa disparaste ahi")
                continue
            
            if contar_barcos(tablero_j2) == 0:
                print("\nGana Jugador 1")
                break
            
            input("\nEnter para cambiar turno...")
            turno = 2
            
        else:
            print("\nTURNO JUGADOR 2")
            print("-" * 40)
            print("Tablero enemigo:")
            mostrar_tablero(tablero_j1, ocultar_barcos=True)
            
            fila, col = obtener_coordenadas(2)
            resultado = disparar(tablero_j1, fila, col)
            
            if resultado == "tocado":
                print("\nTocado")
            elif resultado == "agua":
                print("\nAgua")
            else:
                print("\nYa disparaste ahi")
                continue
            
            if contar_barcos(tablero_j1) == 0:
                print("\nGana Jugador 2")
                break
            
            input("\nEnter para cambiar turno...")
            turno = 1

jugar()