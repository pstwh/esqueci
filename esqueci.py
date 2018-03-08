
import json
import os

def generate_file(data, dir):
    os.makedirs(os.path.dirname(dir), exist_ok=True)
    generated_file = open(dir, "w")
    generated_file.write(data)

def unwrap_format(factories):
    for factory in factories:
        for key in factory["format"]:
            if(type(factory["format"][key]) is list):
                unwrap_format(factory["format"][key])
                template = open(factory["format"][key][0]["template"], 'r').read()

                factory["format"][key] = template.replace('{', '(--').replace('}', '--)').replace('[--', '{').replace('--]', '}').format(**factory["format"][key][0]["format"]).replace('(--', '{').replace('--)', '}')

def compile_file(template, f):
    template = open(template, 'r').read()

    data = template.replace('{', '(--').replace('}', '--)').replace('[--', '{').replace('--]', '}').format(**f).replace('(--', '{').replace('--)', '}')
    return data

def compile_schema(schema):
    config = json.load(open('{}.json'.format(schema)))
    project = config["project"]
    
    unwrap_format(config["factory"])

    for schema in config["factory"]:
        instance = compile_file(schema["template"], schema["format"])
        generate_file(instance, schema["name"])


compile_schema('schema')

