class FileManufacturer():
    def __init__(self, template_file):
        self.template = template_file

    def compile(self, f):
        data = template\
        .replace('{', '(--')\
        .replace('}', '--)')\
        .replace('[--', '{')\
        .replace('--]', '}')\
        .format(**f)\
        .replace('(--', '{')\
        .replace('--)', '}')

        return data

    def generate(self, data, dir):
        os.makedirs(os.path.dirname(dir), exist_ok=True)
        file = open(dir, "w")
        file.write(data)

     