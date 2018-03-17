import os
import sys
import json
from client import Client

class Manufacturer():
    def __init__(self, url, config):
        self.client = Client(url)
        self.config = config
    
if __name__ == '__main__':
    manufacturer = Manufacturer('http://localhost:5000')