from src.models.model import Model

class Files(Model):
    def __init__(self, name, table_name, primary_key):
        Model.__init__(self, name, table_name, primary_key)
        

