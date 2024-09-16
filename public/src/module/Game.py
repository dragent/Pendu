
# Demande à l'utilisateur d'écrire lettre par lettre
# Tant que le mot caché est différent du mot donné par l'utilisateur
# Si la lettre n'est pas dans le mot appelle la fonction des erreurs
# Si la lettre existe appelle la fonction de rajout de lettre
def searchWord(randomWord, hiddenWord):
    while hiddenWord != randomWord:
        letter = input("Veuillez rentrer une lettre : ").lower()
        if len(letter) == 1 and randomWord.find(letter) == -1:
            print("La lettre n'est pas dedans")
        else:
            hiddenWord= addLetter(randomWord,letter,hiddenWord)
            print(hiddenWord)
    print("Félicitation vous avez trouvé")


# Transforme le mot en liste
# Compare la lettre à chaque lettre du mot
# Rajoute la lettre à l'index
# Renvoie le mot
def addLetter(randomWord, letter,  hiddenWord):
    i=0
    hiddenWord = list(hiddenWord)
    for c in randomWord:
        if c == letter:
            hiddenWord[i]=letter
        i+=1
    return "".join(hiddenWord)