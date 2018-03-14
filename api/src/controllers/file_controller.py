from src.models.files import Files
from loader import app

file = Files()

@app.route("/files/", defaults={'search': None})
@app.route("/files/search/<string:search>")
def index(search):
    files = file.all()
    return files

@app.route("/files/create")
def create():
    pass

@app.route("/files/retrieve/<string:name>")
def retrieve():
    pass