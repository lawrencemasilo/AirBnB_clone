#!/usr/bin/python3
"""Import modules for tests."""
import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for the amenity class."""

    @classmethod
    def setUpClass(cls):
        """Sets up class for test."""
        cls.testAmenity = Amenity()
        cls.testAmenity.name = "Lunch"

    @classmethod
    def tearDownClass(cls):
        """Deletes after test is done."""
        del cls.testAmenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_Amenity(self):
        """Tests for docstrings."""
        self.assertIsNotNone(self.testAmenity.__doc__)

    def test_attr_Amenity(self):
        """Tests for attributes."""
        self.assertTrue('id' in self.testAmenity.__dict__)
        self.assertTrue('created_at' in self.testAmenity.__dict__)
        self.assertTrue('updated_at' in self.testAmenity.__dict__)
        self.assertTrue('name' in self.testAmenity.__dict__)

    def test_attrtype_Amenity(self):
        """
        Tests for attribute types.
        """
        self.assertEqual(type(self.testAmenity.name), str)

    def test_save(self):
        """Tests save()."""
        self.testAmenity.save()
        self.assertNotEqual(self.testAmenity.created_at,
                            self.testAmenity.updated_at)

    def test_to_dict(self):
        """Tests dict."""
        self.assertEqual('to_dict' in dir(self.testAmenity), True)

    def test_inheritance_Amen(self):
        """Tests for inheritance."""
        self.assertTrue(issubclass(
                        self.testAmenity.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
