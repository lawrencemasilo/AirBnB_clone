#!/usr/bin/python3
"""
Import modules for tests.
"""
import unittest
import os
import tests
import console
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Tests for the console."""

    @classmethod
    def setUpClass(cls):
        """Sets up class."""
        cls.cnsl = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """
        Tears down class after tests.
        """
        del cls.cnsl
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_emptyline(self):
        """Test for emptyline."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("testing")
            self.assertEqual("** Unknown syntax: testing\n", f.getvalue())

    def test_quit(self):
        """Test for quit."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_help(self):
        """Test for help"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("help")
