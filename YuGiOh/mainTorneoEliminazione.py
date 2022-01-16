from player import *
from utils import *

class CreazioeTorneo():
    def __init__(self):
        print("GENERATORE DI TORNEI (i partecipanti deve essere una potenza di 2 (2, 4, 8, 16, ...)")
        nrGiocatori = int(input("Quanti giocatori partecipano? "))
        while(is_power_of_two(nrGiocatori) == False):
            print("Il valore non è valido")
            nrGiocatori = int(input("Quanti giocatori partecipano? "))
        print()
        listPlayer = []
        listOrderTorneo = []
        for i in range(0, nrGiocatori, 1):
            name = input("Inserisci il nome del " + str(i+1) + " giocatore: ")
            p = Player(name)
            listPlayer.append(p)
        
        print()
        print("I giocatori partecipanti sono:")
        for i in range(0, nrGiocatori, 1):
            print(listPlayer[i].name)
        
        for i in range(0, nrGiocatori, 1):
            dice = (roll(nrGiocatori)-1)
            p = listPlayer.pop(dice)
            listOrderTorneo.append(p)
            nrGiocatori -=1
        
        print()
        print("Ordine per il torneo:")
        for i in range(0, len(listOrderTorneo), 1):
            print(str(i+1) + "--> " + listOrderTorneo[i].name)
        
        print()
        print("Con i dati generati puoi creare il tabellone.")

def is_power_of_two(number : int) -> bool:
    while number != 1:
        if number % 2:
            return False
        number /= 2
    return True    
            

cr = CreazioeTorneo()