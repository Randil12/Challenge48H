import pymysql

def selctAll():
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
selctFilter("Terrain-de-sport", "place", "sport")
