from flask import Flask,request,redirect,render_template,url_for
import taskdb

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == "POST":
        enter_task = request.form.get('content')
        taskdb.add_list(enter_task)
        return redirect(url_for('home'))
    else:
        view_list = taskdb.display_list()
        return render_template('main.html',view_list=view_list)
@app.route('/delete/<int:no>')
def del_route(no):
    taskdb.del_list(no)
    return redirect(url_for('home'))
@app.route('/update/<int:no>',methods=['POST','GET'])
def update_route(no):
    if request.method == "POST":
        task_name = request.form.get('content')
        taskdb.update_list(task_name,no)
        return redirect(url_for('home'))
    else:
        task_get = taskdb.get_list(no)
        return render_template('update.html',task_get=task_get)

if __name__ == "__main__":
    app.run(debug=True)
