import json

import requests as requests

from app import config_parser
from app.fs.models.ModelInteractions import ModelInteractions
from app.fs.models.ModelRecipes import ModelRecipes


class APIsSearchServices:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def search_meals(self, ingredients):
        # api-endpoint
        URL = 'http://127.0.0.1:5000/api/v1/labeldata'

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'data': ingredients}

        # sending get request and saving the response as response object
        r = requests.post(url=URL, json=PARAMS)
        if r.status_code == 200:
            return_data = r.json()
            for k,v in return_data.items():
                k_arr = k.split('Cluster_')
                tags = v
                label_index = int(k_arr[1])
                meals = ModelRecipes.query.with_entities(ModelRecipes.id,ModelRecipes.name, ModelRecipes.description, ModelRecipes.n_steps).filter_by(label=label_index).limit(10).all()
            return tags,meals

        return r.status_code

    def show_meal(self, meal_id):
        meal = ModelRecipes.query.with_entities(ModelRecipes.id,ModelRecipes.name, ModelRecipes.minutes, ModelRecipes.n_steps, ModelRecipes.description, ModelRecipes.steps).filter_by(id =meal_id).all()
        interactions = ModelInteractions.query.with_entities(ModelInteractions.user_id,ModelInteractions.date, ModelInteractions.rating, ModelInteractions.review).filter_by(recipe_id=meal_id).all()
        return meal, interactions

