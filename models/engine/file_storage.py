#!/usr/bin/python3
"""
Import modules for class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


"""
Below class serializes instances to a JSON file
and deserializes JSON file to instances.
"""


class FileStorage:
    """Created instance of class."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dict of objects."""
        return self.__objects

    def new(self, obj):
        """Sets obj to __objets."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to json file."""
        json_data = {}
        for key, value in self.__objects.items():
            json_data[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_data, f)

    def reload(self):
        """Deserializes json file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj in data.items():
                    new_obj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = new_obj
        except FileNotFoundError:
            pass
