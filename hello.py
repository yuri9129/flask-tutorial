from flask import Flask

app = Flask(__name__)

@app.route('/japan/<city>')
def tokyo(city):
    return f"<p>Hello, {city} in Japan!!!</p>"
