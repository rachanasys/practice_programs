#write a python program to use a parameterized query
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password='root123',
    database='school'
)
cursor=con.cursor()
sql='SELECT * FROM students WHERE city=%s'
city=("Bengaluru",)
cursor.execute(sql, city)
records=cursor.fetchall()
for row in records:
    print(row)
con.close()
