import config
from flask import Flask, request, render_template, url_for
from flask_login import LoginManager
from werkzeug.utils import redirect
from flask_migrate import Migrate
from models import db
from models import User, Todo

app = Flask(__name__)

migrate = Migrate()
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)

loginManager = LoginManager()
loginManager.init_app(app)

@app.route("/")
def loginPage():
    return render_template("loginPage.html")

@app.route("/todo")
def home():
    return render_template("mainPage.html", todos = Todo.query.all())

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == "POST":
        userId = request.form.get("uesrId")
        password = request.form.get("password")

        return redirect(url_for("todo"))
    else:
        return "잘못된 접근입니다."

@app.route("/todo/add", methods=['GET', 'POST'])
def addTodo():
    if request.method == "POST":
        if request.form.get("content") == "": return redirect(url_for("home"))
        todo = Todo(content = request.form.get("content"), done = False)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return "잘못된 접근입니다."

@app.route("/todo/delete/<int:todoId>", methods=['GET','POST'])
def delTodo(todoId):
    if request.method == "POST":
        todo = Todo.query.filter_by(id=todoId).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return "잘못된 접근입니다."

@app.route("/todo/update/<todoId>", methods=["GET","POST"])
def updateTodo(todoId):
    if request.method == "POST":
        todo = Todo.query.filter_by(id=todoId).first()
        todo.done = not todo.done
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return "잘못된 접근입니다."


if __name__ == "__main__":
    app.run(debug=True)