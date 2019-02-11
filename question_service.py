class Questions:
    def __init__(self,gestellteFragen):  #Object von Questions init mit object(0)
        self.gestellteFragen = gestellteFragen
    
    def frage1(self):                                                           #Erste Frage usw..
        print("Wie lange habe ich gebraucht mir diese Frage auszudenken? ")     #return 1 für richtige
        self.gestellteFragen += 1                                               #return 0 für falsche antwort
        userInput = input("5min (1) : 15min (2) : 30min (3) : 1Stunde (4)\n")    #return -1 für score abzug
        try:
            if int(userInput) == 2:
                print("Richtig!")
                return 1
            else:
                print("Falsch!\nDie richtige Antwort ist: 15min")
                return 0
        except ValueError:
            pass
    
    def frage2(self):
        print("Für welches chemische Element steht das ""N""?")
        self.gestellteFragen += 1
        userInput = input("")
        try:
            userInput = int(userInput)
        except ValueError:
            if userInput == "Stickstoff":
                print("Richtig! ")
                return 1
            else:
                print("Falsch!\nDie richtige Antwort ist: Stickstoff")
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
                print(f"Falsch!\nDie richtige Antwort ist: {self.gestellteFragen}")
                return 0
        except ValueError:
            pass

    def frage4(self):
        print("Welche deutsche Stadt hat die meißten Einwohner?")
        self.gestellteFragen += 1
        userInput = input("Frankfurt(1), Köln(2), München(3), Berlin(4)\n")
        try:
            if int(userInput) == 4:
                print("Richtig! ")
                return 1
            else:
                print("Falsch!\nDie richtige Antwort ist: Berlin")
                return 0
        except ValueError:
            pass
        
    def frage5(self):
        print("In welcher Höhe hängt der Korb beim Basketball")
        self.gestellteFragen += 1
        userInput = input("2,80m (1), 2,20m(2), 3,05m(3), 3,80m(4)\n")
        try:
            if int(userInput) == 3:
                print("Richtig! ")
                return 1
            else:
                print("Falsch!\nDie richtige Antwort ist: 3,05m")
                return 0
        except ValueError:
            pass

    def frage6(self):
        print("Welcher der folgenden Flüsse fließt nicht durch Europa?")
        self.gestellteFragen += 1
        userInput = input("Tiber(1), Paru(2), Vardar(3), Newa(4)\n")
        try:
            if int(userInput) == 2:
                print("Richtig! ")
                return 1
            else:
                print("Falsch!\nDie richtige Antwort ist: Paru")
                return 0
        except ValueError:
            pass

    def frage7(self):
        print("Was ist kein amerikanischer Staat?")
        self.gestellteFragen += 1
        userInput = input("Ontario(1), Ohio(2), Oregon(3), Oklahoma(4)\n")
        try:
            if int(userInput) == 1:
                print("Richtig!")
                return 1
            else:
                print("Falsch!\nDie richtige Antwort ist: Ontario")
                return 0
        except ValueError:
            pass
        
    def frage8(self):
        print("Wann hat der 2. Weltkrieg angefangen?")
        self.gestellteFragen += 1
        userInput = input("")
        try:
            if int(userInput) == 1939:
                print("Richtig! ")
                return 1
            else:
                print("Falsch!")
                return 0
        except ValueError:
            pass
        
    def frage9(self):
        print("Welche Zahl ist das? (MMLI)")
        self.gestellteFragen += 1
        userInput = input("")
        try:
            if int(userInput) == 2051:
                print("Richtig! ")
                return 1
            else:
                print("Falsch!\nDie richtige Antwort ist: 2051")
                return 0
        except ValueError:
            pass
        
    def frage10(self):
        print("Was ist die Frage?")
        self.gestellteFragen += 1
        userInput = input()
        try:
            userInput = int(userInput)
        except ValueError:
            userInput = str(userInput)
            if userInput == "Was ist die Frage?":
                print("Richtig! ")
                return 1
            else:
                print("Falsch!\nDie richtige Antwort ist: Was ist die Frage?")
                return 0