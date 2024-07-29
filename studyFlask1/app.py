from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        print(request.form.get('user'))
        user = request.form.get('user')
        data = {'level':60, 'point':360, 'exp':45000}
        return render_template('index.html', user=user, data = data)
    elif request.method == "GET":
        user = request.form.get('user')
        data = {'level':60, 'point':360, 'exp':45000}
        return render_template('index.html', user=user, data = data)

if __name__ == "__main__":
    app.run(debug=True)