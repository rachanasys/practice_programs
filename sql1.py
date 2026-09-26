#write a python program to connect to a MySql database using 'mysql.connector'
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user='root',
    password='root123',
    database='school'
)
if con.is_connected():
    print("connected to MySQL")
con.close()
