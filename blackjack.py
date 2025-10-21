import random

def crear_baraja():
    palos = ['♠', '♥', '♦', '♣']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baraja = []
    for palo in palos:
        for valor in valores:
            baraja.append(f"{valor}{palo}")
    return baraja

def valor_carta(carta):
    valor = carta[:-1]
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    else:
        return int(valor)

def calcular_puntos(mano):
    puntos = 0
    ases = 0
    for carta in mano:
        valor = valor_carta(carta)
        puntos += valor
        if carta[:-1] == 'A':
            ases += 1
    
    while puntos > 21 and ases > 0:
        puntos -= 10
        ases -= 1
    
    return puntos

def mostrar_mano(nombre, mano, ocultar=False):
    if ocultar and len(mano) > 1:
        print(nombre + ": " + mano[0] + " [?]")
    else:
        cartas_str = ""
        for c in mano:
            cartas_str += c + " "
        print(nombre + ": " + cartas_str + "-> " + str(calcular_puntos(mano)) + " puntos")

def turno_jugador(baraja, mano_jugador):
    while True:
        print("")
        mostrar_mano("Tus cartas", mano_jugador)
        puntos = calcular_puntos(mano_jugador)
        
        if puntos > 21:
            print("Te pasaste! Perdiste")
            return False
        
        if puntos == 21:
            print("BLACKJACK!!!")
            return True
        
        decision = input("Robar carta (r) o plantarte (p)? ")
        
        if decision == 'r':
            nueva = baraja.pop()
            mano_jugador.append(nueva)
            print("Sacaste: " + nueva)
        elif decision == 'p':
            print("Ok, te quedas con " + str(puntos))
            return True

def turno_banca(baraja, mano_banca):
    print("")
    print("--- Turno de la banca ---")
    mostrar_mano("Banca", mano_banca)
    
    while calcular_puntos(mano_banca) < 17:
        nueva = baraja.pop()
        mano_banca.append(nueva)
        print("Banca saca: " + nueva)
        mostrar_mano("Banca", mano_banca)
    
    pts = calcular_puntos(mano_banca)
    
    if pts > 21:
        print("La banca se paso!")
        return False
    else:
        print("Banca se planta con " + str(pts))
        return True

def ver_ganador(mano_jugador, mano_banca, jugador_ok, banca_ok):
    print("")
    print("-------------------")
    
    if not jugador_ok:
        print("Gana la banca")
        return
    
    if not banca_ok:
        print("Ganaste!")
        return
    
    pts_j = calcular_puntos(mano_jugador)
    pts_b = calcular_puntos(mano_banca)
    
    print("Tu: " + str(pts_j) + " | Banca: " + str(pts_b))
    
    if pts_j > pts_b:
        print("Ganaste!")
    elif pts_j < pts_b:
        print("Gana la banca")
    else:
        print("Empate")

def jugar():
    print("*** BLACKJACK ***")
    print("")
    
    baraja = crear_baraja()
    random.shuffle(baraja)
    
    mano_j = [baraja.pop(), baraja.pop()]
    mano_b = [baraja.pop(), baraja.pop()]
    
    print("Repartiendo cartas...")
    mostrar_mano("Tus cartas", mano_j)
    mostrar_mano("Banca", mano_b, ocultar=True)
    
    jugador_ok = turno_jugador(baraja, mano_j)
    
    banca_ok = True
    if jugador_ok:
        banca_ok = turno_banca(baraja, mano_b)
    
    ver_ganador(mano_j, mano_b, jugador_ok, banca_ok)

jugar()