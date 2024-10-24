from flask import Flask, render_template

app = Flask(__name__, static_folder='shoe-frontend', template_folder='shoe-frontend')

@app.route('/')
def index():
    return render_template('index.html')
