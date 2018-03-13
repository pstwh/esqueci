from .model import Model

class Files(Model):
    def __init__(self, mongo, name, table_name, primary_key):
        Model.__init__(self, mongo, name, table_name, primary_key)
        

