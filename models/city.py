#!/usr/bin/pyhton3
'''Creating City Object'''

from models.base_model import BaseModel


class City(BaseModel):
    """The City Class to describe the City informations"""
    state_id = ""
    name = ""
