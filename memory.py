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

driver.get("https://humanbenchmark.com/tests/memory")

pyautogui.moveTo(600,800, duration=1)
pyautogui.leftClick(duration=1)

pyautogui.moveTo(503,600, duration=1)
pyautogui.leftClick()

wait = WebDriverWait(driver, 20)



def startgame():
    matching_divs = set()
    start_time = time.time()
    while time.time() - start_time < 3:
        parent = driver.find_element(By.CLASS_NAME, 'eut2yre0');
        divs = parent.find_elements(By.TAG_NAME, "div")

        for div in divs:
            try:
                background = div.value_of_css_property("background-color")

                if background in ["rgb(255, 255, 255)", "rgba(255, 255, 255, 1)"]:
                    matching_divs.add(div)
            except:
                continue

    for box in matching_divs:
        location = box.location
        size = box.size

        center_x = location['x'] + size['width'] / 2
        center_y = (location['y'] + size['height'] / 2) + 150
        pyautogui.moveTo(center_x,center_y, duration=0.3)
        pyautogui.click()
    time.sleep(1)
    startgame()
    return

startgame()

time.sleep(40000)
