#!/usr/bin/python3
""" Base Model """
from models import storage
import uuid
from datetime import datetime


class BaseModel():
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
            storage.new(self)

    def __str__(self):
        class_name = self.__class__.__name__
        id = self.id
        dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, id, dict)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        class_name = self.__class__.__name__
        attributes = self.__dict__.copy()
        attributes['created_at'] = self.created_at.isoformat()
        attributes['updated_at'] = self.updated_at.isoformat()
        attributes['__class__'] = class_name
        return attributes
