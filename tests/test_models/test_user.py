#!/usr/bin/python3
"""
Defines unittests for User Class.
"""
import unittest
import models
import os
from time import sleep
from datetime import datetime
from models.user import User


class TestUserModel(unittest.TestCase):
    """
    A test case for the User class to ensure its functionality.

    """
    def test_default_values(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_setting_values(self):
        user = User()
        user.email = "test@example.com"
        user.password = "secretpassword"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "secretpassword")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_no_args_init(self):
        self.assertEqual(User, type(User()))

    def test_id(self):
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_two_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_two_diff_created_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_two_diff_updated_at(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_init_stored_in_obj(self):
        self.assertIn(User(), models.storage.all().values())

    def test_str(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        user = User()
        user.id = "123"
        user.created_at = user.updated_at = date_time
        user_str = user.__str__()
        self.assertIn("[User] (123)", user_str)
        self.assertIn("'id': '123'", user_str)
        self.assertIn("'created_at': {}".format(date_time_repr), user_str)
        self.assertIn("'updated_at': {}".format(date_time_repr), user_str)

    def test_args_unused(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_init_with_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        user = User(id="325", created_at=date_time_iso,
                    updated_at=date_time_iso)
        self.assertEqual(user.id, "325")
        self.assertEqual(user.created_at, date_time)
        self.assertEqual(user.updated_at, date_time)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_init_with_args_and_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        user = User("1", id="345", created_at=date_time_iso,
                    updated_at=date_time_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, date_time)
        self.assertEqual(user.updated_at, date_time)


class TestUser_save(unittest.TestCase):
    """Test cases for saving User instances."""
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
        user = User()
        sleep(0.05)
        updated_at_1 = user.updated_at
        user.save()
        self.assertLess(updated_at_1, user.updated_at)

    def test_save2(self):
        user = User()
        sleep(0.05)
        updated_at_1 = user.updated_at
        user.save()
        updated_at_2 = user.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.05)
        user.save()
        self.assertLess(updated_at_2, user.updated_at)

    def test_save_update(self):
        user = User()
        user.save()
        user_id = "User.{}".format(user.id)
        with open("file.json", "r") as file:
            self.assertIn(user_id, file.read())


class TestUser_to_dict(unittest.TestCase):
    """Test cases for the 'to_dict' method of User."""
    def test_to_dict_type(self):
        user = User()
        self.assertTrue(dict, type(user.to_dict()))

    def test_to_dict_right_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_attributes_added(self):
        user = User()
        user.name = "John"
        user.my_number = 404
        self.assertIn("name", user.to_dict())
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_output(self):
        date_time = datetime.today()
        tdict = {
            'id': '123',
            '__class__': 'User',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }

        user = User()
        user.id = "123"
        user.created_at = user.updated_at = date_time
        self.assertDictEqual(user.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
