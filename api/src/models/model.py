from src.database import client

class Model:
    def __init__(self, name, table_name, primary_key):
        self.name = name
        self.table_name = table_name
        self.primary_key = primary_key

    def all(self):
        #print(self.mongo.db.files.find({}))
        #mongo = getattr('%s' % self.mongo)
        #all_ = getattr(mongo.db, '%s' % self.table_name).find({})
        #mongo.db.%s.find({}
        return 'teste'

    def find(id):
        pass

    def create(obj):
        pass

    def update(obj, id):
        pass

    def destroy(id):
        pass
        