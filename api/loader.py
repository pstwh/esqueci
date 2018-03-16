from flask import Flask, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config.from_pyfile('env.cfg')

@app.route("/")
def home():
    return url_for('retrieve_template', template_name='teste_name')

from src.controller import *

if __name__ == '__main__':
    app.run(debug=True) 