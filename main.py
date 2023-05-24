#pip install selenium
#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from classes import * 

# id de competições precisam ser atualizadas todos os anos, times não
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


classicos = ('Barcelona', 'Real Madrid', 'Atlético Madrid', 'Paris SG', 'Bayern München', 'Liverpool', 'Manchester City', 'Manchester United', 'Chelsea', 'Juventus', 
             'Napoli','Internazionale', 'Milan', 'Argentina', 'França', 'Inglaterra', 'Alemanha', 'Portugal', 'Espanha', 'Itália')


dados = (corinthians, corinthians_s20, liga_dos_campeoes, mundial_de_clubes, corinthians_fem, nations_league, copa_america_f)
dados = (real_madrid, barcelona) #variaveis com sufixo por último. Ex.: corinthians, corinthians_fem
dados = (corinthians, corinthians_s20, liga_dos_campeoes, corinthians_fem, selecao_brasileira, barcelona, real_madrid)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for dado in dados:
    if dado['tipo'] == 'competicao':
        jogos_por_pagina = 50
    else:
        jogos_por_pagina = 40
    url = dado['link']
    jogos = extrair_jogos(url, driver)
    page = 2
    
    if len(jogos) == jogos_por_pagina:
        njogos = len(jogos)
        while njogos == jogos_por_pagina:
            url = url + '&page=' + str(page)
            driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            jogos_temp = extrair_jogos(url, driver2)
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
    
        if dado['tipo'] == 'time' or dado['tipo'] == 'classico':
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

        if dado['tipo'] == 'classico':
            if time_fora not in classicos or dado['nome'] == time_fora:
                continue
    
        for div_tv in 'a > ', '', 'div > ':
            try:
                tv = jogo.find_element(By.CSS_SELECTOR, f'td.double.right > {div_tv}div > img').get_attribute('title')
                print(f'{tv}')
            except NoSuchElementException as exc:
                pass

        colorId = dado['colorId']
        sumario = time_casa + ' X ' + time_fora
        link_jogo = jogo.find_element(By.CSS_SELECTOR, 'td.result > a').get_attribute('href')
        data_inicio = data_para_isoformat(data, hora, horas=-30)
        data_final = data_para_isoformat(data, hora, horas=+30)
    
        eventos = listar_eventos(service, data_inicio, data_final)
        for evento in eventos:
            if time_casa + ' X' in evento[0] or 'X ' + time_fora in evento[0] or 'Vencedor' in evento[0]:
                excluirEvento(service, evento[1])
                print(f'{evento[0]} excluído.')
    
        data_inicio = data_para_isoformat(data, hora)
        data_final = data_para_isoformat(data, hora, horas=+2)
        criar_evento(service, sumario, data_inicio, data_final, competicao, fase, tv, link_jogo, colorId)
