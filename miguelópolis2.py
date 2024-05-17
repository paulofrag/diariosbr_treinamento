import json
import requests
import urllib.request
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
#iah-tipk-dhr

def acessar_pagina_dinamica(link):
    navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    navegador.get(link)
    lista_diarios = navegador.find_elements(By.XPATH, "//div[@class='ui-datagrid-column ui-g-12 ui-md-4']") 
    print (len(lista_diarios))
    for diario in lista_diarios: 
        numero_diario= diario.find_element (By.XPATH, "//h4[@class='mb-0']").text
        print(numero_diario)
        

def main():
    link = "https://www.miguelopolis.sp.gov.br/paginas/portal/diarioOficial"
    acessar_pagina_dinamica(link)
    
    
if __name__ == "__main__":
    main()