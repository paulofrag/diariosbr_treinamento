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
iah-tipk-dhr

def acessar_pagina_dinamica(link):
    navegador = webdriver.Chrome
    navegador.get(link)
    # clicar no download pdf
    # find_element_find_elements
    download pdf = navegador find.element 
    # pegar data
    # pegar número da edição
    # clicar na página seguinte
    

def main():
    link = "https://www.miguelopolis.sp.gov.br/paginas/portal/diarioOficial"
    acessar_pagina_dinamica(link)
    
    
if __name__ == "__main__":
    main()