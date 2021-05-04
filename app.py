import flask
from flask import Flask, render_template
from flask import Blueprint
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/MangaDB"
mongo = PyMongo(app)
db = mongo.db

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test/')
def test():
    animes = db.anime_items.find({}, {'_id': 0})
    return flask.jsonify([todo for todo in animes])
    #animes = db.anime_items.find_one({'title' : "T-Rex"}, {'_id' : 0})
    #return flask.jsonify(animes)
