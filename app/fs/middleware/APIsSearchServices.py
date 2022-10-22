import json

import requests as requests

from app import config_parser


class APIsSearchServices:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def get_related_cluster(self, ingredients):
        # api-endpoint
        URL = 'http://127.0.0.1:5000/api/v1/labeldata'

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'data': ingredients}

        # sending get request and saving the response as response object
        r = requests.post(url=URL, json=PARAMS)
        if r.status_code == 200:
            return r.json()

        return r.status_code
