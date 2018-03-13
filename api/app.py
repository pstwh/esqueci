
from flask import Flask
from flask_pymongo import PyMongo

from src.models.files import Files

app = Flask(__name__)
mongo = PyMongo(app)    
    
#file = Files(mongo, 'file', 'files', '_id')
#print(file.all())

#@app.route('/') 
#def index():
#    return "Hello, world"

#if __name__ == '__main__':
#    app.run(debug=True)