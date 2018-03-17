from src.model import Model

class Schemas(Model):

    def __init__(self):
        Model.__init__(self, 'schemas')
        
    def exists(self, schema_name):
        if(self.collection.find({'schema_name': schema_name}).count() > 0):
            return True
        return False
