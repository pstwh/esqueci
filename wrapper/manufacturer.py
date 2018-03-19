import os
import sys
import json

from client import Client
from file_manufacturer import FileManufacturer

class Manufacturer():
    def __init__(self, url, config=None):
        self.client = Client(url)
        #self.config = config

    def saveTemplate(self, template_name, template):
        pass

    def saveSchema(self, schema_name, schema):
        pass
    
if __name__ == '__main__':
    manufacturer = Manufacturer('http://localhost:5000')

    template = manufacturer.client.getTemplate('laravel-form')
    file = FileManufacturer(template)

    print(file.template)
