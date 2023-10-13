#!/usr/bin/python3
"""
Import modules for tests.
"""
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for base class."""

    @classmethod
    def setUpClass(cls):
        """Sets up class"""
        cls.testBase = BaseModel()
        cls.testBase.x = "x"
        cls.testBase.y = 100

    @classmethod
    def tearDownClass(cls):
        """Tears down class"""
        del cls.testBase
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    """def test_pep8_basemodel(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
    """

    def test_init(self):
        """Tests for init"""
        self.assertTrue(isinstance(self.testBase, BaseModel))

    def test_save(self):
        """Test for save"""
        self.testBase.save()
        self.assertNotEqual(self.testBase.created_at, self.testBase.updated_at)

    def test_to_dict(self):
        """Tests for dict"""
        instance_dict = self.testBase.to_dict()
        self.assertEqual(self.testBase.__class__.__name__, 'BaseModel')
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
