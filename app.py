from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Your eyes are like stars, they sparkle with a brilliance that is mesmerizing!'
