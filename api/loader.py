from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)

from src.controller import *

if __name__ == '__main__':
    app.run(debug=True) 