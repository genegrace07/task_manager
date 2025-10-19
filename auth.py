from flask import Flask,request,redirect,render_template,url_for,Blueprint,current_app,flash
from taskdb import UserDB
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint('auth',__name__)

@auth.route('/sign',methods=['POST','GET'])
def signup():
    t_db = current_app.config['userdb']
    if request.method == 'POST':
        get_email = request.form.get('email')
        get_pass = request.form.get('password')
        hash_password = generate_password_hash(get_pass)
        t_db.signing(get_email,hash_password)
        return redirect(url_for('auth.signup'))
    else:
        return render_template('signup.html')

@auth.route('/',methods=['POST','GET'])
def login():
    t_db = current_app.config['userdb']
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = t_db.get_email(email)
        if user and check_password_hash(user['pwd'],password):
            flash('login successfully','success')
            return redirect(url_for('task'))
        else:
            flash('Invalid login','error')
            return render_template('login.html')
    else:
        return render_template('login.html')

