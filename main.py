from flask import Flask,request,redirect,render_template,url_for,flash, get_flashed_messages, session
from taskdb import TaskDB, UserDB
from modify import modify
from auth import auth

app = Flask(__name__)
app.secret_key = "mysecretkey"
app.config['taskdb'] = TaskDB()
app.config['userdb'] = UserDB()

app.register_blueprint(modify, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

@app.route('/task',methods=['POST','GET'])
def task():
    t_db = app.config['taskdb']
    user_id = session.get('user_id')
    if not user_id:
        flash('Invalid, Login first','error')
        return redirect(url_for('auth.login'))

    if request.method == "POST":
        enter_task = request.form.get('content')
        t_db.add_list(enter_task,user_id)
        flash('Successfully added','success')
        return redirect(url_for('task'))
    else:
        view_list = t_db.display_list(user_id)
        return render_template('main.html',view_list=view_list)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

'''
email already exist
'''