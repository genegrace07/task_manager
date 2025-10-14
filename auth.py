from flask import Flask,request,redirect,render_template,url_for,Blueprint
import taskdb

auth = Blueprint('auth',__name__)

@auth.route('/sign')
def signup():
    return render_template('signup.html')

@auth.route('/log')
def login():
    return render_template('login.html')