from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 🔹 Função de log
def log(msg):
    print(f"[BOT] {msg}")

# 🔹 Configuração headless (invisível)
options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")

log("Iniciando navegador (modo invisível)...")
driver = webdriver.Chrome(options=options)

log("Acessando site...")
driver.get('https://rpachallengeocr.azurewebsites.net/')

log("Aguardando tabela carregar...")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "tableSandbox"))
)

dados = []
pagina = 1

while True:
    log(f"📄 Coletando página {pagina}...")

    tabela = driver.find_element(By.ID, "tableSandbox")

    if not dados:
        cabecalhos = [th.text for th in tabela.find_elements(By.TAG_NAME, "th")]
        log(f"🧾 Cabeçalhos detectados: {cabecalhos}")

    linhas = tabela.find_elements(By.CSS_SELECTOR, "tbody tr")

    log(f"✅ {len(linhas)} linhas encontradas!")

    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, "td")
        
        if colunas:
            dados.append({
                cabecalhos[i]: colunas[i].text
                for i in range(len(colunas))
            })

    log(f"📊 Total acumulado: {len(dados)} registros")

    try:
        botao_next = driver.find_element(By.ID, "tableSandbox_next")
        classe = botao_next.get_attribute("class")

        if "disabled" in classe:
            log("🚫 Última página alcançada!")
            break

        log("➡️ Indo para próxima página...")
        botao_next.click()

        WebDriverWait(driver, 10).until(
            EC.staleness_of(linhas[0])
        )

        pagina += 1

    except Exception as e:
        log(f"❌ Erro ao clicar no Next: {e}")
        break

log(f"\n✅ Total coletado: {len(dados)} registros")

arquivo = "dados.txt"

if not dados:
    log("❌ Nenhum dado para salvar!")
else:
    log("💾 Salvando arquivo...")

    with open(arquivo, "w", encoding="utf-8") as f:
        
        cabecalho = " | ".join(dados[0].keys())
        f.write(cabecalho + "\n")
        f.write("-" * len(cabecalho) + "\n")

        for registro in dados:
            linha = " | ".join(registro.values())
            f.write(linha + "\n")

    log(f"✅ Arquivo '{arquivo}' salvo com sucesso!")

driver.quit()
log("🛑 Navegador finalizado.")