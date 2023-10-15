#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_default_name(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_set_name(self):
        state = State()
        state.name = "New State Name"
        self.assertEqual(state.name, "New State Name")


if __name__ == '__main__':
    unittest.main()
