class SchemaManufacturer():
    def __init__(self, schema_file):
        self.schema = schema_file

    def unwrap_format(self, factories):
        for factory in factories:
            for key in factory["format"]:
                if(type(factory["format"][key]) is list):
                    self.unwrap_format(factory["format"][key])

                    partial_unwrapped = ''
                    for module in factory["format"][key]: 
                        template = open(module["template"], 'r').read()

                        partial_unwrapped = partial_unwrapped + template.replace('{', '(--').replace('}', '--)').replace('[--', '{').replace('--]', '}').format(**module["format"]).replace('(--', '{').replace('--)', '}')
                    factory["format"][key] = partial_unwrapped
    
    def compile_schema(self, schema):
        s = self.client.getSchema(schema)

        config = s['schema_description']
        project = config["project"]
        self.unwrap_format(config["factory"])

        for schema in config["factory"]:
            instance = compile_file(schema["template"], schema["format"])
            generate_file(instance, schema["name"])