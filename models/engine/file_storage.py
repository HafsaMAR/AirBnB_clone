#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """Class that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Function that returns dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Set in the dictionnary __objects the obj(value) with key <obj class>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """"serialize the dictionnary __objetcs to Json file"""
        formatted_dictionary = {}
        for key, obj in FileStorage.__objects.items():
            formatted_dictionary[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(formatted_dictionary, f)
    
    def reload(self):
        """Deserialize JSON file to objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                deserialized_objects = json.load(f)
                for key, value in deserialized_objects.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            return



   