#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
import os
import json

class FileStorage:
    """A class for Serializing and Deserializing JSON files"""
    __file_path = 'file.json'
    __objects = {}
    all_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                  "City": City, "Amenity": Amenity, "Place": Place,
                  "Review": Review}

    def __init__(self):
        """Default initializing"""
        pass

    def all(self):
        """Returns a dictionary with all the objects of the program"""
        return self.__objects

    def path(self):
        """Returns the path of the JSON file"""
        return self.__file_path

    def new(self, obj):
        """Creates a new object for the program, or updates an older object"""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        """Serialization:
            Saves all dictionaries from the objects to 'file.json'
        """
        dct = self.__objects.copy()
        for k, o in dct.items():
            dct[k] = o.to_dict()
        with open(self.__file_path, 'w') as fp:
            json.dump(dct, fp)

    def reload(self):
        """Deserialization:
        If 'file.json' exists, extracts all its dicts and converts them in
        objects to be read for the program
        """
        try:
            if os.stat(self.__file_path).st_size == 0:
                raise EOFError()
            with open(self.__file_path, 'r', encoding='UTF-8') as fp:
                obj = json.load(fp)

        except FileNotFoundError:
            pass
        except EOFError:
            pass
