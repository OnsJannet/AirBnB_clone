#!/usr/bin/python3
"""Unittest for FileStorage class"""
from models.engine.file_storage import FileStorage
import models
import unittest
import json
import pep8
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import path
import os
from datetime import datetime


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

<<<<<<< HEAD:tests/test_models/test_engine/test_file_storage.py
    def setUp(self):
        """Sets Model to get tested"""
        self.base = FileStorage()

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def updated_at_test(self):
        """created_at testing"""
        base = FileStorage()
        self.assertEqual(type(base.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "update_at"))

    def test_all(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), {})

    def test_new(self):
        base = FileStorage()
        storage = FileStorage()
        storage.new(base)
        self.assertNotEqual(storage.all(), {})


if __name__ == '__main__':
=======

if __name__ == __'main'__:
>>>>>>> 7fe7a50b1006578930f988cd93c10404bfeb74e5:tests/test_models/test_file_storage.py
    unittest.main()
