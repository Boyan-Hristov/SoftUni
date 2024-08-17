from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self) -> None:
        self.station = RailwayStation("name")

    def test_correct_init(self):
        self.assertEqual("name", self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_name_setter_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "abc"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board_expected_arrival_added_to_arrival_trains(self):
        self.station.new_arrival_on_board("train_1")
        self.assertEqual(deque(["train_1"]), self.station.arrival_trains)

    def test_train_has_arrived_failure_other_trains_to_arrive_first(self):
        self.station.arrival_trains = deque("train_1")
        train_info = "train_2"
        result = self.station.train_has_arrived(train_info)
        self.assertEqual(f"There are other trains to arrive before {train_info}.",
                         result)

    def test_train_has_arrived_success_train_removed_from_arrivals_and_added_to_departures(self):
        self.station.arrival_trains = deque(["train_1"])
        train_info = "train_1"
        result = self.station.train_has_arrived(train_info)
        self.assertEqual(f"{train_info} is on the platform and will leave in 5 minutes.",
                         result)
        self.assertFalse(train_info in self.station.arrival_trains)
        self.assertTrue(train_info in self.station.departure_trains)

    def test_train_has_left_success(self):
        self.station.departure_trains = deque(["train_1"])
        train_info = "train_1"
        result = self.station.train_has_left(train_info)
        self.assertTrue(result)

    def test_train_has_left_failure(self):
        self.station.departure_trains = deque(["train_1"])
        train_info = "train_2"
        result = self.station.train_has_left(train_info)
        self.assertFalse(result)


if __name__ == "__main__":
    main()
