import random

def escullNivell():
    opcioValida = False
    while opcioValida != True:
        nivell = int(input('Introdueix nivell:\n 1. Baix (1vida) \n 2. Mig (2vides) \n 3. Alt (3vides)\n'))
        if nivell >= 1 and nivell <= 3:
            opcioValida = True
        else:
            print('Opcio incorrecta')
        return nivell

def comparaResultat(opUser, opRival, puntUser, puntRival):
    if opUser == 0:
        if opRival == 0:
            print('El rival ha tret, pedra. Resultat: Empatat')
        elif opRival == 1:
            print('El rival ha tret, paper. Resultat: guanya PC')
            puntRival += 1
        else:
            print('El rival ha tret, Tisores. Resultat: guanya User')
            puntUser += 1
    elif opUser == 1:
        if opRival == 0:
            print('El rival ha tret, pedra. Resultat: guanyaUser')
            puntUser += 1
        elif opRival == 1:
            print('El rival ha tret, paper. Resultat: empat')
        else:
            print('El rival ha tret, Tisores. Resultat: guanya PC')
            puntRival += 1
    else:
        if opRival == 0:
            print('El rival ha tret, pedra. Resultat: guanyaPC')
            puntRival += 1
        elif opRival == 1:
            print('El rival ha tret, paper. Resultat: guanyaUser')
            puntUser += 1
        else:
            print('El rival ha tret, Tisores. Resultat: Empat')
    
    print(f'El resultat es:\n User: {puntUser}\n Pc: {puntRival}')
    return puntUser, puntRival

nivell = escullNivell()
puntUser = 0
puntRival = 0

while puntUser < nivell and puntRival < nivell:
    opUser = int(input('Escull la teva elecció: \n0-Piedra \n1-Papel \n2-Tisores \n'))
    opRival = random.randint(0, 2)
    puntUser, puntRival = comparaResultat(opUser, opRival, puntUser, puntRival)

if puntUser == nivell:
    print('Joc acabat, Has guanyat!')
else:
    print('Joc acabat, Has perdut!')