#!/usr/bin/env python3
"""describes the class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """describes state

    attributes:
        place_id (str): ""
        user_id (str): ""
        text (str): ""

    """
    place_id = ""
    user_id = ""
    text = ""
