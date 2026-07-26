import selenium as s
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

campo = wait.until(
    EC.element_to_be_clickable((By.NAME, "q"))
)

campo.send_keys("RPA")
campo.send_keys(Keys.ENTER)

time.sleep(2)

driver.save_screenshot("robo02.png")

input("Pressione ENTER para fechar...")
driver.quit()