import pymysql


# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='loutrerushbdd'
)
# Create a cursor object
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT * FROM Player")

# Fetch data from the database
result = cursor.fetchall()

# Print the result
print(result)

# Close the cursor and the database connection
cursor.close()
connection.close()