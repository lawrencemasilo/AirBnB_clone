#!/usr/bin/python3
"""
Import modules for tests.
"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Tests for file storage class."""

    @classmethod
    def setUpClass(cls):
        """Sets up class."""
        cls.usr = User()
        cls.usr.first_name = "John"
        cls.usr.last_name = "Doe"
        cls.usr.email = "johndoe@gmail.com"
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Deletes class."""
        del cls.usr
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_filestorage(self):
        """Tests for all."""
        new = FileStorage()
        dict_instance = new.all()
        self.assertIsNotNone(dict_instance)
        self.assertEqual(type(dict_instance), dict)
        self.assertIs(dict_instance, new._FileStorage__objects)

    def test_new_filestorage(self):
        """Tests for new."""
        alt_new = FileStorage()
        dic = alt_new.all()
        rev = User()
        rev.id = 69
        rev.name = "Test"
        alt_new.new(rev)
        key = rev.__class__.__name__ + "." + str(rev.id)
        self.assertIsNotNone(dic[key])

    def test_reload_filestorage(self):
        """Tests for reload."""
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except FileNotFoundError:
            pass

        self.storage.save()

        with open(path, 'r') as f:
            lines2 = f.readlines()

        self.assertEqual(lines, lines2)

        try:
            os.remove(path)
        except FileNotFoundError:
            pass

        with open(path, 'w') as f:
            f.write("{}")
        with open(path, 'r') as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
