from flask import Flask, render_template, request
import get_google_serach

app = Flask(__name__)

@app.route('/',methods=('GET','POST'))
def index():
    print(request.form.get('keyword1'))
    print(request.form.get('keyword2'))
    keyword1 = request.form.get('keyword1')
    keyword2 = request.form.get('keyword2')

    if keyword1 is not None and keyword2 is not None:
        data = {
            keyword1 : get_google_serach.get_search_count(keyword1).get('number'),
            keyword2 : get_google_serach.get_search_count(keyword2).get('number'),
        }
        return render_template('index.html',data = data)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    