#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):

    def test_two_BaseModel_unique_ids(self):
        """this function test if two instantiated
        object of review has differents IDs"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
