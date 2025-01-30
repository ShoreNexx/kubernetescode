from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Checking whether the automatic devployment is working or not'
