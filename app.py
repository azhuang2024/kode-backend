from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__) #might have to update static_folder variable
cluster = MongoClient('mongodb+srv://gurish:1234@cluster0.98ccl.mongodb.net/kode?retryWrites=true&w=majority')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/buildings/', methods=['POST', 'GET'])
def get_buildings():

    db = cluster.kode
    buildingDB = db.buildings
    results = buildingDB.find({})
    list = []
    for result in results:
        list.append(result)
    return jsonify(list)
