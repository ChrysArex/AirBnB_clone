#!/usr/bin/python3
""" Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class representing a review for a place.

    This class is intended to store information about a user's
    review of a place, including the place's ID, the user's ID,
    and the review text.

    Attributes:
        place_id (str): The unique identifier of the place being reviewed.
        user_id (str): The unique identifier of the user who wrote the review.
        text (str): The text of the review provided by the user.

    """
    place_id = ""
    user_id = ""
    text = ""
