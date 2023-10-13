#!/usr/bin/python3


import unittest
from models.user import User


class UserTest(unittest.TestCase):

    def test_init(self):
        """Tests that the `email`, `password`,
          `first_name`, and `last_name`
          attributes of a new `User` object are initialized
          to empty strings."""

        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_two_user_unique_ids(self):
        """this function test if two instantiated object
        of user has differents IDs"""
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)


if __name__ == '__main__':
    unittest.main()
