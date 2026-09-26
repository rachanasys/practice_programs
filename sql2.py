#write a python program to create a new database in MySQL
import mysql.connector
con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123'
)
cursor=con.cursor()
cursor.execute("CREATE DATABASE school1")
print('Database created successfully')
con.close()
