#write a python program to update records
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password='root123',
    database='school'
)
cursor=con.cursor()
sql="UPDATE students SET age=21 WHERE id=1"
cursor.execute(sql)
con.commit()
print(cursor.rowcount,"record updated")
con.close()
