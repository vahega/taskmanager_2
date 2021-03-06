import os
from flask import(
Flask,flash,render_template,
redirect, request,session,url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
app = Flask(__name__)


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.SECRET_KEY=os.environ.getenv('SECRET_KEY')

mongo = PyMongo(app)

@app.route("/")

@app.route("/get_tasks")
def get_tasks():
    return render_template("tasks.html", 
                           tasks=mongo.db.tasks.find())




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
