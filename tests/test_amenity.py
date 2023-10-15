#!/usr/bin/python3
""" Difine unittest for Amenity class """
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    A test case for the Amenity class to ensure its functionality.

    """
    def test_default_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_set_name(self):
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_empty_name(self):
        amenity = Amenity()
        amenity.name = ""
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
