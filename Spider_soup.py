import mysql.connector
import requests
from bs4 import BeautifulSoup
# import sqlite3
# import psycopg2



host = 'localhost'
user = 'root'
password = ''
database = 'Spider_student'
print("ab")
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

query_create = f"CREATE TABLE IF NOT EXISTS lyon (nom TEXT)"
cursor.execute(query_create)
print("abccc")
for page in range(1,11):
    url =f"https://www.schlouk-map.com/fr/cities/lyon?page={page}"
    response = requests.get(url)
    print(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    bars = soup.find_all('h2',{'class': 'h4 mb-0'})
    print(bars)
    for bar in bars:
        print("azzzzb")
        nom = bar.find('a', {'class': 'name'}).text.strip()
        query = """INSERT INTO lyon (nom) VALUES (%s)"""
        params = [nom]
        cursor.execute(query, params)
        conn.commit()



conn.close()




