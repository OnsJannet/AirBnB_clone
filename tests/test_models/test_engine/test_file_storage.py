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

    def setUp(self):
        """Sets Model to get tested"""
        self.base = FileStorage()

    def tearDown(self):
        """removes file"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def object_Instance_creation_test(self):
        """ tests Instance Creation"""
        base = FileStorage()
        base.name = "Holberton"
        self.assertTrue(base.name)
        base.my_number = 89
        self.assertTrue(base.my_number)
        self.assertTrue(base.id)

    def created_at_test(self):
        """created_at testing"""
        base = FileStorage()
        self.assertEqual(type(base.created_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "created_at"))

    def updated_at_test(self):
        """created_at testing"""
        base = FileStorage()
        self.assertEqual(type(base.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "update_at"))


    def test_new(self):
        base = FileStorage()
        storage = FileStorage()
        storage.new(base)
        self.assertNotEqual(storage.all(), {})

    def save(self):
        base = FileStorage()
        base.save()
        self.assertTrue(os.path.exists(self.path_file('file.json')))

    def reload(self):
        base = FileStorage()
        base.reload()
        self.assertTrue(os.path.exists(self.path_file('file.json')))

    def to_dict(self):
        base = FileStorage()
        self.assertEqual(type(base.to_dict()), dict)


    def test_path(self):
        storage = FileStorage()
        self.assertTrue(isinstance(storage._FileStorage__file_path, str))



if __name__ == '__main__':
    unittest.main()