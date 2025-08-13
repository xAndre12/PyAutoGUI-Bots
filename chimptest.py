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

driver.get("https://humanbenchmark.com/tests/chimp")

pyautogui.moveTo(600,800, duration=1)
pyautogui.leftClick(duration=1)

pyautogui.moveTo(503,620, duration=1)
pyautogui.leftClick()

wait = WebDriverWait(driver, 20)


def startGame():
    cells = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-cellnumber]')))
    for i in range(1,len(cells)+1):
        print(i)
        cell = wait.until(EC.presence_of_element_located((By.XPATH, f'//div[@data-cellnumber={i}]')))
        location = cell.location
        size = cell.size

        center_x = location['x'] + size['width'] / 2
        center_y = (location['y'] + size['height'] / 2) + 150
        pyautogui.moveTo(center_x,center_y, duration=0.5)
        pyautogui.click()
    pyautogui.moveTo(503,620)
    pyautogui.click()
    startGame()

startGame()

time.sleep(40000)