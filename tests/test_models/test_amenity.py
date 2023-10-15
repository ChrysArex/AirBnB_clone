#!/usr/bin/python3
""" Difine unittest for Amenity class """
import unittest
import models
import os
from time import sleep
from datetime import datetime
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

    def test_no_args_init(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_two_unique_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_two_diff_created_at(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_two_diff_updated_at(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_init_stored_in_obj(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_str(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        amenity = Amenity()
        amenity.id = "123"
        amenity.created_at = amenity.updated_at = date_time
        amenity_str = amenity.__str__()
        self.assertIn("[Amenity] (123)", amenity_str)
        self.assertIn("'id': '123'", amenity_str)
        self.assertIn("'created_at': {}".format(date_time_repr), amenity_str)
        self.assertIn("'updated_at': {}".format(date_time_repr), amenity_str)

    def test_args_unused(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_init_with_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        amenity = Amenity(id="325", created_at=date_time_iso,
                          updated_at=date_time_iso)
        self.assertEqual(amenity.id, "325")
        self.assertEqual(amenity.created_at, date_time)
        self.assertEqual(amenity.updated_at, date_time)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_init_with_args_and_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        amenity = Amenity("1", id="345", created_at=date_time_iso,
                          updated_at=date_time_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, date_time)
        self.assertEqual(amenity.updated_at, date_time)


class TestAmenity_save(unittest.TestCase):
    """Test cases for saving Amenity instances."""
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
        amenity = Amenity()
        sleep(0.05)
        updated_at_1 = amenity.updated_at
        amenity.save()
        self.assertLess(updated_at_1, amenity.updated_at)

    def test_save2(self):
        amenity = Amenity()
        sleep(0.05)
        updated_at_1 = amenity.updated_at
        amenity.save()
        updated_at_2 = amenity.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.05)
        amenity.save()
        self.assertLess(updated_at_2, amenity.updated_at)

    def test_save_update(self):
        amenity = Amenity()
        amenity.save()
        amenity_id = "Amenity.{}".format(amenity.id)
        with open("file.json", "r") as file:
            self.assertIn(amenity_id, file.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Test cases for the 'to_dict' method of Amenity."""
    def test_to_dict_type(self):
        amenity = Amenity()
        self.assertTrue(dict, type(amenity.to_dict()))

    def test_to_dict_right_keys(self):
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())

    def test_to_dict_attributes_added(self):
        amenity = Amenity()
        amenity.name = "John"
        amenity.my_number = 404
        self.assertIn("name", amenity.to_dict())
        self.assertIn("my_number", amenity.to_dict())

    def test_to_dict_output(self):
        date_time = datetime.today()
        tdict = {
            'id': '123',
            '__class__': 'Amenity',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }

        amenity = Amenity()
        amenity.id = "123"
        amenity.created_at = amenity.updated_at = date_time
        self.assertDictEqual(amenity.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
