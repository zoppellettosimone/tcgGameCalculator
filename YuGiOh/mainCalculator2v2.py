from player import *
from utils import *

class Calculator2v2():
    def __init__(self, name1, name2):
        p1 = Player(name1.lower().capitalize())
        p2 = Player(name2.lower().capitalize())
        
        nrPartite = 0

        print('''
INIZIO PARTITE
Esempio frase da inserire: "Simone - 4500"
Le operazioni disponibili sono + e -
Creato da Simone Zoppellettos       
        ''')
        print()

        rollDice = roll(100)
        if(rollDice % 2 == 0):
            print("Il tiro del dado lo ha vinto " + p1.name)
        else:
            print("Il tiro del dado lo ha vinto " + p2.name)

        while((p1.nrVitt < 2) and (p2.nrVitt < 2)):
            p1.LP = 8000
            p2.LP = 8000

            print("INIZIO PARTITA NR: " + str(nrPartite+1))
            print()

            while((p1.LP > 0) and (p2.LP > 0)):
                print(p1.name + " = " + str(p1.LP))
                print(p2.name + " = " + str(p2.LP))

                actionStr = input("Cosa succede? ")
                print()
                actionArr = actionStr.split(" ")
                nameAction =  actionArr[0].lower().capitalize()
                opAction = actionArr[1]
                LP = int(actionArr[2])
                
                while((p1.name != nameAction) and (p2.name != nameAction)):
                    print("Giocatore non valido. Reinserisci i dati correttemente.")
                    print("I Giocaotri sono " + p1.name + " e " + p2.name + ".")
                    print()
                    actionStr = input("Cosa succede? ")
                    print()
                    actionArr = actionStr.split()
                while((opAction != "-") and (opAction != "+")):
                    print("Operazione non valida. Reinserisci i dati correttemente.")
                    print("Le operazioni disponibili sono + e -")
                    print()
                    actionStr = input("Cosa succede? ")
                    print()
                    actionArr = actionStr.split()
                while(LP == int):
                    print("LP inseriti non validi. Reinserisci i dati correttemente.")
                    print("I LP devono essere dei valori numerici interi.")
                    print()
                    actionStr = input("Cosa succede? ")
                    print()
                    actionArr = actionStr.split()
                if(p1.name == nameAction):
                    if(opAction == "+"):
                        p1.LP += LP
                    elif(opAction == "-"):
                        p1.LP -= LP

                    if(p1.LP <= 0):
                        p1.LP = 0
                        p2.nrVitt += 1
                        print("Questa partita ha vinto " + p2.name)
                        print()

                elif(p2.name == nameAction):
                    if(opAction == "+"):
                        p2.LP += LP
                    elif(opAction == "-"):
                        p2.LP -= LP

                    if(p2.LP <= 0):
                        p2.LP = 0
                        p1.nrVitt += 1
                        print("Questa partita ha vinto " + p1.name)
                        print()
                        
            nrPartite += 1
        if(p1.nrVitt == 2):
            print("HA VINTO " + p1.name.upper() + " " + str(p1.nrVitt) + " A " + str(p2.nrVitt))
        elif(p2.nrVitt == 2):
            print("HA VINTO " + p2.name.upper() + " " + str(p2.nrVitt) + " A " + str(p1.nrVitt))
c = Calculator2v2("Simone", "Federico")