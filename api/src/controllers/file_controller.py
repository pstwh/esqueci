from flask import request
from src.models.files import Files
from loader import app

file = Files()

@app.route("/files/", defaults={'search': None})
@app.route("/files/search/<string:search>")
def index(search):
    files = file.all()
    return files

@app.route("/files/create", methods=['POST'])
def create():
    template_name = request.form['template_name']
    if(file.exists(template_name)):
        return "Exists"

    template_file = request.files['template_file']
    #return template_file
    template_file.save(f'/{template_name}')

    return "Ok"

@app.route("/files/retrieve/<string:name>")
def retrieve():
    pass