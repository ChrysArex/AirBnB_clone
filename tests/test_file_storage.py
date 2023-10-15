#!/usr/bin/python3
"""
Defines unittests for File Storage.

"""
import os
import models
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage_init(unittest.TestCase):
    """ Test Cases for the initialization """
    def test_FileStorage_init_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_init_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_priv_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_priv_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorage_methods(unittest.TestCase):
    """ Test cases for saving FileStorage instances. """
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

    def test_all_no_args(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_no_args(self):
        base = BaseModel()
        base_id = base.id
        models.storage.new(base)
        amenity = Amenity()
        amenity_id = amenity.id
        models.storage.new(amenity)
        city = City()
        city_id = city.id
        models.storage.new(city)
        place = Place()
        place_id = place.id
        models.storage.new(place)
        review = Review()
        review_id = review.id
        models.storage.new(review)
        state = State()
        state_id = state.id
        models.storage.new(state)
        user = User()
        user_id = user.id
        models.storage.new(user)
        self.assertIn("BaseModel.{}".format(base_id),
                      models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())
        self.assertIn("Amenity.{}".format(amenity_id),
                      models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("City.{}".format(city_id), models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Place.{}".format(place_id), models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("Review.{}".format(review_id),
                      models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())
        self.assertIn("State.{}".format(state_id),
                      models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("User.{}".format(user_id), models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save_no_args(self):
        base = BaseModel()
        base_id = base.id
        models.storage.new(base)
        amenity = Amenity()
        amenity_id = amenity.id
        models.storage.new(amenity)
        city = City()
        city_id = city.id
        models.storage.new(city)
        place = Place()
        place_id = place.id
        models.storage.new(place)
        review = Review()
        review_id = review.id
        models.storage.new(review)
        state = State()
        state_id = state.id
        models.storage.new(state)
        user = User()
        user_id = user.id
        models.storage.new(user)
        models.storage.save()

        with open("file.json", "r") as file:
            filename = file.read()
            self.assertIn("BaseModel.{}".format(base_id), filename)
            self.assertIn("Amenity.{}".format(amenity_id), filename)
            self.assertIn("City.{}".format(city_id), filename)
            self.assertIn("Place.{}".format(place_id), filename)
            self.assertIn("Review.{}".format(review_id), filename)
            self.assertIn("State.{}".format(state_id), filename)
            self.assertIn("User.{}".format(user_id), filename)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_no_args(self):
        base = BaseModel()
        base_id = base.id
        models.storage.new(base)
        amenity = Amenity()
        amenity_id = amenity.id
        models.storage.new(amenity)
        city = City()
        city_id = city.id
        models.storage.new(city)
        place = Place()
        place_id = place.id
        models.storage.new(place)
        review = Review()
        review_id = review.id
        models.storage.new(review)
        state = State()
        state_id = state.id
        models.storage.new(state)
        user = User()
        user_id = user.id
        models.storage.new(user)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel.{}".format(base_id), objs)
        self.assertIn("Amenity.{}".format(amenity_id), objs)
        self.assertIn("City.{}".format(city_id), objs)
        self.assertIn("Place.{}".format(place_id), objs)
        self.assertIn("Review.{}".format(review_id), objs)
        self.assertIn("State.{}".format(state_id), objs)
        self.assertIn("User.{}".format(user_id), objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
