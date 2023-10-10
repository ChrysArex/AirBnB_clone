#!/usr/bin/python3
""" BaseModel """
import uuid
from datetime import datetime


class BaseModel():
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = created_at

    def __str__(self):
        class_name = self.__class__.__name__
        id = self.id
        dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, id, dict)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        class_name = self.__class__.__name__
        attributes = self.__dict__.copy()
        attributes['created_at'] = self.created_at.isoformat()
        attributes['updated_at'] = self.updated_at.isoformat()
        attributes['__class__'] = class_name
        return attributes
