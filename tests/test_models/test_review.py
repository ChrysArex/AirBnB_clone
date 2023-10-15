#!/usr/bin/python3
"""
Defines unittests for Review Class.
"""
import unittest
import models
import os
from time import sleep
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """
    A test case for the Review class to ensure its functionality.

    """
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

    def test_no_args_init(self):
        self.assertEqual(Review, type(Review()))

    def test_id(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_two_unique_ids(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_two_diff_created_at(self):
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_two_diff_updated_at(self):
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_init_stored_in_obj(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_str(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        review = Review()
        review.id = "123"
        review.created_at = review.updated_at = date_time
        review_str = review.__str__()
        self.assertIn("[Review] (123)", review_str)
        self.assertIn("'id': '123'", review_str)
        self.assertIn("'created_at': {}".format(date_time_repr), review_str)
        self.assertIn("'updated_at': {}".format(date_time_repr), review_str)

    def test_args_unused(self):
        review = Review(None)
        self.assertNotIn(None, review.__dict__.values())

    def test_init_with_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        review = Review(id="325", created_at=date_time_iso,
                        updated_at=date_time_iso)
        self.assertEqual(review.id, "325")
        self.assertEqual(review.created_at, date_time)
        self.assertEqual(review.updated_at, date_time)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_init_with_args_and_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        review = Review("1", id="345", created_at=date_time_iso,
                        updated_at=date_time_iso)
        self.assertEqual(review.id, "345")
        self.assertEqual(review.created_at, date_time)
        self.assertEqual(review.updated_at, date_time)


class TestReview_save(unittest.TestCase):
    """Test cases for saving Review instances."""
    def creation(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def changes(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save1(self):
        review = Review()
        sleep(0.05)
        updated_at_1 = review.updated_at
        review.save()
        self.assertLess(updated_at_1, review.updated_at)

    def test_save2(self):
        review = Review()
        sleep(0.05)
        updated_at_1 = review.updated_at
        review.save()
        updated_at_2 = review.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.05)
        review.save()
        self.assertLess(updated_at_2, review.updated_at)

    def test_save_update(self):
        review = Review()
        review.save()
        review_id = "Review.{}".format(review.id)
        with open("file.json", "r") as file:
            self.assertIn(review_id, file.read())


class TestReview_to_dict(unittest.TestCase):
    """Test cases for the 'to_dict' method of Review."""
    def test_to_dict_type(self):
        review = Review()
        self.assertTrue(dict, type(review.to_dict()))

    def test_to_dict_right_keys(self):
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_to_dict_attributes_added(self):
        review = Review()
        review.name = "John"
        review.my_number = 404
        self.assertIn("name", review.to_dict())
        self.assertIn("my_number", review.to_dict())

    def test_to_dict_output(self):
        date_time = datetime.today()
        tdict = {
            'id': '123',
            '__class__': 'Review',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }

        review = Review()
        review.id = "123"
        review.created_at = review.updated_at = date_time
        self.assertDictEqual(review.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
