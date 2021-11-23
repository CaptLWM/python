# oracle 여결
import cx_Oracle

connection = cx_Oracle.connect('SCOTT/TIGER@XE')
cursor = connection.cursor()
querystring = "SELECT * FROM EMP"
cursor.execute(querystring)

print(cursor.fetchall())

cursor.close()
connection.close()
