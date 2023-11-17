from flask import Flask
from flask import render_template

app = Flask(__name__)

tasks = [
    '1. 朝食を食べる',
    '2. 電車に乗る',
    '3. 会社に行く',
    '4. 昼食を食べる',
    '5. 会社に行く',
]
@app.route('/')
def hello():
    # template側でcity変数を使えるようにする
    return render_template('hello.html', tasks=tasks)
