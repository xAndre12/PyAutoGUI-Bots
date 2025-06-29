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

driver.get("https://humanbenchmark.com/tests/number-memory")

pyautogui.moveTo(590,797, duration=1)
pyautogui.leftClick(duration=1)

wait = WebDriverWait(driver, 20)

button_start = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"e19owgy710")))

button_start.click()

while True:
    number = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"big-number")))
    number = number.text

    input = wait.until(EC.presence_of_element_located((By.XPATH,"//input[contains(@pattern, '[0-9]*')]")))
    input.click()

    pyautogui.write(number)
    time.sleep(1)
    button_submit = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"e19owgy710")))

    button_submit.click()
    time.sleep(1)
    button_next = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"e19owgy710")))

    button_next.click()
    time.sleep(1)
