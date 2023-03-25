from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def basic():
    if request.method == 'POST':
        name = request.form['username']
        return render_template('homepage.html',username=name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()