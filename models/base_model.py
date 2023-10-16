#!/usr/bin/python3
""""BaseModel class module that define all
commun attributes of other classes"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Parent class"""

    def __init__(self, *arg, **kwargs):
        ''' Creating BaseModel object

        Args:
            args (None):    not used
            kwargs (dict):  key/value paires used to instantiate
                            a BaseModel object
        '''
        if kwargs:
            for k, w in kwargs.items():
                if k == '__class__':
                    continue
                elif k in ['created_at', 'updated_at']:
                    w = datetime.now().strptime(w, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, k, w)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Save function to save datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """String representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """Creating the Dictionary representation"""
        dictionary = self.__dict__.copy()

        dictionary['id'] = self.id
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
