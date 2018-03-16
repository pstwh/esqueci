from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.from_pyfile('env.cfg')

@app.route("/")
def home():
    return "home"

from src.controller import *

if __name__ == '__main__':
    app.run(debug=True) 