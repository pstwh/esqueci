class Model:
    def __init__(self, mongo, name, table_name, primary_key):
        self.name = name
        self.table_name = table_name
        self.primary_key = primary_key
        self.mongo = mongo

    def all(self):
        #print(self.mongo.db.files.find({}))
        #mongo = getattr('%s' % self.mongo)
        #all_ = getattr(mongo.db, '%s' % self.table_name).find({})
        #mongo.db.%s.find({}
        return all

    def find(id):
        pass

    def create(obj):
        pass

    def update(obj, id):
        pass

    def destroy(id):
        pass
        