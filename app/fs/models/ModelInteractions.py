# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from sqlalchemy import Column, Integer, String

from app import db


class ModelInteractions(db.Model):

    __tablename__ = 'interactions'

    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer)
    recipe_id = Column(Integer)
    date = Column(String)
    rating = Column(Integer)
    review = Column(String)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            setattr(self, property, value)
        setattr(self, property, value)

    def __repr__(self):
        return str(self.model_id)



