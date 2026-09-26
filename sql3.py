#write a python program to create a table in MySQL using Python
import mysql.connector
con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='school')
cursor=con.cursor()
cursor.execute('Drop table students')
cursor.execute("""
CREATE TABLE students(
id INT PRIMARY KEY,
name VARCHAR(50),
age INT,
city VARCHAR(50)
)
""")
print('Table created successfully')
con.close()
