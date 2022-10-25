# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from sqlalchemy import Column, Integer, String

from app import db


class ModelRecipes(db.Model):

    __tablename__ = 'recipes'

    name = Column(String)
    id = Column(Integer, primary_key=True, unique=True)
    minutes = Column(Integer)
    contributor_id = Column(Integer)
    submitted = Column(String)
    tags = Column(String)
    nutrition = Column(String)
    n_steps = Column(Integer)
    steps = Column(String)
    description = Column(String)
    ingredients = Column(String)
    n_ingredients = Column(Integer)
    label = Column(Integer)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)
        setattr(self, property, value)

    def __repr__(self):
        return str(self.model_id)



