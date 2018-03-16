from flask import request, jsonify, send_from_directory
from src.models.files import Files

from loader import app

import os
import datetime
import shutil

file = Files()

@app.route("/files/", defaults={'search': None})
@app.route("/files/search/<string:search>")
def index(search):
    files = file.all()
    return files

@app.route("/template/create", methods=['POST'])
def create():
    template_name = request.form['template_name']
    selected_name = request.form['selected_name']
    uploaded_file = request.files['template_file']
    uploaded_file_name = uploaded_file.filename
    uploaded_file_extension = uploaded_file_name.rsplit('.', 1)[1].lower()

    template_dir = f'{app.config["STORAGE_DIR"]}/{template_name}/templates'
    uploaded_dir = f'{template_dir}/{selected_name}'

    if not os.path.isdir(template_dir): os.makedirs(template_dir)

    if not os.path.isfile(uploaded_dir): 
        uploaded_file.save(uploaded_dir)  
        print(template_dir)
        shutil.make_archive(f'{template_dir}/compacts/{template_name}', 'zip', template_dir)

        obj_file = {
            "template_name": template_name,
            "selected_name": selected_name,
            "file_extension": uploaded_file_extension,
            "uploaded_dir": uploaded_dir,
            "created_at": datetime.datetime.now(),
            "updated_at": datetime.datetime.now()
            }

        file.create(obj_file)

        return jsonify({"insert": True})
    else:
        return jsonify({"insert": False, "error": "template exists"})

@app.route("/template/retrieve/<string:template_name>")
def retrieve_template(template_name):
    return send_from_directory(f'{app.config["STORAGE_DIR"]}/{template_name}/compacts', f'{template_name}.zip', as_attachment=True)

    

