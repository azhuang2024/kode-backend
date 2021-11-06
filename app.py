from flask import Flask
from pymongo import MongoClient

app = Flask(__name__) #might have to update static_folder variable


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/buildings')
def get_buildings():
    client = MongoClient()
