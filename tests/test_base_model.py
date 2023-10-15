#!/usr/bin/python3
"""
Defines unittests for Base Model Class.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_init(unittest.TestCase):
    """Test cases for initializing the BaseModel class."""
    def test_no_args_init(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_unique_ids(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_two_diff_created_at(self):
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)

    def test_two_diff_updated_at(self):
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.updated_at, base2.updated_at)

    def test_init_stored_in_obj(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_str(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        base = BaseModel()
        base.id = "123"
        base.created_at = base.updated_at = date_time
        base_str = base.__str__()
        self.assertIn("[BaseModel] (123)", base_str)
        self.assertIn("'id': '123'", base_str)
        self.assertIn("'created_at': {}".format(date_time_repr), base_str)
        self.assertIn("'updated_at': {}".format(date_time_repr), base_str)

    def test_args_unused(self):
        base = BaseModel(None)
        self.assertNotIn(None, base.__dict__.values())

    def test_init_with_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        base = BaseModel(id="325", created_at=date_time_iso,
                         updated_at=date_time_iso)
        self.assertEqual(base.id, "325")
        self.assertEqual(base.created_at, date_time)
        self.assertEqual(base.updated_at, date_time)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_init_with_args_and_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        base = BaseModel("1", id="345", created_at=date_time_iso,
                         updated_at=date_time_iso)
        self.assertEqual(base.id, "345")
        self.assertEqual(base.created_at, date_time)
        self.assertEqual(base.updated_at, date_time)


class TestBaseModel_save(unittest.TestCase):
    """Test cases for saving BaseModel instances."""
    def creation(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def deletion(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save1(self):
        base = BaseModel()
        sleep(0.05)
        updated_at_1 = base.updated_at
        base.save()
        self.assertLess(updated_at_1, base.updated_at)

    def test_save2(self):
        base = BaseModel()
        sleep(0.05)
        updated_at_1 = base.updated_at
        base.save()
        updated_at_2 = base.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.05)
        base.save()
        self.assertLess(updated_at_2, base.updated_at)

    def test_save_update(self):
        base = BaseModel()
        base.save()
        baseid = "BaseModel.{}".format(base.id)
        with open("file.json", "r") as f:
            self.assertIn(baseid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Test cases for the 'to_dict' method of BaseModel."""
    def test_to_dict_type(self):
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_to_dict_right_keys(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())

    def test_to_dict_attributes_added(self):
        base = BaseModel()
        base.name = "John"
        base.my_number = 404
        self.assertIn("name", base.to_dict())
        self.assertIn("my_number", base.to_dict())

    def test_to_dict_output(self):
        date_time = datetime.today()
        tdict = {
            'id': '123',
            '__class__': 'BaseModel',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }

        base = BaseModel()
        base.id = "123"
        base.created_at = base.updated_at = date_time
        self.assertDictEqual(base.to_dict(), tdict)


if __name__ == "__main__":
    unittest.main()
