from flask import Flask,request,redirect,render_template,url_for,Blueprint,current_app,flash,session
from taskdb import UserDB
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint('auth',__name__)

@auth.route('/sign',methods=['POST','GET'])
def signup():
    t_db = current_app.config['userdb']
    if request.method == 'POST':
        get_email = request.form.get('email')
        get_pass = request.form.get('password')
        get_confirm = request.form.get('confirm')
        if len(get_email) == 0:
            flash('Email cannot be empty','error')
            return redirect(url_for('auth.signup'))
        elif len(get_pass) == 0:
            flash('Password cannot be empty','error')
            return redirect(url_for('auth.signup'))
        elif get_pass != get_confirm:
            flash('Password not match','error')
            return redirect(url_for('auth.signup'))
        else:
            hash_password = generate_password_hash(get_pass)
            t_db.signing(get_email,hash_password)
            flash('Successfully registered', 'success')
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
            session['user_id'] = user['id']
            flash('login successfully','success')
            return redirect(url_for('task'))
        else:
            flash('Invalid login','error')
            return render_template('login.html')
    else:
        return render_template('login.html')

