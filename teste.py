import requests
from bs4 import BeautifulSoup
import mysql.connector


host = 'localhost'
user = 'root'
password = ''
database = 'Spider_student'

def service(bar):
# mise en forme 
    barF = bar.replace(' ','-').replace('\'', '')
    print(bar)
# Se connecter à la base de données MySQL
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()


# Se connecter à la page
    url = f'https://www.schlouk-map.com/fr/places/{barF}'
    response = requests.get(url)

# Parser le HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

# Trouver les services proposés
    services_offer = soup.find('table',{'class': 'table table-sm table-borderless table-services mb-0'})
    print(services_offer)


# get all service
    all_service = []
    for service_offer in services_offer.find_all('tr'):
        cells = service_offer.find_all('td')
        for cell in cells:
            [s.extract() for s in cell('span')]
# print('check')
        service = service_offer.find('td', {'class': 'text-truncate'}).text.strip()
        print(service)
        all_service.append(service)
    

# mise en forme   
    all_service = [service.replace('-', '').replace(' ', '_').replace('&','and').replace('/','and') for service in all_service]

# create bdd
    query_create = f"CREATE TABLE IF NOT EXISTS test (nom TEXT,{all_service[0]} TEXT,{all_service[1]} TEXT, {all_service[2]} TEXT,{all_service[3]} TEXT,{all_service[4]} TEXT, {all_service[5]} TEXT,{all_service[6]} TEXT,{all_service[7]} TEXT, {all_service[8]} TEXT,{all_service[9]} TEXT,{all_service[10]} TEXT, {all_service[11]} TEXT,{all_service[12]} TEXT,{all_service[13]} TEXT, {all_service[14]} TEXT)"
    cursor.execute(query_create)


# get reponse


# check and close
    conn.commit()
    conn.close()



service('Le Fennec')