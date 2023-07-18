from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = 'https://www.uol.com.br/esporte/futebol/central-de-jogos/#/18-07-2023'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.minimize_window()
driver.get(url)
jogos = driver.find_elements(By.CLASS_NAME, 'match-full')

for jogo in jogos:
    if jogo.find_element(By.CLASS_NAME, 'match-info').text != '':
        dados_jogo = jogo.get_attribute('data-cfg')
        if '18/07' in dados_jogo:
            print(dados_jogo)
            print(jogo.find_element(By.CLASS_NAME, 'match-info').text)
            try:
                print(jogo.find_element(By.CLASS_NAME, 'transmitions').text)
            except:
                pass
# print(len(jogos))
# print(jogos[15].get_attribute('data-cfg'))