from question_service import *
import random

class Quiz_Ablauf:
    
    global fragen_liste                                     
    fragen_liste = [1,2,3]

    def fragen_auswahl(self):                               
        global ausgewählte_frage
        ausgewählte_frage = random.randint(1,3)
        anzahl_der_fragen = len(fragen_liste)
        zähler = 0
        for item in fragen_liste:                           
            if ausgewählte_frage == fragen_liste[zähler]:  
                fragen_liste.remove(ausgewählte_frage)
            zähler += 1
        if anzahl_der_fragen == len(fragen_liste):
            self.fragen_auswahl()
    
    def start(self):
        global score
        global spielername
        x = 1
        score = 0
        frage = Questions(0)
        spielername = input("Spielername: ")
        while x <= 3:
            self.fragen_auswahl()
            if ausgewählte_frage == 1:
                score += frage.frage1()
            if ausgewählte_frage == 2:
                score += frage.frage2()
            if ausgewählte_frage == 3:
                try:
                    score += frage.frage3()
                except TypeError:
                    score -= 1
                    print("Ungültige Angabe! -1 Score!")
            if ausgewählte_frage == 4:
                score += frage.frage4()
            if ausgewählte_frage == 5:
                score += frage.frage5()
            if ausgewählte_frage == 6:
                score += frage.frage6()
            if ausgewählte_frage == 7:
                score += frage.frage7()
            if ausgewählte_frage == 8:
                score += frage.frage9()
            if ausgewählte_frage == 9:
                score += frage.frage9()
            if ausgewählte_frage == 10:
                score += frage.frage10()
            x += 1
        self.result()
    
    def result(self):
        path = "HighScore.txt"
        with open(path,"a") as file:
            file.write(f"Spieler : {spielername} Score : {score}\n")
            print(f"Spieler : {spielername} Score : {score}")