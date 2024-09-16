import module.Word as word
import module.Game as game

randomArrayWord=["python","vipère","cobra","kaai","serpent"]

randomWord = word.randomWord(randomArrayWord)
hiddenWord = "_"*len(randomWord)
game.searchWord(randomWord,hiddenWord)

