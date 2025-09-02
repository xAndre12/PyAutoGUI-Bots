import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://humanbenchmark.com/tests/sequence")


pyautogui.moveTo(600,800, duration=1)
pyautogui.leftClick(duration=1)

pyautogui.moveTo(520,600, duration=1)
pyautogui.leftClick()

wait = WebDriverWait(driver, 10)            

squares = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"squares")))

def startGame(level):    
    boxes = []
    time.sleep(0.5)
    for x in range(level):
        time.sleep(0.5)
        box = squares.find_element(By.CLASS_NAME, 'active')
        boxes.append(box)
    for i in range(len(boxes)):
        location = boxes[i].location
        size = boxes[i].size

        center_x = location['x'] + size['width'] / 2
        center_y = (location['y'] + size['height'] / 2) + 150
        pyautogui.moveTo(center_x,center_y, duration=0.3)
        pyautogui.click()
    nextLevel = level + 1
    startGame(nextLevel)
    return

startGame(1)
        
time.sleep(40000)