#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    A test case class for the City class.

    """
    def test_default_values(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_setting_values(self):
        city = City()
        city.state_id = "NY"
        city.name = "New York"
        self.assertEqual(city.state_id, "NY")
        self.assertEqual(city.name, "New York")


if __name__ == '__main__':
    unittest.main()
