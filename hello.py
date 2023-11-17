from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/japan/<city>')
def hello(city):
    # template側でcity変数を使えるようにする
    return render_template('hello.html', city=city)
