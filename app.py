# Importando Bibliotecas

from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Acessar o site que deseja,site exemplo: https://www.novaliderinformatica.com.br/computadores-gamers

driver = webdriver.Chrome()
driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

# Criando planilha

workbook = openpyxl.Workbook()

# Criando a página 'produtos'
workbook.create_sheet('produtos')

# Selecionando a página produtos
sheet_produtos = workbook['produtos']

# Colocando titulos na planilha
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'

# Salvando a planilha
workbook.save('produtos.xlsx')

# Extrair todos os títulos

titulos = driver.find_elements(By.XPATH, "//a[@class='nome-produto']")

# Extrair todos os preços
precos = driver.find_elements(By.XPATH, "//strong[@class='preco-promocional']")

# Inserir os títulos e preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, preco.text])


# Salvando a planilha
workbook.save('produtos.xlsx')
