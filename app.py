from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/MangaDB"
mongo = PyMongo(app)
db = mongo.db


@app.route('/')
def home():

    return render_template('home.html')


@app.route('/list/', methods=["POST"])
def test():
    type = request.form['type']
    number_of_episode = request.form['nbEpisode']

    if type == "Tout":
        if number_of_episode == "1-15":
            animes = db.animes.find({'$and': [
                {'episodesInt': {'$gt': 1}},
                {'episodesInt': {'$lt': 15}}]},
                {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})
        elif number_of_episode == "15-50":
            animes = db.animes.find({'$and': [
                {'episodesInt': {'$gt': 15}},
                {'episodesInt': {'$lt': 50}}]},
                {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})
        elif number_of_episode == "50-100":
            animes = db.animes.find({'$and': [
                {'episodesInt': {'$gt': 50}},
                {'episodesInt': {'$lt': 100}}]},
                {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})
        elif number_of_episode == "> 1":
            animes = db.animes.find(
                {'episodesInt': {'$gt': 1}},
                {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})
        else:
            animes = db.animes.find({'$and': [
                {'episodesInt': {'$gt': 100}}]},
                {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})
    else:
        selected_type = str(type)
        if number_of_episode == "1-15":
            animes = db.animes.find({'$and': [
                {'type': selected_type},
                {'episodesInt': {'$gt': 1}},
                {'episodesInt': {'$lt': 15}}]},
                {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})
        elif number_of_episode == "15-50":
            animes = db.animes.find({'$and': [
                {'type': selected_type},
                {'episodesInt': {'$gt': 15}},
                {'episodesInt': {'$lt': 50}}]},
                {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})
        elif number_of_episode == "50-100":
            animes = db.animes.find({'$and': [
                {'type': selected_type},
                {'episodesInt': {'$gt': 50}},
                {'episodesInt': {'$lt': 100}}]},
                {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})
        elif number_of_episode == "> 1":
            animes = db.animes.find({'$and': [
                {'type': selected_type},
                {'episodesInt': {'$gt': 1}}]},
                {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})
        else:
            animes = db.animes.find({'$and': [
                {'type': selected_type},
                {'episodesInt': {'$gt': 100}}]},
                {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})

    print animes
    #print("Type selectionne : '" + type + "' - Nombre episodes selectionnes :" + number_of_episode + "' - Affichage selectione : '" + sort + "'")
    print("Type selectionne : '" + type + "' - Nombre episodes selectionnes :" + number_of_episode)
    return render_template('list.html', animes=list(animes))


@app.route('/details/', methods=["POST"])
def details():
    return render_template('details.html')