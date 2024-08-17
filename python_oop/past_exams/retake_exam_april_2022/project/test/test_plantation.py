from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(100)

    def test_correct_init(self):
        self.assertEqual(100, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_already_hired_raises_value_error(self):
        self.plantation.workers = ["Pesho"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Pesho")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_success_worker_added(self):
        result = self.plantation.hire_worker("Pesho")
        self.assertEqual(["Pesho"], self.plantation.workers)
        self.assertEqual("Pesho successfully hired.", result)

    def test_len(self):
        self.plantation.plants = {"worker1": ["plant1"], "worker2": ["plant2", "plant3"]}
        self.assertEqual(3, len(self.plantation))

    def test_planting_invalid_worker_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Pesho", "plant1")
        self.assertEqual("Worker with name Pesho is not hired!", str(ve.exception))

    def test_planting_full_plantation_raises_value_error(self):
        self.plantation.size = 3
        self.plantation.workers = ["worker1", "worker2"]
        self.plantation.plants = {"worker1": ["plant1"], "worker2": ["plant2", "plant3"]}
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("worker1", "plant4")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_success_first_plant_for_worker_plant_added(self):
        self.plantation.workers = ["worker1", "worker2"]
        self.plantation.plants = {"worker1": ["plant1"]}
        result = self.plantation.planting("worker2", "plant2")
        self.assertEqual({"worker1": ["plant1"], "worker2": ["plant2"]}, self.plantation.plants)
        self.assertEqual("worker2 planted it's first plant2.", result)

    def test_planting_success_worker_already_planted_plant_added(self):
        self.plantation.workers = ["worker1", "worker2"]
        self.plantation.plants = {"worker1": ["plant1"], "worker2": ["plant2"]}
        result = self.plantation.planting("worker2", "plant3")
        self.assertEqual({"worker1": ["plant1"], "worker2": ["plant2", "plant3"]},
                         self.plantation.plants)
        self.assertEqual("worker2 planted plant3.", result)

    def test_str(self):
        self.plantation.workers = ["worker1", "worker2"]
        self.plantation.plants = {"worker1": ["plant1"], "worker2": ["plant2", "plant3"]}
        expected = "Plantation size: 100\n" \
                   "worker1, worker2\n" \
                   "worker1 planted: plant1\n" \
                   "worker2 planted: plant2, plant3"
        self.assertEqual(expected, str(self.plantation))

    def test_repr(self):
        self.plantation.workers = ["worker1", "worker2"]
        expected = "Size: 100\n" \
                   "Workers: worker1, worker2"
        self.assertEqual(expected, self.plantation.__repr__())


if __name__ == "__main__":
    main()
