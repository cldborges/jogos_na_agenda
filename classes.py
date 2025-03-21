from datetime import date
from selenium.webdriver.common.by import By
from datetime import datetime
from dateutil.relativedelta import relativedelta


def link_uol():
    url_base = 'https://www.uol.com.br/esporte/futebol/central-de-jogos'
    # url_base = 'https://www.uol.com.br/esporte/futebol/central-de-jogos/#/30-10-2024'
    url = url_base
    return url

def data_en__data_pt(data):
    # Converter para o objeto datetime
    data_formatada = datetime.strptime(data, '%Y-%m-%d')

    # Formatar para o padrão brasileiro
    data_pt = data_formatada.strftime('%d-%m-%Y')

    return data_pt


def extrair_jogos(url, driver):
    driver.get(url)
    jogos = driver.find_elements(By.CSS_SELECTOR, '.parent')
    while len(jogos) == 0:
        try:
            erro_ao_carregar = driver.find_element(By.CSS_SELECTOR, '#container > div.zz_error_message').text
            if erro_ao_carregar != '':
                driver.refresh()
                jogos = driver.find_elements(By.CSS_SELECTOR, '.parent')
        except:
            break
    print(f'{len(jogos)} jogos extraídos')
    return jogos


def google_auth():
    #from __future__ import print_function

    import os.path
    from googleapiclient.discovery import build

    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('calendar', 'v3', credentials=creds)
    return service


def criar_evento(service, sumario, data_inicio, data_final, competicao, fase, tv, link_jogo, colorId, data):
    from googleapiclient.errors import HttpError
    hoje = date.today().strftime("%d/%m/%Y")
    data_pt = data
    uol = link_uol()
    try:
        event = {
            'summary': sumario,
            'colorId': colorId,
            'description': f'{competicao}: {fase}\n{tv}\n\n\n{uol}\n\n{link_jogo}\nAtualizado em: {hoje}',
            'start': {
                'dateTime': data_inicio,
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': data_final,
                'timeZone': 'America/Sao_Paulo',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 5}, {'method': 'popup', 'minutes': 30}, {'method': 'email', 'minutes': 60}
                ],
            },
        }
        event = service.events().insert(calendarId='primary', body=event).execute()
        # print('Evento criado: %s' % (event.get('htmlLink')))
        print(sumario, 'criado.')
    except HttpError as error:
        print('Ocorreu um erro: %s' % error)


def data_para_isoformat(data, hora, horas=0):
    datat = data + ' ' + hora
    datafinal = datetime.strptime(datat, '%Y-%m-%d %H:%M')
    if horas != 0:
        horafinal = relativedelta(hours=(horas))
        datafinal = datafinal + horafinal
    return datafinal.isoformat() + '-03:00'


def old_listar_eventos(service, data_inicio, data_final):
    eventos = []
    events = service.events().list(calendarId='primary', maxAttendees=5, timeMin=data_inicio, timeMax=data_final).execute()
    for event in events['items']:
        #print(event['summary'], event['id'])
        eventos.append((event['summary'], event['id']))
    return eventos


def excluirEvento(service, idEvento):
    service.events().delete(calendarId='primary', eventId=idEvento).execute()


def listar_eventos(service, data_inicio, data_final):
    eventos = []
    page_token = None

    while True:
        events = service.events().list(
            calendarId='primary',
            maxResults=100,  # Ajuste conforme necessário
            timeMin=data_inicio,
            timeMax=data_final,
            pageToken=page_token
        ).execute()

        for event in events['items']:
            eventos.append((event['summary'], event['id']))

        page_token = events.get('nextPageToken')
        if not page_token:
            break

    return eventos
