#!/usr/bin/python3

import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def test_init(self):
        """Test that the `name` attribute of a new `Amenity` object is initialized to an empty string."""

        city = City()
        self.assertEqual(city.name, '')
        self.assertEqual(city.state_id, '')

if __name__ == '__main__':
    unittest.main()