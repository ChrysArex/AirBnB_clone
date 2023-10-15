#!/usr/bin/python3
"""
Defines unittests for State Class.
"""
import unittest
import models
import os
from time import sleep
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """
    A test case for the State class to ensure its functionality.

    """
    def test_default_name(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_set_name(self):
        state = State()
        state.name = "New State Name"
        self.assertEqual(state.name, "New State Name")

    def test_no_args_init(self):
        self.assertEqual(State, type(State()))

    def test_id(self):
        self.assertEqual(str, type(State().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_two_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_two_diff_created_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_two_diff_updated_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_init_stored_in_obj(self):
        self.assertIn(State(), models.storage.all().values())

    def test_str(self):
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        state = State()
        state.id = "123"
        state.created_at = state.updated_at = date_time
        state_str = state.__str__()
        self.assertIn("[State] (123)", state_str)
        self.assertIn("'id': '123'", state_str)
        self.assertIn("'created_at': {}".format(date_time_repr), state_str)
        self.assertIn("'updated_at': {}".format(date_time_repr), state_str)

    def test_args_unused(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_init_with_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        state = State(id="325", created_at=date_time_iso,
                      updated_at=date_time_iso)
        self.assertEqual(state.id, "325")
        self.assertEqual(state.created_at, date_time)
        self.assertEqual(state.updated_at, date_time)

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_init_with_args_and_kwargs(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        state = State("1", id="345", created_at=date_time_iso,
                      updated_at=date_time_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, date_time)
        self.assertEqual(state.updated_at, date_time)


class TestState_save(unittest.TestCase):
    """Test cases for saving State instances."""
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
        state = State()
        sleep(0.05)
        updated_at_1 = state.updated_at
        state.save()
        self.assertLess(updated_at_1, state.updated_at)

    def test_save2(self):
        state = State()
        sleep(0.05)
        updated_at_1 = state.updated_at
        state.save()
        updated_at_2 = state.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.05)
        state.save()
        self.assertLess(updated_at_2, state.updated_at)

    def test_save_update(self):
        state = State()
        state.save()
        state_id = "State.{}".format(state.id)
        with open("file.json", "r") as file:
            self.assertIn(state_id, file.read())


class TestState_to_dict(unittest.TestCase):
    """Test cases for the 'to_dict' method of State."""
    def test_to_dict_type(self):
        state = State()
        self.assertTrue(dict, type(state.to_dict()))

    def test_to_dict_right_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_to_dict_attributes_added(self):
        state = State()
        state.name = "John"
        state.my_number = 404
        self.assertIn("name", state.to_dict())
        self.assertIn("my_number", state.to_dict())

    def test_to_dict_output(self):
        date_time = datetime.today()
        tdict = {
            'id': '123',
            '__class__': 'State',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat()
        }

        state = State()
        state.id = "123"
        state.created_at = state.updated_at = date_time
        self.assertDictEqual(state.to_dict(), tdict)


if __name__ == '__main__':
    unittest.main()
