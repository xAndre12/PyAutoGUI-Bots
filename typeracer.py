import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Se creaza serviciul care ne ajuta sa manipulam Chrome-ul
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Comanda care deschide site-ul web
driver.get("https://play.typeracer.com/")


# while True:
#     print(pyautogui.position())

pyautogui.moveTo(590,787, duration=1)
pyautogui.leftClick(duration=1)
pyautogui.moveTo(164,465, duration=1)
pyautogui.leftClick(duration=1)

wait = WebDriverWait(driver, 20)

# Mod de selectare elemente dupa XPATH
text_parent = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@style, 'font-family: monospace')]" )))
text_span_first = text_parent.find_element(By.XPATH, ".//span[1]")
text_span_second = text_parent.find_element(By.XPATH, ".//span[2]")
text_span_third = text_parent.find_element(By.XPATH, ".//span[3]")

text1 = text_span_first.text
text2 = text_span_second.text
text3 = text_span_third.text

text = f"{text1}{text2} {text3}"

# Mod de selectare elemente dupa CLASS_NAME
input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "txtInput")))

time.sleep(10)

input.click()

time.sleep(0.2)
a = 0
for letter in text:
    a=a+1
    if a<=2:
        time.sleep(0.05)
        pyautogui.write(letter)
    else:
        pyautogui.write(letter)


# Selectezi cu ajutorul selenium-ului inputul in care scrii text-ul si apesi click pe el
# apesi click tot cu ajutorul slenium (variabila_element.click)
time.sleep(1000)
