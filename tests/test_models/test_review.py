#!/usr/bin/python3
"""Import modules for tests."""
import unittest
import os
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """tests for review class."""

    @classmethod
    def setUpClass(cls):
        """Sets up class."""
        cls.testReview = Review()
        cls.testReview.place_id = "1234567"
        cls.testReview.user_id = "Me"
        cls.testReview.text = "Nice place"

    @classmethod
    def tearDownClass(cls):
        """deletes class after test."""
        del cls.testReview

    def tearDownClass(self):
        """tears down class."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_Review(self):
        """Tests for docstring."""
        self.assertIsNotNone(Review.__doc__)

    def test_attr_Review(self):
        """
        Tests for instance attributes.
        """
        self.assertTrue('id' in self.testReview.__dict__)
        self.assertTrue('created_at' in self.testReview.__dict__)
        self.assertTrue('updated_at' in self.testReview.__dict__)
        self.assertTrue('place_id' in self.testReview.__dict__)
        self.assertTrue('text' in self.testReview.__dict__)
        self.assertTrue('user_id' in self.testReview.__dict__)

    def test_attr_types_Review(self):
        """
        Tests instance of attr type.
        """
        self.assertEqual(type(self.testReview.text), str)
        self.assertEqual(type(self.testReview.place_id), str)
        self.assertEqual(type(self.testReview.user_id), str)

    def test_subclass_Review(self):
        """tests inheritance."""
        self.assertTrue(issubclass(self.testReview.__class__, BaseModel), True)

    def test_save(self):
        """tests save()."""
        self.testReview.save()
        self.assertNotEqual(self.testReview.created_at,
                            self.testReview.updated_at)

    def test_to_dict(self):
        """tests dict."""
        self.assertEqual('to_dict' in dir(self.testReview), True)


if __name__ == "__main__":
    unittest.main()
