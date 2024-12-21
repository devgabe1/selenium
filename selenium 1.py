from selenium import webdriver 
import time

#abrir um navegador
navegador = webdriver.Chrome()
#acessar um site
navegador.get("https://www.youtube.com/")

#maximizar a tela
navegador.maximize_window()

#encontrar um elemento
botao_procura = navegador.find_element("class name", "ytSearchboxComponentSearchForm''")
#clicar no elemento
botao_procura.click()

time.sleep(10)