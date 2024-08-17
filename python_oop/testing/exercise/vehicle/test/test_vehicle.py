from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(50, 150)

    def test_correct_init(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(150, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_without_enough_fuel(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(50)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_expected_decrease_fuel(self):
        self.vehicle.drive(20)
        self.assertEqual(25, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(40)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_expected_increase_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(20)
        self.assertEqual(20, self.vehicle.fuel)

    def test_str(self):
        self.assertEqual("The vehicle has 150 "
                         "horse power with 50 fuel left "
                         "and 1.25 fuel consumption", self.vehicle.__str__())


if __name__ == "__main__":
    main()
