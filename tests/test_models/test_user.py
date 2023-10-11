#!/usr/bin/python3
"""
Import modules for tests.
"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for user class."""

    @classmethod
    def setUpClass(cls):
        """Sets up class."""
        cls.testUser = User()
        cls.testUser.email = "email"
        cls.testUser.password = "xxx"
        cls.testUser.first_name = "first"
        cls.testUser.last_name = "last"

    @classmethod
    def tearDownClass(cls):
        """Deletes class."""
        del cls.testUser
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstrings(self):
        """Tests docstrings."""
        self.assertTrue(len(User.__doc__) > 0)
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)

    def test_init_and_class_variables(self):
        """Tests init and class variables."""
        self.assertTrue(isinstance(self.testUser, User))
        self.assertTrue(issubclass(type(self.testUser), BaseModel))
        self.assertTrue('email' in self.testUser.__dict__)
        self.assertTrue('id' in seld.testUser.__dict__)
        self.assertTrue('created_at' in self.testUser.__dict__)
        self.assertTrue('updated_at' in self.testUser.__dict__)
        self.assertTrue('password' in self.testUser.__dict__)
        self.assertTrue('first_name' in self.testUser.__dict__)
        self.assertTrue('last_name' in self.testUser.__dict__)

    def test_save(self):
        """Tests save."""
        self.testUser.save()
        self.assertTrue(self.testUser.updated_at != self.testUser.created_at)

    def test_strings(self):
        """Tests strings."""
        self.assertEqual(type(self.testUser.email), str)
        self.assertEqual(type(self.testUser.password), str)
        self.assertEqual(type(self.testUser.first_name), str)
        self.assertEqual(type(self.testUser.last_name), str)

    def test_to_dict(self):
        """Tests dict."""
        self.assertEqual('to_dict' in dir(self.testUser), True)


if __name__ == "__main__":
    unittest.main()
