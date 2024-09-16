import numpy as np


randomArrayWord=["python","vipère","cobra","kaai","serpent"]

# Renvoie une variable aléatoire donnée dans le tableau
def randomWord() :
    return np.random.choice(randomArrayWord) 