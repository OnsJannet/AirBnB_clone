#!/usr/bin/python3
''' Class Test '''
import unittest
import json
import pep8
import inspect
import datetime
import os
from models.state import State


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Sets Model to get tested"""
        self.base = State()

    def tearDown(self):
        """removes file"""
        self.base = State()

    def object_Instance(self):
        """ tests Instance Creation"""
        self.assertIsInstance(self.state, BaseModel)

    def created_at_test(self):
        """created_at testing"""
        base = State()
        self.assertEqual(type(base.created_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "created_at"))

    def updated_at_test(self):
        """updated testing"""
        base = State()
        self.assertEqual(type(base.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "update_at"))

    def test_id(self):
        """city id testing"""
        base = State()
        self.assertEqual(type(base.id), str)
        self.assertTrue(hasattr(base, "city_id"))

    def test_user_id(self):
        """ user id testing"""             
        base = State()
        self.assertEqual(type(base.id), str)
        self.assertTrue(hasattr(base, "user_id"))

    def test_place_description(self):
        '''description testing'''
        base = State()
        self.assertTrue(hasattr(base, "description"))
        self.assertEqual(type(base.description), str)

    def test_place_number_rooms(self):
        '''number of rooms testing'''
        base = State()
        self.assertTrue(hasattr(base, "number_rooms"))
        self.assertEqual(type(base.number_rooms), int)

    def test_place_number_bathrooms(self):
        '''number of Tbathrooms testing'''
        base = State()
        self.assertTrue(hasattr(base, "number_bathrooms"))
        self.assertEqual(type(base.number_bathrooms), int)

    def test_place_max_guest(self):
        '''max guest testing'''
        base = State()
        self.assertTrue(hasattr(base, "max_guest"))
        self.assertEqual(type(base.max_guest), int)

    def test_price_by_night(self):
        '''price by night testing'''
        base = State()
        self.assertTrue(hasattr(base, "price_by_night"))
        self.assertEqual(type(base.price_by_night), int)

    def test_latitude(self):
        '''latitude testing'''
        base = State()
        self.assertTrue(hasattr(base, "latitude"))
        self.assertEqual(type(base.latitude), float)

    def test_longitude(self):
        '''longtitude testing'''
        base = State()
        self.assertTrue(hasattr(base, "longitude"))
        self.assertEqual(type(base.longitude), float)

    def test_amenity(self):
        '''amenity testing'''
        base = State()
        self.assertTrue(hasattr(base, "amenity_ids"))
        self.assertEqual(type(base.amenity_ids), list)



if __name__ == '__main__':
    unittest.main()
