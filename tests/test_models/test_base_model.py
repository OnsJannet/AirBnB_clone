#!/usr/bin/python3
import unittest
import json
import pep8
import inspect
import datetime
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Sets Model to get tested"""
        self.base = BaseModel()

    def tearDown(self):
        """removes file"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def object_Instance_creation_test(self):
        """ tests Instance Creation"""
        base = BaseModel()
        base.name = "Holberton"
        self.assertTrue(base.name)
        base.my_number = 89
        self.assertTrue(base.my_number)
        self.assertTrue(base.id)

    def created_at_test(self):
        """created_at testing"""
        base = BaseModel()
        self.assertEqual(type(base.created_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "created_at"))

    def updated_at_test(self):
        """created_at testing"""
        base = BaseModel()
        self.assertEqual(type(base.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "update_at"))

    def test_all(self):
        storage = FileStorage()
        self.assertEqual(storage.all(), {})

    def test_new(self):
        base = BaseModel()
        storage = FileStorage()
        storage.new(base)
        self.assertNotEqual(storage.all(), {})


if __name__ == '__main__':
    unittest.main()
