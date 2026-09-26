#write a python program to delete records
import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password='root123',
    database='school'
)
cursor=con.cursor()
sql="DELETE FROM students WHERE id=4"
cursor.execute(sql)
con.commit()
print(cursor.rowcount,"record deleted")
con.close()
