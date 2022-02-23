# pip install python-dateutil

def extrair_jogos(url):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

#   driver = webdriver.Chrome(r"C:\Users\Claudio\Google Drive\Python\chromedriver.exe")
    driver = webdriver.Chrome()
    driver.get(url)
    jogos = driver.find_elements(By.CSS_SELECTOR, '.parent')
    while len(jogos) == 0:
        driver.refresh()
        jogos = driver.find_elements(By.CSS_SELECTOR, '.parent')
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


def criar_evento(service, sumario, data_inicio, data_final, competicao, fase, tv):

    from googleapiclient.errors import HttpError

    try:
        event = {
            'summary': sumario,
            'description': f'{competicao}: {fase} \n{tv}',
            'start': {
                'dateTime': data_inicio,
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': data_final,
                'timeZone': 'America/Sao_Paulo',
            }
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Evento criado: %s' % (event.get('htmlLink')))

    except HttpError as error:
        print('Ocorreu um erro: %s' % error)


def data_para_isoformat(data, hora, horas=0):


    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    datat = data + ' ' + hora
    datafinal = datetime.strptime(datat, '%Y-%m-%d %H:%M')
    if horas != 0:
        horafinal = relativedelta(hours=(horas))
        datafinal = datafinal + horafinal
    return datafinal.isoformat() + '-03:00'


def listar_eventos(service, data_inicio, data_final):

    eventos = []
    events = service.events().list(calendarId='primary', maxAttendees=5, timeMin=data_inicio, timeMax=data_final).execute()
    for event in events['items']:
        #print(event['summary'], event['id'])
        eventos.append((event['summary'], event['id']))
    return eventos


def excluirEvento(service, idEvento):
    service.events().delete(calendarId='primary', eventId=idEvento).execute()
