#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_default_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.text, "")

    def test_set_attributes(self):
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "A great place!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "A great place!")


if __name__ == '__main__':
    unittest.main()
