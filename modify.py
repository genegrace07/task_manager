from flask import Blueprint,url_for,request,redirect,render_template
import taskdb

modify = Blueprint('modify',__name__)

@modify.route('/delete/<int:no>')
def del_route(no):
    taskdb.del_list(no)
    return redirect(url_for('home'))

@modify.route('/update/<int:no>',methods=['POST','GET'])
def update_route(no):
    if request.method == "POST":
        task_name = request.form.get('content')
        taskdb.update_list(task_name,no)
        return redirect(url_for('home'))
    else:
        task_get = taskdb.get_list(no)
        return render_template('update.html',task_get=task_get)