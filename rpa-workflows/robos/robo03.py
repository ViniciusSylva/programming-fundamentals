import selenium as s
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.mime.text import MIMEText

driver = None

try:
    print("Iniciando navegador...")

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    driver.get('https://www.melhorcambio.com/dolar-hoje')

    wait = WebDriverWait(driver, 10)

    campo = wait.until(
        EC.element_to_be_clickable((By.ID, 'comercial'))
    )
    valor = campo.get_attribute('value')
    print(f'Valor do dólar comercial: {valor}')

    driver.close()

    email = "teste@gmail.com"
    senha = "teste"

    msg = MIMEText(f"Valor coletado: {valor}")
    msg['Subject'] = "Resultado do robô"
    msg['From'] = email
    msg['To'] = email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email, senha)
        server.send_message(msg)

    print("Email enviado!")

except Exception as e:
    print(f"Erro: {e}")

    try: 
        email = "teste@gmail.com"
        senha = "teste"

        msg = MIMEText(f"Erro no robô:\n{e}")
        msg['Subject'] = "Erro no robô"
        msg['From'] = email
        msg['To'] = email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email, senha)
            server.send_message(msg)
        
        print("Email de erro enviado!")

    except:
        print("Falha ao enviar email de erro")

finally:
    if driver:
        driver.quit()
        print("Navegador encerrado")