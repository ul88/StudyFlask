from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("mainPage.html", todos = todoList)

@app.route("/add", methods=['GET', 'POST'])
def addTodo():
    if request.method == "POST":
        global id
        dic = {"id" : id, "todo" : request.form.get("todo"), "done" : False}
        id+=1
        todoList.append(dic)
        return render_template("mainPage.html", todos = todoList)
    else:
        return "잘못된 접근입니다."

@app.route("/delete/<todoId>", methods=['GET','POST'])
def delTodo(todoId):
    if request.method == "POST":
        global todoList
        todoList = [todos for todos in todoList if todos['id'] != int(todoId)]
        return render_template("mainPage.html", todos = todoList)
    else:
        return "잘못된 접근입니다."

@app.route("/update/<todoId>", methods=["GET","POST"])
def updateTodo(todoId):
    if request.method == "POST":
        idx = 0
        for now in todoList:
            if now["id"] == int(todoId):
                break
            idx+=1
        todoList[idx]["done"] = not todoList[idx]["done"]
        return render_template("mainPage.html", todos = todoList)
    else:
        return "잘못된 접근입니다."
    
id = 0
todoList = []

if __name__ == "__main__":
    app.run(debug=True)