from question_service import *

path = "HighScore.txt"

questions = Questions(0)
score = questions.frage3()

with open(path,"a") as file:
    file.append(f"Spieler : {spielername} Score : {score}")