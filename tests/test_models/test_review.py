#!/usr/bin/python3

import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_init(self):
        review = Review()
        self.assertEqual(review.place_id , "")
        self.assertEqual(review.user_id  , "")
        self.assertEqual(review.text  , "")
    
    
    def test_two_review_unique_ids(self):
        """this function test if two instantiated object of review has differents IDs"""
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)


if __name__ == '__main__':
    unittest.main()
