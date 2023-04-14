import pymysql

def selctAll(table):
    # Connect to the database
    connection = pymysql.connect(
        host='db4free.net',
        user  ='challenge48h',
        password='rootroot',
        database='spiderbase'
    )
# Create a cursor object
    cursor = connection.cursor()
# Execute a query
    cursor.execute(f"SELECT * FROM {table}")
# Fetch data from the database
    result = cursor.fetchall()
# Print the result
    print(result)
# Close the cursor and the database connection
    cursor.close()
    connection.close()
    
# test
# selctAll("sport")  
    
    
def selctAllFromCity(value):
    # Connect to the database
    connection = pymysql.connect(
        host='db4free.net',
        user  ='challenge48h',
        password='rootroot',
        database='spiderbase'
    )
# Create a cursor object
    cursor = connection.cursor()
# Execute a query
    cursor.execute(f"SELECT * FROM services WHERE cities = '{value}'")
# Fetch data from the database
    result = cursor.fetchall()
# Print the result
    print(result)
# Close the cursor and the database connection
    cursor.close()
    connection.close()
    
# test
# selctAllFromCity("lyon")

def selctFilter(value, column, table):
    # Connect to the database
    connection = pymysql.connect(
        host='db4free.net',
        user  ='challenge48h',
        password='rootroot',
        database='spiderbase'
    )
# Create a cursor object
    cursor = connection.cursor()
# Execute a query
    cursor.execute(f"SELECT * FROM {table} WHERE {column} = '{value}'")
# Fetch data from the database
    result = cursor.fetchall()
# Print the result
    print(result)
# Close the cursor and the database connection
    cursor.close()
    connection.close()

# test
# selctFilter("Terrain-de-sport", "place", "sport")

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

def get_bar_by_city(city):
    city = city.lower()
    cursor.execute(f"SELECT nom FROM services WHERE cities = '{city}' ")
    result = list(set(cursor.fetchall()))
    l = [x[0] for x in result]
    return l

def get_name_bar(option , option2 , option3):
    cursor.execute(f'SELECT nom FROM services WHERE {option} = "Oui" AND {option2} = "Oui" AND {option3} = "Oui"')
    result = list(set(cursor.fetchall()))
    l = [x[0] for x in result]
    return l



