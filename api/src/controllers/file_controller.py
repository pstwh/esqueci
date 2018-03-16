from flask import request, jsonify
from src.models.files import Files

from loader import app

import os

file = Files()

@app.route("/files/", defaults={'search': None})
@app.route("/files/search/<string:search>")
def index(search):
    files = file.all()
    return files

@app.route("/files/create", methods=['POST'])
def create():
    uploaded_file = request.files['template_file']

    template_name = request.form['template_name']
    file_name = uploaded_file.filename

    if not os.path.isdir(f'{app.config["STORAGE_DIR"]}/{template_name}'): os.makedirs(f'{app.config["STORAGE_DIR"]}/{template_name}')

    if(file.exists(f'{app.config["STORAGE_DIR"]}/{template_name}/{file_name}')): 
        return jsonify({"insert": False, "error": "template exists"})
    else:
        uploaded_file.save(f'{app.config["STORAGE_DIR"]}/{template_name}/{file_name}')    
        return jsonify({"insert": True, "template_name": template_name})
    

@app.route("/files/retrieve/<string:name>")
def retrieve():
    pass