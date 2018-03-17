import os
import sys
import json
import pyperclip

def unwrap_format(factories):
    for factory in factories:
        for key in factory["format"]:
            if(type(factory["format"][key]) is list):
                unwrap_format(factory["format"][key])

                partial_unwrapped = ''
                for module in factory["format"][key]: 
                    template = open(module["template"], 'r').read()
                    partial_unwrapped = partial_unwrapped + template.replace('{', '(--').replace('}', '--)').replace('[--', '{').replace('--]', '}').format(**module["format"]).replace('(--', '{').replace('--)', '}')
                factory["format"][key] = partial_unwrapped

def generate_file(data, dir):
    os.makedirs(os.path.dirname(dir), exist_ok=True)
    generated_file = open(dir, "w")
    generated_file.write(data)

def generate_clipboard(data):
    pyperclip.copy(data)

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


if __name__ == '__main__':
        file_name = sys.argv[1]

        if len(sys.argv) < 3:
            compile_schema(file_name)
            
        else:
            file_params = sys.argv[2:]

            file_params = dict(i.split(':::') for i in file_params)
            file_data = compile_file(file_name, file_params)
            generate_clipboard(file_data)
