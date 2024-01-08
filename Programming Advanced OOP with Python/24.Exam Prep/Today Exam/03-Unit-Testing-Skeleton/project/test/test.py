import unittest
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):
    def setUp(self):
        self.station = RailwayStation("TestStation")

    def test_station_name_validation(self):
        with self.assertRaises(ValueError):
            self.station.name = "abc"

    def test_station_name_validation_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "abc"

        self.assertEqual(str(ve.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.station.arrival_trains = deque()
        self.assertEqual(len(self.station.arrival_trains), 0)

        self.station.new_arrival_on_board("Train A")
        self.assertEqual(len(self.station.arrival_trains), 1)

    def test_train_has_arrived_on_platform(self):
        self.station.new_arrival_on_board("Train B")
        result = self.station.train_has_arrived("Train B")
        self.assertIn("Train B is on the platform", result)
        self.assertEqual(len(self.station.departure_trains), 1)

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board("Train B")
        result = self.station.train_has_arrived("Train B")
        expected_message = "Train B is on the platform and will leave in 5 minutes."
        self.assertIn(expected_message, result)
        self.assertEqual(len(self.station.departure_trains), 1)

    def test_train_has_arrived_with_other_trains_in_queue(self):
        self.station.new_arrival_on_board("Train C")
        self.station.new_arrival_on_board("Train D")
        result = self.station.train_has_arrived("Train D")
        self.assertIn("There are other trains to arrive before Train D", result)

    def test_train_has_left(self):
        self.station.new_arrival_on_board("Train E")
        self.station.train_has_arrived("Train E")
        result = self.station.train_has_left("Train E")
        self.assertTrue(result)
        self.assertEqual(len(self.station.departure_trains), 0)

    def test_train_has_left_nonexistent_train(self):
        self.station.departure_trains = deque()
        self.assertEqual(len(self.station.departure_trains), 0)

        result = self.station.train_has_left("Nonexistent Train")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
