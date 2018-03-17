from flask import request, jsonify, send_from_directory, after_this_request, send_file
from src.models.files import Files

from loader import app

import os
import datetime
import zipfile
from io import BytesIO

file = Files()

@app.route("/template")
def index_template():
    files = file.find({})
    return files

@app.route("/template/create", methods=['POST'])
def create_template():
    template_name = request.form['template_name']
    selected_name = request.form['selected_name']
    uploaded_file = request.files['template_file']
    uploaded_file_name = uploaded_file.filename
    uploaded_file_extension = uploaded_file_name.rsplit('.', 1)[1].lower()

    template_dir = f'{app.config["TEMPLATE_DIR"]}/{template_name}'
    uploaded_dir = f'{template_dir}/{selected_name}'

    if not os.path.isdir(template_dir): os.makedirs(template_dir)

    if not os.path.isfile(uploaded_dir): 
        uploaded_file.save(uploaded_dir)  
        #print(template_dir)
        #shutil.make_archive(f'{template_dir}/{template_name}', 'zip', template_dir)

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

@app.route("/template/<string:template_name>")
def retrieve_template(template_name):
    try:
        template_dir = f'{app.config["TEMPLATE_DIR"]}/{template_name}'
        b = BytesIO()
        zf = zipfile.ZipFile(b, "w")

        for template in os.listdir(template_dir):
            print(f'{template_dir}/{template}')
            zf.write(f'{template_dir}/{template}', template)
        zf.close()
        b.seek(0)

        return send_file(b, mimetype = "application/zip", as_attachment=True, attachment_filename=f'{template_name}.zip')
    except:
        return jsonify({"template": False, "error": "template not found"})

    

