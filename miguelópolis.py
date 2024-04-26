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
    # clicar no download 
    # find_element e find_elements
    lista_data= navegador.find_elements(By.XPATH,"//span [@class='font-weight-light text-dark']")
    print(len(lista_data))
    for diario in lista_data: 
        
        # pegar data e quantidade de páginas
        data = diario
        print (data.text)
        # pegar número da edição e ano.
    lista_edição= navegador.find_elements (By.XPATH, "//span [@class='h4 class=mb-0']")
    for diario in lista_edição:
        print (diario)
        
        
        # regular ou extraordinária
    lista_tipo = navegador.find_elements (By.XPATH, "//span [@class= 'h4 class=mt-0']")
    for diario in lista_tipo:
        print (diario)
        
        

        #lista_diarios= navegador.find_element (By.XPATH,"//*[@id='formDiarioOficial:listaArquivos_content']/div[1]/div[1]/div/div/div/div/div[1]/div/h4[2]")
    
        # clicar na página seguinte
        #lista_diarios= navegador.find_element (By.XPATH,"//*[@id='formDiarioOficial:listaArquivos_paginator_bottom']/span[1]/a[1]")

def main():
    link = "https://www.miguelopolis.sp.gov.br/paginas/portal/diarioOficial"
    acessar_pagina_dinamica(link)
    
    
if __name__ == "__main__":
    main()