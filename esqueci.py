
import json
import os

def generate_file(data, dir):
    os.makedirs(os.path.dirname(dir), exist_ok=True)
    generated_file = open(dir, "w")
    generated_file.write(data)

def compile_file(template, f):
    template = open(template, 'r').read()

    data = template.replace('{', '(--').replace('}', '--)').replace('[--', '{').replace('--]', '}').format(**f).replace('(--', '{').replace('--)', '}')
    return data

def compile_schema(schema):
    config = json.load(open('{}.json'.format(schema)))
    project = config["project"]
    for schema in config["factory"]:
        instance = compile_file(schema["template"], schema["format"])
        generate_file(instance, schema["name"])


compile_schema('schema')

