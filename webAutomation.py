"""
Trabalhamos em uma importadora e o preço dos nossos produtos é vinculado a cotação de:
- dólar
- euro
- ouro

Precisamos pegar na internet, de forma automática, a cotação desses 3 itens e saber quanto devemos cobrar pelos nossos produtos,
considerando uma margem de contribuição que temos na nossa base de dados.

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

navegador = webdriver.Chrome()

# Pegar a cotação do dólar
navegador.get("https://www.google.com/")
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(f"Dólar: R$ {cotacao_dolar}")

# Pegar a cotação do euro
navegador.get("https://www.google.com/")
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(f"Euro: R$ {cotacao_euro}")

# Pegar a coração do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element("xpath", '//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(f"Ouro: R$ {cotacao_ouro}")

navegador.quit()

# Atualizar a base de preços (compra e venda)
tabela = pd.read_excel('Produtos.xlsx')

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)

# Exportar a base de preços atualizada
tabela.to_excel("Produtos Novo.xlsx", index=False)