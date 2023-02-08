#!/usr/bin/python3
"""Class FileStorage: serializes instances to a JSON file
    and deserializes JSON file to instances."""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


class_keys = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
              "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    # string - path to the JSON file (ex: file.json)
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        #Serialization is the process of converting the state of an object, that is, 
        #the values of its properties, into a form that can be stored or transmitted.
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps({key: value.to_dict() for key, value
                                in self.__objects.items()}))

    def reload(self):
        """deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists;
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)"""
        #Deserialization reconstructs an object from the serialized form.
