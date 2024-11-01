# Automação de Vagas Emprego

Este projeto consiste em uma automação para preencher automaticamente uma planilha do Google com informações relevantes, utilizando o Selenium e Python. O objetivo é facilitar o registro de dados relacionados a vagas de emprego.

## Pré-requisitos

1. **Python 3.8+** - Certifique-se de que o Python está instalado.
2. **Google Chrome** - Versão compatível com o ChromeDriver que será usado.

## Instalação

1. Clone o repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu_usuario/automacao_vagas_emprego.git
    cd automacao_vagas_emprego
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv myenv
    myenv\Scripts\activate      
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. **ChromeDriver**: Baixe a versão do [ChromeDriver](https://chromedriver.chromium.org/downloads) que corresponde à versão do seu Google Chrome. Coloque o executável do `chromedriver` na pasta do projeto ou adicione-o ao PATH do sistema.

## Configuração do ChromeDriver

Certifique-se de que o `chromedriver` está localizado no PATH do sistema ou no diretório principal do projeto. No código, especifique o caminho correto, se necessário.

## Como Executar

Execute o seguinte comando para iniciar a automação:
```bash
python teste_selenium.py
