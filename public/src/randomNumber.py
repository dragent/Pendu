import module.randomNumber.getNumber as getNumber
import module.randomNumber.gameRandomNumber as game

hiddenValue = getNumber.getRandomNumber()
game.findValue(hiddenValue, 10)