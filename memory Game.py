import pyautogui 
import random
import tkinter as tk

def Text(text, duration):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg='black')

    label = tk.Label(root, text=text, fg='white', bg='black', font=('Arial', 24))
    label.pack(padx=20, pady=10)

    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'+{x}+{y}')

    root.after(duration, root.destroy)
    root.mainloop()

lvlSettings = {
    "lvl1": {
        "array": [1,2,3],
        "speed":250,
        "nextLvlText":"Level 2",
        "nextLvl":"lvl2"
    },
    "lvl2": {
        "array": [1,2,3,4,5,6],
        "speed":300,
        "nextLvlText":"Level 3",
        "nextLvl":"lvl3"
    },
    "lvl3": {
        "array": [1,2,3,4,5,6,7,8,9],
        "speed":350,
        "nextLvlText":"Level 4",
        "nextLvl":"lvl4"
    },
    "lvl4": {
        "array": [1,2,3,4,5,6,7,8,9,1,2,3],
        "speed":400,
    },
    "tries": 3,
}


def startGame(lvl):
    if lvlSettings["tries"] >0:
        rightOrder = True
        array = lvl["array"]
        random.shuffle(array)

        for i in range(len(array)):
            Text(array[i], lvl["speed"])
        answer= pyautogui.prompt(text="Enter the numbers in order", title="Memory Game")

        if len(answer)<len(array):
            pyautogui.alert(text="Not enough Numbers",title="Memory Game",button="retry")
            startGame(lvl)
            return
        if len(answer)>len(array):
            pyautogui.alert(text="Too many Numbers",title="Memory Game",button="retry")
            startGame(lvl)
            return
  
        for i in range(len(array)):
            if int(answer[i]) != array[i]:
                rightOrder = False
                lvlSettings["tries"	] = lvlSettings["tries"] -1
                pyautogui.alert(text="Wrong combination",title="Memory Game",button="okay")
                pyautogui.alert(text=f"Remaining lifes = {lvlSettings['tries']}",title="Memory Game",button="retry")
                startGame(lvl)
                return

        if rightOrder == True: 
            pyautogui.alert(text=lvl["nextLvlText"],title="Memory Game",button="okay")
            startGame(lvlSettings[lvl["nextLvl"]])
    else:
        answer2 = pyautogui.confirm(text="You lost, but still, do you want to try again?",title= "Memory Game", buttons=["Yes", 'No']  )
        if answer2 == "Yes":
            lvlSettings["tries"] = 3
            startGame(lvlSettings["lvl1"])
            return
            
        else:
            pyautogui.alert(text="Better luck next time",title="Memory Game",button="Thank you")

startQuestion = pyautogui.confirm(text=f"Are you ready?",title= "Memory Game", buttons=["Let's go", 'No']  )
if startQuestion == "Let's go":
    pyautogui.alert(text="Level 1",title="Memory Game",button="okay")
    startGame(lvlSettings["lvl1"])
else:
    pyautogui.alert(text="Maybe next time",title="Memory Game",button="sure!")