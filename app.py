from flask import Flask, render_template, request, render_template_string
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/MangaDB"
mongo = PyMongo(app)
db = mongo.db


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/details', methods=["GET", "POST"])
def details_of_animes():

    title = str(request.form['selected_anime'])
    print(title)
    test = 123456
    details = db.animes.find({'title': title}, {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0})

    for detail in details:
        print(detail)

    return render_template('details.html', title=title, details=details, test=test)


@app.route('/list', methods=["GET", "POST"])
def list_of_animes():

    if request.method == "POST":
        print("POOOOOOOOOST")

    type = request.form['type']
    number_of_episode = request.form['nbEpisode']
    
    end_request = {'title': 1, 'rating': 1, 'type': 1, 'episodesInt': 1, 'synopsis': 1, '_id': 0}

    if type == "Tout":
        if number_of_episode == "1-15":
            animes = db.animes.find({'$and': [
                {'episodesInt': {'$gt': 1}},
                {'episodesInt': {'$lt': 15}}]}, end_request)
        elif number_of_episode == "15-50":
            animes = db.animes.find({'$and': [
                {'episodesInt': {'$gt': 15}},
                {'episodesInt': {'$lt': 50}}]}, end_request)
        elif number_of_episode == "50-100":
            animes = db.animes.find({'$and': [
                {'episodesInt': {'$gt': 50}},
                {'episodesInt': {'$lt': 100}}]}, end_request)
        elif number_of_episode == "> 1":
            animes = db.animes.find(
                {'episodesInt': {'$gt': 1}},
                end_request)
        else:
            animes = db.animes.find({'$and': [
                {'episodesInt': {'$gt': 100}}]}, end_request)
    else:
        selected_type = str(type)
        if number_of_episode == "1-15":
            animes = db.animes.find({'$and': [
                {'type': selected_type},
                {'episodesInt': {'$gt': 1}},
                {'episodesInt': {'$lt': 15}}]}, end_request)
        elif number_of_episode == "15-50":
            animes = db.animes.find({'$and': [
                {'type': selected_type},
                {'episodesInt': {'$gt': 15}},
                {'episodesInt': {'$lt': 50}}]}, end_request)
        elif number_of_episode == "50-100":
            animes = db.animes.find({'$and': [
                {'type': selected_type},
                {'episodesInt': {'$gt': 50}},
                {'episodesInt': {'$lt': 100}}]}, end_request)
        elif number_of_episode == "> 1":
            animes = db.animes.find({'$and': [
                {'type': selected_type},
                {'episodesInt': {'$gt': 1}}]}, end_request)
        else:
            animes = db.animes.find({'$and': [
                {'type': selected_type},
                {'episodesInt': {'$gt': 100}}]}, end_request)

    print("Type selectionne : '" + type + "' - Nombre episodes selectionnes :" + number_of_episode)
    return render_template('list.html', animes=list(animes))