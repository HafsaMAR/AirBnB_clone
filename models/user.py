#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """class that defines the user of the Hbnb Platform"""
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''

        

    