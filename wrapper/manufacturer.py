import os
import sys
import json

class Manufacturer():
    def unwrap_format(self, factories):
        for factory in factories:
            for key in factory["format"]:
                if(type(factory["format"][key]) is list):
                    unwrap_format(factory["format"][key])

                    partial_unwrapped = ''
                    for module in factory["format"][key]: 
                        template = open(module["template"], 'r').read()
                        partial_unwrapped = partial_unwrapped + template.replace('{', '(--').replace('}', '--)').replace('[--', '{').replace('--]', '}').format(**module["format"]).replace('(--', '{').replace('--)', '}')
                    factory["format"][key] = partial_unwrapped

    def generate_file(self, data, dir):
        os.makedirs(os.path.dirname(dir), exist_ok=True)
        generated_file = open(dir, "w")
        generated_file.write(data)

    def compile_file(self, template, f):
        template = open(template, 'r').read()
        data = template.replace('{', '(--').replace('}', '--)').replace('[--', '{').replace('--]', '}').format(**f).replace('(--', '{').replace('--)', '}')
        return data

    def compile_schema(self, schema):
        config = json.load(open('{}.json'.format(schema)))
        project = config["project"]
        unwrap_format(config["factory"])

        for schema in config["factory"]:
            instance = compile_file(schema["template"], schema["format"])
            generate_file(instance, schema["name"])
