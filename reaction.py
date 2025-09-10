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

driver.get("https://humanbenchmark.com/tests/reactiontime")


pyautogui.moveTo(600,800, duration=1)
pyautogui.leftClick(duration=1)

pyautogui.moveTo(520,600, duration=1)
pyautogui.leftClick()

wait = WebDriverWait(driver, 999999, poll_frequency=0.0001)  

for i in range(5):
    if i >= 1:
        pyautogui.moveTo(520,600, duration=1)
        pyautogui.leftClick()
    click = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".css-yg2dtu.view-go"))
    )

    click.click()

time.sleep(40000)