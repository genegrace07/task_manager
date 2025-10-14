from flask import Flask,request,redirect,render_template,url_for
from taskdb import TaskDB
from modify import modify
from auth import auth

taskdb = TaskDB()
app = Flask(__name__)

app.register_blueprint(modify, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == "POST":
        enter_task = request.form.get('content')
        taskdb.add_list(enter_task)
        return redirect(url_for('home'))
    else:
        view_list = taskdb.display_list()
        return render_template('main.html',view_list=view_list)


if __name__ == "__main__":
    app.run(debug=True)


'''
user login
flash
encrypt pass
'''
