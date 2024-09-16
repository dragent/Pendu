import numpy as np

def getRandomNumber():
    return np.random.randint(0,101)

def getUserNumber():
    value = input("Donnez moi un nombre positif : ")
    if not value.isnumeric():
        return -1
    return int(value)