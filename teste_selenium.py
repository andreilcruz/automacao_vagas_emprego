import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Configuração do logging
logging.basicConfig(filename='automacao.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Função para capturar a tela
def capture_screenshot(driver, step_name):
    screenshot_name = f"screenshot_{step_name}.png"
    driver.save_screenshot(screenshot_name)
    logging.info(f"Captura de tela salva: {screenshot_name}")

# Configuração do Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("user-data-dir=C:/ChromeDev")  # Diretório do perfil do usuário

# Inicializa o WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Acessa a página de login do Google
    driver.get("https://accounts.google.com/signin")
    logging.info("Página de login acessada.")

    # Insere o e-mail e avança
    email_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "identifier"))
    )
    email_input.send_keys("autredes1")  # Substitua pelo seu e-mail
    email_input.send_keys(Keys.RETURN)
    logging.info("E-mail enviado.")

    # Captura de tela após enviar o e-mail
    capture_screenshot(driver, "email_enviado")

    # Aguarda a transição para a página de senha e que o campo esteja visível
    password_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@type="password"]'))
    )

    # Insere a senha
    password_input.send_keys("andreiRedes1")  # Substitua pela sua senha
    password_input.send_keys(Keys.RETURN)  # Envia a senha
    logging.info("Senha enviada.")

    # Captura de tela após enviar a senha
    capture_screenshot(driver, "senha_enviada")

    # Aguarda o carregamento da página do Google Docs
    driver.get("https://docs.google.com/spreadsheets/d/14G_kyb44CM4tUB62VDqQSQ9_xv7fopaWYSoAGNLFFgA/edit?usp=sharing")
    logging.info("Página da planilha acessada.")

    # Espera até que um elemento da planilha esteja disponível
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="t-formula-bar-input"]/div[2]/div/div[2]/div'))
    )
    logging.info("Elemento da planilha encontrado.")

    # Inserindo dados na planilha
    cell_a1 = driver.find_element(By.XPATH, '//*[@id="t-formula-bar-input"]/div[2]/div/div[2]/div')
    cell_a1.click()
    cell_a1.send_keys("Nome")
    cell_a1.send_keys(Keys.TAB)

    cell_b1 = driver.switch_to.active_element
    cell_b1.send_keys("Email")
    cell_b1.send_keys(Keys.TAB)

    logging.info("Dados inseridos na planilha.")

    # Captura de tela do estado final
    capture_screenshot(driver, "dados_inseridos")

    time.sleep(5)  # Pausa para visualizar

finally:
    driver.quit()  # Fecha o navegador
    logging.info("Navegador fechado.")
