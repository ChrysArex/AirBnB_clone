#!/usr/bin/python3
""" File Storage """
import json
from os.path import exists
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        for key, value in self.__objects.items():
            obj_dict = {}
            obj_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)

            for key, value in obj_dict.items():
                class_name, obj_id = key.split(".")
                cls = globals()[class_name]
                obj = cls(**value)
                self.__objects[key] = obj
