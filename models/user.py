#!/usr/bin/env python3
"""User inherit the BaseModel"""


from models.base_model import BaseModel


class User(BaseModel):
    """A class User that inherits from BaseModel

    Attributes:
        email= ""
        password=""
        first_name = ""
        last_name = ""
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
