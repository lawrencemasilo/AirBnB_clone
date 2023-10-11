#!/usr/bin/python3
"""
Import modules for tests.
"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for file storage class."""

    @classmethod
    def setUpClass(cls):
        """Sets up class."""
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_all_filestorage(self):
        """Tests for all."""
        new = FileStorage()
        dict_instance = new.all()
        self.assertIsNotNone(dict_instance)
        self.assertEqual(type(dict_instance), dict)
        self.assertIs(dict_instance, new._FileStorage__objects)

if __name__ == "__main__":
    unittest.main()
