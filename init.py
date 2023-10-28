#!.venv/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Abrir navegador
driver = webdriver.Chrome()
driver.get('https://www.sigestonline.com.br/ica/')


#Digitar login e senha 
driver.find_element('xpath', '//*[@id="txtLogin"]').send_keys('henrique.projetos@institutocarioca.org.br')
driver.find_element('xpath', '//*[@id="txtSenha"]').send_keys('152155')

#Clicar no botão
driver.find_element('xpath', '//*[@id="btEntrar"]').click()
time.sleep(3)

#Selecionar ano base e equipamentos
dropdown = driver.find_element(By.ID,'slcAnoB')
driver.quit()

print(dropdown)