#write a python program to insert multiple records
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password='root123',
    database='school'
)
cursor=con.cursor()
sql="INSERT INTO students (id, name, age, city) VALUES (%s, %s,%s, %s)"
records=[
    (2, 'Anita', 21, 'Mumbai'),
    (3, 'Kiran', 19, 'Delhi'),
    (4, 'Priya', 22, 'Chennai')
]
cursor.executemany(sql, records)
con.commit()
print(cursor.rowcount, "Record inserted")
con.close()