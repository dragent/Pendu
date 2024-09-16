import module.Word as word
import module.Game as game


randomWord = word.randomWord()
hiddenWord = "_"*len(randomWord)
game.searchWord(randomWord,hiddenWord)

