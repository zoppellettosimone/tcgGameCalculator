from player import *
from utils import *

class CreazioeGirone():
    def __init__(self):
        nrGiocatori = int(input("Quanti giocatori partecipano? "))
        print()
        listPlayer = []
        for i in range(0, nrGiocatori, 1):
            name = input("Inserisci il nome del " + str(i+1) + " giocatore: ")
            p = Player(name)
            listPlayer.append(p)
        
        print()
        print("I giocatori partecipanti sono:")
        for i in range(0, nrGiocatori, 1):
            print(listPlayer[i].name)
        
        print()
        for i in range(0, (nrGiocatori-1), 1):
            print("Turno " + str(i+1))
            print("PARTITE:")
            #DA FARE
            print()

cr = CreazioeGirone()