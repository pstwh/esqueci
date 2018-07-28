from flask import Blueprint, request, jsonify

schema_module = Blueprint("schema", __name__, url_prefix="/schema")


@schema_module.route("/schema")
def index_schema():
    schemas = schema.find({})
    return schemas


@schema_module.route("/schema/create", methods=["POST"])
def create_schema():
    schema_name = request.form["schema_name"]
    schema_file = request.files["schema_file"]
    schema_json = json.loads(schema_file.read())

    obj_schema = {
        "schema_name": schema_name,
        "schema_description": schema_json,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    }

    schema.create(obj_schema)

    return jsonify({"insert": True})


@schema_module.route("/schema/<string:schema_name>")
def retrieve_schema(schema_name):
    schema_json = schema.find_one({"schema_name": schema_name})
    return schema_json
