#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_default_values(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, "")

    def test_initialization(self):
        place = Place(
            city_id="1",
            user_id="user123",
            name="Sample Place",
            description="A cozy place",
            number_rooms=2,
            number_bathrooms=1,
            max_guest=4,
            price_by_night=100,
            latitude=12.345,
            longitude=67.890,
            amenity_ids="1,2,3"
        )
        self.assertEqual(place.city_id, "1")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "Sample Place")
        self.assertEqual(place.description, "A cozy place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 12.345)
        self.assertEqual(place.longitude, 67.890)
        self.assertEqual(place.amenity_ids, "1,2,3")


if __name__ == '__main__':
    unittest.main()
