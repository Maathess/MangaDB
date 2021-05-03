from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Manga"
mongo = PyMongo(app)


@app.route('/')
def home():
    online_users = mongo.db.users.find({"online": True})
    return render_template('home.html',
                           online_users = online_users)

@app.route('/test/')
def test():
    return render_template('test.html')