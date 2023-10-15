#!/usr/bin/python3
""" BaseModel """
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    BaseModel is the base class for all models in the application.
    It provides common functionality for managing object attributes,
    serialization, and storage.

    Attributes:
        id (str): A unique identifier for the instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.

    Methods:
        __init__(self, *args, **kwargs):
            Initializes a new BaseModel instance. If keyword arguments
            (kwargs) are provided, it populates the instance attributes with
            those values. If no kwargs are provided, it generates
            a new unique ID and sets the creation and update timestamps.

        __str__(self):
            Returns a string representation of the instance, including its
            class name, ID, and attributes in dictionary format.

        save(self):
            Updates the 'updated_at' timestamp and saves the instance
            to storage.

        to_dict(self):
            Converts the instance into a dictionary containing its attributes,
            suitable for serialization.

    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.
                            strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        class_name = self.__class__.__name__
        id = self.id
        dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, id, dict)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        class_name = self.__class__.__name__
        attributes = self.__dict__.copy()
        attributes['created_at'] = self.created_at.isoformat()
        attributes['updated_at'] = self.updated_at.isoformat()
        attributes['__class__'] = class_name
        return attributes
