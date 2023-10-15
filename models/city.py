#!/usr/bin/python3
""" City """
from models.base_model import BaseModel


class City(BaseModel):
    """
    A class representing a city, typically associated with a state.

    Attributes:
        state_id (str): A reprsentation of the state id.
        name (str): The name of the Amenity.

    """
    state_id = ""
    name = ""
