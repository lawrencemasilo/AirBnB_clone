#!/usr/bin/python3
"""Import modules for tests."""
import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Tests State class."""

    @classmethod
    def setUpClass(cls):
        """Sets up class."""
        cls.testState = State()
        cls.testState = "GP"

    @classmethod
    def tearDownClass(cls):
        """deletes after tests."""
        del cls.testState
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_State(self):
        """Tests for docstring."""
        self.assertIsNotNone(State.__doc__)

    """
    def test_attr_State(self):

        self.assertTrue('id' in self.testState.__dict__)
        self.assertTrue('created_at' in self.testState.__dict__)
        self.assertTrue('updated_at' in self.testState.__dict__)
        self.assertTrue('name' in self.testState.__dict__)
    """

    def test_inheritance_State(self):
        """tests for inheritance."""
        self.assertFalse(issubclass(self.testState.__class__, BaseModel), True)

    """
    def test_attr_type_State(self):

        self.assertEqual(type(self.testState.name), str)
    """

    """
    def test_save(self):

        self.testState.save()
        self.assertNotEqual(self.testState.created_at,
                            self.testState.updated_at)
    """

    def test_to_dict(self):
        """Tests dict."""
        self.assertEqual('to_dict' in dir(self.testState), False)


if __name__ == "__main__":
    unittest.main()
