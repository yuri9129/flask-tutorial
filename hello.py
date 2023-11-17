from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # templatesフォルダ内のhello.htmlを読み込む
    return render_template('hello.html')
