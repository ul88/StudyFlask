import config
from flask import Flask, request, render_template, url_for, session, g, flash
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
    return render_template("mainPage.html", todos = Todo.query.all(), userId = session["userId"])

@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method == "POST":
        password = request.form.get("password")
        password2 = request.form.get("password2")

        user = User.query.filter_by(userId=request.form.get("userId")).first()
        if not user:
            if password == password2:
                user = User(userId = request.form.get("userId"), password = bcrypt.generate_password_hash(password = request.form.get("password")))
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("loginPage"))
            else:
                flash("비밀번호가 서로 다릅니다.")
        else:
            flash("이미 있는 아이디입니다.")
    return redirect(url_for("signupPage"))


@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == "POST":
        user = User.query.filter_by(userId=request.form.get("uesrId")).first()

        if not user:
            flash("잘못 입력했습니다.")
        elif not bcrypt.check_password_hash(user.password, request.form.get("password")):
            flash("잘못 입력했습니다.")
        else:
            session.clear()
            session["userId"] = request.form.get("uesrId")
            return redirect(url_for("home"))
    return redirect(url_for("loginPage"))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("loginPage"))

@app.route("/todo/add", methods=['GET', 'POST'])
def addTodo():
    if request.method == "POST":
        if request.form.get("content") == "": return redirect(url_for("home"))
        todo = Todo(userId = session["userId"], content = request.form.get("content"), done = False)
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