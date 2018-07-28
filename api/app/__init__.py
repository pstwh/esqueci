from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app.schema.controller import schema_module
from app.template.controller import template_module

app.register_blueprint(schema_module)
app.register_blueprint(template_module)
