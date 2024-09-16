import numpy as np



def randomCumputer(SHIFUMI):
    return np.random.choice(SHIFUMI)

def userChoice(SHIFUMI):
    choice =""
    while choice not in SHIFUMI:
       choice =  input("Veuillez choisir entre pierre, papier et ciseau : ").lower()
    return choice