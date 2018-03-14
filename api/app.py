from flask import Flask
from flask_pymongo import PyMongo
from src.models.files import Files


app = Flask(__name__)

file = Files('files', 'files', '_id')
print(file.all())