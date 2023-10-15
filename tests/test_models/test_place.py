#!/usr/bin/python3
"""
Defines unittests for Place Class.
"""
import unittest
import models
import os
from time import sleep
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    A test case for the Place class to ensure its functionality.

    """
    def test_default_values(self):
        place = Place()
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.city_id, "")

    def test_init(self):
        place = Place(
            place_id="1",
            user_id="user123",
            name="Sample Place",
            description="A cozy place",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=12.345,
            longitude=67.890,
            city_id="1,2,3"
        )
        self.assertEqual(place.place_id, "1")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "Sample Place")
        self.assertEqual(place.description, "A cozy place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 12.345)
        self.assertEqual(place.longitude, 67.890)
        self.assertEqual(place.city_id, "1,2,3")

    def test_no_args_init(self):
        self.assertEqual(Place, type(Place()))

    def test_id(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_two_unique_ids(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_two_diff_created_at(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_two_diff_updated_at(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_init_stored_in_obj(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_str(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        place = Place()
        place.id = "123"
        place.created_at = place.updated_at = date_time
        place_str = place.__str__()
        self.assertIn("[Place] (123)", place_str)
        self.assertIn("'id': '123'", place_str)
        self.assertIn("'created_at': {}".format(date_time_repr), place_str)
        self.assertIn("'updated_at': {}".format(date_time_repr), place_str)

    def test_args_unused(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_init_with_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        place = Place(id="325", created_at=date_time_iso,
                      updated_at=date_time_iso)
        self.assertEqual(place.id, "325")
        self.assertEqual(place.created_at, date_time)
        self.assertEqual(place.updated_at, date_time)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_init_with_args_and_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        place = Place("1", id="345", created_at=date_time_iso,
                      updated_at=date_time_iso)
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, date_time)
        self.assertEqual(place.updated_at, date_time)


class TestPlace_save(unittest.TestCase):
    """Test cases for saving Place instances."""
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
        place = Place()
        sleep(0.05)
        updated_at_1 = place.updated_at
        place.save()
        self.assertLess(updated_at_1, place.updated_at)

    def test_save2(self):
        place = Place()
        sleep(0.05)
        updated_at_1 = place.updated_at
        place.save()
        updated_at_2 = place.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.05)
        place.save()
        self.assertLess(updated_at_2, place.updated_at)

    def test_save_update(self):
        place = Place()
        place.save()
        place_id = "Place.{}".format(place.id)
        with open("file.json", "r") as file:
            self.assertIn(place_id, file.read())


class TestPlace_to_dict(unittest.TestCase):
    """Test cases for the 'to_dict' method of Place."""
    def test_to_dict_type(self):
        place = Place()
        self.assertTrue(dict, type(place.to_dict()))

    def test_to_dict_right_keys(self):
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_to_dict_attributes_added(self):
        place = Place()
        place.name = "John"
        place.my_number = 404
        self.assertIn("name", place.to_dict())
        self.assertIn("my_number", place.to_dict())

    def test_to_dict_output(self):
        date_time = datetime.today()
        tdict = {
            'id': '123',
            '__class__': 'Place',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }

        place = Place()
        place.id = "123"
        place.created_at = place.updated_at = date_time
        self.assertDictEqual(place.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
