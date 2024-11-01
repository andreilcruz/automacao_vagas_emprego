from selenium import webdriver
from selenium.webdriver.opera.service import Service
from selenium.webdriver.opera.options import Options

# Defina o caminho para o executável do Opera
opera_options = Options()
opera_options.binary_location = r"C:\Users\User\AppData\Local\Programs\Opera GX\opera.exe"

# Defina o caminho para o OperaDriver
service = Service(r"C:\Users\User\OneDrive\Área de Trabalho\operadriver_win64\operadriver.exe")

# Inicializa o navegador Opera
driver = webdriver.Opera(service=service, options=opera_options)

# Abre uma página para teste
driver.get("https://www.youtube.com")

# Fechar o navegador ao final do script
driver.quit()
