import pymysql


# Connect to the database
connection = pymysql.connect(
    host='db4free.net',
    user='challenge48h',
    password='rootroot',
    db='spiderbase'
)
# Create a cursor object
cursor = connection.cursor()


def get_bar(ville):
    ville = ville.lower()
    cursor.execute(f"SELECT * FROM {ville}")
    result = cursor.fetchall()
   
    cursor.close()
    connection.close()
    return list(set(result))

def get_all_column():
    cursor.execute("SELECT * FROM information_schema.columns WHERE table_name = 'services' ")
    result = list(cursor.fetchall())
    l = result
    newl = []
    for i in range(len(l)):
        newl.append(l[i][3])
        
    return newl

