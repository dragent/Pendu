import module.pendu.Word as word
import module.pendu.Game as game


randomWord = word.randomWord()
hiddenWord = "_"*len(randomWord)
game.searchWord(randomWord,hiddenWord)

