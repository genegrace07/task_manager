import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "task_list"
)
dbcursor = db.cursor(dictionary=True)
dbcursor.execute('show tables')
show = dbcursor.fetchall()
print(show)