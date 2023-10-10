#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

""""BaseModel class module that define all commun attributes of other classes"""


class BaseModel():
    """" Parent class""" 
    # id = str(uuid4())   
    def __init__(self):
        self.id = str(uuid4())  
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # @property
    # def id(self):
    #     return self.id
    
    # @id.setter
    # def id(self, value):
    #     self.id = value

    
    def save(self):
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['id'] = self.id   
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

# model = BaseModel()
# print(model.created_at)


bm = BaseModel() 

print(bm.to_dict())