#pip install selenium
#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from classes import *

# id de competições precisam ser atualizadas todos os anos, times não
corinthians_s20 = {'nome': 'Corinthians S20', 'tipo': 'time',
                   'link': 'https://www.ogol.com.br/team_matches.php?id=27018&grp=1&epoca_id=151', 'colorId': 1}
liga_dos_campeoes = {'nome': 'Liga dos Campeões', 'tipo': 'competicao',
                     'link': 'https://www.ogol.com.br/edition_matches.php?id=166025', 'colorId': 9}
corinthians = {'nome': 'Corinthians', 'tipo': 'time',
                     'link': 'https://www.ogol.com.br/team_matches.php?id=2234&grp=1&epoca_id=151', 'colorId': 8}
can = {'nome': 'Copa Africana de Nações', 'tipo': 'competicao',
                     'link': 'https://www.ogol.com.br/edition_matches.php?id=136090', 'colorId': 10}
selecao_brasileira = {'nome': 'Brasil', 'tipo': 'time',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=816&grp=1&epoca_id=151', 'colorId': 5}
mundial_de_clubes = {'nome': 'Mundial de Clubes', 'tipo': 'competicao',
                     'link': 'https://www.ogol.com.br/edition_matches.php?id=170592', 'colorId': 9}
corinthians_fem = {'nome': 'Corinthians Fem.', 'tipo': 'time',
                      'link': 'https://www.ogol.com.br/team_matches.php?id=31546&grp=1&epoca_id=151', 'colorId': 4}
nations_league = {'nome': 'Uefa Nation League', 'tipo': 'competicao',
                     'link': 'https://www.ogol.com.br/edition_matches.php?id=161165', 'colorId': 9}

dados = (selecao_brasileira, liga_dos_campeoes, corinthians_s20, corinthians_fem, nations_league, corinthians)
dados = (can, liga_dos_campeoes) # tem que ter 2 no mínimo

for dado in dados:
    if dado['tipo'] == 'competicao':
        jogos_por_pagina = 50
    else:
        jogos_por_pagina = 40
    url = dado['link']
    jogos = extrair_jogos(url)
    page = 2
    
    if len(jogos) == jogos_por_pagina:
        njogos = len(jogos)
        while njogos == jogos_por_pagina:
            url = url + '&page=' + str(page)
            jogos_temp = extrair_jogos(url)
            njogos = len(jogos_temp)
            page += 1
            jogos.extend(jogos_temp)
        print(f'{len(jogos)} jogos no total')
    
    service = google_auth()
    
    for jogo in jogos:  
        resultado = jogo.find_element(By.CSS_SELECTOR, 'td.result').text
        if resultado != '-' and resultado != 'vs':
            continue

        hora = jogo.find_element(By.XPATH, 'td[3]').text
        if hora == '':
            hora = '12:00'

        tv = 'Sem informações de local de transmissão'

        if dado['tipo'] == 'competicao':
            time_casa = jogo.find_element(By.CSS_SELECTOR, 'td.text.home').text
            time_fora = jogo.find_element(By.CSS_SELECTOR, 'td.text.away').text
            data = jogo.find_element(By.CSS_SELECTOR, 'td.date').text
            fase = jogo.find_element(By.CSS_SELECTOR, 'td.phase').text
            competicao = dado['nome']
            #div_tv = ''
    
        if dado['tipo'] == 'time':
            mando = jogo.find_element(By.XPATH, 'td[4]').text
            if mando == '(C)':
                time_casa = dado['nome']
                time_fora = jogo.find_element(By.CSS_SELECTOR, 'td.text').text
            if mando == '(F)':
                time_fora = dado['nome']
                time_casa = jogo.find_element(By.CSS_SELECTOR, 'td.text').text
            data = jogo.find_element(By.CSS_SELECTOR, 'td.double').text
            fase = jogo.find_element(By.CSS_SELECTOR, 'td.away').text
            competicao = jogo.find_element(By.XPATH, '//*/td[7]/div/div[2]/a').text
            #div_tv = 'a > '

        for div_tv in 'a > ', '', 'div > ':
            try:
                tv = jogo.find_element(By.CSS_SELECTOR, f'td.double.right > {div_tv}div > img').get_attribute('title')
                print(f'{tv}')
            except NoSuchElementException as exc:
                pass

        colorId = dado['colorId']
        sumario = time_casa + ' X ' + time_fora
        link_jogo = jogo.find_element(By.CSS_SELECTOR, 'td.result > a').get_attribute('href')
        data_inicio = data_para_isoformat(data, hora, horas=-24)
        data_final = data_para_isoformat(data, hora, horas=+24)
    
        eventos = listar_eventos(service, data_inicio, data_final)
        for evento in eventos:
            if time_casa + ' X' in evento[0] or 'X ' + time_fora in evento[0] or 'Vencedor' in evento[0]:
                excluirEvento(service, evento[1])
                print(f'{evento[0]} excluído.')
    
        data_inicio = data_para_isoformat(data, hora)
        data_final = data_para_isoformat(data, hora, horas=+2)
        criar_evento(service, sumario, data_inicio, data_final, competicao, fase, tv, link_jogo, colorId)
