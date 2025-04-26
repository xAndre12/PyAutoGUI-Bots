import pyautogui
import math
import random

gameSettings = {
    "promptTitle": 'Number guessing tool',
    "playerNumber": 0,
    "firstGuessNumber": 1,
    "lastGuessNumber":0,
    "gameOn": True,
    "tries": 5,
}

def guessingNumber():
    print(gameSettings['firstGuessNumber'],gameSettings['lastGuessNumber'])
    if gameSettings['tries'] > 0:
        randomNumber = random.randint(gameSettings['firstGuessNumber'], gameSettings['lastGuessNumber'])
        answer = pyautogui.confirm(text=f"Is your selected number {randomNumber}?",title= gameSettings['promptTitle'], buttons=['Yes', 'No']  )
        if answer == "No":
            gameSettings['tries'] = gameSettings['tries']-1
            guessingNumber()
        else:
            pyautogui.alert(text = "I won", title="Akinator", button="OK")
            
def startGuessing():
    if gameSettings['gameOn']:
        answer = pyautogui.confirm(text=f"Is your selected number between {gameSettings['firstGuessNumber']} and {gameSettings['lastGuessNumber']}?",title= gameSettings['promptTitle'], buttons=['Yes', 'No']  )
        if answer == 'Yes': 
            if gameSettings['firstGuessNumber'] * 2 != gameSettings['lastGuessNumber']:
                gameSettings['lastGuessNumber'] = math.ceil(gameSettings['lastGuessNumber']/2)
                startGuessing()
            else:
                gameSettings['lastGuessNumber'] = math.ceil((gameSettings['lastGuessNumber']+gameSettings['firstGuessNumber'])/2)
                gameSettings['gameOn'] = False
                startGuessing()
        else:
            gameSettings['firstGuessNumber'] = gameSettings['lastGuessNumber']
            gameSettings['lastGuessNumber'] = gameSettings['lastGuessNumber']*2
            startGuessing()
    else:
        if int(gameSettings['playerNumber']) < gameSettings['lastGuessNumber']:
            guessingNumber()
        else:
            firstNumber = gameSettings['firstGuessNumber']
            gameSettings['firstGuessNumber'] = gameSettings['lastGuessNumber']
            gameSettings['lastGuessNumber'] = firstNumber * 2
            guessingNumber()
            

game = pyautogui.confirm(text='Number guessing tool', title= gameSettings['promptTitle'], buttons=['Start', 'Cancel'])

if game == "Start" : 
    gameSettings['playerNumber'] = pyautogui.prompt(text='Choose a number',title = gameSettings['promptTitle'],default='Type here')
    gameSettings['lastGuessNumber'] = 10 ** len(gameSettings['playerNumber'])
    startGuessing()
    
else:
    pyautogui.alert(text = "Maybe next time", title="Akinator", button="OK")