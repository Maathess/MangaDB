import jinja2
from flask import Flask, render_template, request, Blueprint, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/MangaDB"
mongo = PyMongo(app)
db = mongo.db

@app.route('/')
def home():
    print "test"
    return render_template('home.html')

@app.route('/test/', methods =["POST"])
def test():

    type = request.form['type']
    number_of_episode = request.form['nbEpisode']
    sort = request.form['affichage']

    selected_type = ""
    selected_number_of_episode_min = 0
    selected_number_of_episode_max = 0
    selected_sort = ""

    if type == "Tout":
        selected_type = selected_type
    elif type == "TV":
        selected_type = str(type)
    elif type == "Anime":
        selected_type = str(type)
    elif type == "OVA":
        selected_type = str(type)
    elif type == "Movie":
        selected_type = str(type)
    elif type == "Special":
        selected_type = str(type)
    else:
        selected_type = str(type)

    if number_of_episode == "1-15":
        selected_number_of_episode_min = 1
        selected_number_of_episode_max = 15
    elif number_of_episode == "15-50":
        selected_number_of_episode_min = 15
        selected_number_of_episode_max_ = 50
    elif number_of_episode == "50-100":
        selected_number_of_episode_min = 50
        selected_number_of_episode_max = 100
    else:
        selected_number_of_episode_min = 100
        selected_number_of_episode_max = 1000



    #, "episodes": { $gt: selected_number_of_episode_min }
    animes = db.anime_items.find( {'type': selected_type}, {'title': 1, 'rating': 1, 'type': 1, '_id': 0})

    print("Type selectionne : '" + type + "' - Nombre episodes selectionnes :" + number_of_episode + "' - Affichage selectione : '"  + affichage + "'")

    return render_template('test.html', animes=list(animes))







    #flask.jsonify([todo for todo in animes])
    #animes = db.anime_items.find_one({'title' : "T-Rex"}, {'_id' : 0})
    #return flask.jsonify(animes)
