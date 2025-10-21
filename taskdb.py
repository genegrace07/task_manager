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
        #self.dbcursor = self.db.cursor(dictionary=True)

    def display_list(self, user_id):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor(dictionary=True,buffered=True)
        c_value = 'select * from tasks where auth_id = %s'
        cursor.execute(c_value,(user_id,))
        result = cursor.fetchall()
        cursor.close()
        return result
    def add_list(self,enter_task,user_id):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor(dictionary=True, buffered=True)
        c_value = ('insert into tasks(tasks,auth_id)values(%s,%s)')
        cursor.execute(c_value,(enter_task,user_id,))
        self.db.commit()
        cursor.close()
    def del_list(self,no):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor(dictionary=True, buffered=True)
        c_value = ('delete from tasks where id = %s')
        cursor.execute(c_value,(no,))
        self.db.commit()
        cursor.close()
    def get_list(self,no):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor(dictionary=True, buffered=True)
        c_value = ('select * from tasks where id = %s')
        cursor.execute(c_value,(no,))
        result = cursor.fetchone()
        cursor.close()
        return result
    def update_list(self,task_name,no):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor(dictionary=True, buffered=True)
        c_value = ('update tasks set tasks = %s where id = %s')
        cursor.execute(c_value,(task_name,no))
        self.db.commit()
        cursor.close()
class UserDB(TaskDB):
    def signing(self,user_name,passwd):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor(dictionary=True, buffered=True)
        c_value = ('insert into auth(username,pwd) values(%s,%s)')
        cursor.execute(c_value,(user_name,passwd))
        self.db.commit()
        cursor.close()
    def get_email(self,email):
        self.db.ping(reconnect=True)
        cursor = self.db.cursor(dictionary=True, buffered=True)
        c_value = 'select * from auth where username = %s'
        cursor.execute(c_value,(email,))
        result = cursor.fetchone()
        cursor.close()
        return result

    # def log_in(self,email,password):
    #     c_value = 'select * from auth where username = %s and pwd = %s'
    #     self.dbcursor.execute(c_value,(email,password))
    #     return self.dbcursor.fetchone()
