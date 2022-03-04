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
    """Class where we serialize and wish to serialize Json files"""
    all_class = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Review": Review, "Amenity": Amenity, "Place": Place}
    __objets = {}
    __file_path ='file.json'
    
    def __init__(self):
        """Initiation"""
        pass

    def all(self):
        """Returns the dictionary objects"""
        return self.__objets

    def new(self, obj):
        obj_key = "{}.{}".format(obj.__class__.name, obj.id)
        self.__objetcs[obj_key] = obj 

    def save(self):
        """Serialization"""
        dct = self.__objects.copy()
        for i, j in dct.items():
            dct[i] = j.to_dict()
        with open(self.__file_path, 'w') as fp:
            json.dump(dct, fp)
        
    def reload(self):
        """Deserialization"""
        try:
            if os.stat(self.__file_path).st_size == 0:
                raise EOFError()
            with open(self.__file_path, 'r', encoding='UTF-8') as fp:
                obj = json.load(fp)
        except FileNotFoundError:
            pass
        except EOFError:
            pass
        
    def path(self):
        """Returns the path of the Json file"""
        return self.__file_path
