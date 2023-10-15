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
    """
    A class for managing storage and retrieval of objects in a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all objects currently stored in the FileStorage instance.

        Returns:
            dict: A dictionary containing all objects,
            where keys are in the format "<class_name>.<object_id>"
            and values are the objects themselves.
        """
        return type(self).__objects

    def new(self, obj):
        """
        Add a new object to the FileStorage instance.

        Args:
            obj: The object to be added to the storage.

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """
        Save the current objects in the FileStorage instance to a JSON file.

        """
        obj_dict = {}
        for key, value in type(self).__objects.items():
            obj_dict[key] = value.to_dict()

        with open(type(self).__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Reload objects from the JSON file into the FileStorage instance.

        If the JSON file doesn't exist, this method does nothing.

        """
        if exists(self.__file_path):
            with open(type(self).__file_path, "r") as file:
                obj_dict = json.load(file)

            for key, value in obj_dict.items():
                class_name, obj_id = key.split(".")
                cls = globals()[class_name]
                obj = cls(**value)
                type(self).__objects[key] = obj
