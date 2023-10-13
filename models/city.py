#!/usr/bin/pyhton3

from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """The City Class to describe the City informations"""
    state_id = ""
    name = ""