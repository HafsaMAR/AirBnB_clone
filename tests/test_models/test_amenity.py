#!/usr/bin/python3

import unittest
from models.amenity import Amenity

class AmenityTest(unittest.TestCase):

    def test_init(self):
        """Test that the `name` attribute of a new `Amenity` object is initialized to an empty string."""

        amenity = Amenity()
        self.assertEqual(amenity.name, '')

if __name__ == '__main__':
    unittest.main()