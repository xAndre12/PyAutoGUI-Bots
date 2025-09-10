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

driver.get("https://humanbenchmark.com/tests/verbal-memory")

pyautogui.moveTo(600,820, duration=1)
pyautogui.leftClick(duration=1)

pyautogui.moveTo(500,620, duration=1)
pyautogui.leftClick()

wait = WebDriverWait(driver, 10)            

wordlist = []
seen = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='SEEN']")))
new = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='NEW']")))

while True:
    word = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"word")))
    if word.text in wordlist:
        seen.click()
    else:
        wordlist.append(word.text)
        new.click()



time.sleep(40000)