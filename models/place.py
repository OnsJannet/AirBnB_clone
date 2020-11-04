#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """Inherits from BaseModel"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int
    number_bathrooms = int
    max_guest = int
    price_by_night = int
    latitude = float
    longitude = float
    amenity_ids = []