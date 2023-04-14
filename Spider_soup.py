import mysql.connector
import requests
from bs4 import BeautifulSoup
# import sqlite3
# import psycopg2
from Get_yes_no import service


def spiderBarSoup(table, nbPages):
    host = 'db4free.net'
    user = 'challenge48h'
    password = 'rootroot'
    database = 'spiderbase'
    # host = 'localhost'
    # user = 'root'
    # password = ''
    # database = 'spider_student'
# connect to db
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
   
# scrapping page
    for page in range(1,nbPages):
        url =f"https://www.schlouk-map.com/fr/cities/{table}?page={page}"
        response = requests.get(url)
        print(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        bars = soup.find_all('h2',{'class': 'h4 mb-0'})
# scrapping bars
        for bar in bars:
            name = bar.find('a', {'class': 'name'}).text.strip()
            barFormat = name.replace('-!', '').replace('Red-House','red-house-1').replace('Moi-JMen-Fous-Je-Triche','moi-jm-en-fous-je-triche').replace('.', '-').replace('(','').replace(')','').replace(' - ', '-').replace(' & ','-').replace('&','-').replace(' ','-').replace('\'', '').replace('’','')
            service(name,barFormat,table)
            # print(params)
            print(barFormat)
            print(name)
            # cursor.execute(query, params)
            conn.commit()
    conn.close()


# spiderBarSoup("lille", 6)
# spiderBarSoup("clermont-ferrand",3)
# spiderBarSoup("lyon",11)





def spiderSportSoup(place,url, nbPages):
    host = 'db4free.net'
    user = 'challenge48h'
    password = 'rootroot'
    database = 'spiderbase'
    
    # host = 'localhost'
    # user = 'root'
    # password = ''
    # database = 'spider_student'
# connect to db
    conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
# create database
    query_create = f"CREATE TABLE IF NOT EXISTS sport (place TEXT,name TEXT)"
    cursor.execute(query_create)
# scrapping page
    for page in range(0,nbPages):
        url_Final= url + str(page)
        response = requests.get(url_Final)
        print(url)
        soup = BeautifulSoup(response.content, 'html.parser')
# scapping data
        sports = soup.find_all('div', {'class':'actu-texte'})
        for sport in sports:
            name = sport.find('h2').text.strip()
            query = """INSERT INTO sport (place, name) VALUES (%s,%s)"""
            cursor.execute(query, (place,name))
            conn.commit()

    conn.close()
    
# spiderSportSoup("Gymnases-Salles-Halles" ,"https://www.lyon.fr/equipements?search_api_fulltext=&field_secteur_geographique=All&items_per_page=30&field_sous_types_tmp=1387&field_sous_types_tmp_bis=All&field_sous_types=All&filter_theme=Filtrer%20les%20types&filter_sous_theme=Filtrer%20les%20sous-types&page=",4)
# spiderSportSoup("Patinoire" ,"https://www.lyon.fr/equipements?search_api_fulltext=&field_secteur_geographique=All&items_per_page=1&field_sous_types_tmp=1387&field_sous_types_tmp_bis=1639&field_sous_types=All&filter_theme=Filtrer%20les%20types&filter_sous_theme=Filtrer%20les%20sous-types&page=",2)
# spiderSportSoup("Piscine" ,"https://www.lyon.fr/equipements?search_api_fulltext=&field_secteur_geographique=All&items_per_page=10&field_sous_types_tmp=1387&field_sous_types_tmp_bis=1602&field_sous_types=All&filter_theme=Filtrer%20les%20types&filter_sous_theme=Filtrer%20les%20sous-types&page=",3)
# spiderSportSoup("Stade" ,"https://www.lyon.fr/equipements?search_api_fulltext=&field_secteur_geographique=All&items_per_page=10&field_sous_types_tmp=1387&field_sous_types_tmp_bis=1513&field_sous_types=All&filter_theme=Filtrer%20les%20types&filter_sous_theme=Filtrer%20les%20sous-types&page=",3)
# spiderSportSoup("Terrain-de-boules" ,"https://www.lyon.fr/equipements?search_api_fulltext=&field_secteur_geographique=All&items_per_page=10&field_sous_types_tmp=1387&field_sous_types_tmp_bis=1464&field_sous_types=All&filter_theme=Filtrer%20les%20types&filter_sous_theme=Filtrer%20les%20sous-types&page=",4)
# spiderSportSoup("Terrain-de-sport" ,"https://www.lyon.fr/equipements?search_api_fulltext=&field_secteur_geographique=All&items_per_page=10&field_sous_types_tmp=1387&field_sous_types_tmp_bis=1460&field_sous_types=All&filter_theme=Filtrer%20les%20types&filter_sous_theme=Filtrer%20les%20sous-types&page=",4)