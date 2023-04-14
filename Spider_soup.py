import mysql.connector
import requests
from bs4 import BeautifulSoup
from Get_yes_no import service

def spiderSoup(table, nbPages):
    # host = 'db4free.net'
    # user = 'challenge48h'
    # password = 'rootroot'
    # database = 'spiderbase'
    # host = 'localhost'
    # user = 'root'
    # password = ''
    # database = 'spider_student'
    
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()

    table_utl = table.replace('-','')
    # query_create = f"CREATE TABLE IF NOT EXISTS "+table_utl+" (nom TEXT)"
    # cursor.execute(query_create)
    count =0
    for page in range(1,nbPages):
        url =f"https://www.schlouk-map.com/fr/cities/{table}?page={page}"
        response = requests.get(url)
        print(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        bars = soup.find_all('h2',{'class': 'h4 mb-0'})
        print(bars)
        count += 1
        for bar in bars:
            print(count)
            nom = bar.find('a', {'class': 'name'}).text.strip()
            # query = """INSERT INTO """+table_utl+""" (nom) VALUES (%s)"""
            # params = [nom]
            barF = nom.replace('-!', '').replace('Red-House','red-house-1').replace('Moi-JMen-Fous-Je-Triche','moi-jm-en-fous-je-triche').replace('.', '-').replace('(','').replace(')','').replace(' - ', '-').replace(' & ','-').replace('&','-').replace(' ','-').replace('\'', '').replace('’','')
            service(nom,barF,table)
            # print(params)
            print(barF)
            print(nom)
            # cursor.execute(query, params)
            conn.commit()



    conn.close()
    
def spiderSportSoup(table, nbPages):
    # host = 'db4free.net'
    # user = 'challenge48h'
    # password = 'rootroot'
    # database = 'spiderbase'
    # host = 'localhost'
    # user = 'root'
    # password = ''
    # database = 'spider_student'
    
    # conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    # cursor = conn.cursor()

    table_utl = table.replace('-','')
    # query_create = f"CREATE TABLE IF NOT EXISTS "+table_utl+" (nom TEXT)"
    # cursor.execute(query_create)
    count =0
    for page in range(1,nbPages):
        url =f"https://www.lyon.fr/equipements?search_api_fulltext=&field_secteur_geographique=All&items_per_page=30&field_sous_types_tmp=1387&field_sous_types_tmp_bis=All&field_sous_types=All&filter_theme=Filtrer%20les%20types&filter_sous_theme=Filtrer%20les%20sous-types&page={page}"
        response = requests.get(url)
        print(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        bars = soup.find_all('div', {'class':'actu-texte'})
        count += 1
        for bar in bars:
            print(count)
            nom = bar.find('h2').text.strip()
            # query = """INSERT INTO """+table_utl+""" (nom) VALUES (%s)"""
            params = [nom]
            # barF = nom.replace('-!', '').replace('Red-House','red-house-1').replace('Moi-JMen-Fous-Je-Triche','moi-jm-en-fous-je-triche').replace('.', '-').replace('(','').replace(')','').replace(' - ', '-').replace(' & ','-').replace('&','-').replace(' ','-').replace('\'', '').replace('’','')
            # service(nom,barF,table)
            print(params)
    #         cursor.execute(query, params)
    #         conn.commit()

    # conn.close()
    
spiderSportSoup("lyon" ,6)