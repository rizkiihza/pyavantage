import urllib.request
import json
import logging

logging.basicConfig(level=logging.ERROR)

class Client(object):
    def __init__(self):
        self.main_url = "https://www.alphavantage.co/query?"

    def get_response(self, path):
        url = self.main_url + path
        res = ""

        with urllib.request.urlopen(url) as response:
            res = response.read()

        json_response = json.loads(res)

        return json_response