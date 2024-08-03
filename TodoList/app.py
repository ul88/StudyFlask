import config
from flask import Flask, request, render_template, url_for, session, g
from flask_bcrypt import Bcrypt
from werkzeug.utils import redirect
from flask_migrate import Migrate
from models import db
from models import User, Todo

app = Flask(__name__)

migrate = Migrate()
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)

bcrypt = Bcrypt(app)

@app.route("/")
def loginPage():
    return render_template("loginPage.html")

@app.route("/signupPage")
def signupPage():
    return render_template("signupPage.html")

@app.route("/todo")
def home():
    return render_template("mainPage.html", todos = Todo.query.all())

@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method == "POST":
        userId = request.form.get("uesrId")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        user = User.query.filter_by(userId=userId).first()
        if not user and password == password2:
            user = User(userId = request.form.get("userId"), password = bcrypt.generate_password_hash(password = request.form.get("password")))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("loginPage"))
    return "잘못된 접근입니다."


@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == "POST":
        userId = request.form.get("uesrId")
        password = request.form.get("password")
        user = User.query.filter_by(userId=userId).first()
        print(user)

        if not user:
            return "존재하지 않는 데이터입니다."
        elif not bcrypt.check_password_hash(user.password, password):
            return "비밀번호가 틀립니다."
        
        session.clear()
        session['user_id'] = user.id
        return redirect(url_for("home"))
    else:
        return "잘못된 접근입니다."

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("loginPage"))

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