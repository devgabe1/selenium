from selenium import webdriver 
import time

#abrir um navegador
navegador = webdriver.Chrome()
#acessar um site
navegador.get("https://www.youtube.com")

#maximizar a tela
navegador.maximize_window()

time.sleep(90)