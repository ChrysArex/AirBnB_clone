#!/usr/bin/python3
"""
Defines unittests for City Class.
"""
import unittest
import models
import os
from time import sleep
from datetime import datetime
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

    def test_no_args_init(self):
        self.assertEqual(City, type(City()))

    def test_id(self):
        self.assertEqual(str, type(City().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_two_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_two_diff_created_at(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_two_diff_updated_at(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_init_stored_in_obj(self):
        self.assertIn(City(), models.storage.all().values())

    def test_str(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        city = City()
        city.id = "123"
        city.created_at = city.updated_at = date_time
        city_str = city.__str__()
        self.assertIn("[City] (123)", city_str)
        self.assertIn("'id': '123'", city_str)
        self.assertIn("'created_at': {}".format(date_time_repr), city_str)
        self.assertIn("'updated_at': {}".format(date_time_repr), city_str)

    def test_args_unused(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_init_with_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        city = City(id="325", created_at=date_time_iso,
                    updated_at=date_time_iso)
        self.assertEqual(city.id, "325")
        self.assertEqual(city.created_at, date_time)
        self.assertEqual(city.updated_at, date_time)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_init_with_args_and_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        city = City("1", id="345", created_at=date_time_iso,
                    updated_at=date_time_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, date_time)
        self.assertEqual(city.updated_at, date_time)


class Testcity_save(unittest.TestCase):
    """Test cases for saving City instances."""
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
        city = City()
        sleep(0.05)
        updated_at_1 = city.updated_at
        city.save()
        self.assertLess(updated_at_1, city.updated_at)

    def test_save2(self):
        city = City()
        sleep(0.05)
        updated_at_1 = city.updated_at
        city.save()
        updated_at_2 = city.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.05)
        city.save()
        self.assertLess(updated_at_2, city.updated_at)

    def test_save_update(self):
        city = City()
        city.save()
        city_id = "City.{}".format(city.id)
        with open("file.json", "r") as file:
            self.assertIn(city_id, file.read())


class TestCity_to_dict(unittest.TestCase):
    """Test cases for the 'to_dict' method of City."""
    def test_to_dict_type(self):
        city = City()
        self.assertTrue(dict, type(city.to_dict()))

    def test_to_dict_right_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_to_dict_attributes_added(self):
        city = City()
        city.name = "John"
        city.my_number = 404
        self.assertIn("name", city.to_dict())
        self.assertIn("my_number", city.to_dict())

    def test_to_dict_output(self):
        date_time = datetime.today()
        tdict = {
            'id': '123',
            '__class__': 'City',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }

        city = City()
        city.id = "123"
        city.created_at = city.updated_at = date_time
        self.assertDictEqual(city.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
