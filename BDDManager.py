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
    cursor.execute("SELECT * FROM *")
# Fetch data from the database
    result = cursor.fetchall()
# Print the result
    print(result)
# Close the cursor and the database connection
    cursor.close()
    connection.close()
    
def selctAllFromCity(city):
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
    cursor.execute("SELECT * FROM " + city)
# Fetch data from the database
    result = cursor.fetchall()
# Print the result
    print(result)
# Close the cursor and the database connection
    cursor.close()
    connection.close()

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

selctFilter("Oui", "Restauration", "services")
