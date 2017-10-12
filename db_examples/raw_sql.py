import psycopg2

# Try to connect

connection = psycopg2.connect(dbname='db1', host='localhost', user='db1_user', password='qwerty')
cursor = connection.cursor()
cursor.execute("select * from todos")
rows = cursor.fetchall()

for row in rows:
    #print(row[1][1])
    print(row)

connection.close()
