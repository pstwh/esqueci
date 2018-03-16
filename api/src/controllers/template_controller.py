from flask import request, jsonify, send_from_directory, after_this_request, send_file, Response
from src.models.files import Files

from loader import app

import os
import datetime
import shutil
import hashlib
import zipfile
from io import BytesIO

file = Files()

@app.route("/template")
def index():
    files = file.find({})
    return files

@app.route("/template/create", methods=['POST'])
def create():
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

"""
@app.route("/template/<string:template_name>")
def retrieve_template(template_name):
    temp_md5 = hashlib.md5(template_name.encode('utf-8')).hexdigest()
    temp_path = f'{app.config["TEMP_DIR"]}/{temp_md5}'
    template_dir = f'{app.config["TEMPLATE_DIR"]}/{template_name}'

    shutil.make_archive(temp_path, 'zip', template_dir)
    temp_file = open(f'{temp_path}.zip', 'r')

    return send_file(temp_file, attachment_filename=f'{template_name}.zip')
    
"""

@app.route("/template/<string:template_name>")
def retrieve_template(template_name):
    temp_md5 = hashlib.md5(template_name.encode('utf-8')).hexdigest()
    temp_path = f'{app.config["TEMP_DIR"]}/{temp_md5}'
    template_dir = f'{app.config["TEMPLATE_DIR"]}/{template_name}'

    temp_zip = BytesIO()
    with zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zf:
        for root, dirs, files in os.walk(template_dir):
            for f in files:
                data = zipfile.ZipInfo(f['fileName'])
                data.date_time = time.localtime(time.time())[:6]
                data.compress_type = zipfile.ZIP_DEFLATED
                zf.writestr(data, f['fileData'])
    memory_file.seek(0)
    return send_file(temp_zip, attachment_filename=f'{template_name}.zip')
    

