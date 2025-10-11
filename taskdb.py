import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
    host = os.getenv('db_host'),
    user = os.getenv('db_user'),
    password = os.getenv('db_password'),
    database = os.getenv('db_database')
)
dbcursor = db.cursor(dictionary=True)

def display_list():
    dbcursor.execute('select * from tasks order by date_time')
    return dbcursor.fetchall()
def add_list(enter_task):
    c_value = ('insert into tasks(tasks)values(%s)')
    dbcursor.execute(c_value,(enter_task,))
    db.commit()
def del_list(no):
    c_value = ('delete from tasks where id = %s')
    dbcursor.execute(c_value,(no,))
    db.commit()
def get_list(no):
    c_value = ('select * from tasks where id = %s')
    dbcursor.execute(c_value,(no,))
    return dbcursor.fetchone()
def update_list(task_name,no):
    c_value = ('update tasks set tasks = %s where id = %s')
    dbcursor.execute(c_value,(task_name,no))
    db.commit()