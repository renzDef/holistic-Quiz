class Questions:
    def __init__(self,gestellteFragen):  #Object von Questions init mit object(0)
        self.gestellteFragen = gestellteFragen
    
    def frage1(self):                                                           #Erste Frage usw..
        print("Wie lange habe ich gebraucht mir diese Frage auszudenken? ")     #return 1 für richtige
        self.gestellteFragen += 1                                               #return 0 für falsche antwort
        userInput = input("5min (1) : 15min (2) : 30min (3) : 1Stunde (4) ")    #return -1 für score abzug
        if userInput == "2":
            print("Richtig! ")
            return 1
        else:
            print("Falsch!")
            return 0
    
    def frage2(self):
        print("Für welches chemische Element steht das ""N""?")
        self.gestellteFragen += 1
        userInput = input("")
        if userInput == "Stickstoff":
            print("Richtig! ")
            return 1
        else:
            print("Falsch!")
            return 0

    def frage3(self):
        print("Die wievielte Frage ist diese?")
        self.gestellteFragen += 1
        userInput = input("")
        try:
            if int(userInput) == self.gestellteFragen:
                print("Richtig! ")
                return 1
            else:
                print("Falsch!")
                return 0
        except ValueError:
            print("Ungültige Angabe! -1 Score!")