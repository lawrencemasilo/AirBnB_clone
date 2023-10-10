#!/usr/bin/python3
"""
This module contains a review class
"""
from base_model import BaseModel


class Review(BaseModel):
    """
    handles reviews
    """
    place_id = ""
    user_id = ""
    text = ""
