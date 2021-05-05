from operator import gt

import jinja2
from flask import Flask, render_template, request, Blueprint, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/MangaDB"
mongo = PyMongo(app)
db = mongo.db

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/list/', methods =["POST"])
def test():
    type = request.form['type']
    number_of_episode = request.form['nbEpisode']
    sort = request.form['affichage']

    if type == "Tout":
        animes = db.anime_items.find({}, {'title': 1, 'rating': 1, 'type': 1, '_id': 0})
    else:
        selected_type = str(type)

        if number_of_episode == "1-15":
            print number_of_episode
            #animes = db.anime_items.find({ $and: [{'type': selected_type}, {'episodes': {$gt: 1, $lt: 15}}], {'title': 1, 'rating': 1, 'type': 1, '_id': 0}})
        elif number_of_episode == "15-50":
            print number_of_episode
            #animes = db.anime_items.find({ $and: [{'type': selected_type}, {'episodes': {$gt: 15, $lt: 50}}], {'title': 1, 'rating': 1, 'type': 1, '_id': 0}})
        elif number_of_episode == "50-100":
            print number_of_episode
            #animes = db.anime_items.find({ $and: [{'type': selected_type}, {'episodes': {$gt: 50, $lt: 100}}], {'title': 1, 'rating': 1, 'type': 1, '_id': 0}})
        else:
            print number_of_episode
            #animes = db.anime_items.find({ $and: [{'type': selected_type}, {'episodes': {$gt: 1}], {'title': 1, 'rating': 1, 'type': 1, '_id': 0}})


    print("Type selectionne : '" + type + "' - Nombre episodes selectionnes :" + number_of_episode + "' - Affichage selectione : '"  + sort + "'")

    return render_template('list.html', animes=list(animes))