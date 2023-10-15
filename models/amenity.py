#!/usr/bin/python3
""" Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A class representing an Amenity.

    An Amenity is a basic unit that may have a name associated with it.

    Attributes:
        name (str): The name of the Amenity.

    """
    name = ""
