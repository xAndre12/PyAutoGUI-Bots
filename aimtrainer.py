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

driver.get("https://humanbenchmark.com/tests/aim")

pyautogui.moveTo(600,800, duration=1)
pyautogui.leftClick(duration=1)

pyautogui.moveTo(503,441, duration=1)
pyautogui.leftClick()

wait = WebDriverWait(driver, 20)

# # element = driver.find_element(By.CSS_SELECTOR, '[data-aim-target="true"]')
# # div = element.find_element(By.XPATH, ".//div[1]")


# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-aim-target="true"]')))

# # Găsește elementul țintă
# target = driver.find_element(By.CSS_SELECTOR, '[data-aim-target="true"]')
# print("target:",target)
# # Forțează click pe el cu JavaScript
# driver.execute_script("arguments[0].click();", target)
# print("sunt aici")
for i in range(30):
    target = driver.find_element(By.CSS_SELECTOR, '[data-aim-target="true"] div')

    location = target.location
    size = target.size

    # Coordonatele centrului
    center_x = location['x'] + size['width'] / 2
    center_y = (location['y'] + size['height'] / 2) + 150


    pyautogui.moveTo(center_x, center_y)
    pyautogui.click()

# print(f"Center X: {center_x}, Center Y: {center_y}")

time.sleep(4000000)