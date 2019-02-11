from question_service import *
import random, os

class Quiz_Ablauf:
    
    global fragen_liste                                     
    fragen_liste = [1,2,3,4,5,6,7,8,9,10]
    
    def fragen_auswahl(self):                               
        global ausgewählte_frage
        ausgewählte_frage = random.randint(1,10)
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
        fehler_zähler = 0
        punkte_zähler = 0
        frage = Questions(0)
        spielername = input("Spielername: ")
        while x <= 10:
            self.fragen_auswahl()
            score_vorher = score
            try:
                if ausgewählte_frage == 1:
                    score += frage.frage1()
                if ausgewählte_frage == 2:
                    score += frage.frage2()
                if ausgewählte_frage == 3:
                    score += frage.frage3()
                if ausgewählte_frage == 4:
                    score += frage.frage4()
                if ausgewählte_frage == 5:
                    score += frage.frage5()
                if ausgewählte_frage == 6:
                    score += frage.frage6()
                if ausgewählte_frage == 7:
                    score += frage.frage7()
                if ausgewählte_frage == 8:
                    score += frage.frage8()
                if ausgewählte_frage == 9:
                    score += frage.frage9()
                if ausgewählte_frage == 10:
                    score += frage.frage10()
            except TypeError:
                    score -= 1
                    print("Ungültige Angabe! -1 Score!")
            x += 1
            if score_vorher == score + 1:
                fehler_zähler += 1
                punkte_zähler = 0
            if score_vorher == score - 1:
                punkte_zähler += 1
                fehler_zähler = 0
            else: 
                fehler_zähler = 0
                punkte_zähler = 0
            if fehler_zähler == 3:     
                score -= 1
            if fehler_zähler == 5:    
                score -= 2
            if fehler_zähler == 8:   
                score -= 3
            if fehler_zähler == 10:   
                score -= 4
            if punkte_zähler == 3:    
                score += 1
            if punkte_zähler == 5:     
                score += 2
            if punkte_zähler == 8: 
                score += 3
            if punkte_zähler == 10:    
                score += 4

        self.result()
    
    def result(self):
        path = "HighScore.txt"
        remake = 0

        with open(path,"r") as file:
            textZeilen = file.readlines()
            if len(textZeilen) == 0:
                setHighScore = 2
            else:
                setHighScore = 0
        
        with open(path,"a") as file:
            if setHighScore == 0:
                x = 0
                highscoreFound = 0
                remake = 0
                for item in textZeilen:
                    if highscoreFound == 0:
                        try:
                            text1,text2 = textZeilen[x].split("\t")
                            if text2 == "(HIGHSCORE)\n":
                                highscoreFound = 1
                                if highscoreFound == 1:
                                    textHalter = text1[len(text1)-2:len(text1)]
                                    textHalter = textHalter.split(" ")
                                    if score > int(textHalter[1]):
                                        textZeilen.pop(x)
                                        textZeilen.insert(x,text1+"\n")
                                        setHighScore = 1
                                        remake = 1
                        except ValueError:
                            pass
                        x+=1
                    else:
                        pass

                if setHighScore == 0:
                    textZeilen.append(f"Spieler : {spielername} Score : {score} \n")
                    print(f"Spieler : {spielername} Score : {score}")
                    remake = 1

        if remake == 1:
            if os.path.exists(path):
                os.remove(path)
            else:
                print("Datei nicht gefunden!")
            
        with open(path,"w") as file:
            if setHighScore == 1:
                textZeilen.append(f"Spieler : {spielername} Score : {score}\t(HIGHSCORE)\n")
                print(f"Spieler : {spielername} Score : {score}")
                print("Sie haben einen neuen HighScore erreicht!")
            if setHighScore == 2:
                file.write("Liste:\n")
                file.write(f"Spieler : {spielername} Score : {score}\t(HIGHSCORE)\n")
                print(f"Spieler : {spielername} Score : {score}")
                print("Sie haben einen neuen HighScore erreicht!")
            if remake == 1:
                loop = 0
                for item in textZeilen:
                    file.write(textZeilen[loop])
                    loop += 1