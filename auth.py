from flask import Flask,request,redirect,render_template,url_for,Blueprint,current_app
from taskdb import UserDB

auth = Blueprint('auth',__name__)

@auth.route('/sign',methods=['POST','GET'])
def signup():
    t_db = current_app.config['userdb']
    if request.method == 'POST':
        get_email = request.form.get('email')
        get_pass = request.form.get('password')
        t_db.signing(get_email,get_pass)
        return redirect(url_for('auth.signup'))
    else:
        return render_template('signup.html')

@auth.route('/',methods=['POST','GET'])
def login():
    t_db = current_app.config['userdb']
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        t_db.log_in(email,password)
        return redirect(url_for('task'))
    else:
        return render_template('login.html')

