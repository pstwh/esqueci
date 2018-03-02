
import json

config = json.load(open('config.json'))

def compiler(template, f):
    data = template.replace('{', '(--').replace('}', '--)').replace('[--', '{').replace('--]', '}').format(**f).replace('(--', '{').replace('--)', '}')
    return data

for schema in config["factory"]:
    with open('templates/{}'.format(schema["template"])) as template:
        schema_file = template.read()
    template.close()


    instance = compiler(schema_file, schema["format"])
    print(instance)


