import pyautogui
import time    
import subprocess
import random
import math
import os

def drawSquare(xPoz, yPoz):
    pyautogui.leftClick()
    pyautogui.mouseDown()
    size = random.randint(150,200)
    pyautogui.moveTo(xPoz + size, yPoz)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz + size, yPoz - size)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz, yPoz - size)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz, yPoz)
    pyautogui.mouseUp()

def drawCircle(xPoz,yPoz):
    radius = 100
    steps = 360
    pyautogui.moveTo(xPoz + radius, yPoz)
    for i in range(steps + 1):
        angle = 2 * math.pi * i / steps
        x = xPoz + radius * math.cos(angle)
        y = yPoz + radius * math.sin(angle)
        pyautogui.mouseDown()
        pyautogui.moveTo(x, y)
    pyautogui.mouseUp()

def drawRectangular(xPoz, yPoz):
    pyautogui.leftClick()
    pyautogui.mouseDown()
    size = random.randint(150,200)
    size2 = size + 200
    pyautogui.moveTo(xPoz + size2, yPoz)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz +size2 , yPoz - size)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz, yPoz -size)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz, yPoz)
    pyautogui.mouseUp()

def drawTriangle(xPoz,yPoz):
    pyautogui.leftClick()
    pyautogui.mouseDown()
    size = random.randint(150,200)
    pyautogui.moveTo(xPoz + size, yPoz)
    pyautogui.leftClick()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz + size/2, yPoz - size/2)
    pyautogui.leftClick()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz, yPoz)
    pyautogui.mouseUp()

def drawPiramid(xPoz, yPoz):
    pyautogui.leftClick()
    pyautogui.mouseDown()
    size = random.randint(150,350)
    size2 = size -100
    pyautogui.moveTo(xPoz + size, yPoz)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz , yPoz - size2)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz - size, yPoz)
    pyautogui.mouseUp()
    pyautogui.mouseDown()
    pyautogui.moveTo(xPoz, yPoz)
    pyautogui.mouseUp()

draw = [drawSquare,drawRectangular,drawTriangle,drawPiramid,drawCircle]

def randomColor(xArea,yArea):
    pyautogui.moveTo(305,89,1)
    pyautogui.leftClick()
    xEqual = random.randint(0,10)*21+792
    yEqual = random.randint(0,1)*23+84
    if xEqual == 792 and yEqual == 84:
        xEqual = random.randint(0,10)*21+792
        yEqual = random.randint(0,1)*23+84
        if xEqual == 792 and yEqual == 84:
            xEqual = random.randint(0,10)*21+792
            yEqual = random.randint(0,1)*23+84
    pyautogui.moveTo(xEqual,yEqual,1)
    pyautogui.leftClick()
    pyautogui.moveTo(xArea + 25,yArea - 15,1)
    pyautogui.leftClick()
    pyautogui.leftClick()

subprocess.Popen("mspaint")
time.sleep(2)

for i in range(random.randint(20,20)):
    pyautogui.moveTo(792,108,1)
    pyautogui.leftClick()
    pyautogui.moveTo(405,97,1)
    pyautogui.leftClick()
    xArea= random.randint(400,1348)
    yArea= random.randint(400,771)
    pyautogui.moveTo(xArea,yArea,2)
    draw[random.randint(0,3)](xArea,yArea)
    randomColor(xArea,yArea)
    
pyautogui.moveTo(305,89,1)
pyautogui.leftClick()
xEqual = random.randint(0,10)*21+792
yEqual = random.randint(0,1)*23+84
pyautogui.moveTo(xEqual,yEqual,1)
pyautogui.leftClick()
pyautogui.moveTo(320,295,1)
pyautogui.leftClick()
pyautogui.moveTo(310,878,1)
pyautogui.leftClick()

x = 308
y = 288
width = 1303
height = 591 
im = pyautogui.screenshot(region=(x, y, width, height))
desktop_path = r"C:\Users\macar\OneDrive\Desktop"
file_path = os.path.join(desktop_path, "screenshot2.png")
im.save(file_path)