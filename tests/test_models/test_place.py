#!/usr/bin/python3
"""Import modules for tests."""
import unittest
import os
from models.base_models import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for place class."""

    @classmethod
    def setUpClass(cls):
        """sets up class."""
        cls.testPlace = Place()
        cls.testPlace.city_id = "anywhere"
        cls.testPlace.user_id = "someone"
        cls.testPlace.name = "somewhere"
        cls.testPlace.description = "example"
        cls.testPlace.number_rooms = 0
        cls.testPlace.number_bathrooms = 0
        cls.testPlace.max_guest = 0
        cls.testPlace.price_by_night = 0
        cls.testPlace.latitude = 0.0
        cls.testPlace.longitude = 0.0
        cls.testPlace.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """
        deletes class after test is done.
        """
        del cls.testPlace
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstrings(self):
        """Tests for docstrings."""
        self.assertTrue(len(Place.__doc__) > 0)
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)

    def test_subclass(self):
        """Tests subclasses."""
        self.assertTrue(issubclass(
                        self.testPlace.__class__, BaseModel), True)

    def test_attr_and_init(self):
        """Tests attributes and init"""
        self.assertTrue(isinstance(self.testPlace, Place))
        self.assertTrue('id' in self.testPlace.__dict__)
        self.assertTrue('created_at' in self.testPlace.__dict__)
        self.assertTrue('updated_at' in self.testPlace.__dict__)
        self.assertTrue('city_id' in self.testPlace.__dict__)
        self.assertTrue('user_id' in self.testPlace.__dict__)
        self.assertTrue('name' in self.testPlace.__dict__)
        self.assertTrue('description' in self.testPlace.__dict__)
        self.assertTrue('number_rooms' in self.testPlace.__dict__)
        self.assertTrue('number_bathrooms' in self.testPlace.__dict__)
        self.assertTrue('max_guest' in self.testPlace.__dict__)
        self.assertTrue('price_by_night' in self.testPlace.__dict__)
        self.assertTrue('latitude' in self.testPlace.__dict__)
        self.assertTrue('longitude' in self.testPlace.__dict__)
        self.assertTrue('amenity_ids' in self.testPlace.__dict__)

    def test_strings(self):
        """Tests for strings."""
        self.assertEqual(type(self.testPlace.city_id), str)
        self.assertEqual(type(self.testPlace.user_id), str)
        self.assertEqual(type(self.testPlace.name), str)
        self.assertEqual(type(self.testPlace.description), str)
        self.assertEqual(type(self.testPlace.number_rooms), int)
        self.assertEqual(type(self.testPlace.number_bathrooms), int)
        self.assertEqual(type(self.testPlace.max_guest), int)
        self.assertEqual(type(self.testPlace.price_by_night), int)
        self.assertEqual(type(self.testPlace.latitude), float)
        self.assertEqual(type(self.testPlace.longitude), float)
        self.assertEqual(type(self.testPlace.amenity_ids), list)

    def test_save(self):
        """tests save()."""
        self.testPlace.save()
        self.assertNotEqual(self.testPlace.created_at,
                            self.testPlace.updated_at)

    def test_to_dict(self):
        """Tests dict."""
        self.assertEqual('to_dict' in dir(self.testPlace), True)


if __name__ == "__main__":
    unittest.main()
