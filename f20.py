#write a python program to perform order by query in MySQL 
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password='root123',
    database='school'
)
cursor=con.cursor()
cursor.execute('SELECT * FROM students ORDER BY age')
records=cursor.fetchall()
for row in records:
    print(row)
con.close()
