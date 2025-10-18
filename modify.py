from flask import Blueprint,url_for,request,redirect,render_template,current_app
from taskdb import TaskDB

modify = Blueprint('modify',__name__)

@modify.route('/delete/<int:no>')
def del_route(no):
    t_db = current_app.config['taskdb']
    t_db.del_list(no)
    return redirect(url_for('task'))

@modify.route('/update/<int:no>',methods=['POST','GET'])
def update_route(no):
    t_db = current_app.config['taskdb']
    if request.method == "POST":
        task_name = request.form.get('content')
        t_db.update_list(task_name,no)
        return redirect(url_for('task'))
    else:
        task_get = t_db.get_list(no)
        return render_template('update.html',task_get=task_get)