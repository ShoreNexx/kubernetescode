from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'checking the discord notifier new message style'
