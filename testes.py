from selenium.webdriver.common.by import By
from classes import *
from selenium.common.exceptions import *
from datetime import datetime, date

print(date.today().strftime("%d/%m/%Y"))

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
print(idEvento)
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

for i, jogo in enumerate(jogos):
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


corinthians_s20 = {'nome': 'Corinthians S20', 'tipo': 'time',
                   'link': 'https://www.ogol.com.br/team_matches.php?id=27018', 'colorId': 1}
liga_dos_campeoes = {'nome': 'Liga dos Campeões 2022/23', 'tipo': 'competicao',
                     'link': 'https://www.ogol.com.br/edition_matches.php?id=166025', 'frequencia': 1, 'colorId': 9}
corinthians = {'nome': 'Corinthians', 'tipo': 'time',
                     'link': 'https://www.ogol.com.br/team_matches.php?id=2234', 'colorId': 8}
can = {'nome': 'Copa Africana de Nações 2023', 'tipo': 'competicao',
                     'link': 'https://www.ogol.com.br/edition_matches.php?id=162225', 'frequencia': 2, 'colorId': 10}
selecao_brasileira = {'nome': 'Brasil', 'tipo': 'time',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=816', 'colorId': 5}
mundial_de_clubes = {'nome': 'Mundial de Clubes 2022', 'tipo': 'competicao',
                     'link': 'https://www.ogol.com.br/edition_matches.php?id=170592', 'frequencia': 1, 'colorId': 9}
corinthians_fem = {'nome': 'Corinthians Fem.', 'tipo': 'time',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=31546', 'colorId': 4}
nations_league = {'nome': 'Uefa Nation League 2022', 'tipo': 'competicao',
                     'link': 'https://www.ogol.com.br/edition_matches.php?id=161164', 'frequencia': 2, 'colorId': 9}
copa_america_f = {'nome': 'Copa América Feminina 2022', 'tipo': 'competicao',
                     'link': 'https://www.ogol.com.br/edition_matches.php?id=165255', 'frequencia': 4, 'colorId': 3}
copa_mundo = {'nome': 'Copa do Mundo 2022', 'tipo': 'competicao',
                     'link': 'https://www.ogol.com.br/edition_matches.php?id=132894', 'frequencia': 4, 'colorId': 6}
barcelona = {'nome': 'Barcelona', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=40', 'colorId': 11}
real_madrid = {'nome': 'Real Madrid', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=50', 'colorId': 11}
psg = {'nome': 'Paris SG', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=127', 'colorId': 11}
bayern_munchen = {'nome': 'Bayern München', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=108', 'colorId': 11}
atletico_madrid = {'nome': 'Atlético Madrid', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=39', 'colorId': 11}
liverpool = {'nome': 'Liverpool', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=85', 'colorId': 11}
manchester_city = {'nome': 'Manchester City', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=86', 'colorId': 11}
manchester_united = {'nome': 'Manchester United', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=87', 'colorId': 11}
chelsea = {'nome': 'Chelsea', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=81', 'colorId': 11}
juventus = {'nome': 'Juventus', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=64', 'colorId': 11}
napoli = {'nome': 'Napoli', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=3735', 'colorId': 11}
internazionale = {'nome': 'Internazionale', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=63', 'colorId': 11}
milan = {'nome': 'Milan', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=66', 'colorId': 11}
argentina = {'nome': 'Argentina', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=814', 'colorId': 11}
franca = {'nome': 'França', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=824', 'colorId': 11}
inglaterra = {'nome': 'Inglaterra', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=826', 'colorId': 11}
alemanha = {'nome': 'Alemanha', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=812', 'colorId': 11}
portugal = {'nome': 'Portugal', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=811', 'colorId': 11}
espanha = {'nome': 'Espanha', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=822', 'colorId': 11}
italia = {'nome': 'Itália', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=828', 'colorId': 11}

dados = ({'nome': 'Espanha', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=822', 'colorId': 11}, {'nome': 'Itália', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=828', 'colorId': 11}, {'nome': 'Espanha', 'tipo': 'classico',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=822', 'colorId': 11})

print (dados[0])

for dado in dados:
    print(dado['nome'])