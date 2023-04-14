import mysql.connector
import requests
from bs4 import BeautifulSoup
# import sqlite3
# import psycopg2
from Get_yes_no import service

host = 'db4free.net'
user = 'challenge48h'
password = 'rootroot'
database = 'spiderbase'

conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

query_create = f"CREATE TABLE IF NOT EXISTS lyon (nom TEXT)"
cursor.execute(query_create)
count =0
for page in range(1,11):
    url =f"https://www.schlouk-map.com/fr/cities/lyon?page={page}"
    response = requests.get(url)
    print(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    bars = soup.find_all('h2',{'class': 'h4 mb-0'})
    print(bars)
    count += 1
    for bar in bars:
        print(count)
        nom = bar.find('a', {'class': 'name'}).text.strip()
        query = """INSERT INTO lyon (nom) VALUES (%s)"""
        params = [nom]
        barF = nom.replace('-!', '').replace('Red-House','red-house-1').replace('Moi-JMen-Fous-Je-Triche','moi-jm-en-fous-je-triche').replace('.', '-').replace('(','').replace(')','').replace(' - ', '-').replace(' & ','-').replace('&','-').replace(' ','-').replace('\'', '').replace('’','')
        service(barF)
        cursor.execute(query, params)
        conn.commit()

conn.close()
