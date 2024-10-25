from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Your eyes are the missing piece in a puzzle, and your presence is the perfect fit that completes the picture!'
