from src.model import Model

class Files(Model):

    def __init__(self):
        Model.__init__(self, 'files')
        
    def exists(self, template_name):
        if(self.collection.find({'template_name': template_name}).count() > 0):
            return True
        return False
