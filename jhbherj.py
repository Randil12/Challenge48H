def name_from(table, research):
    # connection
    conn = psycopg2.connect("dbname=cranaruge user=postgres password=root")

# request
    cursor = conn.cursor()
    query_request = "SELECT * FROM "+table+" WHERE Name LiKE "+"'"+research+"%"+"'"
    
    cursor.execute(query_request)

# result
    res = cursor.fetchall() 
    print(res)
    print(len(res))
# connection close
    conn.close()
    return res