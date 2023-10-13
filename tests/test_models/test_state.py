#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_init(self):
        """Tests that the name attribute
          of a new `State` object are initialized
            to empty strings."""
        state = State()
        self.assertEqual(state.name, "")

    def test_two_state_unique_ids(self):
        """this function test if two
          instantiated object of STATE
            has differents IDs"""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)


if __name__ == '__main__':
    unittest.main()
