#!/usr/bin/python3
'''Creating the User Function'''

from models.base_model import BaseModel


class User(BaseModel):
    '''Class that contain object attribute'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
