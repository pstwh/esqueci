
class FileManufacturer():
    def __init__(self, template):
        self.template = template

    def compile(self, f):
        data = self.template\
        .replace('{', '(--')\
        .replace('}', '--)')\
        .replace('[--', '{')\
        .replace('--]', '}')\
        .format(**f)\
        .replace('(--', '{')\
        .replace('--)', '}')

        return data

    def generate(self, dir, f):
        os.makedirs(os.path.dirname(dir), exist_ok=True)

        data = self.compile(f)

        file = open(dir, "w")
        file.write(data)

     