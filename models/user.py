#!/usr/bin/env python3
"""User inherit the BaseModel"""


import base_model


class User(base_model.BaseModel):
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
