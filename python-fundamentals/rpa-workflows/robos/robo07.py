import selenium as s
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import requests
import time


try:
    driver = webdriver.Chrome()
    driver.get('https://rpachallenge.com/')
    driver.maximize_window()
    print('✅ Site aberto e maximizado com sucesso!!')
except Exception as e:
    print(f'❌ Nao foi possivel abrir o navegador!! erro {e}')
time.sleep(2)

try:
    botao = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[contains(@href, "challenge.xlsx")]')
        )
    )
    print('✅ Botao e o arquivo encontrados com sucesso!')
except Exception as e:
    print(f'❌ Nao foi possivel encontrar o botao com os arquivos! erro {e}')
time.sleep(2)


link = botao.get_attribute("href")
# Conteudo do arquivo fica salvo dentro de requests 
# #E depois e arrumado para dentro de um arquivo criado
res = requests.get(link)


try:
    with open("challenge.xlsx", "wb") as f:
        f.write(res.content)
    print('✅ Arquivo salvo e alocado na pasta')
except Exception as e:
    print(f'❌ Nao foi possivel salvar o arquivo na pasta! erro {e}')

dados = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(dados, columns=["First Name", "Last Name", "Company Name", "Role in Company", "Address", "Email", "Phone Number"])

botao_start = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Start')]"))
)
botao_start.click()

for i, row in df.iterrows():
    firstName = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelFirstName']"))
    )
    firstName.send_keys(row["First Name"])

    company_Name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelCompanyName']"))
    )
    company_Name.send_keys(row["Company Name"])

    lastName = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelLastName']"))
    )
    lastName.send_keys(row["Last Name"])

    roleCompany = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelRole']"))
    )
    roleCompany.send_keys(row["Role in Company"])

    phoneNumber = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelPhone']"))
    )
    phoneNumber.send_keys(row["Phone Number"])

    address = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelAddress']"))
    )
    address.send_keys(row["Address"])

    email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@ng-reflect-name='labelEmail']"))
    )
    email.send_keys(row["Email"])

    botao_submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Submit']"))
    )
    botao_submit.click()

time.sleep(5)