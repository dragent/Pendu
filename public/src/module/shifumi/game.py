from module.shifumi import playersChoices as playerTurn

SHIFUMI = ["papier", "ciseau", "pierre"]


def play():
    replay ="o"
    userWin = 0
    pcWin = 0
    win = True
    while replay =="o":
        pcPlay = playerTurn.randomCumputer(SHIFUMI)
        userPlay = playerTurn.userChoice(SHIFUMI)
        if userPlay == pcPlay:
            print("Vous avez fait égalité.  Il y a ", userWin," - ", pcWin)
        elif userPlay==SHIFUMI[0]:
            if pcPlay == SHIFUMI[1]:
                win = False
            else:
                win = True
        elif userPlay== SHIFUMI[1]:
                if pcPlay == SHIFUMI[2]:
                    win = False
                else:
                    win = True
        else:
                if pcPlay == SHIFUMI[0]:
                     win = False
                else: 
                    win = True
        if(pcPlay != userPlay):
            if win == True:
                userWin+=1
                print("Vous avez gagné. Il y a ", userWin," - ", pcWin)
            else:
                pcWin +=1
                print("Vous avez perdu. Il y a ", userWin," - ", pcWin)