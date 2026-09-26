#write a python program to fetch all records
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password='root123',
    database='school'
)
cursor=con.cursor()
cursor.execute('SELECT * FROM students')
records=cursor.fetchall()
for row in records:
    print(row)
con.close()
