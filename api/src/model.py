from src.database import database
from bson.objectid import ObjectId
from bson.json_util import dumps

class Model:
    def __init__(self, table_name):
        self.collection = database[table_name]

    def all(self):
        cursor = self.collection.find()
        return dumps(cursor)

    def find(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def create(self, obj):
        return self.collection.insert_one(obj)

    def update(self, obj, id):
        pass

    def destroy(self, id):
        pass
        