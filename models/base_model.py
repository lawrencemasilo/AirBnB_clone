#!/usr/bin/python3
"""This module contains the base class for all classes"""
import uuid
import datetime


class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        instance_dict = self.__dict__

        instance_dict["__class__"] = self.id
        instance_dict["__class__"] = str(self.created_at.isoformat())
        instance_dict["__class__"] = str(self.updated_at.isoformat())

        return instance_dict
