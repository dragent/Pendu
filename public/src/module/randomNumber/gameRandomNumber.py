from module.randomNumber import getNumber as getNumber

def findValue(hiddenValue, nbTry):
    i=0
    value = "-1"
    while i<nbTry and  value != hiddenValue:
        i+=1
        value = getNumber.getUserNumber()
        if value > hiddenValue:
            print("La valeur recherchée est plus petite")
        elif value < hiddenValue:
            print("La valeur recherchée est plus grande")
        else:
            break
    if value != hiddenValue:
        print("Vous avez perdu. La valeur était : ", hiddenValue)
    else:
        print("Vous avez trouvé en ", i," essais")