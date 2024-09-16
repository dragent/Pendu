import numpy as np


# Choisi un mot aléatoire
def randomWord(array) :
    max= len(array)
    return array[np.random.randint(0,max)]
        