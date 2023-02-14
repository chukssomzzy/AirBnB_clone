#!/usr/bin/env python3
"""describes the class Amenity"""

from models.base_model import BaseModel


class Place(BaseModel):
    """describes state

    attributes:
        name: ""
        user_id: ""
        city_id: ""
        description: ""
        number_rooms (int): 0
        max_guest (int): 0
        price_by_night (int): 0
        latitude (float): 0.0
        longitude (float): 0.0
        number_bathrooms (int): 0
        amenity_ids (list:str): ""
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    numbers_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    amenity_ids = []
