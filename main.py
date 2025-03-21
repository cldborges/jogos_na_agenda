#pip install selenium
#pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from classes import *
from unidecode import unidecode
    
# id de competições precisam ser atualizadas na frequência delas, times não
# Nas competições, o dado que direciona para a competição não é o nome, é o campo edição
dados = (
        {'nome': 'Corinthians', 'tipo': 'time', 'equipe': 2234, 'colorId': 8},
        {'nome': 'Corinthians S20', 'tipo': 'time', 'equipe': 27018, 'sub': 27018, 'colorId': 1},
        {'nome': 'Corinthians Fem.', 'tipo': 'time', 'equipe': 31546, 'sub': 31546, 'colorId': 4},
        {'nome': 'Brasil', 'tipo': 'time', 'equipe': 816, 'colorId': 5},
        {'nome': 'Liga dos Campeões 2024/25', 'tipo': 'competicao', 'edicao': 187408, 'frequencia': 1, 'colorId': 9},
        # {'nome': 'Fifa Intercontinental Cup 2024', 'tipo': 'competicao', 'edicao': 189570, 'frequencia': 1, 'colorId': 6},
        # {'nome': 'Euro 2024', 'tipo': 'competicao', 'edicao': 168932, 'frequencia': 4, 'colorId': 7},
        # {'nome': 'Copa América 2024', 'tipo': 'competicao', 'edicao': 181194, 'frequencia': 4, 'colorId': 2},
        # {'nome': 'Copa Africana de Nações 2023', 'tipo': 'competicao', 'edicao': 162225, 'frequencia': 2, 'colorId': 10},
        {'nome': 'Mundial de Clubes 2025', 'tipo': 'competicao', 'edicao': 186041, 'frequencia': 1, 'colorId': 9},
        {'nome': 'UEFA Nations League 2024/25', 'tipo': 'competicao', 'edicao': 193042, 'frequencia': 2, 'colorId': 9},
        # {'nome': 'Copa América Feminina 2022', 'tipo': 'competicao', 'edicao': 165255, 'frequencia': 4, 'colorId': 3},
        # {'nome': 'Copa do Mundo 2022', 'tipo': 'competicao', 'edicao': 132894, 'frequencia': 4, 'colorId': 6},
        # {'nome': 'Copa do Mundo Feminina 2023', 'tipo': 'competicao', 'edicao' : 145950, 'frequencia': 4, 'colorId': 3},
        {'nome': 'Barcelona', 'tipo': 'classico', 'equipe': 40, 'colorId': 11},
        {'nome': 'Real Madrid', 'tipo': 'classico', 'equipe': 50, 'colorId': 11},
        {'nome': 'Paris SG', 'tipo': 'classico', 'equipe': 127, 'colorId': 11},
        {'nome': 'Bayern München', 'tipo': 'classico', 'equipe': 108, 'colorId': 11},
        {'nome': 'Atlético de Madrid', 'tipo': 'classico', 'equipe': 39, 'colorId': 11},
        {'nome': 'Liverpool', 'tipo': 'classico', 'equipe': 85, 'colorId': 11},
        {'nome': 'Manchester City', 'tipo': 'classico', 'equipe': 86, 'colorId': 11},
        {'nome': 'Manchester United', 'tipo': 'classico', 'equipe': 87, 'colorId': 11},
        {'nome': 'Chelsea', 'tipo': 'classico', 'equipe': 81, 'colorId': 11},
        {'nome': 'Arsenal', 'tipo': 'classico', 'equipe': 75, 'colorId': 11},
        {'nome': 'Tottenham', 'tipo': 'classico', 'equipe': 92, 'colorId': 11},
        {'nome': 'Juventus', 'tipo': 'classico', 'equipe': 64, 'colorId': 11},
        {'nome': 'Napoli', 'tipo': 'classico', 'equipe': 3735, 'colorId': 11},
        {'nome': 'Internazionale', 'tipo': 'classico', 'equipe': 63, 'colorId': 11},
        {'nome': 'Milan', 'tipo': 'classico', 'equipe': 66, 'colorId': 11},
        {'nome': 'Al Nassr', 'tipo': 'classico', 'equipe': 4042, 'colorId': 11},
        {'nome': 'Al-Ahli Jeddah', 'tipo': 'classico', 'equipe': 7816, 'sub': 7816, 'colorId': 11},
        {'nome': 'Al-Ittihad Jeddah', 'tipo': 'classico', 'equipe': 5977, 'sub': 5977, 'colorId': 11},
        {'nome': 'Al Hilal', 'tipo': 'classico', 'equipe': 4043, 'colorId': 11},
        {'nome': 'Inter Miami CF', 'tipo': 'classico', 'equipe': 231636, 'colorId': 11},
        {'nome': 'Argentina', 'tipo': 'classico', 'equipe': 814, 'colorId': 11},
        {'nome': 'França', 'tipo': 'classico', 'equipe': 824, 'colorId': 11},
        {'nome': 'Inglaterra', 'tipo': 'classico', 'equipe': 826, 'colorId': 11},
        {'nome': 'Alemanha', 'tipo': 'classico', 'equipe': 812, 'colorId': 11},
        {'nome': 'Portugal', 'tipo': 'classico', 'equipe': 811, 'colorId': 11},
        {'nome': 'Espanha', 'tipo': 'classico', 'equipe': 822, 'colorId': 11},
        {'nome': 'Itália', 'tipo': 'classico', 'equipe': 828, 'colorId': 11},
        {'nome': 'Holanda', 'tipo': 'classico', 'equipe': 0, 'colorId': 11},
        {'nome': 'Bélgica', 'tipo': 'classico', 'equipe': 0, 'colorId': 11},
        {'nome': 'Países Baixos', 'tipo': 'classico', 'equipe': 0, 'colorId': 11}
)


classicos = ('Campo Neutro', 'Barcelona', 'Real Madrid', 'Atlético de Madrid', 'Paris SG', 'Bayern München', 'Liverpool', 
             'Manchester City', 'Manchester United', 'Chelsea', 'Arsenal', 'Tottenham', 'Juventus', 'Napoli','Internazionale', 'Milan',
             'Al Nassr', 'Al-Ahli Jeddah', 'Al-Ittihad Jeddah', 'Al Hilal', 'Inter Miami CF'
             'Argentina', 'França', 'Inglaterra', 'Alemanha', 'Portugal', 'Espanha', 'Itália', 'Holanda', 'Bélgica', 'Países Baixos')

# caracteres_especiais = ((' ', '-'), ('é', 'e'), ('ü', 'u'), ('ç', 'c'))

driver = webdriver.Chrome()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.minimize_window()

for dado in dados:
    print('--------------------------------------------------------------')
    print(dado['nome'])
    if dado['tipo'] == 'competicao':
        jogos_por_pagina = 50
        # url = dado['link']
        competicao_url = dado['nome'].lower()
        competicao_url  = unidecode(competicao_url)
        if ' ' in competicao_url:
            competicao_url = competicao_url.replace(' ', '-')
        if '/' in competicao_url:
            competicao_url = competicao_url.replace('/', '-')
        
        # 'https://www.ogol.com.br/edicao/liga-dos-campeoes-2023-24/176177/calendario'
        url = f'https://www.ogol.com.br/edicao/{competicao_url}/{dado["edicao"]}/calendario'
        # url = f'https://www.ogol.com.br/edition_matches.php?id={dado["edicao"]}/calendario'
    else:
        jogos_por_pagina = 40
        # url = f'https://www.ogol.com.br/team_matches.php?grp=0&ond=&epoca_id={epoca}&compet_id_jogos=0&ved=&epoca_id={epoca}&comfim=0&id={dado["equipe"]}&equipa_1={dado["equipe"]}&menu=allmatches'
        equipe = dado['nome'].lower()
        if ' ' in equipe:
            equipe = equipe.replace(' ', '-')
        equipe = unidecode(equipe)
        if 'sub' in dado.keys():
            url = f'https://www.ogol.com.br/equipe/{equipe}/{dado["sub"]}/todos-os-jogos'
        else:
            url = f'https://www.ogol.com.br/equipe/{equipe}/todos-os-jogos'
    jogos = extrair_jogos(url, driver)
    page = 2
    if len(jogos) == jogos_por_pagina:
        njogos = len(jogos)
        while njogos == jogos_por_pagina:
            # url = url + '&page=' + str(page)
            url_paginas = url + '?page=' + str(page)
            driver2 = webdriver.Chrome()
            # driver2 = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver2.minimize_window()
            jogos_temp = extrair_jogos(url_paginas, driver2)
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
        if dado['tipo'] == 'time' or dado['tipo'] == 'classico':
            mando = jogo.find_element(By.XPATH, 'td[4]').text
            if mando == '(C)' or mando == '':
                time_casa = dado['nome']
                time_fora = jogo.find_element(By.CSS_SELECTOR, 'td.text').text
            if mando == '(F)':
                time_fora = dado['nome']
                time_casa = jogo.find_element(By.CSS_SELECTOR, 'td.text').text
            # if mando == '':
            #     time_casa = dado['nome']
            #     time_fora = 'Campo Neutro'
            data = jogo.find_element(By.CSS_SELECTOR, 'td.double').text
            fase = jogo.find_element(By.CSS_SELECTOR, 'td.away').text
            # competicao = jogo.find_element(By.XPATH, '//*/td[7]/div/div[2]/a').text
            competicao = jogo.find_elements(By.CLASS_NAME, 'text')[1].text
        if dado['tipo'] == 'classico':
            if time_fora not in classicos or dado['nome'] == time_fora:
                continue
        # lista de possíveis tags antes da tag do canal de transmissão
        for div_tv in 'a > ', '', 'div > ', 'div > a > ':
            try:
                tv = jogo.find_element(By.CSS_SELECTOR, f'td.double.right > {div_tv}div > img').get_attribute('title')
                print(f'{tv}')
            except NoSuchElementException as exc:
                pass
        colorId = dado['colorId']
        sumario = time_casa + ' X ' + time_fora
        if fase == 'F':
            sumario = '🏆 ' + sumario
        elif fase == 'SF' or fase == 'QF' or fase == '1/8':
            sumario = '☠️ ' + sumario
        link_jogo = jogo.find_element(By.CSS_SELECTOR, 'td.result > a').get_attribute('href')
        data_inicio = data_para_isoformat(data, hora, horas=-30)
        data_final = data_para_isoformat(data, hora, horas=+30)
        eventos = listar_eventos(service, data_inicio, data_final)
        for evento in eventos:
            if time_casa + ' X' in evento[0] or 'X ' + time_fora in evento[0] or 'Vencedor' in evento[0] or 'Winner' in evento[0] or 'Loser' in evento[0]:
                excluirEvento(service, evento[1])
                print(f'{evento[0]} excluído.')
        data_inicio = data_para_isoformat(data, hora)
        data_final = data_para_isoformat(data, hora, horas=+2)
        criar_evento(service, sumario, data_inicio, data_final, competicao, fase, tv, link_jogo, colorId, data)
