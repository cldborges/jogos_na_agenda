from selenium.webdriver.common.by import By
from classes import *
from selenium.common.exceptions import *

'''service = google_auth()

data = '2022-03-15'
hora = '17:00'

data_inicio = data_para_isoformat(data, hora) + '-03:00'
data_final = data_para_isoformat(data, hora, horas=+6) + 'Z'''

#eventos = listar_eventos(service, data_inicio, data_final)
'''for event in eventos['items']:
    print(event['id'])
    excluirEvento(service, event['id'])'''
'''idEvento = eventos['items']['id']
print(idEvento)'''
#excluirEvento(service, )

#url = 'https://www.ogol.com.br/edition_matches.php?id_edicao=161104&fase_in&equipa=0&estado=&filtro=&op=calendario&page=5'
#url = 'https://www.ogol.com.br/team_matches.php?id=26824&grp=1'
url = 'https://www.ogol.com.br/team_matches.php?id=2234&grp=1&epoca_id=151'
#url = 'https://www.ogol.com.br/edition_matches.php?id_edicao=155920&fase_in&equipa=0&estado=&filtro=&op=calendario&page=3'

jogos = extrair_jogos(url)

for jogo in jogos:
    try:
        local = jogo.find_element(By.XPATH, 'td[4]').text
        #local = jogo.find_element(By.CSS_SELECTOR, 'td: nth - child(4)').text
        print(local)
    except NoSuchElementException as exc:
        pass

'''for i, jogo in enumerate(jogos):
    try:
        tv = jogo.find_element(By.CSS_SELECTOR, 'td.multimedia.right').text
        print(f'{i}, {tv}')
    except NoSuchElementException as exc:
        pass

    try:
        tv = jogo.find_elements(By.LINK_TEXT, 'cd')
        for texto in tv:
            print(f'{i}, {texto.text}')
    except NoSuchElementException as exc:
        pass

    try:
        tv = jogo.find_element(By.CSS_SELECTOR, 'td.double.right > div > img').get_attribute('title')
        print(f'{i}, {tv}')
    except NoSuchElementException as exc:
        pass'''
