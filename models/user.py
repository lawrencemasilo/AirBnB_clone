#!/usr/bin/python3
"""Import modules for class."""
from models.base_model import BaseModel


"""
Below class inherits from BaseModel class.
"""


class User(BaseModel):
    """Created instance of class."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
