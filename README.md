# Automatizador de Extração de Dados de Produtos em Site

Este script Python utiliza a biblioteca selenium para automatizar a extração de dados de produtos de um site específico, neste exemplo, Novalider Informática, e os armazena em uma planilha Excel.

# Requisitos
Python 3.x

Bibliotecas Python: selenium, openpyxl

Google Chrome

WebDriver: ChromeDriver

# Como Usar

## Clone o repositório para sua máquina:

git clone https://github.com/Vinicius555/bot_excel

## Instale as dependências:

pip install selenium openpyxl

Baixe o nevegador Google Chrome

## Execute o script:

python app.py

## Configuração
Certifique-se de ter o WebDriver apropriado para o seu navegador instalado.

Ajuste o link do site no script para o site desejado.

Personalize as expressões XPath para os elementos de acordo com a estrutura do site.

## Saída
Os dados extraídos (títulos e preços) são salvos na planilha 'produtos.xlsx' no mesmo diretório.

## Observações
Certifique-se de que a página do site está acessível e os elementos XPath são válidos.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
