from pymysql import connect, err, sys, cursors

# Doing our connection
conn = connect(host='localhost',
               port=3306,
               user='root',
               passwd='admin',
               db='mydb');
# Setting cursors and defining type of returns we need from Database, here it's gonna be returning as dictionary data
cursor = conn.cursor(cursors.DictCursor);
cursor.execute("SELECT * FROM ProjectStudent")
data = cursor.fetchall()
print(data)