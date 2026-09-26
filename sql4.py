#write a python program to insert a single record
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password='root123',
    database='school'
)
cursor=con.cursor()
sql="INSERT INTO students (id, name, age, city) VALUES (1, 'Rahul', 20, 'Bengaluru')"
cursor.execute(sql)
con.commit()
print("Record inserted successfully")
con.close()
