#!/usr/bin/python3
"""This module contains the base class for all classes"""
import uuid
import datetime


class BaseModel:
    """Creates Base model class."""
    def __init__(self, *args, **kwargs):
        """Initialises the class."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
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
        instance_dict = self.__dict__

        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict
