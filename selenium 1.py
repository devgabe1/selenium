from selenium import webdriver 
import time

#abrir um navegador
navegador = webdriver.Chrome()
navegador.get("https://www.youtube.com")

time.sleep(90)