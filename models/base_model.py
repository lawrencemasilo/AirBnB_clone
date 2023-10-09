#!/usr/bin/python3
"""This module contains the base class for all classes"""
import uuid
import datetime


class BaseModel:
    """Creates Base model class."""
    def __init__(self):
        """Initialises the class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Defines string representation of base model.
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the attribute with current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns dict representation of object.
        """
        instance_dict = dict(self.__dict__)

        instance_dict['__class__'] = str(self.__class__.__name__)
        instance_dict['created at'] = self.created_at.isoformat()
        instance_dict['updated at'] = self.updated_at.isoformat()

        return instance_dict
