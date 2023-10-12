#!/usr/bin/python3
"""Import modules for tests."""
import unittest
import os
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests for city."""

    @classmethod
    def setUpClass(cls):
        """sets up class for tests."""
        cls.testCity = City()
        cls.testCity.name = "London"
        cls.testCity.state_id = "L"

    @classmethod
    def tearDownClass(cls):
        """
        Deletes test class after its done.
        """
        del cls.testCity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_doctstrings_City(self):
        """Tests for docstring."""
        self.assertTrue(len(City.__doc__) > 0)
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

    def test_init_class_City(self):
        """
        Tests init and class variables.
        """
        self.assertTrue(isinstance(self.testCity, City))
        self.assertTrue(issubclass(type(self.testCity), BaseModel))
        self.assertTrue(self.testCity.name == "London")
        self.assertTrue(self.testCity.state_id == "L")
        self.assertIsNotNone(self.testCity.id)
        self.assertIsNotNone(self.testCity.created_at)
        self.assertIsNotNone(self.testCity.updated_at)

    def test_save_City(self):
        """Tests save()."""
        self.testCity.save()
        self.assertTrue(self.testCity.updated_at != self.testCity.created_at)


if __name__ == "__main__":
    unittest.main()
