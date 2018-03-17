from flask import request, jsonify
from src.models.schema import Schemas

from loader import app

import datetime
import json

schema = Schemas()

@app.route("/schema")
def index_schema():
    schemas = schema.find({})
    return schemas

@app.route("/schema/create", methods=['POST'])
def create_schema():
    schema_name = request.form['schema_name']
    schema_file = request.files['schema_file']
    schema_json = json.loads(schema_file.read())

    obj_schema = {
        "schame_name": schema_name,
        "schema_description": schema_json,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now()
    }

    schema.create(obj_schema)

    return jsonify({"insert": True})
    