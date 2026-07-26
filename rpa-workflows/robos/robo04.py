import pyautogui as p 
import selenium as s
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.udemy.com/?gad_source=1&gad_campaignid=23625265871&gbraid=0AAAABCp9oWX7Q4fXvWh2Iij2gIEFv0DC0&gclid=CjwKCAjwhe3OBhABEiwA6392zFLQFzL8YByB-KqKJk_j43bpxX-IaVTkTf7pqHwTopW6E74m0ARJABoCKtQQAvD_BwE")
driver.maximize_window()

time.sleep(3)

botao = p.locateCenterOnScreen('barra.png', confidence=0.6)

if botao:
    p.click(botao)
    time.sleep(1)
    p.write("Charles Lima")
    p.press("enter")

time.sleep(5)

driver.save_screenshot("robo04.png")

p.moveTo(x=1893, y=21, duration=1)
p.click()