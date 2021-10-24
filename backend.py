from flask import Flask

app = Flask(__name__) #might have to update static_folder variable


@app.route('/')
def hello():
    return 'Hello, World!'