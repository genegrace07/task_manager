import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class TaskDB:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = os.getenv('db_host'),
            user = os.getenv('db_user'),
            password = os.getenv('db_password'),
            database = os.getenv('db_database')
        )
        self.dbcursor = self.db.cursor(dictionary=True)

    def display_list(self, user_id):
        self.dbcursor.execute('select * from tasks where id = %s order by date_time',(user_id,))
        return self.dbcursor.fetchall()
    def add_list(self,enter_task):
        c_value = ('insert into tasks(tasks)values(%s)')
        self.dbcursor.execute(c_value,(enter_task,))
        self.db.commit()
    def del_list(self,no):
        c_value = ('delete from tasks where id = %s')
        self.dbcursor.execute(c_value,(no,))
        self.db.commit()
    def get_list(self,no):
        c_value = ('select * from tasks where id = %s')
        self.dbcursor.execute(c_value,(no,))
        return self.dbcursor.fetchone()
    def update_list(self,task_name,no):
        c_value = ('update tasks set tasks = %s where id = %s')
        self.dbcursor.execute(c_value,(task_name,no))
        self.db.commit()

class UserDB(TaskDB):
    def signing(self,user_name,passwd):
        c_value = ('insert into auth(username,pwd) values(%s,%s)')
        self.dbcursor.execute(c_value,(user_name,passwd))
        self.db.commit()
    def get_email(self,email):
        c_value = 'select * from auth where username = %s'
        self.dbcursor.execute(c_value,(email,))
        return self.dbcursor.fetchone()

    # def log_in(self,email,password):
    #     c_value = 'select * from auth where username = %s and pwd = %s'
    #     self.dbcursor.execute(c_value,(email,password))
    #     return self.dbcursor.fetchone()
