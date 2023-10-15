#!/usr/bin/python3
""" User model """
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class representing a user in the application.

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user's account.
        first_name (str): The user's first name.
        last_name (str): The user's last name.

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
