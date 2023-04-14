import requests
from bs4 import BeautifulSoup
import mysql.connector

def service(bar_rl,bar, city):
    # host = 'localhost'
    # user = 'root'
    # password = ''
    # database = 'spider_student'
    host = 'db4free.net'
    user = 'challenge48h'
    password = 'rootroot'
    database = 'spiderbase'
# format
    bar = bar.replace('-!', '').replace('Red-House','red-house-1').replace('Moi-JMen-Fous-Je-Triche','moi-jm-en-fous-je-triche').replace('.', '-').replace('(','').replace(')','').replace(' - ', '-').replace(' & ','-').replace('&','-').replace(' ','-').replace('\'', '').replace('’','')
    print(bar)
# SConnect to MySQL Database
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()


# Connect to scrapped website
    url = f'https://www.schlouk-map.com/fr/places/{bar}'
    response = requests.get(url)

# Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

# Find every service 
    services_offer = soup.find('table',{'class': 'table table-sm table-borderless table-services mb-0'})
    # print(services_offer)


# get response of services
    result_tab = []
    for service_result in services_offer.find_all('td', {'class','float-right float-md-none'}):
        result = service_result.find('span').text.strip()
        print(result)
        result_tab.append(result)
    print(result_tab)


# get all services
    all_service = []
    for service_offer in services_offer.find_all('tr'):
        cells = service_offer.find_all('td')
        for cell in cells:
            [s.extract() for s in cell('span')]
# print('check')
        service = service_offer.find('td', {'class': 'text-truncate'}).text.strip()
        print(service)
        all_service.append(service)
    

# format   
    all_service = [service.replace('-', '').replace(' ', '_').replace('&','and').replace('/','and') for service in all_service]

# create database
    query_create = f"CREATE TABLE IF NOT EXISTS services (cities TEXT,nom TEXT,{all_service[0]} TEXT,{all_service[1]} TEXT, {all_service[2]} TEXT,{all_service[3]} TEXT,{all_service[4]} TEXT, {all_service[5]} TEXT,{all_service[6]} TEXT,{all_service[7]} TEXT, {all_service[8]} TEXT,{all_service[9]} TEXT,{all_service[10]} TEXT, {all_service[11]} TEXT,{all_service[12]} TEXT,{all_service[13]} TEXT, {all_service[14]} TEXT)"
    cursor.execute(query_create)
    
# insert into
    query_insert = f"INSERT INTO services (cities ,nom , {all_service[0]},{all_service[1]}, {all_service[2]} ,{all_service[3]} ,{all_service[4]} , {all_service[5]} ,{all_service[6]} ,{all_service[7]} , {all_service[8]} ,{all_service[9]} ,{all_service[10]} , {all_service[11]} ,{all_service[12]} ,{all_service[13]} , {all_service[14]}) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query_insert, (city,bar_rl,result_tab[0],result_tab[1],result_tab[2],result_tab[3],result_tab[4],result_tab[5],result_tab[6],result_tab[7],result_tab[8],result_tab[9],result_tab[10],result_tab[11],result_tab[12],result_tab[13],result_tab[14],))


# check and close
    conn.commit()
    conn.close()