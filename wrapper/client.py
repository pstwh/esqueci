import requests
import json

class Client():
    def __init__(self, url):
        self.url = url

    def getTemplate(self, template_name):
        url = f'{self.url}/template/{template_name}'
        resp = requests.request("GET", url)

        return resp.content

    def getSchema(self, schema_name):
        url = f'{self.url}/schema/{schema_name}'
        resp = requests.request("GET", url)

        return json.loads(resp.text)